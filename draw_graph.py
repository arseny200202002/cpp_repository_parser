import networkx as nx
from Graph import Graph
import matplotlib.pyplot as plt
from pyvis.network import Network


import os
cwd = os.getcwd()
ROOT = cwd + "\\CuraEngine"


if __name__ == "__main__":
    graph = Graph(ROOT)
    graph.build_graph()

    G = nx.DiGraph(directed=True)
    G.add_nodes_from(list(graph.files.keys()))
    G.add_edges_from(graph.get_vertexes())
    
    nx.draw(G)
    plt.show()

    g = Network(notebook=True)

