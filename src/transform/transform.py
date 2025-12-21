import os
import pandas as pd
import json
import re

from sqlalchemy import create_engine
from src.common.config import settings

engine = create_engine(settings.DATABASE_URL)

from src.common.utils import (
    get_connection,
    retrieve_data
)

# ----- Settings -----

conn = get_connection()

# ----- main -----

data, cols = retrieve_data(conn, 'raw_data')

df = pd.DataFrame(data, columns=cols)

raw_payloads = df['payload'].tolist()

df_items = pd.json_normalize(
    raw_payloads,
    record_path=['response', 'body', 'items', 'item']
)

cols_to_numeric = [
    'lat',
    'lng',
    'output'
]
cols_to_timestamp = [
    'statUpdDt',
    'lastTedt',
    'lastTsdt',
    'nowTsdt'
]

for col in cols_to_numeric:
    if col in df_items.columns:
        df_items[col] = pd.to_numeric(df_items[col], errors='coerce')

for col in cols_to_timestamp:
    if col in df_items.columns:
        df_items[col] = pd.to_datetime(df_items[col], format='%Y%m%d%H%M%S', errors='coerce')

def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

df_items.columns = [to_snake_case(col) for col in df_items.columns]

wrong_convention_name = {
    'last_tedt': 'last_te_dt',
    'last_tsdt': 'last_ts_dt',
    'now_tsdt': 'now_ts_dt'
}

df_items.rename(columns=wrong_convention_name, inplace=True)

# ONLY in the scheme of analytics.ev_charger.
target_columns = [
    'stat_nm', 'stat_id', 'chger_id', 'chger_type', 'addr', 'addr_detail',
    'location', 'lat', 'lng', 'use_time', 'busi_id', 'bnm', 'busi_nm',
    'busi_call', 'stat', 'stat_upd_dt', 'last_ts_dt', 'last_te_dt',
    'now_ts_dt', 'output', 'method', 'zcode', 'zscode', 'kind',
    'kind_detail', 'parking_free', 'note', 'limit_yn', 'limit_detail',
    'del_yn', 'del_detail', 'traffic_yn', 'year', 'floor_num', 'floor_type'
]

df_items = df_items[[col for col in target_columns if col in df_items.columns]]

def load_to_analytics(df:pd.DataFrame):
    try:
        df.to_sql(
            name='ev_chargers',
            con=engine,
            schema='analytics',
            if_exists='append',
            index=False,
            method='multi'
        )
        print('[INFO] Success: Data loaded to analytics.ev_chargers')
    except Exception as e:
        print(f'[ERROR] Error loading to DB: {e}')

load_to_analytics(df_items)