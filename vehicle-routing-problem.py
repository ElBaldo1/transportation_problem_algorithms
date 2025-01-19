from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value
import pandas as pd

# Nodes and Distance Matrix
nodes = ["D", 1, 2, 3, 4, 5, 6]
distance_matrix = [
    [0, 20, 18, 14, 16, 12, 19],
    [20, 0, 22, 18, 30, 26, 28],
    [18, 22, 0, 32, 20, 22, 21],
    [14, 18, 32, 0, 20, 22, 21],
    [16, 30, 20, 20, 0, 30, 22],
    [12, 26, 22, 22, 30, 0, 26],
    [19, 28, 21, 21, 22, 26, 0],
]
demands = [0, 4, 6, 3, 5, 3, 6]  # Demands for each node (0 for depot)
truck_capacity = 15  # Maximum capacity per truck

# Create LP problem
problem = LpProblem("Vehicle_Routing", LpMinimize)

# Decision variables
x = [[LpVariable(f"x_{i}_{j}", cat="Binary") for j in range(len(nodes))] for i in range(len(nodes))]
f = [[LpVariable(f"f_{i}_{j}", lowBound=0, cat="Continuous") for j in range(len(nodes))] for i in range(len(nodes))]

# Objective function: Minimize total distance
problem += lpSum(distance_matrix[i][j] * x[i][j] for i in range(len(nodes)) for j in range(len(nodes)) if i != j)

# Constraints
# Each client is visited exactly once
for j in range(1, len(nodes)):
    problem += lpSum(x[i][j] for i in range(len(nodes)) if i != j) == 1
    problem += lpSum(x[j][i] for i in range(len(nodes)) if i != j) == 1

# Flow constraints for demand satisfaction
for i in range(1, len(nodes)):
    problem += lpSum(f[j][i] for j in range(len(nodes)) if j != i) - lpSum(f[i][j] for j in range(len(nodes)) if j != i) == demands[i]

# Ensure flow happens only on selected routes
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i != j:
            problem += f[i][j] <= truck_capacity * x[i][j]

# No self-loops
for i in range(len(nodes)):
    problem += x[i][i] == 0

# Solve the problem
problem.solve()

# Extract solution
routes = []
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if x[i][j].varValue > 0.5:
            routes.append((nodes[i], nodes[j], distance_matrix[i][j]))

# Group routes by vehicles
vehicle_routes = {}
visited = set()
for route in routes:
    start, end, cost = route
    if start == "D":  # Start of a route
        current_vehicle = f"Vehicle {len(vehicle_routes) + 1}"
        vehicle_routes[current_vehicle] = [(start, end, cost)]
        visited.add(end)
    elif end == "D":  # End of a route
        vehicle_routes[current_vehicle].append((start, end, cost))
    elif start in visited:  # Continue existing route
        vehicle_routes[current_vehicle].append((start, end, cost))
        visited.add(end)

# Print the solution
print("Objective Value (Total Distance):", value(problem.objective))
total_distance = 0
for vehicle, route in vehicle_routes.items():
    print(f"\n{vehicle} Route:")
    vehicle_distance = 0
    for leg in route:
        print(f"{leg[0]} -> {leg[1]} with cost {leg[2]}")
        vehicle_distance += leg[2]
    print(f"Total Distance for {vehicle}: {vehicle_distance}")
    total_distance += vehicle_distance

print(f"\nTotal Distance for All Vehicles: {total_distance}")

# Create table for each vehicle
for vehicle, route in vehicle_routes.items():
    data = []
    for i, (start, end, cost) in enumerate(route):
        data.append({"i-j": f"{start}-{end}", "Sij": cost, "Selected": "✓"})

    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j and distance_matrix[i][j] > 0 and (nodes[i], nodes[j], distance_matrix[i][j]) not in route:
                data.append({"i-j": f"{nodes[i]}-{nodes[j]}", "Sij": distance_matrix[i][j], "Selected": "✗"})

    # Filter rows where Sij > 0
    df = pd.DataFrame(data)
    df = df[df['Sij'] > 0].sort_values(by="Sij", ascending=False).reset_index(drop=True)
    print(f"\nTable for {vehicle}:")
    print(df)
