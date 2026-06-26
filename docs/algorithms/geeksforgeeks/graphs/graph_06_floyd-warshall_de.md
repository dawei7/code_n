# Floyd-Warshall (All-Pairs Shortest Path)

| | |
|---|---|
| **ID** | `graph_06` |
| **Kategorie** | graphs |
| **Komplexität (erforderlich)** | $O(n³)$ |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **Wikipedia** | [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) |

## Problemstellung

Gegeben ist ein **gewichteter Graph** `G = (V, E)` (mit potenziell negativen Gewichten, aber **ohne negative Zyklen**). Gesucht ist die **kürzeste Distanz zwischen jedem Knotenpaar**.

**Eingabe:** Ein Graph mit `n` Knoten und Kantengewichten.
**Ausgabe:** Eine `n × n` Distanzmatrix `dist[u][v]` = die kürzeste Distanz von `u` nach `v` (oder `+∞`, falls nicht erreichbar).

**Beispiel:**

```
Weighted directed graph (4 nodes):
  0 → 1   (5)
  0 → 3   (10)
  1 → 2   (3)
  2 → 3   (1)
  3 → 0   (2)  ← note the back edge

Initial distance matrix:
       0    1    2    3
  0  [ 0,   5,   ∞,  10 ]
  1  [ ∞,   0,   3,   ∞ ]
  2  [ ∞,   ∞,   0,   1 ]
  3  [ 2,   ∞,   ∞,   0 ]

After Floyd-Warshall:
       0    1    2    3
  0  [ 0,   5,   8,   9 ]   ← 0→1→2 = 8, 0→1→2→3 = 9
  1  [ 5,   0,   3,   4 ]   ← 1→2→3 = 4
  2  [ 3,   ∞,   0,   1 ]   ← 2→3→0 = 3
  3  [ 2,   7,  10,   0 ]   ← 3→0→1 = 7, 3→0→1→2 = 10
```

## Wann man es verwendet

- Das Problem der **All-Pairs** kürzesten Pfade. Wenn Distanzen von jedem Knoten zu jedem anderen Knoten benötigt werden, ist Floyd-Warshall die Standardlösung.
- Grundlage für **transitive Hüllen**, **Graphdurchmesser**, **Betweenness Centrality** (mit Johnsons Umgewichtung) und das **Erkennen negativer Zyklen**.

## Ansatz

Für jeden Zwischenknoten `k` wird geprüft, ob der Weg über `k` den Pfad zwischen jedem Paar `(i, j)` verkürzt.

**Rekurrenz:**
```
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

für jeden Zwischenknoten `k = 0..n-1`. Nachdem alle Zwischenknoten verarbeitet wurden, enthält `dist[i][j]` die kürzeste Distanz von `i` nach `j`.

**Warum es funktioniert:** Nach der Verarbeitung der Zwischenknoten `{0..k-1}` enthält die Matrix `dist` die kürzesten Pfade, die nur diese Zwischenknoten verwenden. Fügt man `k` als möglichen Zwischenknoten hinzu, ist der kürzeste Pfad `i → j` unter Verwendung von Zwischenknoten aus `{0..k}` entweder der alte Pfad `i → j` oder ein Pfad, der über `k` führt, d. h. `i → k → j`. Beide Hälften verwenden nur Zwischenknoten aus `{0..k-1}` (die bereits berechnet wurden), daher sind `dist[i][k]` und `dist[k][j]` korrekt.

**Erkennung negativer Zyklen:** Wenn nach dem Algorithmus ein `dist[i][i] < 0` vorliegt, existiert ein negativer Zyklus, der von `i` aus erreichbar ist.

**Pfadrekonstruktion:** Führen Sie eine parallele `next[i][j]` Matrix. Aktualisieren Sie diese jedes Mal, wenn Sie `dist[i][j]` aktualisieren.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_06: Floyd-Warshall.

All-pairs shortest distances via the triple-loop DP.
"""


def solve(num_nodes, edges):
    INF = float("inf")
    dist = [[INF] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        dist[i][i] = 0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
    return [[d if d != INF else -1 for d in row] for row in dist]
```

</details>

## Durchlauf

Graph aus dem Beispiel. 4×4 Matrix.

