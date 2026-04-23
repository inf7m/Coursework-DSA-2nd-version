class PropertyAgent:
    def __init__(self, name, reg_no, company, start_year, sharing_rate=0.7):
        self.name = name
        self.reg_no = reg_no
        self.company = company
        self.start_year = start_year
        self.sharing_rate = sharing_rate
        self.unsold = []
        self.sold = []

    def add_property(self, prop):
        self.unsold.append(prop)

    def sell_property(self, prop):
        if prop in self.unsold:
            self.unsold.remove(prop)
            self.sold.append(prop)

    def calculate_commission(self):
        total = 0
        for p in self.sold:
            total += p.valuation * p.commission_rate * self.sharing_rate
        return total
