from dotenv import load_dotenv
import pandas as pd
from etl.extract import extract_and_save
from etl.extract.api import ApiService


# Load environment variables
load_dotenv()

# Pipeline Runner
def main():
    # Extract
    service: ApiService = ApiService()
    raw_nfl_data: pd.DataFrame = extract_and_save(service, 2025)

    # Clean

    # Export and Load


if __name__ == '__main__':
    main()