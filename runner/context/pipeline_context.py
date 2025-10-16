from dataclasses import dataclass

@dataclass
class PipelineContext:
    season_year: int
    is_bulk_upload: bool
    start_week: int | None = None
    end_week: int | None = None

    