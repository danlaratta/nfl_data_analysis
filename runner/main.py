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
    # df = pd.DataFrame(transformed['games'])
    # df = pd.DataFrame(transformed['leaders'])
    # df = pd.DataFrame(transformed['players'])
    # df = pd.DataFrame(transformed['stadium'])
    # df = pd.DataFrame(transformed['teams'])
    # df = pd.DataFrame(transformed['stats'])
    # print(df.head())

    # Week Range
    range_context: PipelineContext = PipelineContext(2025, True, service, 1, 3)
    range_utils: TransformUtils = TransformUtils(range_context)
    range_runner: PipelineRunner = PipelineRunner(range_context, range_utils)

    data: dict[str, Any] = range_runner.run_extract_data()
    transformed: dict[str, pd.DataFrame] = range_runner.run_transform_data(data)
    # df = pd.DataFrame(transformed['games'])
    # df = pd.DataFrame(transformed['leaders'])
    # df = pd.DataFrame(transformed['players'])
    # df = pd.DataFrame(transformed['stadium'])
    # df = pd.DataFrame(transformed['teams'])
    df = pd.DataFrame(transformed['stats'])
    print(df.head(50))
    # print(df.count())

if __name__ == '__main__':
    main()