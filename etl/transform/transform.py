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
def transform_team():
    pass


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

