import math

import pandas as pd


def to_sql(df: pd.DataFrame, table_name, engine, schema="dbo"):
    """
    Exporta um DataFrame pandas para um banco de dados SQL Server.

    Args:
        table_name: Nome da tabela.
        engine: Engine do banco de dados.
    """
    chunksize = math.floor(2097 / len(df.columns))
    chunksize = 1000 if chunksize > 1000 else chunksize
    try:
        df.to_sql(
            table_name, con=engine, index=False, method="multi", chunksize=chunksize, schema=schema, if_exists="append"
        )
    except Exception as e:
        raise e
    else:
        return len(df)
