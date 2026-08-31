import heapq

def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

    return float('inf'), []

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'C': 2, 'D': 2},
    'C': {'G': 5},
    'D': {'G': 1},
    'G': {}
}

cost, path = uniform_cost_search(graph, 'A', 'G')
print(f"Path: {path}, Total Cost: {cost}")
