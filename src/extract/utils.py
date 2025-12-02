import os
import sys
import json
from typing import Any, Dict

import requests
import psycopg2
from psycopg2.extras import Json
from psycopg2.extensions import connection
from dotenv import load_dotenv

# ----- DB -----

def get_connection(
        host:str,
        port:int,
        dbname:str,
        user:str,
        password:str
    ) -> connection:
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        return conn
    except Exception as e:
        print(f'[FATAL] Failed to connect DB: {e}', file=sys.stderr)
        raise

def insert_raw_payload(
        conn:connection,
        source:str,
        payload:Dict[str, Any]
    ) -> None:
    '''
    Insert one data into the table raw_data
    '''

    with conn.cursor() as cur:
        cur.execute(
            '''
            INSERT INTO raw_data(source, payload)
            VALUES (%s, %s)
            ''',
            (source, Json(payload))
        )
    conn.commit()


# ----- API -----

def fetch_data(
    base_url:str,
    api_key:str    
    ) -> Dict[str, Any]:
    '''
    Return JSON by calling API
    '''
    if not base_url or not api_key:
        raise RuntimeError('BASE_URL or API_KEY is missing')
    
    params = {
        'serviceKey' : api_key,
        'pageNo'     : 1,
        'numOfRows'  : 100,
    }

    resp = requests.get(base_url, params=params, timeout=15)
    resp.raise_for_status()

    try:
        data = resp.json()
    except json.JSONDecodeError:
        print('[ERROR] Response was not JSON as following 500 example contents of it:')
        print(resp.text[:500])
        raise

    return data
