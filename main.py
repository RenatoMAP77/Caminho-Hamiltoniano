# main.py

def is_valid(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonian_util(graph, path, pos):
    if pos == len(graph):
        return graph[path[pos - 1]][path[0]] == 1

    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_util(graph, path, pos + 1):
                return True
            path[pos] = -1  # backtrack
    return False

def find_hamiltonian_path(graph):
    path = [-1] * len(graph)
    path[0] = 0  # começa no vértice 0

    if not hamiltonian_util(graph, path, 1):
        return None
    return path

# Exemplo simples de grafo (matriz de adjacência)
if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    result = find_hamiltonian_path(graph)
    if result:
        print("Caminho Hamiltoniano encontrado:", result)
    else:
        print("Não existe Caminho Hamiltoniano.")
