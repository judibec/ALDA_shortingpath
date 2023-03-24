import heapq

"""
O(V+E log V) v = vertex; e = edges
"""


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node].items():
            dist = curr_dist + weight
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))
    return distances


"""
O(VE) v = vertex; e = edges
"""


def bellman_ford(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    return distances


"""
O(v^3) v = vertex
"""


def floyd_warshall(graph, value):
    distance = {}
    for u in graph:
        distance[u] = {}
        for v in graph:
            distance[u][v] = float("inf")
        distance[u][u] = 0
        for neighbor, weight in graph[u].items():
            distance[u][neighbor] = weight

    for intermediate in graph:
        for u in graph:
            for v in graph:
                new_distance = distance[u][intermediate] + distance[intermediate][v]
                if new_distance < distance[u][v]:
                    distance[u][v] = new_distance

    return distance["0"]
