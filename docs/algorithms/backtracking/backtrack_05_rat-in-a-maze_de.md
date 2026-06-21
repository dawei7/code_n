# Rat in a Maze

| | |
|---|---|
| **ID** | `backtrack_05` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(4^(N^2)$) Zeit, $O(N^2)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **GeeksForGeeks Äquivalent** | [Rat in a Maze](https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/) |

## Problemstellung

Betrachten Sie eine Ratte, die sich an der Position `(0, 0)` in einer quadratischen `N x N` Matrix befindet. Sie muss das Ziel bei `(N - 1, N - 1)` erreichen. Finden Sie alle möglichen Pfade, die die Ratte nehmen kann, um vom Start zum Ziel zu gelangen.
Die Richtungen, in die sich die Ratte bewegen kann, sind 'U' (up/hoch), 'D' (down/runter), 'L' (left/links), 'R' (right/rechts).
Der Wert `0` in einer Zelle der Matrix bedeutet, dass sie blockiert ist und nicht durchquert werden kann, während der Wert `1` einen offenen Pfad darstellt.

**Eingabe:** Eine `N x N` Ganzzahl-Matrix.
**Ausgabe:** Eine Liste von Strings, wobei jeder String einen gültigen Pfad darstellt (z. B. `"DDRR"`).

## Wann man es verwendet

- Zur Demonstration von klassischem **2D Grid Backtracking**.
- Wenn Sie *alle* Pfade oder die *exakte Sequenz der Züge* finden müssen, anstatt nur die kürzeste Distanz (was mittels BFS gelöst würde).

## Ansatz

**1. Der Entscheidungsbaum:**
An jeder Zelle `(r, c)` im Labyrinth hat die Ratte bis zu 4 Möglichkeiten: sich nach oben, unten, links oder rechts zu bewegen.
Wenn ein Zug zu einer Wand (`0`) führt oder außerhalb der Grenzen liegt, wird dieser Zweig sofort beschnitten (pruned).
Entscheidend ist: Wenn ein Zug zu einer Zelle führt, die die Ratte *auf diesem spezifischen Pfad bereits besucht hat*, muss der Zweig beschnitten werden, um Endlosschleifen zu verhindern (z. B. ein ewiges Oszillieren zwischen Links und Rechts)!

**2. Der Backtracking-Zustand:**
`backtrack(r, c, current_path)`:
- `r`, `c`: Die aktuellen Zeilen- und Spaltenkoordinaten der Ratte.
- `current_path`: Ein String oder eine Liste von Zeichen, die die bisher gemachten Züge repräsentieren (z. B. `["D", "R", "D"]`).

**3. Zustandsverwaltung (Das `visited`-Array):**
Da sich die Ratte in alle 4 Richtungen bewegen kann, MÜSSEN wir nachverfolgen, welche Zellen sich aktuell im Pfad befinden.
Wir können eine separate `visited` Boolean-Matrix verwenden.
- **Entscheidung treffen:** Setze `visited[r][c] = True`. Füge den Zug zu `current_path` hinzu.
- **Rekursion:** Rufe `backtrack()` für die benachbarte Zelle auf.
- **Backtracking:** Setze `visited[r][c] = False`! Dies ist entscheidend! Wir markieren die Zelle als nicht besucht, damit ein völlig *anderer* Pfad diese Zelle später eventuell nutzen kann!

**4. Basisfall:**
Wenn `r == N - 1` und `c == N - 1`, hat die Ratte den Käse erreicht!
Füge `"".join(current_path)` zur globalen Ergebnisliste hinzu und kehre zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for backtrack_05: Rat in a Maze.

