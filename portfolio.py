import restManager

nb_actif = 20
nb_asset_min = 15
nb_asset_max = 40

def generate_portfolio():
    portfolio = []
    list_asset = restManager.get_list_stock()
    i = 0
    while len(portfolio) < nb_actif:
        portfolio.append(list_asset[i])
        i += 1
    return portfolio # Bad Object

def check_portfolio_conditions(portfolio_id):
    portfolio = restManager.get_portfolio(portfolio_id)
    values = portfolio['values']
    portfolio_size = len(values)
    if (portfolio_size < nb_asset_min) :
        print("portfolio size: " + str(portfolio_size) + " is less than the minimal required size: " + str(nb_asset_min))
        return False
    if (portfolio_size > nb_asset_max):
        print("portfolio size: " + str(portfolio_size) + " is more than the maximal required size: " + str(nb_asset_max))
        return False
    return True