# A*-Suchalgorithmus

| | |
|---|---|
| **ID** | `graph_18` |
| **Kategorie** | Graphen |
| **Komplexität (erforderlich)** | $O(E)$ Zeit, $O(V)$ Platz (stark variabel) |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [A*-Suchalgorithmus](https://en.wikipedia.org/wiki/A*_search_algorithm) |

## Problemstellung

Gegeben ist ein gewichteter Graph, ein Startknoten `S` und ein spezifischer Zielknoten `T`.
Finde den absolut kürzesten Pfad von `S` nach `T`.
*Optimierung:* Dir steht eine Heuristikfunktion h(n) zur Verfügung, die die verbleibende Distanz von einem beliebigen Knoten n zum Ziel `T` schätzt.

**Eingabe:** Eine Adjazenzliste `adj`, ein Startknoten `S`, ein Zielknoten `T` und eine Heuristikfunktion `h(node)`.
**Ausgabe:** Die kürzeste Distanz zu `T` sowie der zurückgelegte Pfad.

## Wann man ihn verwendet

- **Gezielte Pfadsuche:** Wenn du nicht den kürzesten Pfad zu *jedem* Knoten benötigst (wie Dijkstra ihn berechnet), sondern nur daran interessiert bist, ein spezifisches Ziel so schnell wie möglich zu finden.
- Extrem verbreitet bei gitterbasierten Labyrinth- oder Videospiel-KI-Problemen, bei denen die physischen (X, Y)-Koordinaten der Knoten bekannt sind.

## Ansatz

**1. Der Fehler von Dijkstra:**
Dijkstras Algorithmus ist eine "blinde" Suche. Er expandiert perfekt radial in alle Richtungen von der Quelle aus und erkundet Pfade, die komplett in die entgegengesetzte Richtung führen, mit der gleichen Priorität, nur für den Fall, dass sie einen Umweg bilden.
Wenn du von New York nach Los Angeles fährst, würde Dijkstra Routen in den Atlantischen Ozean mit exakt derselben Priorität erkunden wie Straßen, die nach Westen führen!

**2. Die A*-Gleichung:**
A* leitet Dijkstra, indem es ihm einen Richtungssinn gibt.
Bei Dijkstra sortiert die Priority Queue Knoten strikt nach g(n): der exakten akkumulierten Distanz vom Start zum Knoten n.
Bei A* sortiert die Priority Queue Knoten nach f(n) = g(n) + h(n).
- g(n): Die exakten Kosten vom Start bis n.
- h(n): Die *Heuristik* (eine fundierte Schätzung der Kosten von n zum Ziel).
- f(n): Die geschätzten Gesamtkosten der vollständigen Reise von Start \rightarrow n \rightarrow Ziel.

**3. Zulässigkeit:**
Damit A* mathematisch garantieren kann, den absolut kürzesten Pfad zu finden, MUSS die Heuristikfunktion h(n) "zulässig" (admissible) sein.
Eine zulässige Heuristik ÜBERSCHÄTZT NIEMALS die tatsächlichen Kosten, um das Ziel zu erreichen.
- *Beispiel:* Auf einem 2D-Gitter ist die euklidische Luftliniendistanz zulässig, da man unmöglich schneller als auf einer geraden Linie reisen kann. Die Manhattan-Distanz ist ebenfalls zulässig, wenn diagonale Bewegungen nicht erlaubt sind.
Wenn h(n) die Distanz überschätzt, wird A* vor gültigen Pfaden "zurückschrecken" und möglicherweise selbstbewusst einen suboptimalen Pfad zurückgeben!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_18: A* Search on a 2D grid.

Manhattan-distance heuristic. Walk the grid with 4-neighbour
moves; a priority queue keyed on f = g + h (cost so far plus
Manhattan distance to goal) drives the expansion order.
Return the shortest path length in steps, or -1 if no path.
"""


def solve(grid, start, goal, size):
    from heapq import heappush, heappop
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return -1
    if start == goal:
        return 0

    def heuristic(p):
        return abs(p[0] - goal[0]) + abs(p[1] - goal[1])

    open_heap = []
    heappush(open_heap, (heuristic(start), 0, start))
    g_score = {start: 0}
    while open_heap:
        f, g, current = heappop(open_heap)
        if current == goal:
            return g
        if g > g_score.get(current, float("inf")):
            continue
        row, col = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and grid[nr][nc] == 0:
                nbr = (nr, nc)
                tentative = g + 1
                if tentative < g_score.get(nbr, float("inf")):
                    g_score[nbr] = tentative
                    heappush(open_heap, (tentative + heuristic(nbr), tentative, nbr))
    return -1
```

</details>

## Durchlauf

Gittergraph. Start `S(0,0)`, Ziel `T(2,0)`. Kanten kosten 1.
h(n) ist die Manhattan-Distanz.
`g_score = {S: 0}`.
`pq = [(f=2, g=0, S)]`. (Da h(S, T) = |0-2| + |0-0| = 2).

1. `heappop()` -> `curr = S`.
   - Evaluiere Nachbar `A(1,0)` (Bewegung nach rechts).
     - `tentative_g = 0 + 1 = 1`.
     - `h(A, T) = |1-2| + |0-0| = 1`.
     - `f_score = 1 + 1 = 2`.
     - Push `(2, 1, A)`.
   - Evaluiere Nachbar `B(0,1)` (Bewegung nach oben).
     - `tentative_g = 0 + 1 = 1`.
     - `h(B, T) = |0-2| + |1-0| = 3`.
     - `f_score = 1 + 3 = 4`.
     - Push `(4, 1, B)`.
2. `pq` Zustand: `[(2, 1, A), (4, 1, B)]`.
   - `A` ist an die Spitze sortiert! Beachte, wie A* die Bewegung nach oben (die falsche Richtung) komplett ignoriert, da der f-Wert schlechter ist!
3. `heappop()` -> `curr = A(1,0)`.
   - Evaluiere Nachbar `T(2,0)` (Bewegung nach rechts).
     - `tentative_g = 1 + 1 = 2`.
     - `h(T, T) = 0`.
     - `f_score = 2 + 0 = 2`. Push `(2, 2, T)`.
4. `heappop()` -> `curr = T(2,0)`.
   - `curr == T`. ZIEL ERREICHT! Beende!
   - (Knoten `B` wurde komplett ignoriert, was wertvolle Rechenzyklen spart).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(E)$ | $O(V)$ |
| **Durchschnittlicher Fall** | Stark abhängig von der Heuristik | $O(V)$ |
| **Schlechtester Fall** | $O(E log V)$ | $O(V)$ |

Die Komplexität von A* ist bekanntermaßen schwer zu bestimmen, da sie vollständig von der Qualität der Heuristik h(n) abhängt.
Im schlechtesten Fall (wenn h(n) immer exakt 0 ist), degeneriert A* mathematisch zum Standard-Dijkstra-Algorithmus, der radial in alle Richtungen expandiert und eine Zeitkomplexität von $O(E log V)$ ergibt.
Im besten Fall (wenn h(n) die exakte Distanz zum Ziel perfekt modelliert), marschiert A* direkt auf einer geraden Linie zum Ziel, ohne einen einzigen falschen Zweig zu prüfen! Die Zeitkomplexität wird dann in etwa proportional zur Pfadlänge $O(\text{Pfadlänge})$ ~= $O(E_{optimal})$.
Die Platzkomplexität beträgt $O(V)$ für die Priority Queue und das `g_score`-Dictionary.

## Varianten & Optimierungen

- **IDA* (Iterative Deepening A*):** A* speichert die massive "Frontier" in seiner Priority Queue, was bei komplexen Spielzuständen (wie beim Lösen eines Zauberwürfels) hunderte Megabyte RAM verbrauchen kann. IDA* verwirft die Priority Queue und verwendet eine iterative vertiefende Suche (DFS), die durch den f-Wert begrenzt ist. Dies reduziert die Platzkomplexität drastisch auf $O(\text{Pfadlänge})$, auf Kosten von etwas mehr Zeit.

## Anwendungen in der Praxis

- **Videospiel-KI:** 99 % der Pfadsuche in Strategiespielen (Starcraft, Civilization) oder RPGs wird mittels A* in Kombination mit einer Gitterkarte durchgeführt. Die Heuristik leitet Einheiten mühelos um große Hindernisse herum, ohne die gesamte Karte scannen zu müssen.

## Verwandte Algorithmen in cOde(n)

- **[graph_04 - Dijkstras Algorithmus](graph_04_dijkstra.md)** — Exakt derselbe Algorithmus, nur mit h(n) = 0.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*