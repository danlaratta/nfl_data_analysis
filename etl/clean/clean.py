import pandas as pd


def clean_teams(df: pd.DataFrame) -> pd.DataFrame: 
    # Copy dataframe 
    team_df: pd.DataFrame = df.copy() 
    
    # Fix incorrect Team IDs 
    team_df['team_id'] = team_df['team_id'].replace({33: 31, 34: 32}) # Raven's ID: 33 --> 31 | Texan's ID: 34 --> 32 

    # Sort and drop duplicates
    team_df = team_df.drop_duplicates(subset='team_name', keep='last').sort_values(by='team_name').reset_index(drop=True)

    return team_df


# def clean_teams_range(transformed_team: pd.DataFrame, end_week: int) -> pd.DataFrame:
#     team_df = transformed_team.copy()

#     # Fix incorrect team IDs in both DataFrames
#     team_df['team_id'] = team_df['team_id'].replace({33: 31, 34: 32})

#     # Merge these into team_df
#     team_df = team_df.set_index('team_id')
#     team_df['home_wins'] = home_wins
#     team_df['away_wins'] = away_wins
#     team_df = team_df.fillna(0).astype({'home_wins': int, 'away_wins': int})

#     # Compute overall record
#     team_df['overall_record'] = team_df['home_wins'].astype(str) + '-' + team_df['away_wins'].astype(str)

#     team_df = team_df.sort_values(by=['team_name'], ascending=True)
#     team_df = team_df.drop_duplicates(subset=['team_name']).reset_index(drop=True)

#     return team_df


def clean_games(df: pd.DataFrame) -> pd.DataFrame:
    games_df = df.copy()
    return games_df.sort_values(by=['season_week', 'game_id']).reset_index(drop=True)


def clean_players(df: pd.DataFrame) -> pd.DataFrame:
    players_df: pd.DataFrame = df.copy()
    return players_df.sort_values(by='player_name').reset_index(drop=True)


def clean_team_game_stats(df: pd.DataFrame) -> pd.DataFrame:
    stats_df = df.copy()
    return stats_df.sort_values(by='game_id').reset_index(drop=True)


def clean_game_leaders(df: pd.DataFrame) -> pd.DataFrame:
    leaders_df = df.copy()
    return leaders_df.sort_values(by='game_id').reset_index(drop=True)


def clean_stadium(df: pd.DataFrame) -> pd.DataFrame:
    stadium_df: pd.DataFrame = df.copy()
    stadium_df.loc[stadium_df['stadium_country'] != 'USA', 'stadium_state'] = 'INTL'    # Set stadium_state to INTL (International) for games outside of USA
    return stadium_df.sort_values(by='stadium_name').reset_index(drop=True)

    
