# Dinic-Algorithmus (Max Flow)

| | |
|---|---|
| **ID** | `flow_04` |
| **Kategorie** | Flow |
| **Komplexität (erforderlich)** | $O(V^2 * E)$ |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Dinic's algorithm](https://en.wikipedia.org/wiki/Dinic%27s_algorithm) |

## Problemstellung

Gegeben ist ein gerichteter Graph, der ein Netzwerk von Leitungen mit Kapazitäten repräsentiert. Gesucht ist der maximal mögliche Fluss von einem Quellknoten S zu einem Senkenknoten T.
Während Edmonds-Karp (`flow_02`) eine Zeitkomplexität von $O(V \cdot E^2)$ aufweist und für kleine Graphen ausreicht, müssen Sie den **Dinic-Algorithmus** implementieren, um $O(V^2 \cdot E)$ zu erreichen. Dies ist zwingend erforderlich, wenn der Graph dicht ist oder V > 500 gilt, da der Algorithmus in der Praxis deutlich schneller ist, als es die theoretische Schranke vermuten lässt.

**Eingabe:** Ein gerichteter Graph mit Kapazitäten, ein Quellknoten `s` und ein Senkenknoten `t`.
**Ausgabe:** Eine Ganzzahl, die den maximalen Gesamtfluss repräsentiert.

## Wann man ihn verwendet

- Dinic ist der absolute Goldstandard für Max Flow in der wettbewerbsorientierten Programmierung. Wenn sich ein Problem auf Max Flow reduzieren lässt, verwenden Sie immer Dinic.
- Er ist erstaunlich schnell bei Graphen für Bipartite Matching, wobei die Laufzeit auf exakt $O(E \sqrt{V})$ sinkt (äquivalent zu Hopcroft-Karp).

## Ansatz

Edmonds-Karp verwendet BFS, um einen einzelnen kürzesten Pfad zu finden, schickt Fluss durch diesen einen Pfad und verwirft dann den BFS-Baum. Das ist extrem ineffizient.
**Dinic-Erkenntnis:** Warum nicht ALLE kürzesten Pfade der gleichen Länge gleichzeitig finden?

1. **Level-Graph (BFS):**
   Führen Sie eine BFS von S aus, um jedem Knoten ein `level` zuzuweisen (seine kürzeste Distanz von S).
   Wenn T während dieser BFS nicht erreicht werden kann, sind wir fertig! Der maximale Fluss wurde gefunden.
   Diese BFS strukturiert den Residualgraphen im Wesentlichen in Schichten (Level 0, Level 1, Level 2). Fluss darf nur strikt von Level L zu Level L+1 fließen.

2. **Blockierender Fluss (DFS):**
   Führen Sie nun eine DFS von S aus. Da wir die DFS darauf beschränken, nur Kanten zu durchlaufen, für die `level[v] == level[u] + 1` gilt, ist die DFS physisch gezwungen, nur die absolut kürzesten Pfade zu T zu nehmen!
   Wenn die DFS T erreicht, schickt sie den Flaschenhals-Fluss, aktualisiert die Kapazitäten (einschließlich der Rückwärtskanten) und kehrt zurück.
   **Entscheidende Optimierung:** Wir hören nicht nach einer einzigen DFS auf! Wir führen die DFS immer wieder auf demselben *Level-Graph* aus, bis dieser vollständig "blockiert" ist (es existieren keine Pfade mehr zu T, die genau eine Ebene nach oben führen).

3. **Die `next_edge` Pointer-Optimierung:**
   Während der wiederholten DFS-Aufrufe in Schritt 2 könnte ein Knoten feststellen, dass seine ersten 3 Nachbarn vollständig blockiert sind. Wenn wir später erneut zu diesem Knoten gelangen, sollten wir keine Zeit damit verschwenden, diese 3 Sackgassen erneut zu prüfen! Wir führen ein `ptr`-Array, das sich den zuletzt erkundeten Nachbarn für jeden Knoten merkt, um Sackgassen in $O(1)$ zu überspringen.

4. **Wiederholung:** Sobald der aktuelle Level-Graph vollständig blockiert ist, löschen Sie die Level und kehren Sie zu Schritt 1 zurück, um einen neuen Level-Graph zu erstellen.

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

## Ablauf

*(Konzeptionell)*
1. **BFS (Level-Graph):** Weist S als Level 0 zu. Findet Nachbarn A, B als Level 1. Findet T als Level 2.
2. **DFS-Schleife:**
   - DFS-Pfade MÜSSEN exakt 2 Kanten lang sein (L0 -> L1 -> L2).
   - DFS findet `S -> A -> T`. Schickt Fluss.
   - DFS findet sofort `S -> B -> T`. Schickt Fluss.
   - DFS versucht einen weiteren Pfad zu finden, aber alle Knoten auf Level 1 sind gesättigt oder blockiert. Die Schleife bricht ab.
3. **BFS 2 (Neuer Level-Graph):** Weist S als L0 zu. Da die direkten Leitungen zu T voll sind, wird eine längere Route genommen. A, B sind L1, C ist L2, T ist L3.
4. **DFS-Schleife:** Verfolgt nur L0 -> L1 -> L2 -> L3. Schickt Fluss.
5. **BFS 3:** Kann T nicht erreichen. Maximaler Fluss erreicht! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V + E)$ | $O(V + E)$ |
| **Durchschnittlicher Fall** | Viel schneller als V^2 E | $O(V + E)$ |
| **Schlechtester Fall** | $O(V^2 * E)$ | $O(V + E)$ |

Die Gesamtzahl der erstellten Level-Graphen ist strikt \le V (da die Distanz des kürzesten Pfades in jeder Phase um mindestens 1 zunehmen muss).
Innerhalb einer Phase benötigt das Finden des blockierenden Flusses $O(V \cdot E)$ aufgrund der `ptr`-Array-Optimierung für Sackgassen.
Die Gesamtzeit beträgt exakt $O(V \cdot V \cdot E)$ = $O(V^2 \cdot E)$.
In der Praxis ist der Algorithmus bei zufälligen Graphen näher an $O(E \sqrt{V})$, weshalb er Edmonds-Karp weit überlegen ist.
Die Platzkomplexität beträgt $O(V + E)$ bei Verwendung einer Adjazenzliste mit Kanten-Objekten.

## Varianten & Optimierungen

- **Push-Relabel-Algorithmus:** Ein völlig anderer Ansatz für Max Flow, der keine augmentierenden Pfade verwendet, sondern überschüssigen Fluss lokal zwischen Knoten "schiebt" und deren Höhen "neu markiert" (relabels). Er läuft in $O(V^3)$ oder $O(V^2 \sqrt{E})$ und schlägt Dinic oft bei extrem dichten Graphen (siehe `flow_06`).

## Anwendungen in der Praxis

- **Flugplanung:** Zuweisung von Flugbesatzungen zu einem riesigen täglichen Flugplan, bei dem die Einschränkungen ein tiefes, hochgradig vernetztes bipartites/Fluss-Netzwerk bilden.

## Verwandte Algorithmen in cOde(n)

- **[flow_02 - Edmonds-Karp](flow_02_edmonds-karp.md)** — Der einfachere BFS-basierte Algorithmus.
- **[flow_03 - Bipartite Matching](flow_03_bipartite-matching.md)** — Dinic löst Bipartite Matching-Graphen in exakt $O(E \sqrt{V})$ Zeit.

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für wettbewerbsorientierte Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link oben auf der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*