from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Create the LP problem
problem = LpProblem("Shortest_Path_Problem", LpMinimize)

# Define decision variables (x_ij is 1 if edge (i, j) is selected, 0 otherwise)
x12 = LpVariable("x12", 0, 1, cat="Binary")
x13 = LpVariable("x13", 0, 1, cat="Binary")
x24 = LpVariable("x24", 0, 1, cat="Binary")
x25 = LpVariable("x25", 0, 1, cat="Binary")
x34 = LpVariable("x34", 0, 1, cat="Binary")
x36 = LpVariable("x36", 0, 1, cat="Binary")
x45 = LpVariable("x45", 0, 1, cat="Binary")
x46 = LpVariable("x46", 0, 1, cat="Binary")
x47 = LpVariable("x47", 0, 1, cat="Binary")
x57 = LpVariable("x57", 0, 1, cat="Binary")
x67 = LpVariable("x67", 0, 1, cat="Binary")

# Define the objective function (minimize total cost)
problem += lpSum([
    15 * x12 + 20 * x13 + 10 * x24 + 15 * x34 + 25 * x25 + 20 * x36 +
    20 * x45 + 30 * x47 + 15 * x46 + 10 * x57 + 20 * x67
]), "Total Cost"

# Add constraints
problem += x12 + x13 == 1, "Source_Node_1"
problem += -x12 + x24 + x25 == 0, "Node_2"
problem += -x13 + x34 + x36 == 0, "Node_3"
problem += -x24 - x34 + x45 + x46 + x47 == 0, "Node_4"
problem += -x25 - x45 + x57 == 0, "Node_5"
problem += -x36 - x46 + x67 == 0, "Node_6"
problem += -x67 - x47 - x57 == -1, "Sink_Node_7"

# Solve the problem
problem.solve()

# Output the results (only status, objective value, and selected edges)
print("Status:", problem.status)
print("Objective Value (Total Cost):", problem.objective.value())
print("Selected Edges:")
for v in problem.variables():
    if v.varValue > 0:
        print(f"{v.name}: {v.varValue}")
