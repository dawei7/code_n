# TSP via Reduced Matrix (Branch and Bound)

| | |
|---|---|
| **ID** | `bb_06` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(N!)$ Schlechtester Fall |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) |

## Problemstellung

Gegeben ist eine $N \times N$ Matrix, die die Distanzen zwischen Städten repräsentiert. Finden Sie die absolut kürzeste, optimale Travelling Salesman Tour.
Im Gegensatz zu Approximationen (`approx_03`, `approx_04`) müssen Sie die **exakte** optimale Lösung finden.
Im Gegensatz zur Dynamischen Programmierung (Held-Karp `graph_20`, welche $O(N^2 2^N)$ Platz benötigt und bei $N=30$ abstürzt), müssen Sie **Branch and Bound** mit Matrixreduktion verwenden. Dieses Verfahren benötigt sehr wenig Speicherplatz und beschneidet den Suchbaum stark, um im Durchschnitt deutlich größere Datensätze zu lösen.

**Eingabe:** Eine $N \times N$ Adjazenzmatrix mit Ganzzahlen.
**Ausgabe:** Die minimale Gesamtdistanz der exakten optimalen Tour.

## Wann man es verwendet

- Um die exakte mathematische minimale Route für ein Travelling Salesman Problem zu finden, wenn $N$ etwa zwischen 20 und 60 liegt.

## Ansatz

Wir untersuchen den Zustandsraum-Baum, wobei Ebene 0 die Startstadt ist, Ebene 1 die Wahl der nächsten Stadt usw.
Um eine Best-First Search Branch and Bound-Suche durchzuführen, benötigen wir eine extrem präzise mathematische Formel für die **untere Schranke** (Lower Bound). Wenn wir uns aktuell in Stadt 2 befinden, was ist die absolut minimale Distanz, die erforderlich ist, um die Tour zu beenden?
Wir berechnen dies mithilfe der **Reduced Matrix**-Technik!

1. **Matrixreduktion:** Eine Matrix ist "reduziert", wenn jede Zeile und jede Spalte mindestens eine `0` enthält.
   - Um eine Zeile zu reduzieren, finden Sie das kleinste Element und subtrahieren dieses Minimum von jeder Zelle in der Zeile.
   - Um eine Spalte zu reduzieren, finden Sie das kleinste Element und subtrahieren es von jeder Zelle in der Spalte.
   - **Die entscheidende Erkenntnis:** Der Gesamtbetrag, den wir von allen Zeilen und Spalten subtrahiert haben, ist die absolute mathematische untere Schranke für die Kosten *jeder* Tour, die diese Matrix verwendet! (Da jede Stadt betreten und verlassen werden muss, *müssen* Sie mindestens das Zeilenminimum und das Spaltenminimum bezahlen).

2. **Branching:** Wenn wir uns in Stadt $i$ befinden und entscheiden, nach Stadt $j$ zu reisen:
   - Die Kosten für diesen spezifischen Zweig sind: `cost_matrix[i][j]`.
   - Wir erstellen eine neue Matrix für diesen Kindknoten. Da wir $i$ verlassen und in $j$ angekommen sind, können wir $i$ nicht erneut verlassen oder $j$ erneut betreten! Wir setzen Zeile $i$ und Spalte $j$ auf unendlich (`inf`).
   - Wir können auch nicht direkt von $j$ zum Start unseres Pfades zurückkehren, daher setzen wir `cost_matrix[j][start_city] = inf`.
   - Nun **reduzieren wir diese neue Kindmatrix**.
   - Die untere Schranke für diesen Kindknoten ist: `Parent_Bound + cost_matrix[i][j] + Total_Reduction_Cost_Of_Child_Matrix`.

3. **Best-First Search:** Fügen Sie alle Kindknoten in eine Priority Queue ein, sortiert nach dieser unteren Schranke. Erweitern Sie immer den Knoten mit der niedrigsten Schranke, bis wir einen Blattknoten (eine vollständige Tour) erreichen. Da es sich um einen Min-Heap handelt, ist die erste vollständige Tour, die entnommen wird, garantiert optimal!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bb_06: TSP via Reduced Matrix (B&B).

