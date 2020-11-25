import restManager
from pprint import pprint
nb_actif = 2
nb_asset_min = 15
nb_asset_max = 40

sharpe_id = 12

period_start_date = "2016-06-01"
period_end_date = "2020-09-30"


def generate_portfolio():
    portfolio = []
    list_asset = restManager.get_list_stock()
    i = 0
    while len(portfolio) < nb_actif:
        tmp = {"quantity": 5.0, "asset": int(list_asset[i]["ASSET_DATABASE_ID"]["value"])}
        portfolio.append(tmp)
        i += 1
    return portfolio


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
    values = portfolio["values"]
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
