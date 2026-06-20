# 8-Puzzle (Branch-and-Bound)

| | |
|---|---|
| **ID** | `bb_04` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(b^d)$ Worst Case |
| **Schwierigkeitsgrad** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **Wikipedia** | [15-Puzzle](https://en.wikipedia.org/wiki/15_puzzle) |

## Aufgabenstellung

Gegeben ist ein 3 × 3-Raster mit 8 nummerierten Kacheln und einem leeren Feld. Bestimme die minimale Anzahl an Zügen, um die Zielkonfiguration zu erreichen. Ein Zug besteht darin, eine benachbarte Kachel in das leere Feld zu schieben.
Dies entspricht genau der Suche nach dem kürzesten Weg in einem ungewichteten Graphen, was man *mit* Standard-BFS lösen *könnte*. Der Zustandsraum für das 15-Puzzle beträgt jedoch 10^{13}, und BFS würde sofort an Speichergrenzen stoßen.
Sie müssen dies mithilfe von **Branch-and-Bound** mit einer Priority Queue lösen (was in diesem spezifischen Kontext der Wegfindung mathematisch identisch mit dem **A*-Suchalgorithmus** ist).

**Eingabe:** Eine 3 × 3-Matrix, die den Startzustand darstellt, und eine Matrix für den Zielzustand.
**Ausgabe:** Die minimale Anzahl der erforderlichen Züge (oder die Abfolge der Züge).

## Wann man es einsetzt

- Zur Lösung von Raster-Schiebepuzzles, Rubik-Würfeln oder beliebigen deterministischen Pfadfindungsproblemen mit einem riesigen Zustandsraum, bei denen die optimale Sequenzlänge ermittelt werden muss.

## Vorgehensweise

Bei „Branch and Bound“ (oder A*) legen wir den Schwerpunkt auf die Erkundung von Zuständen mit den niedrigsten **geschätzten Gesamtkosten**, bezeichnet als f(x) = g(x) + h(x).
1. **g(x) – Die „Branch“-Kosten:** Die Anzahl der Züge, die wir bisher vom Startzustand bis zum aktuellen Zustand ausgeführt haben.
2. **h(x) – Der „Bound“ (Heuristik):** Die geschätzte *Mindestanzahl* der verbleibenden Züge, die erforderlich sind, um das Ziel zu erreichen.
   – Für das Puzzle verwenden wir die **Manhattan-Distanz-Heuristik**. Für jedes Spielfeld berechnen wir, wie viele Zeilen und Spalten es von seiner korrekten Zielposition entfernt ist. Die Summe dieser Abstände ist unsere absolute untere Grenze! (Da ein Spielstein jeweils nur um ein Feld verschoben werden kann, ist es physikalisch unmöglich, sein Ziel mit weniger Zügen als seiner Manhattan-Distanz zu erreichen).
   - *Hinweis: Eine Heuristik ist für B&B/A* nur dann gültig, wenn sie „zulässig“ ist (sie überschätzt niemals die tatsächlichen Kosten).*

**Algorithmus:**
1. Füge den Startzustand in einen Min-Heap (Priority Queue) ein, sortiert nach f(x) = g(x) + h(x).
2. Solange der Heap nicht leer ist:
   - Entnehme den Zustand mit dem niedrigsten f(x).
   - Wenn der Zustand genau mit dem Zielzustand übereinstimmt, ist die Aufgabe gelöst! Gib g(x) zurück. (Da die Heuristik zulässig ist, ist es mathematisch garantiert, dass es sich beim ersten Mal, wenn wir den Zielzustand entnehmen, um den shortest path handelt).
   - Erzeuge alle gültigen nächsten Züge (indem benachbarte Kacheln in die Lücke geschoben werden).
   - Berechne für jeden Tochterzustand dessen neuen Wert g(x) = parent\_g + 1 und dessen neuen Wert h(x).
   - Füge die Tochterzustände in den Min-Heap ein.
   - *(Optimierung: Verfolge besuchte Zustände in einem HashSet, damit du nicht endlos in einer Schleife hängst).*

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
Zielzustand ist `[[1, 2, 3], [4, 5, 6], [7, 8, 0]]`.
Aktueller Zustand: `[[1, 2, 3], [4, 5, 6], [7, 0, 8]]`.

1. **Berechne h(x):** Kachel 8 befindet sich im Zielzustand bei `(2, 2)`, hier jedoch bei `(2, 1)`. Abstand = 1. Leerräume werden ignoriert. h(x) = 1.
2. **Aktueller Knoten:** g(x) = 0, h(x) = 1 -> f(x) = 1. Vom Heap entfernen.
3. **Leerfeld verschieben (0 bei 2,1):**
   - **Nach rechts verschieben (mit 8 tauschen):** Der Zustand wird zum Ziel! g(x) = 1, h(x) = 0. f(x) = 1.
   - **Nach links verschieben (mit 7 vertauschen):** h(x) steigt, da sich 7 von seinem Ziel entfernt hat!
   - **Nach oben verschieben (mit 5 vertauschen):** h(x) steigt, da sich 5 von ihrem Ziel entfernt hat!
4. **Nächster Heap-Pop:** Der Zustand „Nach rechts verschieben“ hat den niedrigsten Wert f(x) = 1. Er wird vom Heap entfernt.
5. **Prüfung:** h(x) == 0. Wir haben das Ziel in genau g=1 Zügen gefunden! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(d)$ | $O(d)$ |
| **Durchschnittlicher Fall** | Deutlich schneller als BFS | $O(Nodes Generated)$ |
| **Schlechtester Fall** | $O(b^d)$ | $O(b^d)$ |

*Dabei ist b der Verzweigungsfaktor (durchschnittlich ~3 Züge pro Zustand) und d die Tiefe der optimalen Lösung.*
Im absolut schlimmsten Fall (z. B. wenn man eine nutzlose Heuristik wie h(x)=0 verwendet) degeneriert der Algorithmus zu einem Standard-Dijkstra-Verfahren bzw. BFS und erzeugt den gesamten Baum $O(b^d)$.
Mit einer starken Heuristik wie dem Manhattan-Abstand hingegen reduziert der Algorithmus den Suchraum erheblich und steuert direkt auf die Lösung zu. Die Platzkomplexität stellt oft den Engpass dar, da die Priority Queue und die Menge der besuchten Zustände bei tiefen Rätseln (wie dem 15-Puzzle) Millionen von Zuständen im Speicher halten.

## Varianten & Optimierungen

- **Heuristik für lineare Konflikte:** Die Manhattan-Distanz geht davon aus, dass sich Kacheln durcheinander verschieben lassen. Befinden sich Kachel A und Kachel B in der richtigen Reihe, A jedoch rechts von B, müssen sie sich physisch aus der Reihe bewegen, um einander zu umgehen! Man kann für jeden linearen Konflikt +2 zur Manhattan-Heuristik addieren, wodurch die Grenze deutlich enger wird und die Knotenerweiterungen drastisch reduziert werden.
- **IDA* (Iterative Deepening A*):** Um den enormen Speicherbedarf der Priority Queue zu beheben, führt IDA* eine standardmäßige Tiefensuche durch, wobei die f(x)-Grenze streng begrenzt wird. Es benötigt $O(d)$ Speicher!

## Praktische Anwendungen

- **Roboter-Wegplanung:** Sichere Navigation von Drohnen um physische Hindernisse herum zu Zielkoordinaten im 3D-Raum.

## Verwandte Algorithmen in cOde(n)

- **[bb_03 – Least Cost B&B Knapsack](bb_03_0-1-knapsack-least-cost-b-b.md)** — Genau derselbe Explorationsmechanismus mit Priority Queue, der anstelle eines Gitters auf ein Array angewendet wird.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
