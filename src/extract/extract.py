import os
import sys
import json
from typing import Any, Dict

from src.common.config import settings

from utils import (
    get_connection,
    fetch_data,
    save_payload
)

# ----- Settings -----

API_BASE = f'https://apis.data.go.kr/'
SERVICE = f'B552584/EvCharger/getChargerInfo'

endpoint = API_BASE + SERVICE

# ----- main -----

params = {
    'serviceKey' : settings.API_KEY,
    'pageNo' : '1',
    'numOfRows' : '10',
    'zcode' : '26'
}  # zcode; 26=부산, 11=서울

def main():
    resp = fetch_data(endpoint, settings.API_KEY, params)
    conn = get_connection()
    print(conn)
    save_payload(resp.content, conn, 'raw_data')

if __name__ == '__main__':
    main()