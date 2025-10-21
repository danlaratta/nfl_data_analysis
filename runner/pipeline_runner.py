from etl.extract.extract import get_json
from runner.context.pipeline_context import PipelineContext
from etl.transform.transform_utils import TransformUtils
from etl.transform.transform import transform_game_leaders, transform_games, transform_players, transform_stadium, transform_teams, transform_team_game_stats
from etl.clean.clean import clean_game_leaders, clean_games, clean_players, clean_stadium, clean_teams, clean_team_game_stats
from typing import Any
import pandas as pd


class PipelineRunner():
    def __init__(self, context: PipelineContext, utils: TransformUtils) -> None:
        self.context = context
        self.utils = utils

    # Run Pipeline
    def run_pipeline(self) -> None:
        nfl_data: dict[str, Any] = self.run_extract_data()                                  # Extract
        transformed_dfs: dict[str, pd.DataFrame] = self.run_transform_data(nfl_data)        # Transform
        cleaned_dfs: dict[str, pd.DataFrame] = self.run_clean_data(transformed_dfs)         # Clean
        # self.run_load_data()                                          # Load


    # Extract
    def run_extract_data(self) -> dict[str, Any]:
        # extract_and_save(self.context.service, self.context.season_year)
        json = get_json(self.context.season_year)
        return json


    # Transform
    def run_transform_data(self, data: dict[str, Any]) -> dict[str, pd.DataFrame]:
        season_games_data: list[dict[str, Any]] = self.utils.filter_season_events(data, self.context.is_bulk_upload)
        data_to_transform: list[dict[str, Any]] = []


        if self.context.is_bulk_upload:
            # Start and end weeks must be supplied for transforming range of weeks
            if self.context.start_week is None or self.context.end_week is None:
                raise ValueError('Start or end week is missing or incorrect value')
            data_to_transform = self.utils.filter_season_weeks_range(season_games_data, self.context.start_week, self.context.end_week)
        else:
            # Just end week must be supplied for transforming range of weeks
            if self.context.end_week is None:
                raise ValueError('End week is missing or incorrect value')
            
            data_to_transform = self.utils.filter_season_week(season_games_data, self.context.end_week)

        # Call transform functions
        df_leaders: pd.DataFrame = transform_game_leaders(data_to_transform)
        df_games: pd.DataFrame = transform_games(data_to_transform)
        df_players: pd.DataFrame = transform_players(data_to_transform)
        df_stadium: pd.DataFrame = transform_stadium(data_to_transform)
        df_teams: pd.DataFrame = transform_teams(data_to_transform, self.context.is_bulk_upload)
        df_stats: pd.DataFrame = transform_team_game_stats(data_to_transform)

        transformed_dfs: dict[str, pd.DataFrame] = {
            'leaders': df_leaders,
            'games': df_games,
            'players': df_players,
            'stadium': df_stadium,
            'teams': df_teams,
            'stats': df_stats,
        }
 
        return transformed_dfs


    # Clean
    def run_clean_data(self, transformed_dfs: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
        cleaned_leaders_df: pd.DataFrame = clean_game_leaders(transformed_dfs['leaders'])
        cleaned_games_df: pd.DataFrame = clean_games(transformed_dfs['games'])
        cleaned_players_df: pd.DataFrame = clean_players(transformed_dfs['players'])
        cleaned_stadium_df: pd.DataFrame = clean_stadium(transformed_dfs['stadium'])
        cleaned_teams_df: pd.DataFrame = clean_teams(transformed_dfs['teams'])
        cleaned_stats_df: pd.DataFrame = clean_team_game_stats(transformed_dfs['stats'])
        
        cleaned_dfs: dict[str, pd.DataFrame ] = {
            'leaders': cleaned_leaders_df,
            'games': cleaned_games_df,
            'players': cleaned_players_df,
            'stadium': cleaned_stadium_df,
            'teams': cleaned_teams_df,
            'stats': cleaned_stats_df,
        }

        return cleaned_dfs


    # Load
    def run_load_data(self) -> None:
        pass



