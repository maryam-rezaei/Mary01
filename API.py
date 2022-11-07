
import requests
import json
import Config as C
import Functions as F

#   Inventory Data from API
def GetData(nat, count):
    Base_URL= 'https://randomuser.me/api/'
    parameters = GetParameters()
    parameters['nat'] = nat
    parameters['results'] = count    
    response = requests.get(Base_URL, params=parameters)
    
    if response.status_code == 200:
        print(nat, "- OK")
    else:
        print(nat, "- ERROR")
        exit(0)

    data = response.json()
    return data

#   Generate Parameters Json 
def GetParameters():
    Params = {}
    #Params['nat'] = F.GetNationality()
    for key, value in dict(C.PARAMS).items():
        if value != 'NULL':
            Params[key] = value
    return Params