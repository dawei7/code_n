# Edmonds-Karp (Max Flow)

| | |
|---|---|
| **ID** | `flow_02` |
| **Kategorie** | Durchfluss |
| **Komplexität (erforderlich)** | $O(V * E^2)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Edmonds–Karp-Algorithmus](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm) |

## Problemstellung

Gegeben sei ein gerichteter Graph, der ein Rohrleitungsnetz mit Kapazitäten darstellt. Bestimmen Sie den maximal möglichen Fluss von einem Quellknoten S zu einem Senkenknoten T.
Sie müssen die Ford-Fulkerson-Methode so optimieren, dass sie in streng polynomieller Zeit läuft, völlig unabhängig von den tatsächlichen Kapazitätswerten. Dies erreichen Sie durch die Implementierung des **Edmonds-Karp-Algorithmus**.

**Eingabe:** Ein gerichteter Graph mit Kapazitäten, einem Quellknoten `s` und einem Senkenknoten `t`.
**Ausgabe:** Eine ganze Zahl, die den maximalen Gesamtfluss angibt.

## Wann man ihn verwenden sollte

- Dies ist der Standardalgorithmus für den Max-Flow-Algorithmus, der in Vorstellungsgesprächen erwartet wird und als der sicherste sowie am häufigsten verwendete gilt.
- Verwenden Sie ihn immer dann, wenn V \le 500 ist. Ist der Graph deutlich größer (z. B. 10^5 Knoten), müssen Sie auf den Dinic-Algorithmus umsteigen.

## Vorgehensweise

Ford-Fulkerson (`flow_01`) verwendet DFS, um *beliebige* Pfade von S nach T zu finden. Bei sehr hohen Kapazitäten kann DFS hin und her springen und dabei nur winzige Flussinkremente verschieben, was die Zeit $O(E x f)$ in Anspruch nimmt, wobei f der maximale Fluss ist.

**Die Edmonds-Karp-Optimierung:**
Ersetze einfach die DFS durch **Breiten-Tiefen-Suche (BFS)**!
Anstatt *einen beliebigen* Pfad zu finden, garantiert die BFS mathematisch, dass wir immer den **kürzesten augmentierenden Pfad** (gemessen an der Anzahl der Kanten) finden.
Indem wir immer den shortest path wählen, stellen wir sicher, dass die Entfernung von S zu jedem Knoten monoton zunimmt. Es lässt sich mathematisch beweisen, dass aus diesem Grund die Gesamtzahl der Augmentationen (gefundener Pfade) über den gesamten Algorithmus hinweg streng durch $O(V x E)$ begrenzt ist.

1. **Restgraph:** Initialisiere die `capacity`-Matrix.
2. **BFS-Pfadsuche:** Führe BFS von S aus durch. Verwalte ein `parent`-Array, um den Pfad zu rekonstruieren, falls T erreicht wird.
3. **Engpass:** Wenn BFS T erreicht, durchlaufe das `parent`-Array rückwärts von T nach S, um die Kante mit der minimalen Kapazität entlang des Pfades zu finden (`bottleneck`).
4. **Ergänzung:** Durchlaufen Sie das `parent`-Array erneut rückwärts:
   - Subtrahieren Sie `bottleneck` von der Vorwärtskante.
   - Addieren Sie `bottleneck` zur Rückwärtskante.
5. Wiederhole dies, bis BFS T nicht mehr erreichen kann.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for flow_02: Edmonds-Karp.

BFS-based augmenting path. O(V * E^2).
"""


def solve(n, edges):
    from collections import deque
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
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
        path_flow = float("inf")
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
    return flow
```

</details>

## Schritt-für-Schritt-Anleitung

*(Konzeption des pathologischen Falls)*
Stellen Sie sich S, T und die Zwischenknoten A, B vor.
`S -> A (1,000,000)`
`S -> B (1,000,000)`
`A -> B (1)`
`A -> T (1,000,000)`
`B -> T (1,000,000)`

- **DFS (Ford-Fulkerson)** könnte `S -> A -> B -> T` (3 Kanten, Engpass 1) finden und 1 einfügen. Dann `S -> B -> A -> T` (unter Verwendung der Rückwärtskante, 3 Kanten, Engpass 1). Es dauert 2.000.000 Iterationen, bis der Vorgang abgeschlossen ist.
- **BFS (Edmonds-Karp)** findet zuerst die *kürzesten* Pfade!
  - Es findet `S -> A -> T` (2 Kanten). Schiebt 1.000.000 auf den Stack!
  - Es findet `S -> B -> T` (2 Kanten). Schiebt 1.000.000 auf den Stack!
  - Als Nächstes findet BFS keine Wege mehr.
  - Edmonds-Karp bearbeitet den gesamten Graphen in genau 2 Iterationen! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(E)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(V * E)$ | $O(V^2)$ |
| **Schlechtester Fall** | $O(V * E^2)$ | $O(V^2)$ |

Die Gesamtzahl der augmentierenden Pfade, die BFS finden kann, ist mathematisch durch $O(V x E)$ begrenzt.
Jede BFS-Suche dauert $O(E)$ Zeit.
Die Gesamtzeit beträgt genau $O(V x E)$ × $O(E)$ = $O(V \cdot E^2)$.
Beachte, dass dies völlig unabhängig vom maximalen Flusswert f ist!
Die Platzkomplexität beträgt $O(V^2)$ für die Adjacency Matrix (oder $O(V + E)$, wenn sie mithilfe von Listen optimiert wird, wobei Matrizen für dichte Flussgraphen Standard sind).

## Varianten & Optimierungen

- **Dinics Algorithmus:** Eine massive Verbesserung. Anstatt pro BFS-Durchlauf einen Fluss zu senden, nutzt Dinics Algorithmus BFS, um einen „Level-Graphen“ aufzubauen, und verwendet dann DFS, um mehrere Flüsse gleichzeitig entlang dieses Level-Graphen zu schieben! Der Dinic-Algorithmus läuft in $O(V^2 E)$ und ist der De-facto-Standard für fortgeschrittene Wettbewerbs-Programmierung.

## Anwendungen in der Praxis

- **Netzwerkbandbreite:** Berechnung des maximalen Datendurchsatzes, den ein Telekommunikationsnetzwerk zwischen zwei Rechenzentren ohne Paketverlust aufrechterhalten kann.

## Verwandte Algorithmen in cOde(n)

- **[flow_01 – Ford-Fulkerson](flow_01_ford-fulkerson-max-flow.md)** — Der Vorgänger des DFS.
- **[flow_04 – Dinics Algorithmus](flow_04_dinic-s-max-flow.md)** — Der stark optimierte Nachfolger.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
