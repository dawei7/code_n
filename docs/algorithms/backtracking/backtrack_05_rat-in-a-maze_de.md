# Ratte im Labyrinth

| | |
|---|---|
| **ID** | `backtrack_05` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(4^(N^2)$) Zeit, $O(N^2)$ Speicherplatz |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **GeeksForGeeks-Äquivalent** | [Ratte im Labyrinth](https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/) |

## Aufgabenstellung

Betrachten wir eine Ratte, die sich an der Position `(0, 0)` in einer quadratischen `N x N`-Matrix befindet. Sie muss das Ziel bei `(N - 1, N - 1)` erreichen. Finde alle möglichen Wege, die die Ratte nehmen kann, um vom Start zum Ziel zu gelangen.
Die Richtungen, in die sich die Ratte bewegen kann, sind „U“ (nach oben), „D“ (nach unten), „L“ (nach links) und „R“ (nach rechts).
Der Wert `0` in einer Zelle der Matrix bedeutet, dass diese blockiert ist und nicht überquert werden kann, während der Wert `1` einen freien Weg darstellt.

**Eingabe:** Eine `N x N` ganzzahlige Matrix.
**Ausgabe:** Eine Liste von Zeichenketten, wobei jede Zeichenkette einen gültigen Weg darstellt (z. B. `"DDRR"`).

## Wann man es verwendet

- Zur Veranschaulichung des klassischen **2D-Gitter-Backtracking**.
- Wenn Sie *alle* Pfade oder die *genaue Abfolge der Züge* finden müssen, anstatt nur die kürzeste Entfernung (was BFS wäre).

## Vorgehensweise

**1. Der Entscheidungsbaum:**
An jeder Zelle `(r, c)` im Labyrinth hat die Ratte bis zu 4 Möglichkeiten: nach oben, unten, links oder rechts bewegen.
Führt ein Zug zu einer Wand (`0`) oder verlässt er den Spielbereich, wird dieser Zweig sofort entfernt.
Entscheidend ist: Führt ein Zug zu einer Zelle, die die Ratte *auf diesem spezifischen Pfad bereits besucht hat*, muss der Zweig entfernt werden, um Endlosschleifen zu verhindern (z. B. endloses Hin- und Herpendeln zwischen links und rechts)!

**2. Der Backtracking-Zustand:**
`backtrack(r, c, current_path)`:
- `r`, `c`: Die aktuellen Zeilen- und Spaltenkoordinaten der Ratte.
- `current_path`: Eine Zeichenkette oder Liste von Zeichen, die die bisher ausgeführten Züge darstellt (z. B. `["D", "R", "D"]`).

**3. Zustandsverwaltung (das „Visited“-Array):**
Da sich die Ratte in alle vier Richtungen bewegen kann, MÜSSEN wir verfolgen, welche Zellen derzeit auf dem Weg liegen.
Dazu können wir eine separate boolesche Matrix `visited` verwenden.
- **Entscheidung treffen:** `visited[r][c] = True` markieren. Zug an `current_path` anhängen.
- **Rekursion:** Rufe `backtrack()` für die benachbarte Zelle auf.
- **Backtracking:** Markiere `visited[r][c] = False`! Dies ist entscheidend! Wir heben die Markierung der Zelle auf, damit ein völlig *anderer* Pfad diese Zelle später möglicherweise nutzen kann!

**4. Basisfall:**
Wenn `r == N - 1` und `c == N - 1`, hat die Ratte den Käse erreicht!
Füge `"".join(current_path)` an die globale Ergebnisliste an und kehre zurück.

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

## Schritt-für-Schritt-Anleitung

`maze = [[1, 0], [1, 1]]`. N=2.

1. `backtrack(0, 0, [])`:
   - `visited[0][0] = True`.
   - „D“ (nach unten) ausprobieren: `nr = 1, nc = 0`. Zelle ist `1`. Noch nicht besucht.
 - „D“ anhängen. Pfad=`["D"]`.
 - `backtrack(1, 0, ["D"])`:
 - `visited[1][0] = True`.
 - „D“ ausprobieren: Außerhalb des Bereichs.
       - Versuche „L“: Außerhalb des Bereichs.
 - Versuche „R“ (rechts): `nr = 1, nc = 1`. Zelle ist `1`. Noch nicht besucht.
         - „R“ anhängen. Pfad=`["D", "R"]`.
 - `backtrack(1, 1, ["D", "R"])`:
 - `r=1, c=1 == N-1`. BASISFALL! `"DR"` an das Ergebnis anhängen. Zurück.
 - „R“ entfernen.
 - „U“ (nach oben) versuchen: `nr = 0, nc = 0`. Zelle ist `1`, ABER `visited[0][0]` ist wahr! Ausmerzen.
       - `visited[1][0] = False`.
 - „D“ entfernen.
   - „L“ versuchen: Außerhalb des Bereichs.
   - „R“ versuchen: `nr = 0, nc = 1`. Zelle ist `0` (Wand). Verzweigung abbrechen.
   - Versuche „U“: Außerhalb des Bereichs.
   - `visited[0][0] = False`.

Ergebnis: `["DR"]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(3^(N^2)$) | $O(N^2)$ |
| **Schlechtester Fall** | $O(4^(N^2)$) | $O(N^2)$ |

Im absolut schlimmsten Fall (eine vollständig offene Matrix aus Einsen) kann die Ratte endlos umherirren und dabei extrem lange, gewundene Wege zurücklegen. An jeder Zelle hat sie bis zu 3 gültige Auswahlmöglichkeiten (abgesehen von der Zelle, aus der sie gerade gekommen ist). Die Weglänge kann bis zu N² betragen. Somit liegt die obere Grenze der Zeitkomplexität bei etwa $O(3^{N^2})$ oder $O(4^{N^2})$.
Die Platzkomplexität beträgt $O(N^2)$ für den rekursiven Aufrufstapel (der bis zur Gesamtzahl der Zellen im Raster reichen kann) und $O(N^2)$ für die `visited`-Boolesche Matrix.

## Varianten & Optimierungen

- **In-Place-Modifikation (Speicheroptimierung):** Man kann die $O(N^2)$ `visited`-Matrix komplett weglassen! Wenn Sie `maze[r][c]` besuchen, ändern Sie den Wert vorübergehend in `0` (oder `-1`). Beim Backtracking setzen Sie den Wert wieder auf `1` zurück. Dies spart Speicherplatz, jedoch wird vom Ändern von Eingabereferenzen in der Produktion oft abgeraten.

## Praktische Anwendungen

- **Wegfindung für Staubsaugerroboter:** Berechnung aller erschöpfenden topologischen Durchläufe für einen Reinigungsroboter auf einem mit Hindernissen versetzten Grundriss.

## Verwandte Algorithmen in cOde(n)

- **[graph_01 – BFS (kürzester Weg)](../graphs/graph_01_bfs.md)** — Wenn die Aufgabe nur nach dem *kürzesten* Weg fragt, findet BFS diesen in streng $O(N^2)$-Zeit und stellt damit die exponentielle Laufzeit von Backtracking in den Schatten!
- **[backtrack_06 – Rittertour](backtrack_06_knight-s-tour.md)** — Ein weiterer Backtracking-Algorithmus für 2D-Gitter, jedoch mit stark eingeschränkten L-förmigen Sprüngen.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
