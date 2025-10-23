import pandas as pd
from database.db_utils import get_engine, write_df_to_db


# Write cleaned data to database
def load_to_postgres(tables: dict[str, pd.DataFrame]) -> None:
    engine = get_engine(echo=True)

    for table, df in tables.items():
        if df.empty:
            print(f"⚠️ Skipping {table}: no data")
            continue

        write_df_to_db(df, table, engine, if_exists='append')
