import pandas as pd
from pathlib import Path
import json
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = ROOT_DIR / 'data' / 'raw'
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


# Transform Json - filter for just current season's data
def filter_season_events(json_data: dict[str, Any], season_year: int) -> dict[str, Any]:
    # Get all events (games)
    events: list[dict[str, Any]] = json_data.get('events', [])

    # Filter for current season's events (games)
    filtered_events: list[dict[str, Any]]  = [e for e in events if e.get('season', {}).get('year', {}) == season_year]

    # Save copy of filtered raw data
    file_path = RAW_DATA_DIR / f'nfl_filtered_raw_{season_year}.json'

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(filtered_events, f, ensure_ascii=False, indent=4)
    print(f'Saving to: {file_path.resolve()}') 

    return { 'events': filtered_events }


# Transform team json into dataframe
def transform_team(events: dict[str, Any]) -> pd.DataFrame:
    # List of extracted team data for each game each week
    teams_data: list[dict[str, Any]] = []

    # Iterate through json layers to extract the team data for games for each week
    for event in events:
        for comp in events.get('competitions', []):
            for competitor in comp.get('competitors', []):
                # Get the team key's values
                team = competitor.get('team', {})

                # Loop through records and storing them in dictionary (home, away, and overall records)
                records = { rec['name'].title: rec['summary'] for rec in competitor.get('records', {})}
                
                # Creates the rows for team data where each row represents a team
                team_row: dict[str, Any] = {
                    'team_id': int(team.get(id)),
                    'team_name': team.get('name'),
                    'abbreviation': team.get('abbreviation'),
                    'city': team.get('location'),
                    'home_or_away': competitor.get('homeAway'),
                    'home_record': records.get('Home'),
                    'away_record': records.get('Road'),
                    'overall_record': records.get('Overall')
                }
                teams_data.append(team_row)
    
    # Convert teams data into a dataframe
    teams_df: pd.DataFrame = pd.DataFrame(teams_data)

    # Drop duplicate teams - teams_data contains teams for all games, each team will be duplicated for X number of weeks
    teams_df = teams_df.drop_duplicates(subset=[]).reset_index(drop=True)
    return teams_df
                 



# Transform games json into dataframe
def transform_games(json_data):
    pass


# Transform players json into dataframe
def transform_players(json_data):
    pass


# Transform team game stats json into dataframe
def transform_team_game_stats(json_data):
    pass


# Transform game leaders json into dataframe
def transform_gane_leaders(json_data):
    pass


# Transform stadium json into dataframe
def transform_stadium(json_data):
    pass

