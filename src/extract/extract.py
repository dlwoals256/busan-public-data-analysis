import os
import sys
import json
from typing import Any, Dict

import requests
import psycopg2
from psycopg2.extras import Json
from dotenv import load_dotenv

from utils import (
    get_connection,
    insert_raw_payload,
    fetch_data
)

# ----- Settings -----

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

API_BASE = f'https://apis.data.go.kr/'
SERVICE = f'B552584/EvCharger/getChargerInfo'

API_KEY = os.getenv('API_KEY')

# ----- main -----

def main():
    pass

if __name__ == '__main__':
    main()