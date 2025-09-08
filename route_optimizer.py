import heapq

# Step 1: Define the graph (Bins & Roads)
graph = {
    'Bin1': {'Bin2': 1.5, 'Bin3': 2.8},
    'Bin2': {'Bin1': 1.5, 'Bin3': 1.2, 'Bin4': 2.0},
    'Bin3': {'Bin1': 2.8, 'Bin2': 1.2, 'Bin4': 1.5, 'Bin5': 3.0},
    'Bin4': {'Bin2': 2.0, 'Bin3': 1.5, 'Bin5': 2.5},
    'Bin5': {'Bin3': 3.0, 'Bin4': 2.5}
}

# Step 2: Implement Dijkstra's Algorithm
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

# Step 3: Run Algorithm for a Specific Starting Bin
start_bin = 'Bin1'
shortest_paths = dijkstra(graph, start_bin)

print(f"📍 Shortest Paths from {start_bin}:")
for bin, distance in shortest_paths.items():
    print(f"➡️  {bin}: {distance} km")

