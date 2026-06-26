# Minimum S-T Cut

| | |
|---|---|
| **ID** | `flow_05` |
| **Kategorie** | flow |
| **Komplexität (erforderlich)** | $O(Max Flow Time)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Max-flow min-cut theorem](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem) |

## Problemstellung

Gegeben ist ein gerichteter Graph, der ein Netzwerk von Leitungen mit Kapazitäten darstellt, sowie ein `source`-Knoten S und ein `sink`-Knoten T.
Finde den **Minimum S-T Cut**: Eine spezifische Menge von Kanten, die, wenn sie vollständig durchtrennt (aus dem Graphen entfernt) werden, S vollständig von T trennen.
Unter allen möglichen Mengen von Kanten, die S von T trennen, musst du diejenige finden, bei der die Summe der Kapazitäten der durchtrennten Kanten das absolute mathematische Minimum darstellt.

**Eingabe:** Ein gerichteter Graph mit Kapazitäten, ein Quellknoten `s` und ein Senkenknoten `t`.
**Ausgabe:** Eine Liste der spezifischen Kanten `(u, v)`, die den Minimum Cut bilden.

## Anwendung

- Zur Identifizierung der absolut kritischsten strukturellen Engpässe in einem Netzwerk.
- Nach dem **Max-Flow Min-Cut Theorem** ist die Gesamtkapazität des Minimum Cut mathematisch exakt gleich dem Maximum Flow! Diese tiefgreifende Dualität bedeutet, dass du den Min-Cut mit deinem bestehenden Max-Flow-Code lösen kannst.

## Vorgehensweise

1. **Max Flow ausführen:** Führe zunächst einen beliebigen Max-Flow-Algorithmus (Ford-Fulkerson, Edmonds-Karp oder Dinic) auf dem Graphen aus, bis das Netzwerk vollständig gesättigt ist.
2. **Der Residualzustand:** Wenn der Max-Flow endet, terminiert der Algorithmus, weil er im *Residualgraphen* keinen Pfad mehr von S nach T finden kann. Das bedeutet, der Fluss ist vollständig durch eine Wand aus voll gesättigten Leitungen blockiert.
3. **Erreichbare Knoten finden:** Führe eine einfache BFS oder DFS ausgehend von S durch und folge dabei strikt nur den Kanten, die noch eine `residual capacity > 0` aufweisen.
   - Die Menge aller Knoten, die du erreichen kannst, wird als Menge A bezeichnet (die Knoten, die noch mit der Quelle verbunden sind).
   - Die Menge aller Knoten, die du nicht erreichen kannst, wird als Menge B bezeichnet (die Knoten, die von der Quelle abgeschnitten sind).
4. **Cut-Kanten identifizieren:** Der Minimum Cut besteht aus allen ursprünglichen Vorwärtskanten, die in Menge A beginnen und in Menge B enden.
   - Warum? Weil dies genau die Leitungen sind, die vollständig gesättigt waren (Restkapazität 0), weshalb unsere abschließende BFS sie nicht nach Menge B überqueren konnte!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for flow_05: Minimum s-t Cut.