Nach `k=0`: Pfade können Knoten 0 als Zwischenknoten verwenden.
- (1, 3): 1→0→3 = ∞ + 2 = ∞. Keine Verbesserung.
- (1, 0): 1→0 = ∞. Keine Verbesserung.
- (3, 1): 3→0→1 = 2 + 5 = 7. **dist[3][1] = 7**. ✓
- (2, 1): 2→3→0→1 = 1+2+5 = 8. (Wir benötigen 0 als einzigen Zwischenknoten; 2→3 ist OK, aber 3→0 ist direkt, dann ist 0→1 auch direkt, und wir müssen `k=1` zuerst fertigstellen). Der Algorithmus betrachtet `k` in der Reihenfolge. Nach `k=0` können wir Knoten 0 als Zwischenknoten verwenden. (2, 1) benötigt 2→...→1: 2→3→0→1. Nach `k=0` ist 2→3→0 berechnet, wenn 0s Wert bereits in `dist[2][3]` (= 1) und `dist[3][0]` (= 2) steht. Das sind direkte Kanten, die bei der Initialisierung gesetzt wurden. Also `dist[2][0] = 1+2 = 3`. Dann `dist[2][1] = 3+5 = 8`. ✓

Nach `k=1`: Pfade können Knoten {0, 1} als Zwischenknoten verwenden.
- (0, 2): 0→1→2 = 5+3 = 8. **dist[0][2] = 8**. ✓
- (0, 3): 0→1→2→3 = 5+3+1 = 9. **dist[0][3] = 9**. ✓
- (2, 3): 2→3 = 1 (direkt) vs 2→0→1→3 = 3+5+∞ = ∞. Keine Verbesserung.
- (2, 0): 2→3→0 = 1+2 = 3. ✓ (oder 2→1→0 = 3+∞ = ∞)
- (3, 2): 3→0→1→2 = 2+5+3 = 10. **dist[3][2] = 10**. ✓

Nach `k=2`: Pfade können {0, 1, 2} verwenden.
- Alle bereits optimal.

Nach `k=3`: Pfade können {0, 1, 2, 3} verwenden.
- (1, 0): 1→2→3→0 = 3+1+2 = 6. Nein (bereits 5).
- Alle optimal.

Die finale Matrix entspricht dem Beispiel. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n³)$ | $O(n²)$ |
| **Durchschnittlicher Fall** | $O(n³)$ | $O(n²)$ |
| **Schlechtester Fall** | $O(n³)$ | $O(n²)$ |

Drei verschachtelte Schleifen, jede $O(n)$. Die In-Place-Version benötigt $O(n²)$ Platz (nur die Distanzmatrix).

## Varianten & Optimierungen

- **Transitive Hülle** — `weight` ist ein Boolean (erreichbar oder nicht). Floyd-Warshall berechnet die transitive Hülle in $O(n³)$ — gleicher Code, anderer Typ.
- **Pfad rekonstruieren** — verfolgen Sie `next[i][j]` neben `dist[i][j]`. Um den Pfad `i → j` zu erhalten: wenn `next[i][j] = None`, existiert kein Pfad; ansonsten fügen Sie `j` hinzu und rekursieren Sie auf `i → next[i][j]`, dann fügen Sie `i` am Anfang hinzu.
- **Schneller für dünn besetzte Graphen** — Johnsons Algorithmus gewichtet auf nicht-negative Werte um und führt `n` Dijkstra-Läufe durch. Gesamt $O(n · (n + m) \log n)$, was schneller ist, wenn `m << n²`.
- **Negative Zyklen erkennen** — wenn `dist[i][i] < 0` nach dem Lauf, befindet sich `i` auf einem negativen Zyklus.
- **Häufige Abfragen auf einem kleinen Graphen** — Floyd-Warshall einmal vorab berechnen, Abfragen in $O(1)$.

## Anwendungen in der Praxis

- **Routing-Protokolle** — OSPF verwendet Dijkstra für Single-Source, aber BGP und ähnliche verwenden Analysen im Floyd-Warshall-Stil für Inter-Domain-Routing.
- **Netzwerkanalyse** — Latenz zwischen allen Paaren von Rechenzentren.
- **Compiler-Optimierung** — Eliminierung gemeinsamer Teilbereiche über Basisblöcke hinweg.
- **Soziale Netzwerkanalyse** — kürzester Pfad zwischen jedem Nutzerpaar (Graphdurchmesser, Betweenness).
- **Spieltheorie** — Finden von Gleichgewichten über Graphdistanzen.
- **Biologie** — phylogenetische Distanzmatrizen.

## Verwandte Algorithmen in cOde(n)

- **[graph_04 — Dijkstra](graph_04_dijkstra.md)** — Single-Source bei nicht-negativen Gewichten. (d=5/10, r=8/10)
- **[graph_05 — Bellman-Ford](graph_05_bellman-ford.md)** — Single-Source, erlaubt negative Gewichte. (d=6/10, r=8/10)
- **[graph_02 — BFS](graph_02_bfs.md)** — der ungewichtete Spezialfall für alle Paare (Distanzmatrix = Erreichbarkeitsmatrix). (d=4/10, r=8/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*