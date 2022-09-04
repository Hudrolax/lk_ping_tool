import requests
from time import sleep

SERVER = 'http://176.10.119.52'
ROUTE = '/ping_from_lk'

if __name__ == '__main__':
    while True:
        # send request
        data = {
            'api_key': 'lk_api_key',
            'body': 'hello there'
        }
        try:
            requests.post(SERVER+ROUTE, json=data, timeout=5)
            print('ping sent')
        except Exception as ex:
            print(ex)
        print('sleep 15 min...')
        sleep(900)
