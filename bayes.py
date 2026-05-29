from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

import networkx as nx
import matplotlib.pyplot as plt

# Create Bayesian Network
model = DiscreteBayesianNetwork([

    ('Rain', 'Traffic'),

    ('Rain', 'WetRoad')

])
# Probability of Rain
cpd_rain = TabularCPD(

    variable='Rain',

    variable_card=2,

    values=[

        [0.7],   # No Rain

        [0.3]    # Rain

    ]

)
# Probability of Traffic given Rain
cpd_traffic = TabularCPD(
    variable='Traffic',
    variable_card=2,
    values=[
        [0.9, 0.4],   # No Traffic

        [0.1, 0.6]    # Traffic
    ],
    evidence=['Rain'],
    evidence_card=[2]

)
# Probability of WetRoad given Rain
cpd_wetroad = TabularCPD(
    variable='WetRoad',
    variable_card=2,
    values=[
        [0.95, 0.2],   # Dry Road
        [0.05, 0.8]    # Wet Road
    ],
    evidence=['Rain'],
    evidence_card=[2]
)
model.add_cpds(
    cpd_rain,
    cpd_traffic,
    cpd_wetroad
)
# Check model
print("\n========== BAYESIAN NETWORK ==========\n")
print("Model Valid:", model.check_model())
# Inference
inference = VariableElimination(model)
# Query probability
result = inference.query(
    variables=['Traffic'],
    evidence={'Rain': 1}

)
print("\nProbability of Traffic when Rain occurs:\n")
print(result)
# Graph Visualization
G = nx.DiGraph()
G.add_edges_from([
    ('Rain', 'Traffic'),
    ('Rain', 'WetRoad')

])
# Draw graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=4000,
    font_size=12,
    arrows=True

)
plt.title(
    "Bayesian Network",
    fontsize=18,
    fontweight='bold'
)
plt.show()