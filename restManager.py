import requests
import json

host_name = "dolphin.jump-technology.com"
port = 8443
username = "EPITA_GROUPE13"
password = "XMkT6qVPZ4CFkjxh"

period_start_date = "2016-06-01"
period_end_date = "2020-09-30"

url = "https://" + host_name + ":" + str(port)  + "/api/v1/"

portfolio_id = 1832

def get_portfolio(_portfolio_id):
    uri = url + "portfolio/" + str(_portfolio_id) + "/dyn_amount_compo"
    res = requests.get(uri, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri:" + uri)
    return json.loads(res.text)

def get_list_asset():
    uri = url + "asset/"
    res = requests.get(uri, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri:" + uri)
    json.loads(res.text)

def get_asset(asset_id):
    uri = url + "asset/" + str(asset_id)
    res = requests.get(uri, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri:" + uri)
    return json.loads(res.text)