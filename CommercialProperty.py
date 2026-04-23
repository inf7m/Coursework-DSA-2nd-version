from property import Property

class CommercialProperty(Property):
    def __init__(self, address, postal_code, tenure, year, ptype, area, valuation, commercial_type):
        super().__init__(address, postal_code, tenure, year, ptype, area, valuation)
        self.commercial_type = commercial_type