Find the minimum s-t cut in a directed flow network.
"""


def solve(n, edges):
    """Min s-t cut via max-flow then residual reachability.

    Returns a sorted list of (u, v) tuples for the cut.
    """
    from collections import deque
    INF = float("inf")
    # Build a fresh capacity matrix.
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    # Ford-Fulkerson with BFS (Edmonds-Karp) on the residual.
    flow = 0
    while True:
        parent = [-1] * n
        parent[0] = 0
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        while q and parent[n - 1] == -1:
            u = q.popleft()
            for v in range(n):
                if not visited[v] and cap[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        if parent[n - 1] == -1:
            break
        path_flow = INF
        v = n - 1
        while v != 0:
            u = parent[v]
            if cap[u][v] < path_flow:
                path_flow = cap[u][v]
            v = u
        v = n - 1
        while v != 0:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        flow += path_flow
    # Now DFS from s in the residual to find reachable set.
    reachable = [False] * n
    reachable[0] = True
    stack = [0]
    while stack:
        u = stack.pop()
        for v in range(n):
            if not reachable[v] and cap[u][v] > 0:
                reachable[v] = True
                stack.append(v)
    # Cut edges: original edges from reachable to non-reachable.
    cut = []
    for u, v, c in edges:
        if reachable[u] and not reachable[v]:
            cut.append((u, v))
    cut.sort()
    return cut
```

</details>

## Durchlauf

*(Konzeptionell)*
Original: `S -> A (cap 10)`, `A -> T (cap 5)`, `S -> B (cap 5)`, `B -> T (cap 10)`.

1. **Max Flow:** Der Gesamtfluss beträgt 5 + 5 = 10.
   - Die Kante `A -> T` ist vollständig gesättigt (Restkapazität 0).
   - Die Kante `S -> B` ist vollständig gesättigt (Restkapazität 0).
2. **Abschließende BFS von S:**
   - Können wir zu `A` gelangen? Ja, `S -> A` hatte ursprünglich 10, wir haben 5 verbraucht, also bleiben 5. `A` ist erreichbar.
   - Können wir `A -> T` gehen? Nein, die Restkapazität ist 0.
   - Können wir `S -> B` gehen? Nein, die Restkapazität ist 0.
   - Erreichbar (Menge A): `{S, A}`.
   - Nicht erreichbar (Menge B): `{B, T}`.
3. **Cut-Kanten finden:**
   - Betrachte die ursprünglichen Kanten, die von `{S, A}` nach `{B, T}` führen.
   - Die Kante `A -> T` ist im Cut enthalten! (Kapazität 5).
   - Die Kante `S -> B` ist im Cut enthalten! (Kapazität 5).
   - Gesamtkapazität des Cut = 10. (Exakt gleich dem Max Flow!) ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(Max Flow Time)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(Max Flow Time)$ | $O(V^2)$ |
| **Schlechtester Fall** | $O(V * E^2)$ | $O(V^2)$ |

Die Zeitkomplexität wird vollständig durch den anfänglichen Max-Flow-Algorithmus dominiert, der zur Sättigung des Graphen verwendet wird. (z. B. $O(V \cdot E^2)$ bei Verwendung von Edmonds-Karp). Die anschließende BFS und der Kanten-Scan zur Ermittlung des Cut benötigen triviale $O(V + E)$ bzw. $O(V^2)$ Zeit.
Die Platzkomplexität beträgt $O(V^2)$ für die Matrizen.

## Varianten & Optimierungen

- **Global Minimum Cut (Stoer-Wagner):** Was ist, wenn man einfach den absolut schwächsten Punkt in einem ungerichteten Graphen finden möchte, unabhängig von S und T? Man könnte den Min S-T Cut für jedes mögliche Knotenpaar berechnen ($O(V^2)$-mal), aber der Stoer-Wagner-Algorithmus findet den Global Min Cut rein algebraisch in $O(V \cdot E + V^2 log V)$ Zeit, ganz ohne Netzwerkfluss!

## Anwendungen in der Praxis

- **Militär & Infrastruktur:** Identifizierung der absolut minimalen Anzahl an Brücken oder Stromleitungen, die zerstört werden müssen, um die Versorgungslinien eines Gegners von einer Hauptstadt zu einer vorgeschobenen Basis perfekt zu unterbrechen.
- **Bildsegmentierung:** In der Computer Vision werden "Graph Cuts" verwendet, um Vordergrundobjekte vom Hintergrund zu trennen, indem Pixel als Knoten und Kantengewichte als Farbähnlichkeiten behandelt werden.

## Verwandte Algorithmen in cOde(n)

- **[flow_02 - Edmonds-Karp](flow_02_edmonds-karp.md)** — Die Engine, die zur Sättigung des Residualgraphen verwendet wird.
- **[flow_01 - Ford Fulkerson](flow_01_ford-fulkerson-max-flow.md)** — Der grundlegende Theorem-Löser.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*