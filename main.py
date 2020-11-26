from pprint import pprint

import restManager
import portfolio
import reference

if __name__ == "__main__":
    print("Main function")
    res = restManager.get_asset(1855, "2019-06-01")

    tmp = portfolio.generate_portfolio()
    pprint(portfolio.sharpe_id)
    pprint(restManager.get_portfolio(restManager.portfolio_id))

    #port = portfolio.generate_portfolio()
    #pprint(portfolio.sharpe_id)

    pprint(restManager.invoke_ratio([portfolio.sharpe_id], [restManager.portfolio_id], 0, portfolio.period_start_date,
                                    portfolio.period_end_date))
    pprint(portfolio.check_portfolio_conditions(restManager.portfolio_id))
    pprint(restManager.get_portfolio(restManager.portfolio_id))
    #pprint(restManager.get_list_stock())
    #restManager.update_portfolio(restManager.portfolio_id, port)


