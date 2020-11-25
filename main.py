from pprint import pprint

import restManager
import portfolio
import reference

if __name__ == "__main__":
    print("Main function")
    res = restManager.get_asset(1900, "2019-06-20")
    pprint(res)
    pprint("test")
    #pprint(restManager.get_last_close_value(1900, "2019-06-20"))
    #pprint(restManager.get_last_close_value(1900, "2016-06-20"))
    pprint(restManager.invoke_ratio([portfolio.sharpe_id], [1832], 0, "2016-06-20", "2019-06-20"))
