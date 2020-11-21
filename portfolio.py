import restManager

nb_actif = 20

def generate_portfolio():
    portfolio = []
    list_asset = restManager.get_list_stock()
    i = 0
    while len(portfolio) < nb_actif:
        portfolio.append(list_asset[i])
        i += 1
    return portfolio # Bad Object