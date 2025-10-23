# Load environment vars - must be loaded before all other imports that use the vars
from dotenv import load_dotenv
load_dotenv()
from runner.pipeline_runner import PipelineRunner                   # noqa: E402  This silences the meaningless warnings
from runner.context.pipeline_context import PipelineContext         # noqa: E402
from etl.transform.transform_utils import TransformUtils            # noqa: E402
from etl.extract.api.api_service import ApiService                  # noqa: E402



# Pipeline Runner
def main():
    service: ApiService = ApiService()

    # Single Week
    # week_context: PipelineContext = PipelineContext(2025, False, service, None, 1)
    # week_utils: TransformUtils = TransformUtils(week_context)
    # week_runner: PipelineRunner = PipelineRunner(week_context, week_utils)
    # week_runner.run_pipeline()


    # Week Range
    range_context: PipelineContext = PipelineContext(2025, True, service, 1, 7)
    range_utils: TransformUtils = TransformUtils(range_context)
    range_runner: PipelineRunner = PipelineRunner(range_context, range_utils)
    range_runner.run_pipeline()


if __name__ == '__main__':
    main()