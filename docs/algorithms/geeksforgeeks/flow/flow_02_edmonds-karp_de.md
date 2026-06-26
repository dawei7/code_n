# Edmonds-Karp (Max Flow)

| | |
|---|---|
| **ID** | `flow_02` |
| **Kategorie** | flow |
| **Komplexität (erforderlich)** | $O(V * E^2)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Edmonds–Karp algorithm](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm) |

## Problemstellung

Gegeben ist ein gerichteter Graph, der ein Netzwerk von Leitungen mit Kapazitäten repräsentiert. Finden Sie den maximal möglichen Fluss von einem Quellknoten S zu einem Senkenknoten T.
Sie müssen die Ford-Fulkerson-Methode so optimieren, dass sie in strikt polynomieller Zeit läuft, völlig unabhängig von den tatsächlichen Kapazitätswerten. Dies erreichen Sie durch die Implementierung des **Edmonds-Karp-Algorithmus**.

**Eingabe:** Ein gerichteter Graph mit Kapazitäten, ein Quellknoten `s` und ein Senkenknoten `t`.
**Ausgabe:** Eine Ganzzahl, die den maximalen Gesamtfluss repräsentiert.

## Wann man ihn verwendet

- Dies ist der Standardalgorithmus, der in Vorstellungsgesprächen für Max Flow erwartet wird; er ist sicher und weit verbreitet.
- Verwenden Sie ihn, wenn $V \le 500$. Wenn der Graph deutlich größer ist (z. B. $10^5$ Knoten), müssen Sie auf den Dinic-Algorithmus umsteigen.

## Ansatz

Ford-Fulkerson (`flow_01`) verwendet DFS, um *irgendeinen* Pfad von S nach T zu finden. Wenn die Kapazitäten massiv sind, kann DFS hin und her springen und winzige Flussinkremente schieben, was $O(E \cdot f)$ Zeit in Anspruch nimmt, wobei $f$ der maximale Fluss ist.

**Die Edmonds-Karp-Optimierung:**
Ersetzen Sie einfach die DFS durch eine **Breitensuche (BFS)**!
Anstatt *irgendeinen* Pfad zu finden, garantiert die BFS mathematisch, dass wir immer den **kürzesten augmentierenden Pfad** (in Bezug auf die Anzahl der Kanten) finden.
Indem wir immer den kürzesten Pfad wählen, stellen wir sicher, dass die Distanz von S zu jedem Knoten monoton wächst. Es lässt sich mathematisch beweisen, dass dadurch die Gesamtzahl der Augmentierungen (gefundenen Pfade) über den gesamten Algorithmus hinweg strikt durch $O(V \cdot E)$ begrenzt ist.

1. **Residualgraph:** Initialisieren Sie die `capacity`-Matrix.
2. **BFS-Pfadsuche:** Führen Sie eine BFS von S aus durch. Pflegen Sie ein `parent`-Array, um den Pfad zu rekonstruieren, falls T erreicht wird.
3. **Flaschenhals:** Wenn die BFS T erreicht, verfolgen Sie das `parent`-Array von T zurück nach S, um die Kante mit der minimalen Kapazität entlang des Pfades zu finden (`bottleneck`).
4. **Augmentierung:** Verfolgen Sie das `parent`-Array erneut zurück:
   - Subtrahieren Sie den `bottleneck` von der Vorwärtskante.
   - Addieren Sie den `bottleneck` zur Rückwärtskante.
5. Wiederholen Sie den Vorgang, bis die BFS T nicht mehr erreichen kann.

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

## Durchlauf

*(Konzeptualisierung des pathologischen Falls)*
Stellen Sie sich S, T und die Zwischenknoten A, B vor.
`S -> A (1,000,000)`
`S -> B (1,000,000)`
`A -> B (1)`
`A -> T (1,000,000)`
`B -> T (1,000,000)`

- **DFS (Ford-Fulkerson)** könnte `S -> A -> B -> T` finden (3 Kanten, Flaschenhals 1) und 1 schieben. Dann `S -> B -> A -> T` (unter Verwendung der Rückwärtskante, 3 Kanten, Flaschenhals 1). Es dauert 2.000.000 Iterationen, bis der Vorgang abgeschlossen ist.
- **BFS (Edmonds-Karp)** findet zuerst die *kürzesten* Pfade!
  - Er findet `S -> A -> T` (2 Kanten). Schiebt 1.000.000!
  - Er findet `S -> B -> T` (2 Kanten). Schiebt 1.000.000!
  - Die nächste BFS findet keine Pfade mehr.
  - Edmonds-Karp beendet den gesamten Graphen in genau 2 Iterationen! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(E)$ | $O(V^2)$ |
| **Durchschnittlicher Fall** | $O(V * E)$ | $O(V^2)$ |
| **Schlechtester Fall** | $O(V * E^2)$ | $O(V^2)$ |

Die Gesamtzahl der augmentierenden Pfade, die BFS finden kann, ist mathematisch durch $O(V \cdot E)$ begrenzt.
Jede BFS-Suche benötigt $O(E)$ Zeit.
Die Gesamtzeit beträgt exakt $O(V \cdot E) \cdot O(E) = O(V \cdot E^2)$.
Beachten Sie, dass dies völlig unabhängig vom maximalen Flusswert $f$ ist!
Die Platzkomplexität beträgt $O(V^2)$ für die Adjazenzmatrix (oder $O(V + E)$, wenn sie mittels Listen optimiert wird, obwohl Matrizen für dichte Flussgraphen Standard sind).

## Varianten & Optimierungen

- **Dinic-Algorithmus:** Ein massives Upgrade. Anstatt einen Fluss pro BFS zu senden, verwendet Dinic eine BFS, um einen "Level-Graph" zu erstellen, und nutzt dann eine DFS, um mehrere Flüsse gleichzeitig entlang dieses Level-Graphen zu schieben! Dinic läuft in $O(V^2 E)$ und ist der De-facto-Standard für fortgeschrittene Wettbewerbsprogrammierung.

## Anwendungen in der Praxis

- **Netzwerkbandbreite:** Berechnung des maximalen Datendurchsatzes, den ein Telekommunikationsnetzwerk zwischen zwei Rechenzentren aufrechterhalten kann, ohne Pakete zu verlieren.

## Verwandte Algorithmen in cOde(n)

- **[flow_01 - Ford Fulkerson](flow_01_ford-fulkerson-max-flow.md)** — Der DFS-Vorgänger.
- **[flow_04 - Dinic's Algorithm](flow_04_dinic-s-max-flow.md)** — Der stark optimierte Nachfolger.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*