from dotenv import load_dotenv
from typing import Any
from etl.extract import get_json, extract_and_save
from etl.extract.api import ApiService
from etl.transform import TransformUtils


# Load environment variables
load_dotenv()

# Pipeline Runner
def main():
    # Extract
    service: ApiService = ApiService()
    raw_nfl_data = extract_and_save(service, 2025)
    json: dict[str, Any] = get_json(2025)


    # # Transform
    utils = TransformUtils(2025, 6)
    season_games: dict[str, Any] = utils.filter_season_events(json)
    week_one: dict[str, Any] = utils.filter_season_week(season_games)
    
    # utils.save_raw_data(season_games)


    # df: pd.DataFrame = pd.json_normalize(season_games)
    # print(df.head())
    

    # Clean


    # Export and Load


if __name__ == '__main__':
    main()