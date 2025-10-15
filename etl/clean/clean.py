
import pandas as pd


def clean_team(df: pd.DataFrame) -> pd.DataFrame:
    # Copy dataframe
    team_df: pd.DataFrame = df.copy()

    # Fix incorrect Team IDs
    team_df['team_id'] = team_df['team_id'].replace({33: 31, 34: 32})     # Raven's ID: 33 --> 31 | Texan's ID: 34 --> 32

    # Sort and return
    return team_df.sort_values(by='team_name').reset_index(drop=True)




def clean_games(df: pd.DataFrame) -> pd.DataFrame:
    games_df = df.copy()
    return games_df.sort_values(by='game_id').reset_index(drop=True)


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

    
