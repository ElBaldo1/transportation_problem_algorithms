import numpy as np

# Dati iniziali
distance_matrix = np.array([
    [0, 43, 61, 29, 41, 48, 71],
    [43, 0, 27, 36, 65, 65, 65],
    [61, 27, 0, 40, 66, 62, 46],
    [29, 36, 40, 0, 31, 31, 43],
    [41, 65, 66, 31, 0, 11, 46],
    [48, 65, 62, 31, 11, 0, 36],
    [71, 65, 46, 43, 46, 36, 0]
])
demands = [0, 4, 7, 3, 5, 3, 4]
truck_capacity = 15

savings = {}
for i in range(1, len(distance_matrix)):
    for j in range(i + 1, len(distance_matrix)):
        savings[(i, j)] = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]

savings = dict(sorted(savings.items(), key=lambda x: x[1], reverse=True))

routes = []
node_list = set(range(1, len(demands)))

def sum_cap(route):
    return sum(demands[node] for node in route)

def interior(node, route):
    return 0 < route.index(node) < len(route) - 1

def merge(route1, route2):
    return route1[:-1] + route2[1:]

for (i, j), saving in savings.items():
    route_i = None
    route_j = None
    for route in routes:
        if i in route:
            route_i = route
        if j in route:
            route_j = route

    if route_i is None and route_j is None:
        if demands[i] + demands[j] <= truck_capacity:
            routes.append([0, i, j, 0])
            node_list -= {i, j}
    elif route_i is not None and route_j is None:
        if not interior(i, route_i) and sum_cap(route_i) + demands[j] <= truck_capacity:
            if route_i[-2] == i:
                route_i.insert(-1, j)
            else:
                route_i.insert(1, j)
            node_list.remove(j)
    elif route_i is None and route_j is not None:
        if not interior(j, route_j) and sum_cap(route_j) + demands[i] <= truck_capacity:
            if route_j[-2] == j:
                route_j.insert(-1, i)
            else:
                route_j.insert(1, i)
            node_list.remove(i)
    elif route_i != route_j:
        if not interior(i, route_i) and not interior(j, route_j):
            if sum_cap(route_i) + sum_cap(route_j) <= truck_capacity:
                routes.remove(route_i)
                routes.remove(route_j)
                routes.append(merge(route_i, route_j))
                node_list -= {i, j}

for node in node_list:
    routes.append([0, node, 0])

print("Routes found:")
for route in routes:
    print(route)

# Calcolo della distanza totale per i percorsi trovati
total_distance = 0

for route in routes:
    route_distance = 0
    for k in range(len(route) - 1):
        route_distance += distance_matrix[route[k]][route[k + 1]]
    total_distance += route_distance
    print(f"Route: {route}, Distance: {route_distance} km")

print(f"\nTotal Distance for all routes: {total_distance} km")
