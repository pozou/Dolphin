from pprint import pprint

import restManager
import portfolio
import reference

if __name__ == "__main__":
    print("Main function")

    port = portfolio.generate_portfolio()
    port2 = portfolio.post_treatment(port)
    restManager.update_portfolio(restManager.portfolio_id, port2)
    restManager.update_portfolio(restManager.portfolio_id, port2)