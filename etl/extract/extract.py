from .api.api_service import ApiService
from pathlib import Path
import json
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = ROOT_DIR / 'data' / 'raw'
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Take raw json, save a raw copy, and convert into a dataframe
def extract_and_save(service: ApiService, season_year: int) -> None:
    # Get raw data
    json_data = service.fetch_nfl_data(season_year)

    # Save raw data
    file_path = RAW_DATA_DIR / f'nfl_raw_{season_year}.json'

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    print(f'Saving to: {file_path.resolve()}') 


def get_json(season_year: int) -> dict[str, Any]:
    file_path = RAW_DATA_DIR / f'nfl_raw_{season_year}.json'
    
    if not file_path.exists():
        print('file does not exist')

    # Read from file
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)