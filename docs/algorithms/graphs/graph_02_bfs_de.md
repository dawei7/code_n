# Breadth-First Search (BFS)

| | |
|---|---|
| **ID** | `graph_02` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **Wikipedia** | [Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) |

## Problemstellung

Gegeben sei ein Graph `G = (V, E)` und ein Startknoten `s`. Durchlaufe den Graphen **ebenenweise**: Besuche alle Knoten mit Distanz `1` von `s`, bevor Knoten mit Distanz `2` besucht werden, danach Distanz `3` und so weiter. Ausgabe: die BFS-Reihenfolge, die Distanz von `s` zu jedem erreichbaren Knoten und (optional) der Vorgänger jedes Knotens zur Pfadrekonstruktion.

**Eingabe:** ein Graph (Adjazenzliste oder Adjazenzmatrix), ein Startknoten `s`.
**Ausgabe:** BFS-Reihenfolge, Distanz-Array, Vorgänger-Array.

**Beispiel:**

```
    0 - 1 - 3
    |   |   |
    2 - 4   5
    |
    6

Adjazenz:
  0: [1, 2]
  1: [0, 3, 4]
  2: [0, 4, 6]
  3: [1, 5]
  4: [1, 2]
  5: [3]
  6: [2]

BFS von 0:
  Reihenfolge: 0, 1, 2, 3, 4, 6, 5
  Distanz:     0:0, 1:1, 2:1, 3:2, 4:2, 5:3, 6:2
```

## Wann man es verwendet

- Der wichtigste Graphalgorithmus überhaupt. Wird in irgendeiner Form in fast jedem Vorstellungsgespräch abgefragt.
- Grundlage für **kürzeste Pfade in ungewichteten Graphen**, **Zusammenhangskomponenten**, **Bipartitheitsprüfung**, **Level-Order-Traversierung von Bäumen** und **Garbage Collection** (Mark-and-Sweep).

## Ansatz

BFS verwendet eine **FIFO-Queue** (die Deque). Die Invariante: Wenn ein Knoten die Queue verlässt, ist seine kürzeste Distanz von `s` bekannt.

```
mark s as visited
enqueue (s, dist=0)
while queue not empty:
    dequeue (u, du)
    for each neighbor v of u:
        if v not yet visited:
            mark v as visited
            dist[v] = du + 1
            parent[v] = u
            enqueue (v, du + 1)
```

**Performance:** Jeder Knoten wird höchstens einmal in die Queue eingefügt und jede Kante wird höchstens zweimal untersucht (einmal von jedem Endpunkt aus, in einem ungerichteten Graphen). Gesamt: $O(V + E)$ bei einer Adjazenzlisten-Repräsentation. Bei einer Adjazenzmatrix: $O(V²)$.

**Warum es den kürzesten Pfad in ungewichteten Graphen liefert:** Wenn wir einen Knoten `v` zum ersten Mal besuchen, muss jeder Pfad zu `v` über einen Nachbarn führen, der selbst eine Distanz ≤ dist[v] - 1 hat, und diese Nachbarn werden vor `v` verarbeitet. Daher ist `dist[v]` optimal.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_02: Breadth-First Search.

Pure-graph BFS on adjacency lists, returns visit order.
"""


def solve(num_nodes, edges):
    from collections import deque
    adj = [[] for _ in range(num_nodes)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * num_nodes
    order = []
    q = deque([0])
    seen[0] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v in sorted(adj[u]):
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return order
```

</details>

## Durchlauf

Graph aus dem Beispiel. BFS von `s = 0`.

`visited = {0}`, `queue = [(0, 0)]`, `order = []`, `parent = {0: None}`.

| Iter | dequeue | Nachbarn | neu besucht | Queue danach |
|---|---|---|---|---|
| 1 | (0, 0) | 1, 2 | 1 (Dist 1), 2 (Dist 1) | [(1, 1), (2, 1)] |
| 2 | (1, 1) | 0, 3, 4 | 3 (Dist 2), 4 (Dist 2) | [(2, 1), (3, 2), (4, 2)] |
| 3 | (2, 1) | 0, 4, 6 | 6 (Dist 2); 4 bereits besucht | [(3, 2), (4, 2), (6, 2)] |
| 4 | (3, 2) | 1, 5 | 5 (Dist 3) | [(4, 2), (6, 2), (5, 3)] |
| 5 | (4, 2) | 1, 2 | nichts Neues | [(6, 2), (5, 3)] |
| 6 | (6, 2) | 2 | nichts Neues | [(5, 3)] |
| 7 | (5, 3) | 3 | nichts Neues | [] |

BFS-Reihenfolge: `[0, 1, 2, 3, 4, 6, 5]`. Distanzen stimmen überein. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ für Adjazenzliste, $O(V²)$ für Matrix | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V)$ |

Die erforderliche Komplexität ist $O(n²)$ für die $n²$-Matrix-Variante von cOde(n).

## Varianten & Optimierungen

- **Bidirektionale BFS** — starte von `s` und `t` gleichzeitig; stoppe, wenn sich die Fronten treffen. In der Praxis ca. 2x schneller.
- **Multi-Source BFS** — initialisiere die Queue mit allen Startknoten. Nützlich für Probleme wie "rotting oranges" oder "walls and gates".
- **0-1 BFS** — wenn Kanten Gewichte von 0 oder 1 haben, verwende eine Deque: füge Kanten mit Gewicht 0 vorne und mit Gewicht 1 hinten ein. $O(V + E)$ statt Dijkstras $O((V + E) \log V)$. Siehe `graph_17`.
- **BFS zur Bipartitheitsprüfung** — färbe die Ebenen abwechselnd. Wenn eine Ebene beide Farben enthält und eine Kante zwei Knoten gleicher Farbe verbindet, ist der Graph nicht bipartit.
- **BFS für Zusammenhangskomponenten** — wiederhole BFS für jeden unbesuchten Knoten.

## Anwendungen in der Praxis

- **"Degrees of Separation" in sozialen Netzwerken** — BFS von einer Person aus, zähle die Ebenen, bis eine andere Person erreicht wird.
- **Web-Crawler** — BFS von Start-URLs, folge den Links Ebene für Ebene, unter Berücksichtigung von Wartezeiten (Politeness).
- **Garbage Collection** — "Mark-and-Sweep" GC durchläuft den Objektgraphen in BFS-Reihenfolge ausgehend von Wurzelreferenzen.
- **Peer-to-Peer-Netzwerke** — BitTorrent verwendet eine BFS im Kademlia-Stil zur Nachbarschaftssuche.
- **Shortest-Hop-Routing in ungewichteten Netzwerken** — BFS liefert Pfade mit der minimalen Anzahl an Hops.
- **Pfadfindung in Spiele-KI** — ungewichtete Gitter verwenden BFS; gewichtete verwenden A*.

## Verwandte Algorithmen in cOde(n)

- **[graph_03 — DFS](graph_03_dfs.md)** — die andere grundlegende Graphensuche. (d=4/10, r=8/10)
- **[graph_04 — Dijkstra](graph_04_dijkstra.md)** — BFS verallgemeinert auf Graphen mit nicht-negativen Gewichten. (d=5/10, r=8/10)
- **[search_03 — BFS Grid](search_03_bfs-grid.md)** — die konkrete 2D-Gitter-Version. (d=5/10, r=8/10)
- **[graph_17 — 0-1 BFS](graph_17_01-bfs.md)** — für Graphen mit 0/1-Kantengewichten. (d=5/10, r=8/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den enzyklopädischen Standardeintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*