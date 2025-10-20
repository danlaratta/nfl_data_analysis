from dataclasses import dataclass
from etl.extract.api.api_service import ApiService

@dataclass
class PipelineContext:
    season_year: int
    is_bulk_upload: bool
    service: ApiService
    start_week: int | None = None
    end_week: int | None = None

    