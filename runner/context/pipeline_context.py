from dataclasses import dataclass
from etl.extract.api.api_service import ApiService
from etl.transform.transform_utils import TransformUtils

@dataclass
class PipelineContext:
    season_year: int
    is_bulk_upload: bool
    service: ApiService
    utils: TransformUtils
    start_week: int | None = None
    end_week: int | None = None

    