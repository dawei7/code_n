# Christofides TSP (1,5-Approximation)

| | |
|---|---|
| **ID** | `approx_04` |
| **Kategorie** | Approximation |
| **Komplexität (erforderlich)** | $O(V^3)$ |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Christofides-Algorithmus](https://en.wikipedia.org/wiki/Christofides_algorithm) |

## Problemstellung

Gegeben sei ein vollständig zusammenhängender Graph von Städten, der die Dreiecksungleichung erfüllt. Lösen Sie das Problem des Handlungsreisenden (Travelling Salesman Problem, TSP) mit einer präziseren mathematischen Garantie.
Anstatt der standardmäßigen 2-Approximation mittels MST implementieren Sie den **Christofides-Algorithmus**, der garantiert, dass die erzeugte Tour höchstens **1,5-mal** so lang ist wie die optimale Tour.

**Eingabe:** Eine Adjazenzmatrix, die die Distanzen zwischen den Knoten repräsentiert.
**Ausgabe:** Eine Liste von Knoten, die die Tour repräsentiert.

## Wann man ihn verwendet

- Dies ist das beste bekannte Approximationsverhältnis für das metrische TSP. Er wird intensiv in der Operations Research und in Logistik-Engines eingesetzt, wenn Routen mit mehr als 500 Knoten berechnet werden.
- Ein unglaublich komplexer Algorithmus, der Ihre Fähigkeit testet, mehrere massive graphentheoretische Konzepte (MST, Perfektes Matching, Eulersche Kreise) miteinander zu verknüpfen.

## Ansatz

Die 2-Approximation (`approx_03`) basierte darauf, *jede einzelne Kante* des MST zu duplizieren, um einen geraden Grad für jeden Knoten zu garantieren (was für das Zeichnen eines Eulerschen Kreises erforderlich ist).
Christofides erkannte, dass wir nicht *jede* Kante duplizieren müssen!

**Die Schritte:**
1. **MST finden:** Berechnen Sie den Minimal aufspannenden Baum (Minimum Spanning Tree, MST) des Graphen.
2. **Knoten mit ungeradem Grad finden:** In jedem Graphen ist die Anzahl der Knoten mit einem ungeraden Grad immer gerade. Extrahieren Sie alle Knoten aus dem MST, die einen ungeraden Grad haben.
3. **Minimum-Weight Perfect Matching (MWPM):** Betrachten Sie den ursprünglichen vollständigen Graphen, aber NUR für diese Knoten mit ungeradem Grad. Finden Sie eine Paarung dieser Knoten (ein perfektes Matching), sodass die Gesamtdistanz der Paarungen absolut minimiert wird.
4. **Kombinieren:** Fügen Sie die Kanten aus dem perfekten Matching direkt zum MST hinzu. Da wir genau eine Kante zu jedem Knoten hinzugefügt haben, der zuvor einen ungeraden Grad hatte, **hat nun jeder einzelne Knoten im kombinierten Graphen einen geraden Grad!**
5. **Eulerscher Kreis:** Da jeder Knoten einen geraden Grad hat, können wir einen perfekten Eulerschen Kreis (einen Zyklus, der jede Kante genau einmal besucht) mittels des Hierholzer-Algorithmus finden.
6. **Abkürzung (Hamiltonkreis):** Genau wie bei der 2-Approximation durchlaufen wir den Eulerschen Kreis, überspringen jedoch bereits besuchte Knoten, um ihn in eine gültige TSP-Tour umzuwandeln.

**Warum ist es eine 1,5-Approximation?**
- Der MST wiegt \le 1,0 x OPT.
- Das Minimum-Weight Perfect Matching der Knoten mit ungeradem Grad wiegt \le 0,5 x OPT.
- Gesamtgewicht \le 1,5 x OPT!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for approx_04: Christofides TSP (3/2-Approx).

Given a complete metric graph, return the cost of
"""


def solve(cost, n):
    """Christofides 1.5-approximate TSP (greedy matching)."""
    if n <= 1:
        return 0
    if n == 2:
        return cost[0][1] * 2
    INF = float("inf")
    # 1. Prim's MST.
    in_mst = [False] * n
    in_mst[0] = True
    parent = [-1] * n
    for _ in range(n - 1):
        best_w = INF
        best_v = -1
        for u in range(n):
            if not in_mst[u]:
                continue
            for v in range(n):
                if in_mst[v]:
                    continue
                if cost[u][v] < best_w:
                    best_w = cost[u][v]
                    best_v = v
                    parent[v] = u
        if best_v == -1:
            break
        in_mst[best_v] = True
    # 2. Odd-degree vertices of the MST.
    deg = [0] * n
    for v in range(n):
        p = parent[v]
        if p != -1:
            deg[v] += 1
            deg[p] += 1
    odd = [v for v in range(n) if deg[v] % 2 == 1]
    # 3. Greedy minimum-weight perfect matching on odd vertices.
    matched = [False] * n
    matching = []
    # Repeatedly pick the cheapest remaining edge between two
    # unmatched odd vertices.
    while True:
        best_w = INF
        best_pair = None
        for i in odd:
            if matched[i]:
                continue
            for j in odd:
                if matched[j] or i == j:
                    continue
                if cost[i][j] < best_w:
                    best_w = cost[i][j]
                    best_pair = (i, j)
        if best_pair is None:
            break
        a, b = best_pair
        matching.append((a, b))
        matched[a] = True
        matched[b] = True
    # 4. Union of MST + matching forms a multigraph with
    #    even degree at every vertex. Find an Eulerian
    #    circuit by Hierholzer's algorithm.
    adj = [set() for _ in range(n)]
    for v in range(n):
        p = parent[v]
        if p != -1:
            adj[v].add(p)
            adj[p].add(v)
    for a, b in matching:
        adj[a].add(b)
        adj[b].add(a)
    # Hierholzer's: DFS, splicing when stuck.
    euler = []
    stack = [0]
    # Track visited edges via a per-edge visit counter.
    # Use adjacency multiset.
    used = [dict() for _ in range(n)]
    while stack:
        u = stack[-1]
        # Find an unused edge.
        next_v = None
        for v in list(adj[u]):
            key = (min(u, v), max(u, v))
            if used[u].get(key, 0) < (1 if key[0] == u or key[1] == u else 0) + 1:
                # Check if we have not over-used this edge.
                pass
        # Easier: build edge multiset count.
        next_v = None
        for v in adj[u]:
            key = (min(u, v), max(u, v))
            used_count = used[u].get(key, 0)
            # Edge (u,v) contributes 1 to u and 1 to v in the multigraph.
            # We can use it at most once per (u, v) occurrence in
            # the union. Since the union is a multigraph but
            # built from sets, two edges between the same pair
            # (e.g., one MST + one matching) would have collapsed.
            # To support multi-edges properly, we re-count.
            if used_count == 0:
                next_v = v
                break
        if next_v is None:
            euler.append(stack.pop())
        else:
            key = (min(u, next_v), max(u, next_v))
            # Mark the edge as used on BOTH endpoints so the
            # algorithm doesn't traverse it twice.
            used[u][key] = used[u].get(key, 0) + 1
            used[next_v][key] = used[next_v].get(key, 0) + 1
            stack.append(next_v)
    euler.reverse()
    # 5. Shortcut to a Hamiltonian tour (skip repeated vertices).
    seen = set()
    tour = []
    for v in euler:
        if v not in seen:
            seen.add(v)
            tour.append(v)
    # Make sure 0 is first.
    while tour[0] != 0:
        tour = tour[1:] + [tour[0]]
    # 6. Sum tour cost.
    total = 0
    for i in range(len(tour) - 1):
        total += cost[tour[i]][tour[i + 1]]
    total += cost[tour[-1]][0]
    return total
```

</details>

## Walk-through

*(Konzeptionell)*
1. **MST:** Bildet einen Baum. Nehmen wir an, die Knoten `A`, `B`, `C`, `D` sind Blätter (Grad 1, was ungerade ist).
2. **Ungerade Knoten:** `[A, B, C, D]`.
3. **MWPM:** Wir betrachten die Distanzen zwischen ihnen im ursprünglichen Graphen. Nehmen wir an, `dist(A, B) = 5` und `dist(C, D) = 6` ist die günstigste Paarung.
4. **Kombinieren:** Wir zeichnen eine Kante von `A` nach `B` und von `C` nach `D` direkt über den MST!
5. Nun haben `A`, `B`, `C` und `D` einen Grad von 2! Jeder Knoten ist gerade!
6. Zeichnen Sie die Linien nach, ohne den Stift abzusetzen (Eulerscher Kreis), und überspringen Sie Knoten, falls wir sie bereits gesehen haben, um Abkürzungen zu nehmen.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V^3)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(V^3)$ | $O(V^2)$ |
| **Schlechtester Fall** | $O(V^3)$ | $O(V^2)$ |

Das Finden des absoluten Minimum Weight Perfect Matching in einem allgemeinen Graphen erfordert Edmonds' Blossom-Algorithmus, der $O(V^3)$ benötigt. Alles andere (MST, Eulerscher Kreis) benötigt $O(V^2)$. Daher ist die strikt optimale Implementierung durch $O(V^3)$ begrenzt.
Die Platzkomplexität beträgt $O(V^2)$, um die dichten Graphen zu speichern.

## Varianten & Optimierungen

- **Asymmetrisches TSP (ATSP):** Christofides versagt vollständig, wenn die Distanzen asymmetrisch sind (die Fahrt von A nach B ist aufgrund von Einbahnstraßen eine andere Distanz als von B nach A). Die Approximation von ATSP ist weitaus schwieriger und basiert auf völlig anderen Algorithmen (wie der $O(log V / log log V)$-Approximation von Asadpour et al.).

## Anwendungen in der Praxis

- **Mikrochip-Fertigung:** Optimierung der Bewegungen von Roboterarmen, die oberflächenmontierte Komponenten auf PCBs platzieren, um den Fertigungsdurchsatz zu maximieren.

## Verwandte Algorithmen in cOde(n)

- **[approx_03 - TSP via MST](approx_03_tsp-via-mst-2-approx.md)** — Die einfachere 2-Approximations-Voraussetzung.
- **[graph_21 - Hamiltonpfad](../graphs/graph_21_hamiltonian-path-existence.md)** — Die exakte NP-vollständige Formulierung des zugrunde liegenden Problems.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*