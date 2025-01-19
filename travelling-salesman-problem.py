import numpy as np

def nearest_neighbor_tsp(distance_matrix, start_node=0):
    n = len(distance_matrix)  # Number of nodes
    visited = [False] * n  # Track visited nodes
    path = [start_node]  # Start from the start node
    visited[start_node] = True
    total_cost = 0

    for _ in range(n - 1):
        current_node = path[-1]
        # Find the nearest unvisited neighbor
        nearest = None
        nearest_distance = float('inf')

        for neighbor in range(n):
            if not visited[neighbor] and distance_matrix[current_node][neighbor] < nearest_distance:
                nearest = neighbor
                nearest_distance = distance_matrix[current_node][neighbor]

        path.append(nearest)
        visited[nearest] = True
        total_cost += nearest_distance

    # Return to the start node to complete the cycle
    total_cost += distance_matrix[path[-1]][start_node]
    path.append(start_node)

    return path, total_cost

# Distance matrix (i numeri nella tabella)
distance_matrix = [
    [0, 10, 8, 9, 7],
    [10, 0, 10, 5, 6],
    [8, 10, 0, 8, 9],
    [9, 5, 8, 0, 6],
    [7, 6, 9, 6, 0]
]

# Solve the TSP using the nearest neighbor heuristic
start_node = 0  # Starting at node 1 (0-based indexing)
path, total_cost = nearest_neighbor_tsp(distance_matrix, start_node=start_node)

# Output the results
print("Path:", ' -> '.join(map(lambda x: str(x + 1), path)))  # Convert to 1-based indexing
print("Total Cost:", total_cost)
