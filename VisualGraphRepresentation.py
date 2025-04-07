import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define adjacency matrix (example: 4-node undirected graph)
adjacency_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
])

# Create graph from adjacency matrix
G = nx.Graph(adjacency_matrix)

# Set up plot
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Layout algorithm

# Draw nodes and edges
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7)
nx.draw_networkx_labels(G, pos, font_size=12)

# Customize plot
plt.title("Graph Visualization from Adjacency Matrix", size=15)
plt.axis('off')  # Remove axes
plt.tight_layout()
plt.show()
