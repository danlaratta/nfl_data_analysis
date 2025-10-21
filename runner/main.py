from dotenv import load_dotenv
from typing import Any
import pandas as pd
from runner.pipeline_runner import PipelineRunner
from .context.pipeline_context import PipelineContext
from etl.transform.transform_utils import TransformUtils  
from etl.extract.api.api_service import ApiService 

# Load environment variables
load_dotenv()

# Pipeline Runner
def main():
    service: ApiService = ApiService()
    week_context: PipelineContext = PipelineContext(2025, False, service, None, 1)
    week_utils: TransformUtils = TransformUtils(week_context)
    week_runner: PipelineRunner = PipelineRunner(week_context, week_utils)

    data: dict[str, Any] = week_runner.run_extract_data()
    transformed: dict[str, pd.DataFrame] = week_runner.run_transform_data(data)
    df = pd.DataFrame(transformed['games'])
    print(df.head())


if __name__ == '__main__':
    main()