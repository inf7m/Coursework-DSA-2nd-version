from property_agent import PropertyAgent

class Director(PropertyAgent):
    def __init__(self, name, reg_no, company, start_year, sharing_rate=0.75, override_rate=0.05):
        super().__init__(name, reg_no, company, start_year, sharing_rate)
        self.override_rate = override_rate
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def calculate_override(self):
        total = 0
        for agent in self.agents:
            total += agent.calculate_commission() * self.override_rate
        return total
