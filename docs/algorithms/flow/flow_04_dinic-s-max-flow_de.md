# Dinics Algorithmus (Maximalstrom)

| | |
|---|---|
| **ID** | `flow_04` |
| **Kategorie** | Fluss |
| **Komplexität (erforderlich)** | $O(V^2 * E)$ |
| **Schwierigkeitsgrad** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Dinics Algorithmus](https://en.wikipedia.org/wiki/Dinic%27s_algorithm) |

## Problemstellung

Gegeben ist ein gerichteter Graph, der ein Rohrleitungsnetz mit Kapazitäten darstellt. Bestimme den maximal möglichen Fluss von einem Quellknoten S zu einem Senkenknoten T.
Während Edmonds-Karp (`flow_02`) $O(V \cdot E^2)$ Zeit benötigt und für kleine Graphen ausreichend ist, müssen Sie den **Dinic-Algorithmus** implementieren, um $O(V^2 \cdot E)$ Zeit zu erreichen. Dies ist zwingend erforderlich, wenn der Graph dicht ist oder V > 500, da er in der Praxis deutlich schneller ist, als es seine theoretische Grenze vermuten lässt.

**Eingabe:** Ein gerichteter Graph mit Kapazitäten, einem Quellknoten `s` und einem Senkknoten `t`.
**Ausgabe:** Eine ganze Zahl, die den maximalen Gesamtfluss angibt.

## Wann man ihn verwenden sollte

- Der Dinic-Algorithmus ist der absolute Goldstandard für das Max-Flow-Problem in der Wettbewerbsprogrammierung. Wenn sich ein Problem auf das Max-Flow-Problem reduzieren lässt, sollte man immer den Dinic-Algorithmus verwenden.
- Bei biparten Matching-Graphen ist es erstaunlich schnell und sinkt auf genau $O(E \sqrt{V})$ (entspricht Hopcroft-Karp).

## Vorgehensweise

Edmonds-Karp nutzt BFS, um einen einzigen shortest path zu finden, leitet den Fluss über diesen einen Pfad weiter und verwirft anschließend den BFS-Baum. Das ist unglaublich verschwenderisch.
**Dinics Erkenntnis:** Warum nicht ALLE kürzesten Pfade gleicher Länge auf einmal finden?

1. **Ebenengraph (BFS):**
   Führe einen BFS von S aus durch, um jedem Knoten einen Wert von `level` zuzuweisen (seine kürzeste Entfernung von S).
   Wenn T während dieses BFS nicht erreicht werden kann, sind wir fertig! Der maximale Fluss wurde gefunden.
   Dieser BFS strukturiert den Restgraphen im Wesentlichen in Ebenen (Ebene 0, Ebene 1, Ebene 2). Der Fluss darf sich ausschließlich von Ebene L nach Ebene L+1 bewegen.

2. **Blockierender Fluss (DFS):**
   Führe nun eine DFS von S aus durch. Da wir die DFS darauf beschränken, nur Kanten zu durchlaufen, auf denen `level[v] == level[u] + 1` gilt, ist die DFS physikalisch gezwungen, nur die absolut kürzesten Wege zu T zu nehmen!
   Wenn die DFS T erreicht, schiebt sie den Engpassfluss ein, aktualisiert die Kapazitäten (einschließlich der rückwärtsgerichteten Kanten) und kehrt zurück.
   **Entscheidende Optimierung:** Wir hören nicht nach einem einzigen DFS auf! Wir führen den DFS immer wieder auf dem *selben Ebenengraphen* durch, bis der Ebenengraph vollständig „blockiert“ ist (es gibt keine Pfade mehr zu T, die genau eine Ebene nach oben führen).

3. **Die `next_edge`-Zeigeroptimierung:**
   Während der wiederholten DFS-Aufrufe in Schritt 2 kann es vorkommen, dass ein Knoten feststellt, dass seine ersten drei Nachbarn vollständig blockiert sind. Wenn wir später erneut DFS auf diesen Knoten anwenden, sollten wir keine Zeit damit verschwenden, diese drei toten Nachbarn erneut zu überprüfen! Wir verwalten ein `ptr`-Array, das für jeden Knoten den zuletzt erkundeten Nachbarn speichert, wodurch Sackgassen in $O(1)$-Zeit übersprungen werden.

4. **Wiederholen:** Sobald der aktuelle Level-Graph vollständig blockiert ist, lösche die Levels und kehre zu Schritt 1 zurück, um einen neuen Level-Graph zu erstellen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for flow_04: Dinic's Max Flow.

Compute the max s-t flow in a directed capacitated
"""


def solve(n, edges):
    """Dinic's max flow on an adjacency-matrix residual graph.

    Returns the max flow from 0 to n-1.
    """
    from collections import deque
    INF = float("inf")
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    flow = 0
    while True:
        # BFS builds the level graph.
        level = [-1] * n
        level[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v in range(n):
                if level[v] < 0 and cap[u][v] > 0:
                    level[v] = level[u] + 1
                    q.append(v)
        if level[n - 1] < 0:
            break
        # DFS sends blocking flow along level-monotone paths.
        it = [0] * n
        def dfs(u, f):
            if u == n - 1:
                return f
            for i in range(it[u], n):
                v = i
                it[u] = i
                if level[v] == level[u] + 1 and cap[u][v] > 0:
                    pushed = dfs(v, min(f, cap[u][v]))
                    if pushed:
                        cap[u][v] -= pushed
                        cap[v][u] += pushed
                        return pushed
            return 0
        while True:
            pushed = dfs(0, INF)
            if not pushed:
                break
            flow += pushed
    return flow
```

</details>

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
1. **BFS (Ebenengraph):** Weist S als Ebene 0 zu. Findet die Nachbarn A und B als Ebene 1. Findet T als Ebene 2.
2. **DFS-Schleife:**
   - DFS-Pfade MÜSSEN genau 2 Kanten lang sein (L0 -> L1 -> L2).
   - DFS findet `S -> A -> T`. Schiebt den Fluss auf den Stack.
   - DFS findet sofort `S -> B -> T`. Der Fluss wird weitergeleitet.
   - DFS versucht, einen anderen Pfad zu finden, aber alle Knoten der Ebene 1 sind gesättigt oder blockiert. Die Schleife bricht ab.
3. **BFS 2 (Grafik mit neuer Ebene):** Weist S als L0 zu. Da die direkten Leitungen zu T voll sind, wird ein längerer Weg genommen. A und B sind L1, C ist L2, T ist L3.
4. **DFS-Schleife:** Verfolgt nur L0 -> L1 -> L2 -> L3. Schiebt den Fluss weiter.
5. **BFS 3:** T kann nicht erreicht werden. Maximum Flow erreicht! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V + E)$ |
| **Durchschnittlicher Fall** | Deutlich schneller als V^2 E | $O(V + E)$ |
| **Schlechtester Fall** | $O(V^2 * E)$ | $O(V + E)$ |

Die Gesamtzahl der erstellten Level-Graphen ist streng \le V (da die Entfernung des kürzesten Pfades in jeder Phase um mindestens 1 zunehmen muss).
Innerhalb einer einzelnen Phase dauert das Auffinden des blockierenden Flusses $O(V \cdot E)$ aufgrund der Optimierung des Dead-End-Arrays `ptr`.
Die Gesamtzeit beträgt genau $O(V x V \cdot E)$ = $O(V^2 \cdot E)$.
In der Praxis liegt die Laufzeit bei zufälligen Graphen näher bei $O(E \sqrt{V})$, weshalb dieses Verfahren gegenüber Edmonds-Karp deutlich bevorzugt wird.
Die Platzkomplexität beträgt $O(V + E)$ unter Verwendung der Kantenobjekt-Adjacency List.

## Varianten und Optimierungen

- **Push-Relabel-Algorithmus:** Ein völlig anderer Ansatz für den Max-Flow-Algorithmus, der überhaupt keine Augmentierungspfade verwendet, sondern überschüssigen Fluss lokal zwischen Knoten „verschiebt“ und deren Höhen „neu kennzeichnet“. Er läuft in $O(V^3)$ oder $O(V^2 \sqrt{E})$ und übertrifft bei extrem dichten Graphen oft den Dinic-Algorithmus (siehe `flow_06`).

## Anwendungen in der Praxis

- **Flugplanerstellung:** Zuweisung von Flugbesatzungen zu einem umfangreichen täglichen Flugplan, bei dem die Einschränkungen ein tiefes, stark vernetztes bipartites Flow Network bilden.

## Verwandte Algorithmen in cOde(n)

- **[flow_02 – Edmonds-Karp](flow_02_edmonds-karp.md)** — Der einfachere, auf BFS basierende Algorithmus.
- **[flow_03 – Bipartite Matching](flow_03_bipartite-matching.md)** — Der Dinic-Algorithmus löst Bipartite-Matching-Graphen exakt in $O(E \sqrt{V})$-Zeit.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
