class Property:
    def __init__(self, address, postal_code, tenure, year, ptype, area, valuation, commission_rate=0.01):
        self.address = address
        self.postal_code = postal_code
        self.tenure = tenure
        self.year = year
        self.ptype = ptype
        self.area = area
        self.valuation = valuation
        self.commission_rate = commission_rate
