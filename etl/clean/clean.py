
import pandas as pd


def clean_team(df: pd.DataFrame) -> pd.DataFrame:
    # Copy dataframe
    team_df: pd.DataFrame = df.copy()

    # Fix incorrect Team IDs
    df['team_id'] = df['team_id'].replace({33: 31, 34: 32})     # Raven's ID: 33 --> 31 | Texan's ID: 34 --> 32

    # Sort the df
    team_df = df.sort_values(by='team_id').reset_index(drop=True)

    return team_df



def clean_games(df: pd.DataFrame) -> pd.DataFrame:
    games_df = df.copy()
    return games_df.sort_values(by='game_id').reset_index(drop=True)
    


def clean_players(df: pd.DataFrame) -> None:
    pass


def clean_team_game_stats(df: pd.DataFrame) -> pd.DataFrame:
    stats_df = df.copy()
    return stats_df.sort_values(by='game_id').reset_index(drop=True)


def clean_game_leaders(df: pd.DataFrame) -> pd.DataFrame:
    leaders_df = df.copy()
    return leaders_df.sort_values(by='game_id').reset_index(drop=True)


def clean_stadium(df: pd.DataFrame) -> None:
    pass