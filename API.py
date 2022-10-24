
import requests
import json
import config as C

def CallAPI():
    base_url= 'https://randomuser.me/api/'
    parameters={'results':'3', 'page':'1'}
    
    response = requests.get(base_url, params=parameters)
    
    if response.status_code == 200:
        print("OK")
    else:
        print("ERROR")
        exit(0)

    data = response.json()
    return data