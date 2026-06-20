# TSP über reduzierte Matrix (Branch-and-Bound)

| | |
|---|---|
| **ID** | `bb_06` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(N!)$ Worst Case |
| **Schwierigkeitsgrad** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Handelsreisendenproblem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) |

## Problemstellung

Gegeben ist eine N × N-Matrix, die die Entfernungen zwischen Städten darstellt. Finden Sie die absolut kürzeste optimale Route für das Handelsreisendenproblem.
Im Gegensatz zu Approximationen (`approx_03`, `approx_04`) muss die **exakte** optimale Lösung gefunden werden.
Im Gegensatz zur dynamischen Programmierung (Held-Karp `graph_20`, die $O(N^2 2^N)$ Speicherplatz benötigt und bei N=30 abstürzt), müssen Sie **Branch-and-Bound** mit Matrixreduktion verwenden, was sehr wenig Speicherplatz benötigt und den Suchbaum stark beschneidet, um im Durchschnittlicher Fall viel größere Datensätze zu lösen.

**Eingabe:** Eine N × N-Adjacency Matrix aus ganzen Zahlen.
**Ausgabe:** Die minimale Gesamtentfernung der exakten optimalen Route.

## Wann man es verwendet

- Um die exakte mathematische Minimalroute für ein Handlungsreisenden-Problem zu finden, wenn N ungefähr zwischen 20 und 60 liegt.

## Vorgehensweise

Wir durchlaufen den Zustandsraumbaum, wobei Ebene 0 die Startstadt ist, Ebene 1 die Auswahl der nächsten Stadt usw.
Um „Branch and Bound“ mit Best-First-Suche anzuwenden, benötigen wir eine äußerst präzise mathematische Formel für die **untere Schranke**. Wenn wir uns gerade in Stadt 2 befinden, wie groß ist dann die absolut minimale Entfernung, die erforderlich ist, um die Tour zu beenden?
Wir berechnen dies mithilfe der **reduzierten Matrix**-Technik!

1. **Matrixreduktion:** Eine Matrix ist „reduziert“, wenn jede Zeile und jede Spalte mindestens ein `0` enthält.
   - Um eine Zeile zu reduzieren, suche ihr kleinstes Element und ziehe dieses Minimum von jeder Zelle in der Zeile ab.
   - Um eine Spalte zu reduzieren, suche ihr kleinstes Element und ziehe es von jeder Zelle in der Spalte ab.
   - **Die entscheidende Erkenntnis:** Die Gesamtsumme, die wir von allen Zeilen und Spalten abgezogen haben, ist die absolute mathematische Untergrenze der Kosten für *jede* Tour, die diese Matrix nutzt! (Da jede Stadt betreten und wieder verlassen werden muss, *muss* man mindestens das Zeilenminimum und das Spaltenminimum bezahlen).

2. **Verzweigung:** Wenn wir uns in Stadt i befinden und beschließen, nach Stadt j zu reisen:
   - Die Kosten für diese spezifische Verzweigung betragen: `cost_matrix[i][j]`.
   - Wir erstellen eine neue Matrix für diesen untergeordneten Knoten. Da wir i verlassen und in j angekommen sind, können wir i nicht erneut verlassen oder erneut in j ankommen! Wir setzen Zeile i und Spalte j auf unendlich (`inf`).
   - Wir können auch nicht direkt von j zum Anfang unseres Pfades zurückkehren, daher setzen wir `cost_matrix[j][start_city] = inf`.
   - Nun **reduzieren wir diese neue Kindmatrix**.
   - Die untere Grenze für diesen Kindknoten lautet: `Parent_Bound + cost_matrix[i][j] + Total_Reduction_Cost_Of_Child_Matrix`.

3. **Best-First-Suche:** Füge alle untergeordneten Knoten in eine Priority Queue ein, sortiert nach dieser unteren Grenze. Erweitere immer den Knoten mit der niedrigsten Grenze, bis wir einen Blattknoten erreichen (eine vollständige Tour). Da es sich um einen Min-Heap handelt, ist garantiert, dass die erste entnommene vollständige Tour optimal ist!

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
Wenn bei der Reduktion der Wurzelmatrix 10 von den Zeilen und 5 von den Spalten abgezogen werden, betragen die absoluten Mindestkosten *jeder* Tour 15. Der Wurzelknoten wird mit `cost=15` in den Heap geschoben.

Wurzel entfernen. Versuche, `0 -> 1` zu durchlaufen.
- Die Entfernung `matrix[0][1]` betrug 3 (nach der Reduktion der Wurzel).
- Erstelle eine Kindmatrix. Setze Zeile 0 und Spalte 1 auf `inf`. Setze `1 -> 0` auf `inf`.
- Reduziere die Kindmatrix. Angenommen, die Reduktion kostet 2.
- Grenze für den Zweig `0 -> 1` = `Parent_Cost (15) + Edge (3) + Child_Reduction (2) = 20`.
- Auf den Heap schieben.

Wenn `0 -> 2` zu einer Grenze von 18 führt, wird die Priority Queue zuerst `0 -> 2` erweitern!

## Komplexität

| | Zeit | Speicher |
|---|---|---|
| **Bestfall** | $O(N^3)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | Viel schneller als DP! | $O(Nodes * N^2)$ |
| **Schlimmster Fall** | $O(N!)$ | $O(N! * N^2)$ |

Im absolut mathematischen Worst-Case-Szenario, in dem kein Pruning stattfindet, erweitert sich der Baum auf N! Blätter, und an jedem Knoten führen wir eine $O(N^2)$ Matrixkopie und -reduktion durch!
Die untere Schranke der Matrixreduktion ist jedoch so erstaunlich eng und genau, dass die Best-First-Suche bei praktischen Datensätzen (z. B. 40 Städte) direkt zur Lösung gelangt und dabei nur einen winzigen Bruchteil des Baums durchforstet.
Die Platzkomplexität ist hoch, da jeder Knoten in der Priority Queue eine eindeutige N × N-Matrix enthält.

## Varianten und Optimierungen

- **Held-Karp-DP:** Das genaue Gegenteil dieses Paradigmas. Held-Karp benötigt für *jeden* Graphen genau $O(N^2 2^N)$ Zeit und Speicherplatz. B&B benötigt unvorhersehbare Zeit, skaliert jedoch oft auf größere N-Werte, da es die Erkundung des gesamten Zustandsraums vermeidet.

## Anwendungen in der Praxis

- **Lieferkettenlogistik:** Berechnung der exakten minimalen Routenentfernungen für den Lkw-Vertrieb, bei dem die Kraftstoffkosten streng das absolute mathematische Minimum erfordern.

## Verwandte Algorithmen in cOde(n)

- **[graph_20 – TSP Held-Karp-DP](../graphs/graph_20_travelling-salesman-held-karp-dp.md)** — Die exakte Lösung mittels dynamischer Programmierung für dasselbe Problem.
- **[bb_02 – Jobzuordnung (ungarisch)](bb_02_job-assignment-hungarian.md)** – Die Matrixreduktion ist genau derselbe grundlegende Mechanismus, der den ungarischen Zuordnungsalgorithmus antreibt!

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
