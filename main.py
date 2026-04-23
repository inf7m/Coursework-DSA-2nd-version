from Property import Property
from PropertyAgent import PropertyAgent
from Director import Director
from CommissionSlip import CommissionSlip

def create_properties(n):
    props = []
    for i in range(n):
        props.append(Property(f"Addr{i}", 123456, "Freehold", 2020, "Residential", 100, 100000 + i*10000))
    return props

# Create 2 directors
directors = []

for d in range(2):
    director = Director(f"Director{d}", f"D{d}", "CompanyX", 2010)

    # Each director has 3 agents
    for a in range(3):
        agent = PropertyAgent(f"Agent{d}{a}", f"A{d}{a}", "CompanyX", 2015)

        # 5 unsold
        for p in create_properties(5):
            agent.add_property(p)

        # 3-10 sold
        sold_props = create_properties(3 + a)  # vary 3–5
        for p in sold_props:
            agent.add_property(p)
            agent.sell_property(p)

        director.add_agent(agent)

    directors.append(director)

# Print all
for d in directors:
    print(f"\n=== {d.name} ===")
    for a in d.agents:
        CommissionSlip.print_agent(a)

    CommissionSlip.print_director(d)
