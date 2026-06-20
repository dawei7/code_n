# TSP über MST (2-Approximation)

| | |
|---|---|
| **ID** | `approx_03` |
| **Kategorie** | Approximation |
| **Komplexität (erforderlich)** | $O(V^2 log V)$ |
| **Schwierigkeitsgrad** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Handelsreisendenproblem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) |

## Problemstellung

Gegeben sei ein vollständig verbundener Graph, der Städte und die Entfernungen zwischen ihnen darstellt. Finde die kürzestmögliche Route, auf der jede Stadt genau einmal besucht wird und die zum Ausgangspunkt zurückführt.
Dies ist das **Problem des Handlungsreisenden (TSP)**, ein NP-schweres Problem.
Es wird angenommen, dass der Graph der **Dreiecksungleichung** folgt (der direkte Weg zwischen A und B ist immer kürzer oder gleich lang wie der Weg über einen Zwischenpunkt C).
Entwickle einen Algorithmus, der eine Route findet, deren Länge garantiert nicht mehr als das **Zweifache** der Länge der optimalen Route beträgt.

**Eingabe:** Eine Adjacency Matrix, die die Entfernungen zwischen den Knoten darstellt.
**Ausgabe:** Eine Liste der Knoten, die die Route darstellen, sowie die Gesamtentfernung.

## Wann man es verwendet

- Wenn V groß ist (z. B. 1000 Städte), wodurch exakte $O(2^V)$-DP-Lösungen völlig unmöglich werden.
- Als Sprungbrett zum Verständnis des Christofides-Algorithmus mit 1,5-Approximation.

## Vorgehensweise

Die optimale TSP-Route ist ein Zyklus, der alle Knoten besucht. Wenn wir eine Kante aus diesem Zyklus entfernen, erhalten wir einen Spanning Tree!
Daher MUSS das Gewicht des minimalen Spannbaums (MST) des Graphen kleiner sein als das Gewicht der optimalen TSP-Route! `Weight(MST) < Weight(OPT)`.

**Der Algorithmus:**
1. **Den MST finden:** Finde den minimalen Spanning Tree des Graphen mit dem Prim- oder dem Kruskal-Algorithmus.
2. **Verdopplung der Kanten:** Stellen wir uns vor, wir würden den MST entlanggehen. Wenn wir jede Kante hinuntergehen und dann wieder hinaufgehen, besuchen wir jeden Knoten und kehren zum Start zurück. Die Kosten dieses Weges betragen genau `2 * Weight(MST)`. Da `Weight(MST) < Weight(OPT)`, beträgt die Kosten dieses Durchlaufs `< 2 * Weight(OPT)`!
3. **Euler-Tour (Preorder-Traversal):** Wir folgen dem verdoppelten MST.
4. **Abkürzungen:** Der Durchlauf des verdoppelten MST besucht Knoten mehrfach. Da der Graph der Dreiecksungleichung folgt, ist eine direkte Abkürzung zu einem noch nicht besuchten Knoten IMMER kostengünstiger als der erneute Besuch bereits besuchter Knoten! Wir führen eine **Preorder-Traversierung (DFS)** auf dem MST durch und fügen einen Knoten erst beim *ersten* Mal, wenn wir ihn sehen, zu unserer Tour hinzu.

Die resultierende Tour ist gültig (besucht jeden Knoten einmal) und ihre Kosten sind streng \le 2 x OPT.

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

## Schritt-für-Schritt-Anleitung

Graph: 3 Knoten in einer Dreiecksanordnung. `dist(0,1)=10`, `dist(1,2)=10`, `dist(0,2)=15`.
*(Optimales TSP: 0 -> 1 -> 2 -> 0. Kosten = 10 + 10 + 15 = 35).*

1. **MST (Prim):**
   - Start bei 0. Kanten: `(0,1: 10)`, `(0,2: 15)`.
   - `(0,1)` entfernen. 1 hinzufügen. MST-Kanten: `[(0,1)]`.
   - Von 1 aus: Kanten: `(1,2: 10)`.
   - `(1,2)` entfernen. 2 hinzufügen. MST-Kanten: `[(0,1), (1,2)]`. Gewicht ist 20.
2. **Vorwärtsdurchlauf (DFS):**
   - Start bei 0. 0 hinzufügen.
   - Weiter zu 1. 1 hinzufügen.
   - Weiter zu 2. 2 hinzufügen.
3. **Tour beenden:**
   - Startknoten 0 anhängen.
   - Tour = `[0, 1, 2, 0]`.
4. **Entfernungsberechnung:**
   - `0->1` (10) + `1->2` (10) + `2->0` (15) = 35.

Ergebnis: 35. Unsere 2-Approximation hat die exakt optimale Route gefunden! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(V^2 log V)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(V^2 log V)$ | $O(V^2)$ |
| **Schlechtester Fall** | $O(V^2 log V)$ | $O(V^2)$ |

Die Konstruktion des MST in einem dichten, vollständig verbundenen Graphen (wobei E = V^2) unter Verwendung des Prim-Algorithmus mit einem binären Heap dauert $O(E log V)$ = $O(V^2 log V)$. Die anschließende DFS-Durchsuchung dauert $O(V)$ Zeit. Die Gesamtzeit wird durch die MST-Konstruktion dominiert.
Die Platzkomplexität beträgt $O(V^2)$, um die Adjacency Matrix und die Priority Queue zu speichern.

## Varianten & Optimierungen

- **Christofides-Algorithmus:** Eine 1,5-Approximation. Auch hier wird mit einem MST begonnen. Anstatt jedoch einfach blind eine DFS durchzuführen (die darauf angewiesen ist, aufwendige Abkürzungen zu nehmen, um die durch die doppelten Kanten entstandenen Knoten mit ungeradem Grad zu korrigieren), findet Christofides eine perfekte Paarung mit minimalem Gewicht ausschließlich für die Knoten mit ungeradem Grad und fügt genau diese Kanten zum MST hinzu. Dadurch entsteht direkt ein Eulerscher Kreis, wodurch die Approximationsgrenze auf genau 1,5 × OPT sinkt!
- **Held-Karp-DP:** Die exakte Lösung mittels dynamischer Programmierung aus $O(V^2 2^V)$.

## Anwendungen in der Praxis

- **Lieferroutenplanung:** Ein UPS-Lkw ermittelt die Lieferroute für 100 Pakete. Die Abstände zwischen den Häusern gehorchen der Dreiecksungleichung, sodass Approximationen einwandfrei funktionieren.
- **Bohren von Leiterplatten:** Optimierung des Pfades eines Laserbohrers, der Löcher in eine Leiterplatte bohrt.

## Verwandte Algorithmen in cOde(n)

- **[graph_10 – Prim's MST](../graphs/graph_10_prim-s-mst.md)** — Der exakte MST-Algorithmus, der hier als grundlegender Schritt verwendet wird.
- **[approx_04 – Christofides-TSP](approx_04_christofides-tsp-3-2-approx.md)** — Die Verbesserung auf eine 1,5-Approximation.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
