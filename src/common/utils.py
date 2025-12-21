import os
import sys
import json
from typing import Any, Dict

import requests
import psycopg2
from psycopg2 import sql
from psycopg2.extras import Json
from psycopg2.extensions import connection
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import xmltodict

from src.common.config import settings

# ----- Utils -----

def xml_to_json(xml_data: str) -> dict:
    return xmltodict.parse(xml_data)

# ----- DB -----

def get_connection() -> connection:
    try:
        conn = psycopg2.connect(settings.DATABASE_URL)
        return conn
    except Exception as e:
        print(f'[FATAL] Failed to connect DB: {e}', file=sys.stderr)
        raise

def save_payload(xml:str, conn, table_name):
    try:
        json_dict = xml_to_json(xml)

        query = sql.SQL('INSERT INTO {table} (payload) VALUES (%s)').format(
            table=sql.Identifier(table_name)
        )

        with conn:
            with conn.cursor() as cur:
                cur.execute(query, [Json(json_dict)])
        
        print(f"[INFO] Successfully saved to table: {table_name}")

    except Exception as e:
        print(f"[ERROR] Save did not successed: {e}", file=sys.stderr)

def retrieve_data(conn:connection, table_name, schema_name='public', columns='*', limit=None):
    with conn.cursor() as cur:
        query = sql.SQL('SELECT {cols} FROM {schema}.{table}').format(
            cols=sql.SQL(columns) if isinstance(columns, str) else sql.SQL(',').join(map(sql.Identifier, columns)),
            schema=sql.Identifier(schema_name),
            table=sql.Identifier(table_name)
        )
        if limit:
            query += sql.SQL(' LIMIT {limit}').format(limit=sql.Literal(limit))
        
        cur.execute(query)
        colnames = [desc[0] for desc in cur.description]
        
        return cur.fetchall(), colnames

# ----- API -----

def fetch_data(
    base_url:str,
    api_key:str,
    params:dict
    ) -> Dict[str, Any]:
    '''
    Return JSON by calling API
    '''
    if not base_url or not api_key:
        raise RuntimeError('BASE_URL or API_KEY is missing')

    resp = requests.get(base_url, params=params, timeout=15)
    resp.raise_for_status()

    return resp