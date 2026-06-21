# 8-Puzzle (Branch and Bound)

| | |
|---|---|
| **ID** | `bb_04` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(b^d)$ Schlechtester Fall |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **Wikipedia** | [15-Puzzle](https://en.wikipedia.org/wiki/15_puzzle) |

## Problemstellung

Gegeben ist ein 3 x 3 Gitter mit 8 nummerierten Kacheln und einem leeren Feld. Ziel ist es, die minimale Anzahl an Zügen zu finden, um die Zielkonfiguration zu erreichen. Ein Zug besteht darin, eine benachbarte Kachel in das leere Feld zu schieben.
Dies entspricht exakt der Suche nach dem kürzesten Pfad in einem ungewichteten Graphen, was man theoretisch mit einer Standard-BFS lösen *könnte*. Der Zustandsraum des 15-Puzzles beträgt jedoch $10^{13}$, wodurch eine BFS sofort den Arbeitsspeicher erschöpfen würde.
Sie müssen dieses Problem mittels **Branch and Bound** mit einer Priority Queue lösen (was in diesem speziellen Kontext der Pfadsuche mathematisch identisch mit dem **A*-Suchalgorithmus** ist).

**Eingabe:** Eine 3 x 3 Matrix, die den Startzustand repräsentiert, sowie eine Matrix für den Zielzustand.
**Ausgabe:** Die minimale Anzahl der erforderlichen Züge (oder die Sequenz der Züge).

## Wann man es verwendet

- Zur Lösung von Schiebepuzzles, Zauberwürfeln (Rubik's Cubes) oder jedem deterministischen Pfadfindungsproblem mit einem massiven Zustandsraum, bei dem die optimale Sequenzlänge erforderlich ist.

## Ansatz

Bei Branch and Bound (oder A*) priorisieren wir die Erkundung von Zuständen, die die niedrigsten **geschätzten Gesamtkosten** aufweisen, bezeichnet als f(x) = g(x) + h(x).
1. **g(x) - Die "Branch"-Kosten:** Die Anzahl der Züge, die wir bisher vom Startzustand aus getätigt haben, um den aktuellen Zustand zu erreichen.
2. **h(x) - Die "Bound" (Heuristik):** Die geschätzte *minimale* Anzahl an verbleibenden Zügen, die erforderlich sind, um das Ziel zu erreichen.
   - Für das Puzzle verwenden wir die **Manhattan-Distanz-Heuristik**. Berechnen Sie für jede Kachel, wie viele Zeilen und Spalten sie von ihrer korrekten Zielposition entfernt ist. Die Summe dieser Distanzen ist unsere absolute untere Schranke! (Da eine Kachel nur um 1 Feld pro Zug verschoben werden kann, kann sie ihr Ziel physikalisch nicht in weniger Zügen erreichen als ihre Manhattan-Distanz).
   - *Hinweis: Eine Heuristik ist für B&B/A* nur dann gültig, wenn sie "zulässig" (admissible) ist, d. h. sie darf die tatsächlichen Kosten niemals überschätzen.*

**Algorithmus:**
1. Fügen Sie den Startzustand in einen Min-Heap (Priority Queue) ein, sortiert nach f(x) = g(x) + h(x).
2. Solange der Heap nicht leer ist:
   - Entnehmen Sie den Zustand mit dem niedrigsten f(x).
   - Wenn der Zustand exakt dem Zielzustand entspricht, sind Sie fertig! Geben Sie g(x) zurück. (Da die Heuristik zulässig ist, ist das erste Mal, dass wir den Zielzustand entnehmen, mathematisch garantiert der kürzeste Pfad).
   - Generieren Sie alle gültigen nächsten Züge (Verschieben benachbarter Kacheln in das leere Feld).
   - Berechnen Sie für jeden Kindzustand das neue g(x) = parent\_g + 1 und das neue h(x).
   - Fügen Sie die Kindzustände in den Min-Heap ein.
   - *(Optimierung: Verfolgen Sie besuchte Zustände in einem HashSet, um Endlosschleifen zu vermeiden).*

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bb_04: 8-Puzzle (Branch and Bound).

Solve the 8-puzzle (3x3 sliding-tile puzzle with
"""


def solve(start, goal):
    """8-puzzle via B&B with misplaced-tiles heuristic.

    Return the minimum number of moves (depth) of the goal
    node, or -1 if no solution is found within the search
    budget.
    """
    import heapq
    N = 3
    # Flatten the goal to a tuple for O(1) hashing.
    goal_flat = tuple(sum(goal, []))

    def misplaced(board_flat):
        return sum(1 for i, v in enumerate(board_flat) if v != 0 and v != goal_flat[i])

    def neighbors(board, zr, zc, parent_z):
        """Yield (new_board, new_zr, new_zc, move_id) for the four
        possible moves of the blank, skipping the parent
        direction (encoded as the previous (zr, zc))."""
        out = []
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = zr + dr, zc + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) != parent_z:
                # Move blank from (zr, zc) to (nr, nc).
                new = list(board)
                bi = zr * N + zc
                ni = nr * N + nc
                new[bi], new[ni] = new[ni], new[bi]
                out.append((tuple(new), nr, nc))
        return out

    # Find the blank in start.
    start_flat = tuple(sum(start, []))
    try:
        z0 = start_flat.index(0)
    except ValueError:
        return -1
    zr0, zc0 = z0 // N, z0 % N

    # Each entry: (cost, counter, board_flat, zr, zc, depth, parent_z)
    # cost = depth + misplaced(board). We use a counter to break
    # ties so equal-cost nodes are processed FIFO.
    counter = 0
    pq = [(misplaced(start_flat), 0, start_flat, zr0, zc0, 0, None)]
    seen = {start_flat: 0}  # board_flat -> best depth seen
    while pq:
        cost, _, board, zr, zc, depth, parent_z = heapq.heappop(pq)
        if board == goal_flat:
            return depth
        if seen.get(board, float("inf")) < depth:
            continue
        for new_board, nr, nc in neighbors(board, zr, zc, parent_z):
            new_depth = depth + 1
            if seen.get(new_board, float("inf")) <= new_depth:
                continue
            seen[new_board] = new_depth
            counter += 1
            new_cost = new_depth + misplaced(new_board)
            heapq.heappush(pq, (new_cost, counter, new_board, nr, nc,
                                new_depth, (zr, zc)))
    return -1
```

</details>

## Ablaufbeispiel

*(Konzeptionell)*
Zielzustand ist `[[1, 2, 3], [4, 5, 6], [7, 8, 0]]`.
Aktueller Zustand: `[[1, 2, 3], [4, 5, 6], [7, 0, 8]]`.

1. **Berechne h(x):** Kachel 8 befindet sich im Ziel an `(2, 2)`, hier jedoch an `(2, 1)`. Distanz = 1. Das leere Feld wird ignoriert. h(x) = 1.
2. **Aktueller Knoten:** g(x)=0, h(x)=1 -> f(x)=1. Entnahme aus dem Heap.
3. **Verschiebe leeres Feld (0 bei 2,1):**
   - **Nach rechts verschieben (Tausch mit 8):** Zustand wird zum Ziel! g(x)=1, h(x)=0. f(x)=1.
   - **Nach links verschieben (Tausch mit 7):** h(x) steigt, da sich 7 von seinem Ziel entfernt hat!
   - **Nach oben verschieben (Tausch mit 5):** h(x) steigt, da sich 5 von seinem Ziel entfernt hat!
4. **Nächste Heap-Entnahme:** Der Zustand "Nach rechts verschieben" hat das niedrigste f(x)=1. Er wird entnommen.
5. **Überprüfung:** h(x) == 0. Wir haben das Ziel in exakt g=1 Zug gefunden! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(d)$ | $O(d)$ |
| **Durchschnittlicher Fall** | Viel schneller als BFS | $O(Generierte Knoten)$ |
| **Schlechtester Fall** | $O(b^d)$ | $O(b^d)$ |

*Wobei b der Verzweigungsfaktor (durchschnittlich ~3 Züge pro Zustand) und d die Tiefe der optimalen Lösung ist.*
Im absoluten schlimmsten Fall (z. B. bei Verwendung einer nutzlosen Heuristik wie h(x)=0) degeneriert der Algorithmus zu einer Standard-Dijkstra-Suche bzw. BFS und generiert den gesamten Baum $O(b^d)$.
Mit einer starken Heuristik wie der Manhattan-Distanz beschneidet der Algorithmus jedoch den Suchraum massiv und steuert direkt auf die Lösung zu. Die Platzkomplexität ist oft der Flaschenhals, da die Priority Queue und das Set der besuchten Zustände bei tiefen Puzzles (wie dem 15-Puzzle) Millionen von Zuständen im Speicher halten.

## Varianten & Optimierungen

- **Linear Conflict Heuristik:** Die Manhattan-Distanz nimmt an, dass Kacheln durcheinander gleiten können. Wenn Kachel A und Kachel B in der korrekten Zeile sind, aber A rechts von B liegt, müssen sie sich physikalisch aus der Zeile herausbewegen, um aneinander vorbeizukommen! Man kann für jeden linearen Konflikt +2 zur Manhattan-Heuristik addieren, was die Schranke deutlich verschärft und die Knotenerweiterungen drastisch reduziert.
- **IDA* (Iterative Deepening A*):** Um den massiven Speicherverbrauch der Priority Queue zu beheben, führt IDA* eine Standard-Tiefensuche mit einem strikten Cut-off-Limit für die f(x)-Schranke durch. Dies benötigt nur $O(d)$ Speicher!

## Praxisanwendungen

- **Roboter-Pfadplanung:** Sicheres Navigieren von Drohnen um physische Hindernisse zu Zielkoordinaten im 3D-Raum.

## Verwandte Algorithmen in cOde(n)

- **[bb_03 - Least Cost B&B Knapsack](bb_03_0-1-knapsack-least-cost-b-b.md)** — Derselbe Mechanismus der Priority-Queue-Erkundung, angewendet auf ein Array anstelle eines Gitters.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*