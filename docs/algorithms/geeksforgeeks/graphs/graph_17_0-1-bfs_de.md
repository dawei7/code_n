# 0-1 BFS (Kürzester Pfad)

| | |
|---|---|
| **ID** | `graph_17` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(V + E)$ Zeit, $O(V)$ Platzkomplexität |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **GeeksForGeeks Äquivalent** | [0-1 BFS (Shortest Path in a Binary Weight Graph)](https://www.geeksforgeeks.org/0-1-bfs-shortest-path-binary-graph/) |

## Problemstellung

Gegeben ist ein gewichteter Graph, in dem jede Kante ein Gewicht von exakt **0 oder 1** hat. Finde den kürzesten Pfad von einem Startknoten `S` zu allen anderen Knoten.

**Eingabe:** Anzahl der Knoten `V`, eine Adjacency List `adj`, wobei `adj[u] = [(v, weight)]` (weight \in {0, 1}), und ein Startknoten `S`.
**Ausgabe:** Ein Array der minimalen Distanzen von `S`.

## Wann man es verwendet

- Beim Lösen von gitterbasierten Pfadfindungsproblemen, bei denen "freies Bewegen" 0 kostet, aber "eine Wand durchbrechen" oder "die Richtung ändern" 1 kostet.
- *Einschränkung:* Der Standard-Dijkstra-Algorithmus funktioniert zwar, benötigt aber $O(E log V)$. Da die Gewichte strikt binär sind, löst 0-1 BFS das Problem in linearer $O(V + E)$ Zeit!

## Ansatz

**1. Der Overhead der Priority Queue:**
Warum benötigt Dijkstra eine $O(log V)$ Priority Queue? Weil Kantengewichte beliebig sein können (z. B. 5, 20, 100), was bedeutet, dass Distanzkandidaten unvorhersehbar springen können. Die Priority Queue ist notwendig, um diese zwangsweise zu sortieren.

**2. Die 0-1 Einschränkung:**
Wenn Kantengewichte NUR 0 oder 1 sind und unser aktueller Knoten U eine Distanz von D hat, können seine Nachbarn NUR Distanzkandidaten von D (falls das Gewicht 0 ist) oder D + 1 (falls das Gewicht 1 ist) haben.
Es gibt keine Sprünge! Die Queue der ausstehenden Knoten wird zu jedem Zeitpunkt nur Knoten mit der Distanz D und der Distanz D+1 enthalten.

**3. Die Double-Ended Queue (Deque):**
Wir können die teure Priority Queue vollständig durch eine einfache $O(1)$ Double-Ended Queue (`deque`) ersetzen.
Wenn wir uns am Knoten U (Distanz D) befinden und einen Nachbarn V evaluieren:
- Wenn das Kantengewicht **0** ist, ist die Kandidatendistanz zu V weiterhin D. Dies ist ein "kostenloser" Schritt! Wir möchten diesen sofort erkunden, bevor wir irgendwelche D+1 Schritte erkunden. Daher fügen wir V an den **ANFANG** (FRONT) der Deque hinzu.
- Wenn das Kantengewicht **1** ist, ist die Kandidatendistanz zu V D + 1. Wir sollten dies erst erkunden, nachdem alle D-Schritte erschöpft sind. Daher fügen wir V an das **ENDE** (BACK) der Deque hinzu.

Da wir 0-Kosten-Schritte an den Anfang schieben, bleibt die Deque auf natürliche Weise perfekt sortiert, ohne den $O(log V)$ Heap-Overhead!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_17: 0-1 BFS.

Shortest path on a graph with edge weights in {0, 1}. Use a
deque: pop the left, push 0-weight neighbors to the LEFT and
1-weight neighbors to the RIGHT. This is O(V + E).
"""


def solve(num_nodes, edges, start):
    if num_nodes <= 0:
        return {}
    adj = [[] for _ in range(num_nodes)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    INF = float("inf")
    dist = [INF] * num_nodes
    dist[start] = 0
    from collections import deque
    dq = deque([start])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return {i: (-1 if dist[i] == INF else dist[i]) for i in range(num_nodes)}
```

</details>

## Durchlauf

`V = 4`. Kanten: `0-1 (1)`, `0-2 (0)`, `1-3 (0)`, `2-3 (1)`. Start bei `0`.
`dist = [0, inf, inf, inf]`. `queue = [0]`.

1. `popleft()` -> `0` (Distanz 0).
   - Nachbar `1` (Gewicht 1): Kandidatendistanz = 1. `1 < inf`.
     - `dist[1] = 1`. Gewicht ist 1, füge hinten an: `queue = [1]`.
   - Nachbar `2` (Gewicht 0): Kandidatendistanz = 0. `0 < inf`.
     - `dist[2] = 0`. Gewicht ist 0, füge vorne an: `queue = [2, 1]`.
2. `popleft()` -> `2` (Distanz 0).
   - Nachbar `3` (Gewicht 1): Kandidatendistanz = 1. `1 < inf`.
     - `dist[3] = 1`. Gewicht ist 1, füge hinten an: `queue = [1, 3]`.
3. `popleft()` -> `1` (Distanz 1).
   - Nachbar `3` (Gewicht 0): Kandidatendistanz = 1 + 0 = 1.
     - `1` ist NICHT strikt kleiner als die aktuelle `dist[3]` (welche 1 ist).
     - Ignorieren.
4. `popleft()` -> `3` (Distanz 1).
   - Keine Nachbarn.

Finale Distanzen: `[0, 1, 0, 1]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V + E)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V + E)$ | $O(V)$ |

Jeder Knoten wird verarbeitet und seine ausgehenden Kanten werden evaluiert. Das Hinzufügen zum Anfang oder Ende einer Deque benötigt $O(1)$ Zeit. Daher ist die Zeitkomplexität strikt $O(V + E)$, was der Standard-BFS für ungewichtete Graphen entspricht und Dijkstras $O(E log V)$ bei weitem übertrifft.
Die Platzkomplexität beträgt $O(V)$ für die Deque und das Distanz-Array.

## Varianten & Optimierungen

- **Multi-Source 0-1 BFS:** Wenn Sie mehrere Startpunkte haben, fügen Sie einfach alle zu Beginn mit Distanz 0 zur Deque hinzu!
- **Dial-Algorithmus:** Eine Verallgemeinerung von 0-1 BFS. Wenn Kantengewichte auf kleine ganze Zahlen beschränkt sind, die durch einen Maximalwert W begrenzt sind (z. B. Gewichte von 0 bis 9), können Sie ein Array von W+1 Queues (oder Buckets) anstelle einer einzelnen Deque verwenden. Dies löst das Problem in $O(V + E \cdot W)$ Zeit.

## Anwendungen in der Praxis

- **Roboternavigation / Pac-Man:** Finden des optimalen Pfades durch ein Gitter, bei dem "vorwärts bewegen" 0 kostet, aber "90 Grad drehen" 1 Zeit- oder Energieeinheit kostet. Ein Zustand ist `(x, y, facing_direction)`.

## Verwandte Algorithmen in cOde(n)

- **[graph_02 - Breadth-First Search](graph_02_bfs.md)** — Die Grundlage. 0-1 BFS ist lediglich eine BFS mit einer Double-Ended Queue.
- **[graph_04 - Dijkstra's Algorithm](graph_04_dijkstra.md)** — Der langsamere Algorithmus, den Sie verwenden müssten, wenn ein Kantengewicht 2 wäre.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*