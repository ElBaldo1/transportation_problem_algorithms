from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Definisci il problema
problem = LpProblem("Minimum_Cost_Flow", LpMinimize)

# Definisci le variabili decisionali per gli archi (x_ij rappresenta il flusso da nodo i a nodo j)
x12 = LpVariable("x12", lowBound=0)
x13 = LpVariable("x13", lowBound=0)
x24 = LpVariable("x24", lowBound=0)
x25 = LpVariable("x25", lowBound=0)
x34 = LpVariable("x34", lowBound=0)
x35 = LpVariable("x35", lowBound=0)
x45 = LpVariable("x45", lowBound=0)

# Funzione obiettivo (sostituisci i costi con i costi degli archi del tuo grafo)
# al posto di 4,8 ecc meetere il costo dellarco
problem += 5 * x12 + 8 * x13 + 5 * x24 + 6 * x34 + 7 * x25 + 3 * x35 + 4 * x45, "Total Cost"

# Vincoli per la conservazione del flusso in ogni nodo
# Nodo 1 (supply): Nodo 1 fornisce 6 unità
# mettere il numero che ce sopra il nodo
problem += x12 + x13 == 6, "Node_1"

# Nodo 2 (transshipment): Nodo 2 è un nodo intermedio senza offerta o domanda netta
problem += x12 - x24 - x25 == 0, "Node_2"

# Nodo 3 (supply): Nodo 3 fornisce 4 unità
problem += x13 - x34 - x35 == 4, "Node_3"

# Nodo 4 (demand): Nodo 4 richiede 5 unità
problem += x24 + x34 - x45 == -5, "Node_4"

# Nodo 5 (demand): Nodo 5 richiede 5 unità
problem += x25 + x35 + x45 == -5, "Node_5"

# Risolvi il problema
problem.solve()

# Stampa i risultati
print("Status:", problem.status)
print("Valore della funzione obiettivo (Costo Minimo):", problem.objective.value())
print("Flussi:")
for v in problem.variables():
    print(f"{v.name}: {v.varValue}")
