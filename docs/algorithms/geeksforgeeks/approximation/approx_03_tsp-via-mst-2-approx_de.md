# TSP via MST (2-Approximation)

| | |
|---|---|
| **ID** | `approx_03` |
| **Kategorie** | approximation |
| **Komplexität (erforderlich)** | $O(V^2 log V)$ |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) |

## Problemstellung

Gegeben ist ein vollständig zusammenhängender Graph, der Städte und die Distanzen zwischen ihnen repräsentiert. Gesucht ist die kürzestmögliche Route, die jede Stadt genau einmal besucht und zum Ausgangspunkt zurückkehrt.
Dies ist das **Travelling Salesman Problem (TSP)**, ein NP-schweres Problem.
Nehmen wir an, der Graph erfüllt die **Dreiecksungleichung** (der direkte Weg zwischen A und B ist immer kürzer oder gleich lang wie der Weg über einen Zwischenpunkt C).
Entwerfen Sie einen Algorithmus, der eine Route findet, deren Länge garantiert nicht mehr als das **Doppelte** der optimalen Route beträgt.

**Eingabe:** Eine Adjazenzmatrix, die die Distanzen zwischen den Knoten repräsentiert.
**Ausgabe:** Eine Liste von Knoten, die die Tour repräsentieren, sowie die Gesamtdistanz.

## Wann man es verwendet

- Wenn V groß ist (z. B. 1000 Städte), was exakte $O(2^V)$ DP-Lösungen völlig unmöglich macht.
- Als Sprungbrett zum Verständnis des 1,5-Approximations-Algorithmus von Christofides.

## Ansatz

Die optimale TSP-Tour ist ein Zyklus, der alle Knoten besucht. Wenn wir eine Kante aus diesem Zyklus entfernen, erhalten wir einen Spannbaum!
Daher muss das Gewicht des Minimum Spanning Tree (MST) des Graphen kleiner sein als das Gewicht der optimalen TSP-Tour! `Weight(MST) < Weight(OPT)`.

**Der Algorithmus:**
1. **MST finden:** Finden Sie den Minimum Spanning Tree des Graphen mithilfe des Algorithmus von Prim oder Kruskal.
2. **Kanten verdoppeln:** Stellen Sie sich vor, Sie laufen entlang des MST. Wenn wir jede Kante hin und wieder zurück laufen, besuchen wir jeden Knoten und kehren zum Start zurück. Die Kosten dieses Weges betragen genau `2 * Weight(MST)`. Da `Weight(MST) < Weight(OPT)`, ist dieser Weg `< 2 * Weight(OPT)`!
3. **Euler-Tour (Preorder-Traversierung):** Wir verfolgen den verdoppelten MST.
4. **Abkürzungen:** Der Weg über den verdoppelten MST besucht Knoten mehrfach. Da der Graph die Dreiecksungleichung erfüllt, ist es IMMER günstiger, eine direkte Abkürzung zu einem unbesuchten Knoten zu nehmen, als alte Knoten erneut zu besuchen! Wir führen eine **Preorder-Traversierung (DFS)** auf dem MST durch und fügen einen Knoten nur dann zu unserer Tour hinzu, wenn wir ihn das *erste* Mal sehen.

Die resultierende Tour ist gültig (besucht jeden einmal) und ihre Kosten sind strikt \le 2 x OPT.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for approx_03: TSP via MST (2-Approx).

