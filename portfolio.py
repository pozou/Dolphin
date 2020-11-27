import json
import requests

import restManager
from pprint import pprint

nb_actif = 40
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
    sharpe_actif_min = 0.8
    sharpe_actif_max = 1000.0
    print(len(list_asset))
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

        # ratio de sharpe d'un actif
        sharpe_actif = float(restManager.invoke_ratio([sharpe_id], [asset_id], 0, period_start_date, period_end_date)[str(asset_id)][str(sharpe_id)]['value'].replace(',', '.'))
        '''
        #-------------------
        correlation = ratio_correlation(1832, asset_id)
        ratio_sharpe_correlation = sharpe_actif / correlation
        if sharpe_actif > 0.8 and ratio_sharpe_correlation > 5.0:
            print("id asset : ", asset_id, " sharpe : ", sharpe_actif, " correlation : ", correlation,
                  " ratio sharpe/correlation : ", float(sharpe_actif / correlation))
            tmp = {"quantity": quantity, "asset": int(list_asset[i]["ASSET_DATABASE_ID"]["value"])}
            portfolio.append(tmp)
            print("len portofolio : ", len(portfolio))
        i += 1
        #-------------------
        '''
        if sharpe_actif > sharpe_actif_min:
            correlation = ratio_correlation(1832, asset_id)
            ratio_sharpe_correlation = sharpe_actif / correlation
            if (sharpe_actif > sharpe_actif_max):
                i += 1
                continue
            tmp = {"quantity": quantity, "asset": int(list_asset[i]["ASSET_DATABASE_ID"]["value"])}
            portfolio.append(tmp)
            print("len portofolio : ", len(portfolio))

            print("id asset : ", asset_id, " sharpe : ", sharpe_actif, " correlation : ", correlation, " ratio sharpe/correlation : ", ratio_sharpe_correlation)
        i += 1
        if (i >= len(list_asset)):
            i = 0
            sharpe_actif_max = sharpe_actif_min
            sharpe_actif_min -= 0.1
    print("PORTFOLIO GENERATED")
    return portfolio

def max_list(l):
    index_max = 0
    value_max = l[0]
    i = 1
    while i < len(l):
        if (l[i] > value_max):
            index_max = i
            value_max = l[i]
        i += 1
    return index_max, value_max

def post_treatment(portfolio):
    tmp = portfolio.copy()
    restManager.update_portfolio(restManager.portfolio_id, portfolio)
    restManager.update_portfolio(restManager.portfolio_id, portfolio)
    base_sharpe = float(restManager.invoke_ratio([sharpe_id], [restManager.portfolio_id], 0, period_start_date,
                                    period_end_date)[str(restManager.portfolio_id)][str(sharpe_id)][
                'value'].replace(',', '.'))
    print(base_sharpe)
    while (len(portfolio) > 15):
        ratio_sharpe_list = []
        for i in range(0, len(portfolio) - 1):
            asset = tmp.pop(i)
            restManager.update_portfolio(restManager.portfolio_id, tmp)
            restManager.update_portfolio(restManager.portfolio_id, tmp)
            ratio_sharpe_list.append(float(restManager.invoke_ratio([sharpe_id], [restManager.portfolio_id], 0, period_start_date,
                                    period_end_date)[str(restManager.portfolio_id)][str(sharpe_id)][
                'value'].replace(',', '.')))
            tmp = portfolio.copy()
        index_max, sharpe_max = max_list(ratio_sharpe_list)
        print(ratio_sharpe_list)
        if (sharpe_max < base_sharpe):
            break
        else:
            portfolio.pop(index_max)
            base_sharpe = sharpe_max
            tmp = portfolio.copy()
            pprint(index_max)
            pprint(sharpe_max)
    return portfolio




def ratio_correlation(benchmark, asset):
        return float(restManager.invoke_ratio([11], [asset], benchmark, period_start_date, period_end_date)[str(asset)]['11'][
                'value'].replace(',', '.'))

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
    if (portfolio_size < nb):
        print(
            "portfolio size: " + str(portfolio_size) + " is less than the minimal required size: " + str(nb_asset_min))
        return False
    if (portfolio_size > nb_asset_max):
        print(
            "portfolio size: " + str(portfolio_size) + " is more than the maximal required size: " + str(nb_asset_max))
        return False
    '''
    rate = stock_rate(values, portfolio_size)
    if rate > 50.0:  # voir si ça fait bien la virgule
        print("the rate of stocks : " + rate + "% is more than the required 50%")
        return False
    '''
    return True

def stock_rate(portfolio_values, nb_assets):
    rate = 0
    nb_stocks = 0
    for value in portfolio_values:
        if value["TYPE"]["value"] == "STOCK":
            nb_stocks += 1
    if nb_stocks == 0 or nb_assets == 0:
        return 0
    rate = 100 * float(nb_stocks) / float(nb_assets)
    return rate
