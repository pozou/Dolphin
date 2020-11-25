from pprint import pprint

import requests
import json
import portfolio
import ratioParamMultiAsset

host_name = "dolphin.jump-technology.com"
port = 8443
username = "EPITA_GROUPE13"
password = "XMkT6qVPZ4CFkjxh"

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
    res = requests.get(uri, params={'date': '2016-06-01'},auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri: " + uri)
    return json.loads(res.text)

def get_asset(asset_id, date):
    uri = url + "asset/" + str(asset_id)
    payload = {"columns": ["ASSET_DATABASE_ID", "LABEL","TYPE", "CURRENCY", "LAST_CLOSE_VALUE_IN_CURR"], "date":date}
    res = requests.get(uri, params=payload, auth=(username, password))
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
    res = requests.get(uri, params=payload, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri:" + uri)
    return json.loads(res.text)["rate"]["value"]

def get_last_close_value(asset_id, date):
    uri = url + "asset/" + str(asset_id) + "/attribute/LAST_CLOSE_VALUE"
    payload = {"date": date}
    res = requests.get(uri, params=payload, auth=(username, password))
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

def format_asset(asset):
    return {'asset': asset}

def update_portfolio(_portfolio_id, new_portfolio): #faire attention à l'objet portfolio
    uri = url + "portfolio/" + str(_portfolio_id) + "/dyn_amount_compo"
    list_asset_formated = list(map(format_asset, new_portfolio))
    list_asset_formated.append({'currency': {'amount': 300.0,
                                         'currency': {'code': 'EUR'}}})
    payload = {"id": portfolio_id,"label": "EPITA_PTF_13", "currency": {'code': 'EUR'}, "type": "front", "values": { "2016-06-01": list_asset_formated}}
    try :
        res = requests.put(uri, data=json.dumps(payload), auth=(username, password))
        res.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    if (res.status_code != 200):
        print("Error with uri: " + uri)
        print(res.status_code)
        print(res.text)
        return False
    print("Update OK")
    return True

def get_ratio_list():
    uri = url + "ratio/"
    res = requests.get(uri, auth=(username, password))
    if (res.status_code != 200):
        print("Error with uri: " + uri)
    return json.loads(res.text)

def get_ratio_sharpe():
    ratio_list = get_ratio_list()
    res = list(filter(test_ratio, ratio_list))
    return res

def test_ratio(ratio):
    return ratio["id"] == portfolio.sharpe_id

def invoke_ratio(ratio_id, asset_list, benchmark, start_date, end_date):
    uri = url + "ratio/invoke"
    ratio_param_multi_asset = ratioParamMultiAsset.ratioParamMultiAsset(ratio_id, asset_list, benchmark, start_date, end_date).to_json()
    res = requests.post(uri, auth=(username, password), data=ratio_param_multi_asset)
    if (res.status_code != 200):
        print("Error with uri: " + uri)
    return json.loads(res.text)
