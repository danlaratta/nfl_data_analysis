from dotenv import load_dotenv
from typing import Any
import pandas as pd
from etl.extract import extract_and_save, get_json
from etl.extract.api import ApiService
from etl.transform import filter_season_events


# Load environment variables
load_dotenv()

# Pipeline Runner
def main():
    # Extract
    # service: ApiService = ApiService()
    # raw_nfl_data = extract_and_save(service, 2025)
    json: dict[str, Any] = get_json(2025)


    # # Transform
    events: dict[str, Any] = filter_season_events(json, 2025)
    # df: pd.DataFrame = pd.json_normalize(events)
    # print(df.head())
    

    # Clean


    # Export and Load


if __name__ == '__main__':
    main()