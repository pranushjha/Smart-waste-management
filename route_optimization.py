import heapq

def dijkstra(graph, start):
    heap = [(0, start)]  # (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# Define the waste bin graph
graph = {
    'Bin1': {'Bin2': 1.5, 'Bin3': 2.8},
    'Bin2': {'Bin1': 1.5, 'Bin3': 1.2, 'Bin4': 2.0},
    'Bin3': {'Bin1': 2.8, 'Bin2': 1.2, 'Bin4': 1.5, 'Bin5': 3.0},
    'Bin4': {'Bin2': 2.0, 'Bin3': 1.5, 'Bin5': 2.5},
    'Bin5': {'Bin3': 3.0, 'Bin4': 2.5}
}

# Find shortest paths from Bin1
shortest_paths = dijkstra(graph, 'Bin1')
print("🚛 Optimized Garbage Collection Routes from Bin1:", shortest_paths)
