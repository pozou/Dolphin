from pprint import pprint

import restManager
import portfolio
import reference

if __name__ == "__main__":
    print("Main function")
    res = restManager.get_asset(1855, "2019-06-01")
    pprint(res)
    blou = portfolio.generate_portfolio()
    restManager.update_portfolio(restManager.portfolio_id, blou)
    #pprint(restManager.get_last_close_value(1900, "2019-06-20"))
    #pprint(restManager.get_last_close_value(1900, "2016-06-20"))
    #pprint(restManager.get_quote_list(1900, "2016-06-20", "2019-06-20"))
    #pprint(restManager.get_portfolio(restManager.portfolio_id))
    #pprint(portfolio.check_portfolio_conditions(restManager.portfolio_id))