Find a path from (0, 0) to (n-1, n-1) in a 0/1 maze. 1 = open.
Move 4-neighbour. Backtracking DFS.
"""


def solve(maze, n):
    if n == 0 or maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return []
    visited = [[False] * n for _ in range(n)]
    path = []

    def helper(r, c):
        if r == n - 1 and c == n - 1:
            path.append((r, c))
            return True
        if r < 0 or c < 0 or r >= n or c >= n:
            return False
        if visited[r][c] or maze[r][c] == 0:
            return False
        visited[r][c] = True
        path.append((r, c))
        if helper(r + 1, c) or helper(r, c + 1):
            return True
        path.pop()
        return False

    if helper(0, 0):
        return path
    return []
```

</details>

## Durchlauf

`maze = [[1, 0], [1, 1]]`. N=2.

1. `backtrack(0, 0, [])`:
   - `visited[0][0] = True`.
   - Versuche 'D' (Down): `nr = 1, nc = 0`. Zelle ist `1`. Nicht besucht.
     - Füge 'D' hinzu. Pfad=`["D"]`.
     - `backtrack(1, 0, ["D"])`:
       - `visited[1][0] = True`.
       - Versuche 'D': Außerhalb der Grenzen.
       - Versuche 'L': Außerhalb der Grenzen.
       - Versuche 'R' (Right): `nr = 1, nc = 1`. Zelle ist `1`. Nicht besucht.
         - Füge 'R' hinzu. Pfad=`["D", "R"]`.
         - `backtrack(1, 1, ["D", "R"])`:
           - `r=1, c=1 == N-1`. BASISFALL! Füge `"DR"` zum Ergebnis hinzu. Rückkehr.
         - Entferne 'R'.
       - Versuche 'U' (Up): `nr = 0, nc = 0`. Zelle ist `1`, ABER `visited[0][0]` ist True! Beschneiden.
       - `visited[1][0] = False`.
     - Entferne 'D'.
   - Versuche 'L': Außerhalb der Grenzen.
   - Versuche 'R': `nr = 0, nc = 1`. Zelle ist `0` (Wand). Beschneiden.
   - Versuche 'U': Außerhalb der Grenzen.
   - `visited[0][0] = False`.

Ergebnis: `["DR"]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(3^(N^2)$) | $O(N^2)$ |
| **Schlechtester Fall** | $O(4^(N^2)$) | $O(N^2)$ |

Im absoluten Schlechtesten Fall (eine vollständig offene Matrix aus 1en) kann die Ratte endlos umherirren und extrem lange, verschlungene Pfade nehmen. An jeder Zelle hat sie bis zu 3 gültige Möglichkeiten (abgesehen von der Zelle, aus der sie gerade kam). Die Pfadlänge kann bis zu $N^2$ betragen. Daher liegt die obere Schranke der Zeitkomplexität bei etwa $O(3^{N^2})$ oder $O(4^{N^2})$.
Die Platzkomplexität beträgt $O(N^2)$ für den rekursiven Aufruf-Stack (der so tief wie die Gesamtzahl der Zellen im Gitter werden kann) und $O(N^2)$ für die `visited` Boolean-Matrix.

## Varianten & Optimierungen

- **In-Place Modifikation (Platzoptimierung):** Sie können die $O(N^2)$ `visited`-Matrix komplett weglassen! Wenn Sie `maze[r][c]` besuchen, mutieren Sie den Wert temporär zu `0` (oder `-1`). Beim Backtracking mutieren Sie ihn zurück zu `1`. Dies spart Speicher, aber das Mutieren von Eingabereferenzen wird in der Produktion oft nicht empfohlen.

## Anwendungen in der Praxis

- **Pfadfindung für Saugroboter:** Berechnung aller erschöpfenden topologischen Durchläufe für einen Reinigungsroboter auf einem verstellten Grundriss.

## Verwandte Algorithmen in cOde(n)

- **[graph_01 - BFS (Shortest Path)](../graphs/graph_01_bfs.md)** — Wenn die Frage nur nach dem *kürzesten* Pfad verlangt, findet BFS diesen in strikter $O(N^2)$-Zeit, was die exponentielle Zeit des Backtrackings weit in den Schatten stellt!
- **[backtrack_06 - Knight's Tour](backtrack_06_knight-s-tour.md)** — Ein weiterer 2D-Gitter-Backtracking-Algorithmus, jedoch mit stark eingeschränkten L-förmigen Sprüngen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*