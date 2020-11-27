from pprint import pprint

import restManager
import portfolio
import reference

if __name__ == "__main__":
    print("Main function")

    #pprint(portfolio.sharpe_id)
    #pprint(restManager.get_portfolio(restManager.portfolio_id))

    port = portfolio.generate_portfolio()
    port2 = portfolio.post_treatment(port)
    pprint(port2)
    pprint(len(port2))

    #pprint(portfolio.sharpe_id)
    #pprint(portfolio.check_portfolio_conditions(restManager.portfolio_id))
    pprint(restManager.get_portfolio(restManager.portfolio_id))
    #pprint(restManager.get_list_stock())
    #restManager.update_portfolio(restManager.portfolio_id, port)

    #tmp = portfolio.generate_portfolio()
    #pprint(restManager.get_portfolio(1832))
    restManager.update_portfolio(restManager.portfolio_id, port2)
    print("------------")
    restManager.update_portfolio(restManager.portfolio_id, port2)

    pprint(restManager.invoke_ratio([portfolio.sharpe_id], [restManager.portfolio_id], 0, portfolio.period_start_date,
                                    portfolio.period_end_date))

    #pprint(restManager.invoke_ratio([11], [1956], 1918, portfolio.period_start_date,
    #                                portfolio.period_end_date))

    #pprint(portfolio.ratio_correlation(1956, 1918))
