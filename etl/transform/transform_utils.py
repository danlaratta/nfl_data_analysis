from pathlib import Path
import json
from typing import Any

class TransformUtils:
    def __init__(self, season_year: int, recent_completed_week: int) -> None:
        self.season_year = season_year
        self.recent_completed_week = recent_completed_week
        self.ROOT_DIR = Path(__file__).resolve().parents[2]
        self.RAW_DATA_DIR = self.ROOT_DIR / 'data' / 'raw'
        self.RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


    # Filter for current season's data
    def filter_season_events(self, json_data: dict[str, Any]) -> list[dict[str, Any]]:
        # Get all events (games)
        events: list[dict[str, Any]] = json_data.get('events', [])

        # Filter for current season's events (games)
        filtered_events: list[dict[str, Any]]  = [
            e for e in events if e.get('season', {}).get('type') == 2 and e.get('season', {}).get('year') == self.season_year
        ]

        return filtered_events


    # Filter for most recent completed week of games
    def filter_season_week(self, events: list[dict[str, Any]]) -> list[dict[str, Any]]:
        if events is None:
            return []

        # Filter for most recent completed week
        filtered_week: list[dict[str, Any]] = [
            e for e in events if e.get('week', {}).get('number', 0) == self.recent_completed_week
        ]

        return filtered_week 


    # Filter for all completed week of games
    def filter_season_weeks_range(self, events: list[dict[str, Any]], start_week: int) -> list[dict[str, Any]]:
        if events is None:
            return []
        
        # Filter for weeks within range
        filtered_weeks: list[dict[str, Any]] = [ 
            e for e in events if start_week <= e.get('week', {}).get('number', 0) <= self.recent_completed_week
        ]
        
        return filtered_weeks


    # Save copy of filtered raw data
    def save_raw_data(self, filtered_events: list[dict[str, Any]]) -> None:
        file_path = self.RAW_DATA_DIR / f'nfl_filtered_raw_{self.season_year}.json'
        payload = {'events': filtered_events }

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=4)
        print(f'Saving to: {file_path.resolve()}') 