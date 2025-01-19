### README for Optimization Algorithms in Transportation

This repository contains Python implementations of algorithms designed to solve transportation problems. These algorithms were developed as part of the Logistics Management course, focusing on optimizing transportation, flow, and routing problems in networks. Each script demonstrates a specific algorithm or problem-solving method with real-world relevance to logistics and supply chain optimization.

---

### File Descriptions

#### 1. **Minimum Spanning Tree – Kruskal’s Algorithm**
   - **File:** `Minimum Spanning Tree – Kruskal’s Algorithm.py`
   - **Description:** Implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph. This is useful for designing efficient transport or distribution networks with minimal cost.
   - **Key Features:**
     - Sorting edges by weight.
     - Union-find operations to avoid cycles.
     - Visualization of the MST using Matplotlib.
   - **Input:** Number of nodes, edges, and their weights.
   - **Output:** Selected edges in the MST and the total cost.

---

#### 2. **Minimum Spanning Tree – Prim’s Algorithm**
   - **File:** `Minimum Spanning Tree – Prim’s Algorithm.py`
   - **Description:** Implements Prim’s algorithm to compute the MST. The algorithm is particularly suitable for scenarios where a connected graph is given as an adjacency list.
   - **Key Features:**
     - Interactive step-by-step construction of the MST.
     - Visualization of partial MST states.
   - **Input:** Graph as an adjacency list.
   - **Output:** Selected edges in the MST, their weights, and the total cost.

---

#### 3. **Minimum Cost Flow Problem**
   - **File:** `minimum-cost-flow-constraint.py`
   - **Description:** Solves the Minimum Cost Flow problem using linear programming techniques. It minimizes transportation costs while satisfying supply and demand constraints.
   - **Key Features:**
     - Formulates flow conservation constraints for each node.
     - Optimizes total transportation costs.
   - **Input:** Supply/demand values, arc capacities, and transportation costs.
   - **Output:** Optimal flow on each arc and the total cost.

---

#### 4. **Shortest Path Problem**
   - **File:** `Shortest-Path-Problem.py`
   - **Description:** Solves the shortest path problem for a transportation network using linear programming. This algorithm ensures the least-cost path from a source to a destination node.
   - **Key Features:**
     - Binary decision variables for edge selection.
     - Constraints to ensure a valid path.
   - **Input:** Cost matrix, source, and sink nodes.
   - **Output:** Total cost and the selected path.

---

#### 5. **Travelling Salesman Problem (TSP)**
   - **File:** `travelling-salesman-problem.py`
   - **Description:** Solves the Travelling Salesman Problem (TSP) using a nearest neighbor heuristic. This problem is a classic example of optimizing a delivery route to minimize travel distance.
   - **Key Features:**
     - Heuristic approach to finding a feasible solution.
     - Computes the total cost and path.
   - **Input:** Distance matrix.
   - **Output:** Approximate optimal path and total cost.

---

#### 6. **Vehicle Routing Problem (VRP)**
   - **File:** `vehicle-routing-problem.py`
   - **Description:** Solves the Vehicle Routing Problem (VRP) using linear programming. The VRP is an extension of the TSP where multiple vehicles with capacity constraints are used.
   - **Key Features:**
     - Capacity constraints for vehicles.
     - Route continuity and flow constraints.
     - Minimizes total transportation cost.
   - **Input:** Distance matrix, demands, and truck capacity.
   - **Output:** Routes for each vehicle, total distance per vehicle, and the overall cost.

---

### Requirements

- **Python 3.x**
- **Libraries:**
  - `matplotlib`
  - `numpy`
  - `pulp`
  - `pandas`

Install the required libraries using:
```bash
pip install matplotlib numpy pulp pandas
```

---

### Usage

Each script is self-contained and includes predefined examples to demonstrate its application. To run a script:
1. Open the file in a Python IDE or text editor.
2. Adjust the input data (e.g., distance matrices, supply/demand values) as needed.
3. Execute the script to view the results, including visualizations and optimized solutions.

---

### Acknowledgments

These algorithms were developed during the Logistics Management course to provide practical insights into transportation and network optimization problems. The repository serves as a resource for students, researchers, and professionals aiming to understand and apply optimization techniques in logistics.

