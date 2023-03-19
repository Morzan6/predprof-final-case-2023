import requests

def req(adr, key):
    """
        Returns list of dicts. One dict for each route#
    """

    params = {"X-Auth-Token": key}

    resp = requests.get(adr, headers=params)

    return resp.json()["message"]

#print(req("https://dt.miet.ru/ppo_it_final", "9e83w26h"))