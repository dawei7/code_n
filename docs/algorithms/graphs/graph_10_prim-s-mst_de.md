# Prim-Algorithmus (Minimaler Spannbaum)

| | |
|---|---|
| **ID** | `graph_10` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(E log V)$ Zeit, $O(V)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Prim-Algorithmus](https://en.wikipedia.org/wiki/Prim%27s_algorithm) |

## Problemstellung

Gegeben ist ein zusammenhängender, ungerichteter und gewichteter Graph. Finden Sie einen minimalen Spannbaum (Minimum Spanning Tree, MST) für diesen Graphen.
Ein minimaler Spannbaum ist eine Teilmenge der Kanten, die alle $V$ Knoten miteinander verbindet, keine Zyklen enthält und das kleinstmögliche Gesamtgewicht der Kanten aufweist.

**Eingabe:** Anzahl der Knoten `V` und eine Adjazenzliste `adj`, wobei `adj[u] = [(v, weight)]`.
**Ausgabe:** Eine Ganzzahl, die das minimale Gesamtgewicht des MST repräsentiert.

## Wann man ihn verwendet

- Zur Lösung des klassischen Problems des minimalen Spannbaums.
- Wenn der Graph **dicht** ist ($E \approx V^2$), ist der Prim-Algorithmus mathematisch dem Kruskal-Algorithmus überlegen, da er das globale Sortieren mit $O(E log E)$ vermeidet!

## Ansatz

**1. Die Metapher des "wachsenden Baums":**
Im Gegensatz zum Kruskal-Algorithmus (der blind die global günstigsten Kanten wählt und disjunkte Komponenten zusammenfügt), startet der Prim-Algorithmus bei einem einzelnen Wurzelknoten und lässt langsam einen einzigen, vereinten Baum nach außen wachsen.

**2. Die Priority Queue (Der Cousin von Dijkstra):**
Wir führen ein `visited`-Set, um nachzuverfolgen, welche Knoten bereits Teil unseres wachsenden MST sind.
Wir verwalten eine Priority Queue von Kanten, die sich genau an der *Grenze* zwischen unserem MST und den noch nicht besuchten Knoten befinden.
Anfangs wählen wir Knoten `0`, markieren ihn als besucht und fügen alle seine ausgehenden Kanten zur Priority Queue hinzu.

**3. Die gierige Erweiterung:**
Wir entnehmen (pop) die absolut günstigste Kante aus der Priority Queue.
Wenn diese Kante zu einem Knoten `v` führt, der bereits im `visited`-Set enthalten ist, bedeutet dies, dass das Hinzufügen dieser Kante einen Zyklus innerhalb unseres MST erzeugen würde! Wir verwerfen sie.
Wenn `v` noch nicht besucht wurde, haben wir eine gültige Erweiterung gefunden! Wir fügen `v` zum `visited`-Set hinzu, addieren das Gewicht der Kante zu unseren gesamten MST-Kosten und fügen anschließend alle ausgehenden Kanten von `v` zur Priority Queue hinzu, um unsere Grenze zu erweitern!

**4. Terminierung:**
Der Algorithmus terminiert, wenn die Priority Queue leer ist oder wenn das `visited`-Set alle $V$ Knoten enthält.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_10: Prim's MST.

Vertex-growth MST using a min-heap of (weight, from, to) edges.
"""


def solve(num_nodes, edges):
    import heapq
    if num_nodes == 0:
        return []
    adj = [[] for _ in range(num_nodes)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    visited = [False] * num_nodes
    visited[0] = True
    heap = []
    for v, w in adj[0]:
        heapq.heappush(heap, (w, 0, v))
    mst = []
    while heap:
        w, u, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        mst.append((u, v, w))
        for nxt, w2 in adj[v]:
            if not visited[nxt]:
                heapq.heappush(heap, (w2, v, nxt))
    if len(mst) != num_nodes - 1:
        return []
    return sorted(mst)
```

</details>

## Durchlauf

Graph `V=4`. `adj = {0: [(1, 10), (2, 6), (3, 5)], ... }`.
`visited = set()`, `pq = [(0, 0)]`.

1. `heappop()` -> `weight=0, u=0`.
   - `0` nicht besucht. `visited.add(0)`. `mst_weight = 0`.
   - Kanten hinzufügen: `(10, 1)`, `(6, 2)`, `(5, 3)`.
   - `pq = [(5, 3), (6, 2), (10, 1)]`.
2. `heappop()` -> `(5, 3)`.
   - `3` nicht besucht. `visited.add(3)`. `mst_weight = 5`.
   - Nachbarn von 3: `0 (Kosten 5)`, `1 (Kosten 15)`, `2 (Kosten 4)`.
   - `0` ist besucht (überspringen). `(15, 1)` und `(4, 2)` hinzufügen.
   - `pq = [(4, 2), (6, 2), (10, 1), (15, 1)]`.
3. `heappop()` -> `(4, 2)`.
   - `2` nicht besucht. `visited.add(2)`. `mst_weight = 5 + 4 = 9`.
   - Nachbarn von 2: `0 (Kosten 6)`, `3 (Kosten 4)`. Beide besucht! Nichts hinzufügen.
   - `pq = [(6, 2), (10, 1), (15, 1)]`.
4. `heappop()` -> `(6, 2)`.
   - `2` IST BEREITS BESUCHT! Überspringen!
5. `heappop()` -> `(10, 1)`.
   - `1` nicht besucht. `visited.add(1)`. `mst_weight = 9 + 10 = 19`.
   - `len(visited) == 4`. Terminieren!

Ergebnis `mst_weight = 19`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(E log V)$ | $O(V + E)$ |
| **Durchschnittlicher Fall** | $O(E log V)$ | $O(V + E)$ |
| **Schlechtester Fall** | $O(E log V)$ | $O(V + E)$ |

Jeder Knoten wird genau einmal zum `visited`-Set hinzugefügt. Jede Kante wird genau einmal in die Priority Queue geschoben. Das Entnehmen aus der Priority Queue dauert $O(log E)$.
Die gesamte Zeitkomplexität beträgt $O(E log E)$. Da $E \le V^2$, ist $O(log E) = O(2 log V) = O(log V)$. Daher wird die Zeitkomplexität konventionell als $O(E log V)$ geschrieben.
Die Platzkomplexität beträgt $O(E)$ für die Priority Queue und $O(V)$ für das `visited`-Set.
*(Hinweis: Ein hochkomplexer Fibonacci-Heap kann die Zeit auf $O(E + V log V)$ optimieren, was ihn bei dichten Graphen strikt schneller als den Kruskal-Algorithmus macht, dies wird jedoch in Vorstellungsgesprächen nie erwartet).*

## Varianten & Optimierungen

- **Pfadrekonstruktion:** Wenn Sie die tatsächliche Liste der Kanten im MST benötigen, modifizieren Sie einfach die Priority Queue so, dass sie Tupel der Form `(weight, u, parent_who_pushed_me)` speichert. Wenn Sie erfolgreich `u` entnehmen und besuchen, fügen Sie die Kante `(parent, u, weight)` zu Ihrem `mst_edges`-Array hinzu!

## Anwendungen in der Praxis

- **Labyrintherzeugung:** Wenn Sie einem Gittergraphen zufällige Gewichte zuweisen und den Prim-Algorithmus ausführen, ist der resultierende MST ein perfekt lösbares, zyklusfreies Labyrinth!
- **Approximation des Handlungsreisenden (TSP):** Der absolut kürzeste Pfad, der alle Knoten berührt (TSP), ist NP-schwer. Das Gewicht eines MST ist jedoch eine garantierte untere Schranke für das TSP.

## Verwandte Algorithmen in cOde(n)

- **[graph_08 - Kruskal-MST](graph_08_kruskal-s-mst.md)** — Die Alternative mit Disjoint-Set, die Kanten global sortiert.
- **[graph_04 - Dijkstra-Algorithmus](graph_04_dijkstra.md)** — Verwendet exakt dieselbe Priority-Queue-Struktur, aber die Priority Queue von Dijkstra sortiert nach der *gesamten akkumulierten Distanz von der Quelle*, während Prim strikt nach dem *Rohgewicht der unmittelbaren Kante* sortiert.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*