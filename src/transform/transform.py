import os
import pandas as pd

from src.common.utils import (
    get_connection,
    retrieve_data
)

# ----- Settings -----

conn = get_connection()

# ----- main -----

data, cols = retrieve_data(conn, 'raw_data')

df = pd.DataFrame(data, columns=cols)

print(df.head())

raw_payloads = df['payload'].tolist()

print(raw_payloads)

# df_items = pd.json_normalize(
#     raw_payloads,
#     record_path=['response', 'body', 'items', 'item']
# )

# print(df_items.head())