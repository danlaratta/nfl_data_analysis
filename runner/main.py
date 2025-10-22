from dotenv import load_dotenv
from typing import Any
import pandas as pd
from runner.pipeline_runner import PipelineRunner
from runner.context.pipeline_context import PipelineContext
from etl.transform.transform_utils import TransformUtils  
from etl.extract.api.api_service import ApiService 

# Load environment variables
load_dotenv()

# Pipeline Runner
def main():
    service: ApiService = ApiService()

    # Single Week
    # week_context: PipelineContext = PipelineContext(2025, False, service, None, 1)
    # week_utils: TransformUtils = TransformUtils(week_context)
    # week_runner: PipelineRunner = PipelineRunner(week_context, week_utils)

    # data: dict[str, Any] = week_runner.run_extract_data()
    # transformed: dict[str, pd.DataFrame] = week_runner.run_transform_data(data)
    # cleaned: dict[str, pd.DataFrame] = week_runner.run_clean_data(transformed)
    # df = pd.DataFrame(cleaned['games'])
    # df = pd.DataFrame(cleaned['leaders'])
    # df = pd.DataFrame(cleaned['players'])
    # df = pd.DataFrame(cleaned['stadium'])
    # df = pd.DataFrame(cleaned['teams'])
    # df = pd.DataFrame(cleaned['stats'])

    # Week Range
    range_context: PipelineContext = PipelineContext(2025, True, service, 1, 6)
    range_utils: TransformUtils = TransformUtils(range_context)
    range_runner: PipelineRunner = PipelineRunner(range_context, range_utils)

    data: dict[str, Any] = range_runner.run_extract_data()
    transformed: dict[str, pd.DataFrame] = range_runner.run_transform_data(data)
    cleaned: dict[str, pd.DataFrame] = range_runner.run_clean_data(transformed)

    # df = pd.DataFrame(cleaned['games'])
    # df = pd.DataFrame(cleaned['leaders'])
    # df = pd.DataFrame(cleaned['players'])
    # df = pd.DataFrame(cleaned['stadium'])
    df = pd.DataFrame(cleaned['teams'])
    # df = pd.DataFrame(cleaned['stats'])

    print(df.sort_values(by='team_name').head(50))

if __name__ == '__main__':
    main()