Given a complete graph with edge costs that satisfy
"""


def solve(cost, n):
    """MST-based 2-approximate TSP.

    1. Build MST rooted at 0 via Prim's.
    2. Preorder walk of the MST to produce a tour.
    3. Sum the costs along the tour (including the return
       edge from the last vertex back to 0).
    """
    if n <= 1:
        return 0
    INF = float("inf")
    # Prim's MST.
    in_mst = [False] * n
    in_mst[0] = True
    # parent[i] = the node that brought i into the MST.
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
    # Preorder DFS walk of the MST.
    children = [[] for _ in range(n)]
    for v in range(n):
        p = parent[v]
        if p != -1:
            children[p].append(v)
    tour = []
    def dfs(u):
        tour.append(u)
        for c in children[u]:
            dfs(c)
    dfs(0)
    # Sum tour cost (including the return edge).
    total = 0
    for i in range(len(tour) - 1):
        total += cost[tour[i]][tour[i + 1]]
    total += cost[tour[-1]][0]
    return total
```

</details>

## Durchlauf

Graph: 3 Knoten in einem Dreieck. `dist(0,1)=10`, `dist(1,2)=10`, `dist(0,2)=15`.
*(Optimales TSP: 0 -> 1 -> 2 -> 0. Kosten = 10 + 10 + 15 = 35).*

1. **MST (Prim's):**
   - Start bei 0. Kanten: `(0,1: 10)`, `(0,2: 15)`.
   - Wähle `(0,1)`. Füge 1 hinzu. MST-Kanten: `[(0,1)]`.
   - Von 1 aus, Kanten: `(1,2: 10)`.
   - Wähle `(1,2)`. Füge 2 hinzu. MST-Kanten: `[(0,1), (1,2)]`. Gewicht ist 20.
2. **Preorder-Traversierung (DFS):**
   - Start bei 0. Füge 0 hinzu.
   - Gehe zu 1. Füge 1 hinzu.
   - Gehe zu 2. Füge 2 hinzu.
3. **Tour beenden:**
   - Hänge Startknoten 0 an.
   - Tour = `[0, 1, 2, 0]`.
4. **Distanzberechnung:**
   - `0->1` (10) + `1->2` (10) + `2->0` (15) = 35.

Ergebnis: 35. Unsere 2-Approximation hat die exakte optimale Route gefunden! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V^2 log V)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(V^2 log V)$ | $O(V^2)$ |
| **Schlechtester Fall** | $O(V^2 log V)$ | $O(V^2)$ |

Der Aufbau des MST auf einem dichten, vollständig zusammenhängenden Graphen (wobei E = V^2) unter Verwendung des Algorithmus von Prim mit einem binären Heap benötigt $O(E log V)$ = $O(V^2 log V)$. Die anschließende DFS benötigt $O(V)$ Zeit. Die Gesamtzeit wird durch die MST-Konstruktion dominiert.
Die Platzkomplexität beträgt $O(V^2)$, um die Adjazenzmatrix und die Priority Queue zu speichern.

## Varianten & Optimierungen

- **Christofides-Algorithmus:** Eine 1,5-Approximation. Er beginnt ebenfalls mit einem MST. Anstatt jedoch blind eine DFS durchzuführen (die sich darauf verlässt, teure Abkürzungen zu nehmen, um die Knoten mit ungeradem Grad zu korrigieren, die durch die verdoppelten Kanten entstanden sind), findet Christofides ein Matching minimalen Gewichts für die Knoten mit ungeradem Grad und fügt diese spezifischen Kanten zum MST hinzu. Dies erzeugt direkt einen Euler-Kreis und senkt die Approximationsschranke auf exakt 1,5 x OPT!
- **Held-Karp DP:** Die $O(V^2 2^V)$ dynamische Programmierung für eine exakte Lösung.

## Anwendungen in der Praxis

- **Routenplanung für Lieferdienste:** Ein UPS-LKW bestimmt die Lieferroute für 100 Pakete. Die Distanzen zwischen den Häusern erfüllen die Dreiecksungleichung, daher funktionieren Approximationen einwandfrei.
- **Bohren von Leiterplatten:** Optimierung des Pfades eines Laserbohrers, der Löcher in eine Leiterplatte (PCB) bohrt.

## Verwandte Algorithmen in cOde(n)

- **[graph_10 - Prim's MST](../graphs/graph_10_prim-s-mst.md)** — Der exakte MST-Algorithmus, der hier als grundlegender Schritt verwendet wird.
- **[approx_04 - Christofides TSP](approx_04_christofides-tsp-3-2-approx.md)** — Die 1,5-Approximations-Verbesserung.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*