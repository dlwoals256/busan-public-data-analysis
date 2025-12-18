import os
import sys
import json
from typing import Any, Dict

from dotenv import load_dotenv

from utils import (
    get_connection,
    fetch_data,
    save_payload
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

endpoint = API_BASE + SERVICE

API_KEY = os.getenv('API_KEY')

# ----- main -----

params = {
    'serviceKey' : API_KEY,
    'pageNo' : '1',
    'numOfRows' : '10',
    'zcode' : '26'
}  # zcode; 26=부산, 11=서울

def main():
    resp = fetch_data(endpoint, API_KEY, params)
    conn = get_connection(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print(conn)
    save_payload(resp.content, conn, 'electronic_car_charger')

if __name__ == '__main__':
    main()