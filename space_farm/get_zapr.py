import requests

key  = "9e83w26h"


adr = "https://dt.miet.ru/ppo_it_final"
def req(adr, key):

    params = {"X-Auth-Token": key}

    resp = requests.get(adr, headers=params).text

    return resp

print(req(adr, key))