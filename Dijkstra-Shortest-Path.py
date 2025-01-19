import matplotlib.pyplot as plt
import networkx as nx
import heapq


def dijkstra(graph, start):
    # Priority queue to store (distance, node)
    priority_queue = [(0, start)]

    # Distances dictionary to keep track of shortest path to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Dictionary to store the path taken
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Process each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found, update the distance and path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes


def reconstruct_path(previous_nodes, start, target):
    # Reconstruct the path from start to target
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path


def plot_step_by_step(graph, path, positions):
    # Reset the matplotlib figure numbering
    plt.close('all')

    # Create an empty graph for visualization
    G = nx.DiGraph()

    for i in range(len(path) - 1):
        plt.figure(figsize=(8, 6))

        # Add the current edge to the graph
        G.add_edge(path[i], path[i + 1], weight=graph[path[i]][path[i + 1]])

        # Draw the graph with current edges
        nx.draw(G, positions, with_labels=True, node_color='lightblue', node_size=2000, font_size=15,
                font_weight='bold')
        edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels, font_size=12)

        # Highlight the current nodes and edges in the path
        nx.draw_networkx_edges(G, positions, edgelist=[(path[i], path[i + 1])], edge_color='red', width=2)
        nx.draw_networkx_nodes(G, positions, nodelist=path[:i + 2], node_color='yellow', node_size=2500)

        plt.title(f"Step {i + 1}: Added Edge {path[i]} -> {path[i + 1]}")
        plt.show()


# Define the graph as an adjacency list
# Bidirectional Edges:
# If an edge needs to work both ways (e.g., from 'A' to 'B' and from 'B' to 'A'), you need to define it explicitly in both nodes.
graph = {
    'S': {'A': 4,'C': 8, 'B': 2},
    'A': {'C': 5, 'D': 2},
    'B': {'C': 6, 'E': 9},
    'C': {'A': 5,'D': 1,'T': 4,'E': 3,'B': 6},
    'D': {'A': 2,'C': 1, 'T': 7},
    'E': {'B': 9,'C': 3,'T': 5},
    'T': {}
}

# Define fixed positions for nodes to match desired layout
positions = {
    'S': (0, 2),
    'A': (1, 3),
    'B': (1, 1),
    'C': (2, 2),
    'D': (3, 3),
    'E': (3, 1),
    'T': (4, 2)
}

# Input: Start and Target nodes
start_node = 'S'
target_node = 'T'

# Run Dijkstra's algorithm
distances, previous_nodes = dijkstra(graph, start_node)

# Retrieve and print the shortest path
path = reconstruct_path(previous_nodes, start_node, target_node)

# Plot the step-by-step addition of nodes and edges
plot_step_by_step(graph, path, positions)

# Output the results
print("Shortest distances from start node:", distances)
print("Shortest path from node {} to node {}: {}".format(start_node, target_node, path))
