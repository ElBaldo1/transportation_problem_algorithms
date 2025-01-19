import matplotlib.pyplot as plt


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Numero di nodi
        self.edges = []  # Lista degli archi (peso, nodo1, nodo2)

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        # Ordina gli archi in base al peso
        self.edges.sort()

        parent = []
        rank = []

        # Inizializza i sottoinsiemi
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        mst = []  # Lista per memorizzare gli archi del MST

        for edge in self.edges:
            w, u, v = edge

            # Trova i rappresentanti dei sottoinsiemi per u e v
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            # Se u e v non creano un ciclo, aggiungi l'arco al MST
            if root_u != root_v:
                mst.append((u, v, w))
                self.union(parent, rank, root_u, root_v)

        return mst

    def plot_mst(self, mst):
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
            plt.plot([x1, x2], [y1, y2], 'b-', linewidth=2, label=f"{u + 1}-{v + 1}")

        # Disegna i nodi
        for node, (x, y) in positions.items():
            plt.scatter(x, y, c='red', s=100, zorder=5)
            plt.text(x, y + 0.1, f"{node + 1}", fontsize=12, ha='center')

        plt.title("Minimum Spanning Tree")
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
mst = graph.kruskal_mst()

# Stampa la tabella degli archi selezionati
print("Archi del Minimum Spanning Tree:")
print("\nARC\tW")
total_cost = 0
for u, v, w in mst:
    print(f"{u + 1}-{v + 1}\t{w}")
    total_cost += w

print(f"\nTotal Cost (TC): {total_cost}")

# Mostra il grafico del MST
graph.plot_mst(mst)
