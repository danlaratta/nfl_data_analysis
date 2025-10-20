import pandas as pd
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = ROOT_DIR / 'data' / 'cleaned'
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Export week's data
def export_week_data(df: pd.DataFrame, week: int, base_dir: Path):
    file_path = base_dir / f'week_{week}_data.csv'
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(file_path, index=False)


def bulk_export_week_data(df: pd.DataFrame, start_week: int, end_week: int, base_dir: Path):
    file_path = base_dir / f'week_{start_week}_to_week{end_week}_data.csv'
    file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(file_path, index=False)