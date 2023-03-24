import random
from complexity import constants
import random


def generar_grafo_con_pesos(n, m, min_weight=1, max_weight=10):
    nodes = [str(i) for i in range(n)]
    graph = {node: {} for node in nodes}
    edges = set()
    while len(edges) < m:
        root, end = random.sample(nodes, 2)
        edge = (root, end) if root < end else (end, root)
        edges.add(edge)

    for root, end in edges:
        weight = random.randint(min_weight, max_weight)
        graph[root][end] = weight
        graph[end][root] = weight

    for node in nodes:
        neighbors = list(graph[node].keys())
        if not neighbors:
            neighbor = random.choice(nodes)
            weight = random.randint(min_weight, max_weight)
            graph[node][neighbor] = weight
            graph[neighbor][node] = weight
        else:
            missing_neighbor = set(nodes) - set(neighbors) - set([node])
            if missing_neighbor:
                neighbor = random.choice(list(missing_neighbor))
                weight = random.randint(min_weight, max_weight)
                graph[node][neighbor] = weight
                graph[neighbor][node] = weight

    return graph
