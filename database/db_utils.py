from sqlalchemy import create_engine
import pandas as pd
from db_config import DB_URL
from typing import Literal

# Create engine to connect to database and return it
def get_engine(echo: bool = False):
    return create_engine(DB_URL, echo=echo)

# Write dataframe to a SQL table using
def write_df_to_db(df: pd.DataFrame, table_name: str, engine, if_exists: Literal['fail', 'append'] = 'append') -> None:
    df.to_sql(name= table_name, con=engine, index=False, if_exists=if_exists)