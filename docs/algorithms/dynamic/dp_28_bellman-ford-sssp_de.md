# Bellman-Ford (Formulierung mittels dynamischer Programmierung)

| | |
|---|---|
| **ID** | `dp_28` |
| **Kategorie** | dynamische_Programmierung |
| **Komplexität (erforderlich)** | $O(V * E)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Bellman-Ford-Algorithmus](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) |

## Problemstellung

*(Dieses Dokument untersucht die formale Zustandslogik der dynamischen Programmierung von `graph_05`).*

Finde den kürzesten Weg von einer einzelnen Quelle zu allen anderen Knoten in einem Graphen, der negative Gewichte enthalten kann.

## Herangehensweise als DP-Problem

Obwohl der Bellman-Ford-Algorithmus oft als „einfach V-1-malige Relaxation der Kanten“ gelehrt wird, handelt es sich dabei im Grunde um einen 2D-Algorithmus der dynamischen Programmierung.

**Der DP-Zustand:**
Sei `dp[k][u]` die kürzeste Entfernung vom Startknoten zum Knoten `u` unter Verwendung von **höchstens `k` Kanten**.

**Der Übergang:**
Um den kürzesten Weg zu `u` unter Verwendung von `k` Kanten zu finden, haben wir zwei Möglichkeiten:
1. **Die k-te Kante nicht verwenden:** Der kürzeste Weg verwendete `k-1` oder weniger Kanten. Die Kosten betragen `dp[k-1][u]`.
2. **Die k-te Kante verwenden:** Wir sind über `k-1` Kanten bei einem benachbarten Knoten `v` angekommen und haben dann die direkte Kante `(v, u)` mit dem Gewicht `w` genommen. Die Kosten betragen `dp[k-1][v] + w`. Wir probieren dies für *alle* eingehenden Kanten zu `u` aus.

Daher gilt:
`dp[k][u] = min(dp[k-1][u], min(dp[k-1][v] + weight(v, u)) for all edges v->u)`

Da ein einfacher Pfad (ohne Zyklen) in einem Graphen mit V Knoten höchstens V-1 Kanten enthalten kann, müssen wir diese DP-Tabelle nur bis k = V-1 berechnen.

**Speicheroptimierung:**
Beachte, dass die Zeile `dp[k]` NUR von der Zeile `dp[k-1]` abhängt.
Wir können die Dimension `k` weglassen und einfach ein 1D-Array `dp[u]` verwenden, das wir direkt an Ort und Stelle überschreiben!
*(Dies entspricht funktional der Speicherplatzoptimierung für das 0/1-Rucksackproblem).*

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

Der Algorithmus berechnet explizit V-1 Schichten (die `k`-Schleife). In jeder Schicht wertet er alle E Kanten aus. Die Gesamtzeitkomplexität beträgt streng $O(V \cdot E)$.
Durch die Speicheroptimierung wird der Speicherbedarf von $O(V^2)$ auf ein einziges $O(V)$-Array reduziert.

## Verwandte Algorithmen in cOde(n)

- **[graph_05 – Bellman-Ford](../graphs/graph_05_bellman-ford.md)** – Die Perspektive der Graphentheorie.
- **[dp_27 – Floyd-Warshall](dp_27_floyd-warshall-path.md)** – Die 3D-DP-Formulierung für die kürzesten Wege zwischen allen Paaren.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie unter dem Wikipedia-Link oben auf der Seite.
Quell-Repository:
<https://github.com/dawei7/code_n>.*
