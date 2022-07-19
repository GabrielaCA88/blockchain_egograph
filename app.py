import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
weight_df = pd.read_csv ('weight_df.csv')
weight_df = weight_df.loc[(weight_df['count'] > 2)]

G = nx.Graph()
G = nx.from_pandas_edgelist(weight_df, 'origen', 'destinatario', edge_attr='count')
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["count"] > weight_df["count"].quantile(0.5)]  #mas del 50%
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["count"] <= weight_df["count"].quantile(0.5)]

figure(figsize=(20, 15))
pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
# nodes
nx.draw_networkx_nodes(G, pos, node_size=700) #
# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, edge_color="r")
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=2, alpha=0.5, edge_color="b", style="dashed"
)

# node labels
nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif")

# edge weight labels
edge_labels = nx.get_edge_attributes(G, "count")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.savefig('graph')
plt.show()

#inspired by https://networkx.org/documentation/latest/auto_examples/drawing/plot_weighted_graph.html#sphx-glr-auto-examples-drawing-plot-weighted-graph-py
