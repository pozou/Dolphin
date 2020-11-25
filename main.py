from pprint import pprint

import restManager
import portfolio
import reference

if __name__ == "__main__":
    print("Main function")
    res = restManager.get_asset(1855, "2019-06-01")
    portfolio = portfolio.generate_portfolio()
    pprint(restManager.invoke_ratio([12], [1832], 0, "2016-06-01", "2020-09-30"))
    #pprint(restManager.get_list_stock())
    #restManager.update_portfolio(restManager.portfolio_id, portfolio)
    #pprint(restManager.get_last_close_value(1900, "2019-06-20"))
    #pprint(restManager.get_last_close_value(1900, "2016-06-20"))
    #pprint(restManager.get_quote_list(1900, "2016-06-20", "2019-06-20"))
    #pprint(restManager.get_portfolio(restManager.portfolio_id))
    #pprint(portfolio.check_portfolio_conditions(restManager.portfolio_id))

