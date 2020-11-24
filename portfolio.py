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
    portfolio_amount = 0
    if (portfolio_size < nb_asset_min) :
        print("portfolio size: " + str(portfolio_size) + " is less than the minimal required size: " + str(nb_asset_min))
        return False
    if (portfolio_size > nb_asset_max):
        print("portfolio size: " + str(portfolio_size) + " is more than the maximal required size: " + str(nb_asset_max))
        return False
    rate = stock_rate(values, portfolio_size)
    if rate > 50.0: # voir si ça fait bien la virgule
        print("the rate of stocks : " + rate + "% is more than the required 50%")
        return False
    return True

def stock_rate(portfolio_values, nb_assets):
    rate = 0
    nb_stocks = 0
    for value in portfolio_values:
        if value['TYPE']['value'] == 'STOCK': # à tester
            nb_stocks += 1
    if nb_stocks == 0 or nb_assets == 0:
        return 0
    rate = 100 * float(nb_stocks)/float(nb_assets)
    return rate