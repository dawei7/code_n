# Floyd-Warshall (Dynamische Programmierung Formulierung)

| | |
|---|---|
| **ID** | `dp_27` |
| **Kategorie** | dynamic_programming |
| **Komplexität (erforderlich)** | $O(V^3)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **Wikipedia** | [Floyd-Warshall-Algorithmus](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) |

## Problemstellung

*(Dieses Dokument untersucht die formale DP-Zustandslogik von `graph_06`.)*

Finde die kürzesten Pfade zwischen **allen Paaren** von Knoten in einem gewichteten Graphen. Negative Kantengewichte sind erlaubt, Zyklen mit negativem Gesamtgewicht jedoch nicht.

## Ansatz als DP-Problem

Floyd-Warshall ist nicht nur ein Graphalgorithmus; es ist ein klassischer 3D-Algorithmus der Dynamischen Programmierung.

**Der DP-Zustand:**
Sei `dp[k][i][j]` die kürzeste Distanz vom Knoten `i` zum Knoten `j`, wobei NUR Knoten aus der Menge `{0, 1, 2, ... k}` als Zwischenstopps verwendet werden dürfen.

**Der Übergang:**
Wenn wir den kürzesten Pfad unter Verwendung von Knoten bis `k` (`dp[k][i][j]`) berechnen wollen, haben wir zwei Möglichkeiten:
1. **Knoten `k` nicht verwenden:** Der kürzeste Pfad basiert vollständig auf der vorherigen Menge von Knoten. Die Kosten betragen `dp[k-1][i][j]`.
2. **Knoten `k` verwenden:** Wir gehen von `i` nach `k` (unter Verwendung von Knoten bis `k-1`) und anschließend von `k` nach `j` (unter Verwendung von Knoten bis `k-1`). Die Kosten betragen `dp[k-1][i][k] + dp[k-1][k][j]`.

Daraus folgt:
`dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])`

**Platzoptimierung:**
Beachte, dass `dp[k]` NUR von den Werten aus `dp[k-1]` abhängt.
Des Weiteren ändern sich `dp[k-1][i][k]` und `dp[k-1][k][j]` nicht bei der Berechnung der `k`-ten Schicht, da Pfade, die bei `k` enden oder beginnen, `k` ohnehin nicht als *Zwischenschritt* verwenden können!
Daher können wir die `k`-Dimension vollständig aus unserer DP-Tabelle entfernen und einfach eine 2D-Matrix in-place aktualisieren!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_27: Floyd-Warshall Path Reconstruction.

Standard Floyd-Warshall with a next[][] matrix to
reconstruct the path. Return [] if dest is unreachable.
"""


def solve(n, edges, src, dest):
    if src == dest:
        return [src]
    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    nxt = [[-1] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
            nxt[u][v] = v
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k] if nxt[i][k] != -1 else k
    if dist[src][dest] == INF:
        return []
    path = [src]
    cur = src
    while cur != dest:
        cur = nxt[cur][dest]
        if cur == -1:
            return []
        path.append(cur)
    return path
```

</details>

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V^3)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(V^3)$ | $O(V^2)$ |
| **Schlechtester Fall** | $O(V^3)$ | $O(V^2)$ |

Die drei eng verschachtelten Schleifen `k`, `i` und `j` definieren eindeutig die Zeitkomplexität von $O(V^3)$.
Die in-place DP-Optimierung reduziert die Platzkomplexität von $O(V^3)$ auf $O(V^2)$.

## Verwandte Algorithmen in cOde(n)

- **[graph_06 - Floyd-Warshall](../graphs/graph_06_floyd-warshall.md)** — Die graphentheoretische Perspektive.
- **[dp_28 - Bellman-Ford](dp_28_bellman-ford-sssp.md)** — Die 2D-DP-Formulierung für kürzeste Pfade von einer einzelnen Quelle (Single-Source Shortest Paths).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*