from .api.api_service import ApiService
import pandas as pd
from pathlib import Path
import json

RAW_DATA_DIR = Path('data/raw')
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True) 

# Take raw json, save a raw copy, and convert into a dataframe
def extract_and_save(service: ApiService, season_year: int) -> pd.DataFrame:
    # Get raw data
    json_data = service.fetch_nfl_data(season_year)

    # Save raw data
    file_path = RAW_DATA_DIR / f'nfl_raw_{season_year}.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    
    # Convert to dataframe
    df: pd.DataFrame = pd.json_normalize(json_data)
    return df