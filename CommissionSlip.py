class CommissionSlip:

    @staticmethod
    def print_agent(agent):
        print(f"\nAgent: {agent.name}")
        total = 0
        for p in agent.sold:
            commission = p.valuation * p.commission_rate * agent.sharing_rate
            total += commission
            print(f"Property {p.address}: ${commission:.2f}")
        print(f"Total: ${total:.2f}")

    @staticmethod
    def print_director(director):
        CommissionSlip.print_agent(director)
        override = director.calculate_override()
        print(f"Override Commission: ${override:.2f}")
        print(f"Total Income: ${(override + director.calculate_commission()):.2f}")
