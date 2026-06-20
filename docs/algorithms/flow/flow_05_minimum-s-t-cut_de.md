# Minimaler S-T-Schnitt

| | |
|---|---|
| **ID** | `flow_05` |
| **Kategorie** | flow |
| **Komplexität (erforderlich)** | $O(Max Flow Time)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Max-Flow-Min-Cut-Theorem](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem) |

## Problemstellung

Gegeben sei ein gerichteter Graph, der ein Rohrleitungsnetz mit Kapazitäten darstellt, sowie ein `source`-Knoten S und ein `sink`-Knoten T.
Finde den **minimalen S-T-Schnitt**: Eine bestimmte Menge von Kanten, die, wenn sie vollständig durchtrennt (aus dem Graphen entfernt) würden, S vollständig von T trennen würden.
Unter allen möglichen Mengen von Kanten, die S von T trennen, musst du diejenige finden, bei der die Summe der Kapazitäten der durchtrennten Kanten das absolute mathematische Minimum darstellt.

**Eingabe:** Ein gerichteter Graph mit Kapazitäten, einem Quellknoten `s` und einem Zielknoten `t`.
**Ausgabe:** Eine Liste der spezifischen Kanten `(u, v)`, die den minimum cut bilden.

## Wann man es einsetzt

- Um die absolut anfälligsten strukturellen Engpässe in einem Netzwerk zu identifizieren.
- Nach dem **Max-Flow-Min-Cut-Theorem** ist die Gesamtkapazität des minimalen Schnitts mathematisch genau gleich dem maximum flow! Diese tiefgreifende Dualität bedeutet, dass Sie das Min-Cut-Problem mit Ihrem bestehenden Max-Flow-Code lösen können.

## Vorgehensweise

1. **Max-Flow ausführen:** Führen Sie zunächst einen beliebigen Max-Flow-Algorithmus (Ford-Fulkerson, Edmonds-Karp oder Dinic) auf dem Graphen aus, bis das Netzwerk vollständig gesättigt ist.
2. **Der Restzustand:** Wenn der Max-Flow-Algorithmus beendet ist, bricht er ab, da er im *Restgraphen* keinen Pfad mehr von S nach T finden kann. Das bedeutet, dass der Fluss vollständig durch eine Wand aus vollständig gesättigten Leitungen blockiert ist.
3. **Ermitteln der erreichbaren Knoten:** Führe eine einfache BFS- oder DFS-Suche ausgehend von S durch und folge dabei streng nur den Kanten, die noch `residual capacity > 0` aufweisen.
   - Die Menge aller Knoten, die du erreichen kannst, wird als Menge A bezeichnet (die Knoten, die noch mit der Quelle verbunden sind).
   - Die Menge aller Knoten, die man nicht erreichen kann, wird als Menge B bezeichnet (die von der Quelle abgeschnittenen Knoten).
4. **Identifiziere die Schnittkanten:** Der Minimalschnitt besteht aus allen ursprünglichen Vorwärtskanten, die in Menge A beginnen und in Menge B enden.
   - Warum? Weil dies genau die Leitungen sind, die vollständig ausgelastet waren (keine Restkapazität mehr vorhanden), weshalb unser abschließender BFS sie nicht in Menge B überqueren konnte!

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
Original: `S -> A (cap 10)`, `A -> T (cap 5)`, `S -> B (cap 5)`, `B -> T (cap 10)`.

1. **Maximaler Durchfluss:** Der Gesamtdurchfluss beträgt 5 + 5 = 10.
   - Die Kante `A -> T` ist vollständig ausgelastet (Restkapazität 0).
   - Die Kante `S -> B` ist vollständig ausgelastet (Restkapazität 0).
2. **Abschließender BFS von S:**
   - Können wir zu `A` gehen? Ja, `S -> A` hatte ursprünglich 10, wir haben 5 verbraucht, also bleiben 5 übrig. `A` ist erreichbar.
   - Können wir zu `A -> T` gehen? Nein, die Restkapazität beträgt 0.
   - Können wir zu `S -> B` gehen? Nein, die Restkapazität beträgt 0.
   - Erreichbar (Menge A): `{S, A}`.
   - Nicht erreichbar (Menge B): `{B, T}`.
3. **Schnittkanten finden:**
   - Betrachte die ursprünglichen Kanten, die von `{S, A}` nach `{B, T}` führen.
   - Die Kante `A -> T` liegt im Schnitt! (Kapazität 5).
   - Die Kante `S -> B` liegt im Schnitt! (Kapazität 5).
   - Gesamtschnittkapazität = 10. (Entspricht genau dem maximalen Durchfluss!) ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(Max Flow Time)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(Max Flow Time)$ | $O(V^2)$ |
| **Schlechtester Fall** | $O(V * E^2)$ | $O(V^2)$ |

Die Zeitkomplexität wird vollständig von dem anfänglichen Max-Flow-Algorithmus bestimmt, der zur Sättigung des Graphen verwendet wird. (Z. B. $O(V \cdot E^2)$, wenn Edmonds-Karp verwendet wird). Die anschließende BFS-Suche und der Kanten-Scan zur Ermittlung des Schnitts benötigen nur eine vernachlässigbare Zeit von $O(V + E)$ bzw. $O(V^2)$.
Die Platzkomplexität beträgt $O(V^2)$ für die Matrizen.

## Varianten & Optimierungen

- **Globales Minimalschnitt (Stoer-Wagner):** Was ist, wenn man einfach nur den absolut schwächsten Punkt in einem ungerichteten Graphen finden möchte, unabhängig von S und T? Man könnte den Min-S-T-Schnitt für jedes mögliche Knotenpaar ausführen ($O(V^2)$ Mal), aber der Stoer-Wagner-Algorithmus findet den globalen Minimalschnitt rein algebraisch in $O(V \cdot E + V^2 log V)$ Zeit, ohne den Netzfluss überhaupt zu verwenden!

## Anwendungen in der Praxis

- **Militär & Infrastruktur:** Ermittlung der absolut minimalen Anzahl an Brücken oder Stromleitungen, die zerstört werden müssen, um die feindlichen Versorgungslinien von einer Hauptstadt zu einem vorgeschobenen Stützpunkt vollständig zu unterbrechen.
- **Bildsegmentierung:** In der Bildverarbeitung werden „Graph Cuts“ verwendet, um Objekte im Vordergrund vom Hintergrund zu trennen, indem Pixel als Knoten und Kantengewichte als Farbähnlichkeiten behandelt werden.

## Verwandte Algorithmen in cOde(n)

- **[flow_02 – Edmonds-Karp](flow_02_edmonds-karp.md)** — Die Engine, die zur Sättigung des Restgraphen verwendet wird.
- **[flow_01 – Ford-Fulkerson](flow_01_ford-fulkerson-max-flow.md)** – Der Solver für den Fundamentalsatz.

---

*Diese Dokumentation ist ein für cOde(n) verfasster Originalinhalt,
der sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
