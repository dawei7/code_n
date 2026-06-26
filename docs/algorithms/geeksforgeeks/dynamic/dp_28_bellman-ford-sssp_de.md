# Bellman-Ford (Dynamische Programmierung Formulierung)

| | |
|---|---|
| **ID** | `dp_28` |
| **Kategorie** | dynamic_programming |
| **Komplexität (erforderlich)** | $O(V * E)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Bellman-Ford-Algorithmus](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) |

## Problemstellung

*(Dieses Dokument untersucht die formale DP-Zustandslogik von `graph_05`.)*

Finde den kürzesten Pfad von einer Single Source zu allen anderen Knoten in einem Graphen, der negative Kantengewichte enthalten kann.

## Ansatz als DP-Problem

Obwohl Bellman-Ford oft als „einfaches Relaxieren der Kanten V-1 mal“ gelehrt wird, ist es fundamental ein 2D-Algorithmus der Dynamischen Programmierung.

**Der DP-Zustand:**
Sei `dp[k][u]` die kürzeste Distanz von der Quelle zum Knoten `u` unter Verwendung von **maximal `k` Kanten**.

**Der Übergang:**
Um den kürzesten Pfad zu `u` mit `k` Kanten zu finden, haben wir zwei Möglichkeiten:
1. **Die k-te Kante nicht verwenden:** Der kürzeste Pfad verwendete `k-1` oder weniger Kanten. Die Kosten betragen `dp[k-1][u]`.
2. **Die k-te Kante verwenden:** Wir haben einen benachbarten Knoten `v` mit `k-1` Kanten erreicht und nehmen dann die direkte Kante `(v, u)` mit dem Gewicht `w`. Die Kosten betragen `dp[k-1][v] + w`. Wir versuchen dies für *alle* eingehenden Kanten zu `u`.

Daher gilt:
`dp[k][u] = min(dp[k-1][u], min(dp[k-1][v] + weight(v, u)) für alle Kanten v->u)`

Da ein einfacher Pfad (ohne Zyklen) in einem Graphen mit V Knoten maximal V-1 Kanten enthalten kann, müssen wir diese DP-Tabelle nur bis k = V-1 berechnen.

**Platzoptimierung:**
Beachte, dass die Zeile `dp[k]` NUR von der Zeile `dp[k-1]` abhängt.
Wir können die `k`-Dimension weglassen und einfach ein 1D-Array `dp[u]` verwenden, das in-place überschrieben wird!
*(Dies ist funktional identisch mit der Platzoptimierung beim 0/1-Rucksackproblem).*

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_28: Bellman-Ford (SSSP).

Relax all edges n-1 times.
"""


def solve(n, edges, src):
    INF = 10 ** 9
    dist = [INF] * n
    dist[src] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist
```

</details>

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V * E)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V * E)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V * E)$ | $O(V)$ |

Der Algorithmus berechnet explizit V-1 Schichten (die `k`-Schleife). In jeder Schicht werden alle E Kanten evaluiert. Die gesamte Zeitkomplexität beträgt strikt $O(V \cdot E)$.
Die Platzoptimierung reduziert den Speicherbedarf von $O(V^2)$ auf ein einzelnes $O(V)$-Array.

## Verwandte Algorithmen in cOde(n)

- **[graph_05 - Bellman-Ford](../graphs/graph_05_bellman-ford.md)** — Die graphentheoretische Perspektive.
- **[dp_27 - Floyd-Warshall](dp_27_floyd-warshall-path.md)** — Die 3D-DP-Formulierung für kürzeste Pfade zwischen allen Knotenpaaren (All-Pairs shortest paths).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*