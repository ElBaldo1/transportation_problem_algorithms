import matplotlib.pyplot as plt
import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Numero di nodi
        self.adj_list = {i: [] for i in range(vertices)}  # Lista di adiacenza

    def add_edge(self, u, v, w):
        self.adj_list[u].append((w, v))
        self.adj_list[v].append((w, u))

    def prim_mst(self):
        mst_edges = []  # Lista degli archi del MST
        visited = [False] * self.vertices
        min_heap = []

        # Inizia dal nodo 0
        visited[0] = True
        for weight, v in self.adj_list[0]:
            heapq.heappush(min_heap, (weight, 0, v))

        total_cost = 0

        step = 1  # Contatore per i passi
        while min_heap:
            weight, u, v = heapq.heappop(min_heap)

            if not visited[v]:
                visited[v] = True
                mst_edges.append((u, v, weight))
                total_cost += weight

                print(f"Passo {step}:")
                print(f"Aggiunto arco ({u + 1}-{v + 1}) con peso {weight}")
                print(f"Insieme S1: {sorted([i + 1 for i, vis in enumerate(visited) if vis])}")
                print(f"Insieme S2: {sorted([i + 1 for i, vis in enumerate(visited) if not vis])}\n")
                step += 1

                self.plot_partial_mst(mst_edges, visited)

                for next_weight, next_vertex in self.adj_list[v]:
                    if not visited[next_vertex]:
                        heapq.heappush(min_heap, (next_weight, v, next_vertex))

        return mst_edges, total_cost

    def plot_partial_mst(self, mst, visited):
        # Definizione dei nodi e delle loro posizioni per il grafo
        positions = {
            0: (0, 2),  # Nodo 1
            1: (1, 3),  # Nodo 2
            2: (1, 1),  # Nodo 3
            3: (2, 3),  # Nodo 4
            4: (2, 1),  # Nodo 5
        }

        plt.figure(figsize=(6, 6))

        # Disegna gli archi del MST
        for u, v, w in mst:
            x1, y1 = positions[u]
            x2, y2 = positions[v]
            plt.plot([x1, x2], [y1, y2], 'b-', linewidth=2)

        # Disegna i nodi
        for node, (x, y) in positions.items():
            color = 'green' if visited[node] else 'red'
            plt.scatter(x, y, c=color, s=100, zorder=5)
            plt.text(x, y + 0.1, f"{node + 1}", fontsize=12, ha='center')

        plt.title("Minimum Spanning Tree - Stato Parziale")
        plt.axis('off')
        plt.show()

# Definizione del grafo
graph = Graph(5)  # 5 nodi nel grafo
graph.add_edge(0, 1, 5)  # Arco tra nodo 1 e 2 con peso 5
graph.add_edge(0, 2, 6)  # Arco tra nodo 1 e 3 con peso 6
graph.add_edge(1, 4, 6)  # Arco tra nodo 2 e 5 con peso 6
graph.add_edge(2, 4, 6)  # Arco tra nodo 3 e 5 con peso 6
graph.add_edge(1, 2, 7)  # Arco tra nodo 2 e 3 con peso 7
graph.add_edge(2, 3, 8)  # Arco tra nodo 3 e 4 con peso 8
graph.add_edge(3, 4, 8)  # Arco tra nodo 4 e 5 con peso 8

# Calcola il MST
mst, total_cost = graph.prim_mst()

# Stampa il risultato finale
print("Archi del Minimum Spanning Tree:")
print("\nARC\tW")
for u, v, w in mst:
    print(f"{u + 1}-{v + 1}\t{w}")

print(f"\nTotal Cost (TC): {total_cost}")
