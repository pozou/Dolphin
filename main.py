from pprint import pprint

import restManager
import portfolio
import reference

if __name__ == "__main__":
    print("Main function")

    #pprint(portfolio.sharpe_id)
    #pprint(tmp)
    #pprint(restManager.get_portfolio(restManager.portfolio_id))

    #port = portfolio.generate_portfolio()
    #pprint(portfolio.sharpe_id)
    #pprint(portfolio.check_portfolio_conditions(restManager.portfolio_id))
    pprint(restManager.get_portfolio(restManager.portfolio_id))
    #pprint(restManager.get_list_stock())
    #restManager.update_portfolio(restManager.portfolio_id, tmp, money_total)

    #tmp = portfolio.generate_portfolio()
    #pprint(restManager.get_portfolio(1832))
    #restManager.update_portfolio(restManager.portfolio_id, tmp)
    #print("------------")
    #restManager.update_portfolio(restManager.portfolio_id, tmp)

    pprint(restManager.invoke_ratio([portfolio.sharpe_id], [reference.ref_id], 0, portfolio.period_start_date,
                                    portfolio.period_end_date))

    #pprint(restManager.invoke_ratio([portfolio.sharpe_id], [restManager.portfolio_id], 0, portfolio.period_start_date,
    #                                portfolio.period_end_date))

    #pprint(restManager.invoke_ratio([11], [1956], 1918, portfolio.period_start_date,
    #                                portfolio.period_end_date))

    #pprint(portfolio.ratio_correlation(1956, 1918))
