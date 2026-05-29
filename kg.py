import networkx as nx
import matplotlib.pyplot as plt
# Create Directed Graph
G = nx.DiGraph()
# Knowledge Base Relationships
relations = [
    ("Goa", "Beach", "has_type"),
    ("Hyderabad", "Biryani", "famous_for"),
    ("Manali", "Snow", "has_weather"),
    ("Jaipur", "Palace", "known_for"),
    ("Ooty", "Tea", "produces"),
    ("Goa", "Seafood", "famous_food"),
    ("Manali", "Mountains", "has_terrain"),
    ("Hyderabad", "Charminar", "contains"),
    ("Jaipur", "Tourism", "supports"),
    ("Ooty", "Nature", "attracts")
]
# Add edges
for source, target, relation in relations:
    G.add_edge(source, target, relation=relation)
# Print relationships
print("\n========== TOURISM KNOWLEDGE GRAPH ==========\n")
for source, target, data in G.edges(data=True):
    print(source,
          "-->",
          data['relation'],
          "-->",
          target)

# Better Layout
pos = nx.spring_layout(
    G,
    k=1.8,
    iterations=100,
    seed=42
)
# Large Figure
plt.figure(figsize=(14, 10))
# Draw Nodes
nx.draw_networkx_nodes(
    G,
    pos,
    node_size=3500,
    alpha=0.95
)
# Draw Edges
nx.draw_networkx_edges(
    G,
    pos,
    edge_color="black",
    arrows=True,
    arrowsize=25,
    width=2,
    connectionstyle="arc3,rad=0.1"
)
# Node Labels
nx.draw_networkx_labels(
    G,
    pos,
    font_size=10,
    font_weight='bold'
)
# Edge Labels
edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=8,
    rotate=False
)
# Title
plt.title(
    "AI Tourism Knowledge Graph",
    fontsize=20,
    fontweight='bold'
)
# Remove axis
plt.axis('off')
# Tight layout
plt.tight_layout()
# Show graph
plt.show()