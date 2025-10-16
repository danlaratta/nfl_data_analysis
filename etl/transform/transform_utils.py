from pathlib import Path
import json
from typing import Any
from runner.context.pipeline_context import PipelineContext

class TransformUtils:
    def __init__(self, context: PipelineContext) -> None:
        self.context = context
        self.ROOT_DIR = Path(__file__).resolve().parents[2]
        self.RAW_DATA_DIR = self.ROOT_DIR / 'data' / 'raw'
        self.RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


    # Filter for current season's weekly data
    def filter_season_events(self, json_data: dict[str, Any]) -> list[dict[str, Any]]:
        # Get all events (games)
        events: list[dict[str, Any]] = json_data.get('events', [])

        # Completed weeks in season 
        season_completed_games = [
            e for e in events
            if e.get('status', {}).get('type') == 'completed' and
            e.get('season', {}).get('year') == self.context.season_year
        ]

        if self.context.is_bulk_upload:
            # Multiple completed weeks within specified range
            week_events: list[dict[str, Any]]  = [
                e for e in season_completed_games if self.context.start_week <= e.get('week', {}).get('number') <= self.context.end_week
            ]
        else:
            # Previous/Last completed week (use in automation for each week)
            week_events: list[dict[str, Any]]  = [
                e for e in season_completed_games if e.get('week', {}).get('number') == self.context.end_week
            ]
        return week_events


    # Filter for most recent completed week of games
    def filter_season_week(self, events: list[dict[str, Any]], season_week: int) -> list[dict[str, Any]]:
        if events is None:
            return []

        # Filter for most recent completed week
        filtered_week: list[dict[str, Any]] = [
            e for e in events if e.get('week', {}).get('number', 0) == season_week
        ]

        return filtered_week 


    # Filter for all completed week of games
    def filter_season_weeks_range(self, events: list[dict[str, Any]], start_week: int, end_week: int) -> list[dict[str, Any]]:
        if events is None:
            return []
        
        # Filter for weeks within range
        filtered_weeks: list[dict[str, Any]] = [ 
            e for e in events if start_week <= e.get('week', {}).get('number', 0) <= end_week
        ]
        
        return filtered_weeks


    # Save copy of filtered raw data
    def save_raw_data(self, filtered_events: list[dict[str, Any]]) -> None:
        file_path = self.RAW_DATA_DIR / f'nfl_filtered_raw_{self.context.season_year}.json'
        payload = {'events': filtered_events }

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=4)
        print(f'Saving to: {file_path.resolve()}') 



