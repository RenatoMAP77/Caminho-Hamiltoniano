# view.py

import networkx as nx
import matplotlib.pyplot as plt
from main import find_hamiltonian_path

def draw_graph(graph_matrix, path=None):
    G = nx.Graph()

    n = len(graph_matrix)
    for i in range(n):
        G.add_node(i)

    for i in range(n):
        for j in range(i + 1, n):
            if graph_matrix[i][j]:
                G.add_edge(i, j)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold')

    # Destaque o caminho Hamiltoniano se existir
    if path:
        hamiltonian_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        hamiltonian_edges.append((path[-1], path[0]))  # Para formar o ciclo
        nx.draw_networkx_edges(G, pos, edgelist=hamiltonian_edges, edge_color='red', width=2)

    plt.title("Grafo com Caminho Hamiltoniano" if path else "Grafo")
    plt.show()

if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    path = find_hamiltonian_path(graph)
    draw_graph(graph, path)
