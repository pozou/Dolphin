from pprint import pprint

import restManager

if __name__ == "__main__":
    print("Main function")
    res = restManager.get_asset(1900, "2019-06-20")
    pprint(restManager.get_change_rate("2019-06-20", "USD", "EUR"))