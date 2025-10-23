from sqlalchemy import create_engine
import pandas as pd
from database.db_utils import get_engine, write_df_to_db


# Write cleaned data to database
def load_to_postges(tables: dict[str, pd.DataFrame]) -> None:
    engine = get_engine()

    for table, df in tables.items():
        write_df_to_db(df, table, engine, if_exists='append')