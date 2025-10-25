import pandas as pd


def clean_teams(df: pd.DataFrame) -> pd.DataFrame: 
    # Copy dataframe 
    team_df: pd.DataFrame = df.copy() 
    
    # Fix incorrect Team IDs 
    team_df['team_id'] = team_df['team_id'].replace({33: 31, 34: 32}) # Raven's ID: 33 --> 31 | Texan's ID: 34 --> 32 

    # Sort and drop duplicates
    team_df = team_df.drop_duplicates(subset='team_name', keep='last').sort_values(by='team_name').reset_index(drop=True)

    return team_df


def clean_games(df: pd.DataFrame) -> pd.DataFrame:
    games_df = df.copy()
    games_df['home_team_id'] = games_df['home_team_id'].replace({33: 31, 34: 32})
    games_df['away_team_id'] = games_df['away_team_id'].replace({33: 31, 34: 32})
    return games_df.sort_values(by=['season_week', 'game_id']).reset_index(drop=True)


def clean_players(df: pd.DataFrame) -> pd.DataFrame:
    players_df: pd.DataFrame = df.copy()
     
    return players_df.sort_values(by='player_name').reset_index(drop=True)


def clean_team_game_stats(df: pd.DataFrame) -> pd.DataFrame:
    stats_df = df.copy()
    stats_df['team_id'] = stats_df['team_id'].replace({33: 31, 34: 32})
    return stats_df.sort_values(by='game_id').reset_index(drop=True)


def clean_game_leaders(df: pd.DataFrame) -> pd.DataFrame:
    leaders_df = df.copy()
    leaders_df['team_id'] = leaders_df['team_id'].replace({33: 31, 34: 32})
    return leaders_df.sort_values(by='game_id').reset_index(drop=True)


def clean_stadium(df: pd.DataFrame) -> pd.DataFrame:
    stadium_df: pd.DataFrame = df.copy()
    stadium_df.loc[stadium_df['stadium_country'] != 'USA', 'stadium_state'] = 'INTL'    # Set stadium_state to INTL (International) for games outside of USA
    return stadium_df.sort_values(by='stadium_name').reset_index(drop=True)

    
