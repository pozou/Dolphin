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
        print("Error with uri: " + uri)
    return json.loads(res.text)

def get_list_asset():
    uri = url + "asset/"
    res = requests.get(uri, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri: " + uri)
    return json.loads(res.text)

def get_asset(asset_id, date):
    uri = url + "asset/" + str(asset_id)
    payload = {"columns": ["ASSET_DATABASE_ID", "LABEL","TYPE", "CURRENCY", "LAST_CLOSE_VALUE_IN_CURR"], "date":date}
    res = requests.get(uri, params = payload, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri: " + uri)
    return json.loads(res.text)

def test(asset):
    return asset["TYPE"]["value"] == "STOCK"

def get_list_stock():
    list_asset = get_list_asset()
    res = list(filter(test, list_asset))
    return res

def get_change_rate(date, src_currency, tgt_currency):
    uri = url + "currency/rate/" + src_currency + "/to/" + tgt_currency
    payload = {"date": date}
    res = requests.get(uri, params = payload, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri:" + uri)
    return json.loads(res.text)["rate"]["value"]

def get_ratio_list():
    uri = url + "ratio/"
    res = requests.get(uri, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri: " + uri)
    return json.loads(res.text)

def get_last_close_value(asset_id, date):
    uri = url + "asset/" + str(asset_id) + "/attribute/LAST_CLOSE_VALUE"
    payload = {"date": date}
    res = requests.get(uri, params = payload, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri: " + uri)
    return json.loads(res.text)

def get_quote_list(asset_id, start_date, end_date):
    uri = url + "asset/" + str(asset_id) + "/quote"
    payload = {"sart_date": start_date, "end_date": end_date}
    res = requests.get(uri, params = payload, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri: " + uri)
    return json.loads(res.text)

def update_portfolio(_portfolio_id, new_portfolio): #faire attention à l'objet portfolio
    uri = url + "portfolio/" + _portfolio_id + "/dyn_amount_compo"
    res = requests.put(uri, new_portfolio)
    if (res.status_code != 200):
        print("Error with uri: " + uri)
        return False
    print("Update OK")
    return True