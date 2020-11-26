from pprint import pprint

import restManager
import portfolio
import reference

if __name__ == "__main__":
    print("Main function")

    #pprint(restManager.get_portfolio(restManager.portfolio_id))

    #port = portfolio.generate_portfolio()

    #restManager.update_portfolio(restManager.portfolio_id, port)

    pprint(restManager.invoke_ratio([portfolio.sharpe_id], [reference.ref_id], 0, portfolio.period_start_date,
                                    portfolio.period_end_date))

    pprint(restManager.invoke_ratio([11], [1956], 1918, portfolio.period_start_date,
                                    portfolio.period_end_date))

    #pprint(portfolio.check_portfolio_conditions(restManager.portfolio_id))
    pprint(restManager.get_portfolio(restManager.portfolio_id))
    #pprint(restManager.get_list_stock())


