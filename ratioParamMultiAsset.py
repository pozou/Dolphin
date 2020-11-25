import json

class ratioParamMultiAsset:
    def __init__(self, ratio, asset, benchmark, start_date, end_date):
        self.ratio = ratio
        self.asset = asset
        self.benchmark = benchmark
        self.start_date = start_date
        self.end_date = end_date

    def to_json(self):
        return json.dumps(self, default=lambda l: l.__dict__)#, sort_keys=True, indent=4)
