# Floyd-Warshall (Formulierung als dynamische Programmierung)

| | |
|---|---|
| **ID** | `dp_27` |
| **Kategorie** | dynamische_Programmierung |
| **Komplexität (erforderlich)** | $O(V^3)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **Wikipedia** | [Floyd-Warshall-Algorithmus](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) |

## Problemstellung

*(Dieses Dokument befasst sich mit der formalen Zustandslogik der dynamischen Programmierung von `graph_06`).*

Finde die kürzesten Wege zwischen **allen Paaren** von Knoten in einem gewichteten Graphen. Negative Gewichte sind zulässig, Zyklen mit negativen Gewichten jedoch nicht.

## Herangehensweise als DP-Problem

Floyd-Warshall ist nicht nur ein Graphenalgorithmus, sondern ein klassischer 3D-Algorithmus der dynamischen Programmierung.

**Der DP-Zustand:**
Sei `dp[k][i][j]` die kürzeste Entfernung vom Knoten `i` zum Knoten `j`, wobei AUSSCHLIESSLICH Knoten aus der Menge `{0, 1, 2, ... k}` als Zwischenstationen verwendet werden.

**Der Übergang:**
Wenn wir den kürzesten Weg unter Verwendung von Knoten bis einschließlich `k`(`dp[k][i][j]`) berechnen wollen, haben wir zwei Möglichkeiten:
1. **Knoten `k` nicht verwenden:** Der kürzeste Weg stützt sich vollständig auf die vorherige Menge von Knoten. Die Kosten betragen `dp[k-1][i][j]`.
2. **Knoten `k` verwenden:** Wir gehen von `i` nach `k` (unter Verwendung von Knoten bis einschließlich `k-1`) und gehen dann von `k` nach `j` (unter Verwendung von Knoten bis einschließlich `k-1`). Die Kosten betragen `dp[k-1][i][k] + dp[k-1][k][j]`.

Daher gilt:
`dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])`

**Speicheroptimierung:**
Beachten Sie, dass `dp[k]` sich AUSSCHLIESSLICH auf die Werte aus `dp[k-1]` stützt.
Außerdem ändern sich `dp[k-1][i][k]` und `dp[k-1][k][j]` bei der Berechnung der `k`-ten Ebene nicht, da Pfade, die bei `k` enden oder beginnen, `k` ohnehin nicht als *Zwischenschritt* nutzen können!
Daher können wir die Dimension `k` vollständig aus unserer DP-Tabelle weglassen und einfach eine 2D-Matrix an Ort und Stelle aktualisieren!

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

| | Zeit | Speicher |
|---|---|---|
| **Bestfall** | $O(V^3)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(V^3)$ | $O(V^2)$ |
| **Schlechteste** | $O(V^3)$ | $O(V^2)$ |

Die drei eng verschachtelten Schleifen `k`, `i` und `j` bestimmen eindeutig die Zeitkomplexität $O(V^3)$.
Die In-Place-DP-Optimierung reduziert die Platzkomplexität von $O(V^3)$ auf $O(V^2)$.

## Verwandte Algorithmen in cOde(n)

- **[graph_06 – Floyd-Warshall](../graphs/graph_06_floyd-warshall.md)** – Die Perspektive der Graphentheorie.
- **[dp_28 – Bellman-Ford](dp_28_bellman-ford-sssp.md)** – Die 2D-DP-Formulierung für kürzeste Wege mit einer Quelle.

---

*Diese Dokumentation ist ein für cOde(n) verfasster Originalbeitrag,
der sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