Solve the traveling salesman problem using the
"""


def solve(cost, n):
    """TSP via reduced-matrix LC branch and bound.

    Each live node has: (lb, path, matrix, cost_so_far).
    Lower bound = path cost + row/column reduction cost.
    Branching: include or exclude the next edge from the
    current node to an unvisited city.
    """
    INF = float("inf")
    N_MAX = 12
    if n <= 1:
        return 0
    if n == 2:
        return cost[0][1] + cost[1][0]

    def reduce(mat):
        """Return (reduced_matrix, reduction_cost)."""
        red = [row[:] for row in mat]
        reduction = 0
        # Row reduction.
        for i in range(n):
            finite = [v for v in red[i] if v < INF]
            if not finite:
                continue
            min_val = min(finite)
            if min_val == 0:
                continue
            reduction += min_val
            for j in range(n):
                if red[i][j] < INF:
                    red[i][j] -= min_val
        # Column reduction.
        for j in range(n):
            col_vals = [red[i][j] for i in range(n) if red[i][j] < INF]
            if not col_vals:
                continue
            min_val = min(col_vals)
            if min_val == 0:
                continue
            reduction += min_val
            for i in range(n):
                if red[i][j] < INF:
                    red[i][j] -= min_val
        return red, reduction

    # Each priority queue entry:
    # (lb, path_tuple, matrix, cost_so_far, parent_reduction)
    # lb = cost_so_far + (current reduction). The reduction at
    # this node has been accounted for in `lb`; for the child,
    # we use: new_lb = lb + edge_cost + (new_reduction - old_reduction).
    import heapq
    root_red, root_red_cost = reduce(cost)
    pq = [(root_red_cost, (0,), tuple(tuple(row) for row in root_red), 0, root_red_cost)]
    best = INF
    while pq:
        lb, path, mat_t, cost_so_far, parent_red = heapq.heappop(pq)
        if lb >= best:
            continue
        if len(path) == n:
            # Complete tour: return to start.
            total = cost_so_far + cost[path[-1]][0]
            if total < best:
                best = total
            continue
        # Branch: try each unvisited city from path[-1].
        cur = path[-1]
        for nxt in range(n):
            if nxt in path:
                continue
            edge_cost = cost[cur][nxt]
            if edge_cost >= INF:
                continue
            new_mat = [list(row) for row in mat_t]
            for j in range(n):
                new_mat[cur][j] = INF
            for i in range(n):
                new_mat[i][nxt] = INF
            new_mat[nxt][0] = INF
            new_red, new_red_cost = reduce(new_mat)
            new_lb = lb + edge_cost + (new_red_cost - parent_red)
            if new_lb < best:
                new_path = path + (nxt,)
                heapq.heappush(pq, (new_lb, new_path,
                                    tuple(tuple(row) for row in new_red),
                                    cost_so_far + edge_cost,
                                    new_red_cost))
    return best if best < INF else -1
```

</details>

## Durchlauf

*(Konzeptionell)*
Wenn durch das Reduzieren der Wurzelmatrix 10 von den Zeilen und 5 von den Spalten subtrahiert werden, betragen die absoluten Minimalkosten *jeder* Tour 15. Der Wurzelknoten wird mit `cost=15` in den Heap geschoben.

Wurzel entnehmen. Versuche die Reise `0 -> 1`.
- Die Distanz `matrix[0][1]` war 3 (nach der Wurzelreduktion).
- Erstelle Kindmatrix. Setze Zeile 0 und Spalte 1 auf `inf`. Setze `1 -> 0` auf `inf`.
- Reduziere Kindmatrix. Angenommen, die Reduktion kostet 2.
- Schranke für den Zweig `0 -> 1` = `Parent_Cost (15) + Edge (3) + Child_Reduction (2) = 20`.
- In den Heap schieben.

Wenn `0 -> 2` zu einer Schranke von 18 führt, wird die Priority Queue zuerst `0 -> 2` erweitern!

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^3)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | Viel schneller als DP! | $O(Nodes * N^2)$ |
| **Schlechtester Fall** | $O(N!)$ | $O(N! * N^2)$ |

Im absoluten mathematischen Schlechtesten Fall, in dem kein Beschneiden (Pruning) stattfindet, expandiert der Baum $N!$ Blätter, und an jedem Knoten führen wir eine $O(N^2)$ Matrixkopie und -reduktion durch!
Da die untere Schranke der Matrixreduktion jedoch erstaunlich präzise und genau ist, steuert die Best-First Search bei praktischen Datensätzen (z. B. 40 Städte) direkt auf die Lösung zu und untersucht nur einen winzigen Bruchteil des Baumes.
Die Platzkomplexität ist hoch, da jeder Knoten in der Priority Queue eine eindeutige $N \times N$ Matrix speichert.

## Varianten & Optimierungen

- **Held-Karp DP:** Das exakte Gegenstück. Held-Karp benötigt für *jeden* Graphen exakt $O(N^2 2^N)$ Zeit und Platz. B&B benötigt unvorhersehbare Zeit, skaliert aber oft besser auf größere $N$, da es die vollständige Untersuchung des Zustandsraums vermeidet.

## Anwendungen in der Praxis

- **Supply Chain Logistik:** Berechnung exakter minimaler Routendistanzen für die LKW-Flottenverteilung, bei denen Treibstoffkosten zwingend das absolute mathematische Minimum erfordern.

## Verwandte Algorithmen in cOde(n)

- **[graph_20 - TSP Held Karp DP](../graphs/graph_20_travelling-salesman-held-karp-dp.md)** — Die exakte Lösung mittels Dynamischer Programmierung für dasselbe Problem.
- **[bb_02 - Job Assignment (Hungarian)](bb_02_job-assignment-hungarian.md)** — Die Matrixreduktion ist exakt derselbe fundamentale Mechanismus, der den ungarischen Algorithmus zur Zuordnung antreibt!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*