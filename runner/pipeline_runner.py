from multiprocessing.sharedctypes import Value
from typing import Any
from etl.extract.extract import extract_and_save, get_json
from .context.pipeline_context import PipelineContext

class PipelineRunner():
    def __init__(self, context: PipelineContext) -> None:
        self.context = context

    # Run Pipeline
    def run_pipeline(self) -> None:
        nfl_data: dict[str, Any] = self.run_extract_data()

        # self.run_transform_data()
        # self.run_clean_data()
        # self.run_load_data()

    # Extract
    def run_extract_data(self) -> dict[str, Any]:
        extract_and_save(self.context.service, self.context.season_year)
        json = get_json(self.context.season_year)
        return json


    # Transform
    def run_transform_data(self, data: dict[str, Any]) -> None:
        # Get the games for the season
        season_games_data: list[dict[str, Any]] = self.context.utils.filter_season_events(data)
        
        if self.context.start_week is None or self.context.end_week is None:
            raise ValueError('Start or end week is missing or incorrect value')

        if self.context.is_bulk_upload:
            self.context.utils.filter_season_weeks_range(season_games_data, self.context.start_week, self.context.end_week)




    # Clean
    def run_clean_data(self) -> None:
        pass


    # Load
    def run_load_data(self) -> None:
        pass



