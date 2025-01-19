from pulp import LpProblem, LpMinimize, LpVariable, PULP_CBC_CMD

# Define the problem
# This is a linear programming problem to minimize the total cost of flow in a network
problem = LpProblem("Minimum_Cost_Flow", LpMinimize)

# Define decision variables (flows on edges)
# Each variable represents the flow along an edge in the network, with a lower bound of 0 (non-negative flow)
x12 = LpVariable("x12", lowBound=0)  # Flow from node 1 to node 2
x13 = LpVariable("x13", lowBound=0)  # Flow from node 1 to node 3
x24 = LpVariable("x24", lowBound=0)  # Flow from node 2 to node 4
x25 = LpVariable("x25", lowBound=0)  # Flow from node 2 to node 5
x34 = LpVariable("x34", lowBound=0)  # Flow from node 3 to node 4
x35 = LpVariable("x35", lowBound=0)  # Flow from node 3 to node 5
x45 = LpVariable("x45", lowBound=0)  # Flow from node 4 to node 5

# Define the objective function (minimize total cost)
# The objective is to minimize the total cost associated with the flows on each edge
problem += (
    5 * x12 + 8 * x13 + 5 * x24 + 6 * x34 + 3 * x25 + 7 * x35 + 4 * x45
), "Total Cost"

# Flow conservation constraints
# Node 1 (Supply): Total flow out of node 1 must equal 6 units
# all positive ---> furniture node
problem += x12 + x13 == 6, "Node_1_Supply"

# Node 2 (Balance): Flow into node 2 equals flow out of node 2
problem += x12 - x24 - x25 == 0, "Node_2_Balance"

# Node 3 (Supply): Total flow out of node 3 must exceed flow into node 3 by 4 units
problem += x13 - x34 - x35 == 4, "Node_3_Supply"

# Node 4 (Demand): Total flow into node 4 minus flow out must equal -5 (demand)
problem += x24 + x34 - x45 == -5, "Node_4_Demand"

# Node 5 (Demand): Total flow into node 5 must equal -5 (demand)
## all plus demand-only node
problem += x25 + x35 + x45 == -5, "Node_5_Demand"

# Debugging: Print the problem formulation
print("=== Linear Programming Problem ===")
print(problem)

# Solve the problem with CBC solver
problem.solve(PULP_CBC_CMD(msg=True))

# Output the results
print("\n=== RESULTS ===")

# Status of the solution
status_dict = {
    1: "Optimal",   # Solution found and satisfies all constraints
    0: "Not Solvable",  # Problem is unsolvable
    -1: "Infeasible",  # Constraints conflict, no solution exists
    -2: "Unbounded",  # Problem is unbounded (objective can go to infinity)
    -3: "Error"       # An error occurred during solving
}
print(f"Solution Status: {status_dict.get(problem.status, 'Unknown')}")

# Value of the objective function (minimum total cost)
if problem.status == 1:  # If the solution is optimal
    print(f"Minimum Total Cost: {problem.objective.value()}\n")

    # Print the optimal flow on each edge (only if the flow > 0)
    print("Optimal Flows on Edges:")
    for v in problem.variables():
        if v.varValue > 0:
            print(f"  {v.name}: {v.varValue} units")

    # Print the edges with no flow (optional for analysis)
    print("\nEdges with No Flow:")
    for v in problem.variables():
        if v.varValue == 0:
            print(f"  {v.name}: {v.varValue} units")
else:
    print("The problem could not be solved due to infeasibility or other issues.")
