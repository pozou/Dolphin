import json

import requests

import restManager
from pprint import pprint
nb_actif = 20
nb_asset_min = 15
nb_asset_max = 40

sharpe_id = 12

period_start_date = "2016-06-01"
period_end_date = "2020-09-30"

def convert_currency(currency, value):
    uri = restManager.url + 'currency/rate/' + currency + '/to/EUR'
    req = requests.get(uri, params={'date': period_start_date}, auth=(restManager.username, restManager.password))
    rate = float((json.loads(req.text)['rate']['value']).replace(',', '.'))
    converted_value = float(value.replace(',', '.').replace(' '+currency, ''))
    return converted_value * rate

def generate_portfolio():
    portfolio = []
    list_asset = restManager.get_list_stock()
    i = 0
    money_total = 10000
    money_res = 0
    while len(portfolio) < nb_actif:
        try:
            if list_asset[i]['CURRENCY']['value'] != 'EUR':
                value = convert_currency(list_asset[i]['CURRENCY']['value'], list_asset[i]['LAST_CLOSE_VALUE_IN_CURR']['value'])
            else:
                value = float(list_asset[i]['LAST_CLOSE_VALUE_IN_CURR']['value'].replace(',', '.').replace(' EUR', ''))
        except:
            i += 1
            continue
        quantity = int((money_total / value) * (1 / nb_actif))

        # Trie des assets ici
        asset_id = list_asset[i]['ASSET_DATABASE_ID']['value']
        #
        # ratio de sharpe d'un actif
        sharpe_actif = float(restManager.invoke_ratio([sharpe_id], [asset_id], 0, period_start_date, period_end_date)[str(asset_id)][str(sharpe_id)]['value'].replace(',', '.'))
        #pprint(sharpe_actif)
        if  sharpe_actif > 0.8:
            tmp = {"quantity": quantity, "asset": int(list_asset[i]["ASSET_DATABASE_ID"]["value"])}
            portfolio.append(tmp)
            money_res += quantity * value + 1
            print("len portofolio : ", len(portfolio))
        i += 1
    print("PORTFOLIO GENERATED")
    print(money_res)
    return (portfolio, money_total)


'''
def generate_fifty_percent_best_stocks(list_stock):
    assets = []
    for asset in list_stock:
        if asset["MARKET_PLACE_CURRENCY"]["value"] != "EUR":
            restManager.get_change_rate()
    return assets
'''

'''
Conditions :
    - Le portefeuille doit être exactement composé d'un minimum de 15 actifs, et d'un maximum de 40 actifs.
    - Chaque actif doit représenter un %NAV du portefeuille entre 1 et 10% à la date du 01/06/2016
    - Le portefeuille n'aura qu'une unique composition commençant le 01/06/2016
    _ On évaluera le sharpe sur la période du 01/06/2016 au 30/09/2020
    - Le portefeuille devra comporter au moins 50% d'actions
    => Tout est en montant et pas en quantité
'''


def check_portfolio_conditions(portfolio_id):
    portfolio = restManager.get_portfolio(portfolio_id)
    values = portfolio["values"][period_start_date]
    portfolio_size = len(values)
    portfolio_amount = 0
    if (portfolio_size < nb_asset_min):
        print(
            "portfolio size: " + str(portfolio_size) + " is less than the minimal required size: " + str(nb_asset_min))
        return False
    if (portfolio_size > nb_asset_max):
        print(
            "portfolio size: " + str(portfolio_size) + " is more than the maximal required size: " + str(nb_asset_max))
        return False
    rate = stock_rate(values, portfolio_size)
    if rate > 50.0:  # voir si ça fait bien la virgule
        print("the rate of stocks : " + rate + "% is more than the required 50%")
        return False
    return True


def stock_rate(portfolio_values, nb_assets):
    rate = 0
    nb_stocks = 0
    for value in portfolio_values:
        if value["TYPE"]["value"] == "STOCK":  # à tester
            nb_stocks += 1
    if nb_stocks == 0 or nb_assets == 0:
        return 0
    rate = 100 * float(nb_stocks) / float(nb_assets)
    return rate
