import restManager

ref_id = 2201

def get_reference():
    return restManager.get_portfolio(ref_id)
