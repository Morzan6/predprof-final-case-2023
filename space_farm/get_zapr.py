import requests

def req(adr, key):

    params = {"X-Auth-Token": key}

    resp = requests.get(adr, headers=params).text

    return resp
