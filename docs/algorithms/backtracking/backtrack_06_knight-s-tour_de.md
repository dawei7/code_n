# Knight's Tour

| | |
|---|---|
| **ID** | `backtrack_06` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(8^(N^2)$) Zeit, $O(N^2)$ Platz |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Knight's tour](https://en.wikipedia.org/wiki/Knight%27s_tour) |

## Problemstellung

Gegeben ist ein leeres `N x N` Schachbrett. Ein Springer startet auf dem ersten Feld `(0, 0)` und muss exakt `N^2 - 1` legale "L-förmige" Züge ausführen, um jedes einzelne Feld auf dem Brett genau einmal zu besuchen.
Finden und geben Sie die Matrix zurück, die die exakte Sequenz der Züge des Springers darstellt. Das Startfeld sollte mit `0` markiert werden, das nächste Feld mit `1` und so weiter. Falls keine solche Tour existiert, geben Sie eine leere Matrix zurück.

**Eingabe:** Eine Ganzzahl `N`.
**Ausgabe:** Eine `N x N` Matrix, gefüllt mit Ganzzahlen von `0` bis `N^2 - 1`, die die Schrittnummern repräsentieren.

## Wann man es verwendet

- Um die reine Erschöpfung eines 2D-Constraint-Satisfaction-Problems zu demonstrieren.
- Ein klassisches theoretisches Informatikproblem, das zeigt, wie Heuristiken (Warnsdorff-Regel) ein Brute-Force-Backtracking massiv optimieren können.

## Ansatz

**1. Der Entscheidungsbaum:**
Auf jedem Feld `(r, c)` hat der Springer exakt 8 mögliche L-förmige Sprünge.
Wenn ein Sprung außerhalb der Grenzen liegt oder auf einem Feld landet, das bereits eine Schrittnummer \ge 0 hat, ist er ungültig und wird verworfen (Pruning).

**2. Der Backtracking-Zustand:**
`backtrack(r, c, move_number)`:
- `r`, `c`: Die aktuellen Koordinaten des Springers.
- `move_number`: Eine Ganzzahl von `1` bis `N^2 - 1`, die die aktuelle Tiefe der Tour verfolgt.

**3. Zustandsverwaltung (Das Schachbrett):**
Wir verwenden eine `N x N` Matrix `board`, die vollständig mit `-1` initialisiert ist.
- **Wahl treffen:** `board[r][c] = move_number`.
- **Rekursion:** Iterieren Sie durch alle 8 gültigen Sprünge und rufen Sie `backtrack(next_r, next_c, move_number + 1)` auf. Wenn IRGENDEINER dieser rekursiven Aufrufe `True` zurückgibt, bedeutet dies, dass das Brett erfolgreich vervollständigt wurde! Wir geben sofort `True` zurück, um den Erfolg nach oben weiterzureichen.
- **Backtrack:** `board[r][c] = -1`. Der Springer verlässt das Feld wieder, damit ein anderer Pfad es später versuchen kann.

**4. Basisfall:**
Wenn `move_number == N * N`, bedeutet dies, dass wir den Springer erfolgreich N^2 Mal platziert haben! Die Tour ist vollständig. Geben Sie `True` zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for backtrack_06: Knight's Tour.

For a board of size n, find any sequence of knight moves that
visits every cell exactly once. Backtracking with Warnsdorff's
heuristic: at each step, prefer the move with the fewest
onward neighbours.
"""


def solve(n):
    if n <= 1:
        return [(0, 0)] if n == 1 else []
    if n < 5:
        return []
    visited = [[False] * n for _ in range(n)]
    path = []
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def degree(r, c):
        count = 0
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                count += 1
        return count

    def helper(r, c, step):
        visited[r][c] = True
        path.append((r, c))
        if step == n * n:
            return True
        candidates = []
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                candidates.append((degree(nr, nc), nr, nc))
        candidates.sort()
        for _, nr, nc in candidates:
            if helper(nr, nc, step + 1):
                return True
        visited[r][c] = False
        path.pop()
        return False

    if helper(0, 0, 1):
        return path
    return []
```

</details>

## Durchlauf

*(Die Knight's Tour auf N < 5 ist mathematisch unmöglich! Wir gehen konzeptionell eine Sackgasse bei N=3 durch).*

`N = 3`. Start bei `(0, 0)`. `board[0][0] = 0`.
`backtrack(0, 0, 1)`:
- Versuche Sprünge:
  - `i=0 (+2, +1)`: `nr=2, nc=1`. Gültig!
    - `board[2][1] = 1`.
    - `backtrack(2, 1, 2)`:
      - Versuche Sprünge von `(2, 1)`:
        - `(-2, -1)` landet auf `(0, 0)` -> Besucht!
        - `(-2, +1)` landet auf `(0, 2)`. Gültig!
          - `board[0][2] = 2`.
          - `backtrack(0, 2, 3)`:
            - Versuche Sprünge von `(0, 2)`:
              - `(+2, -1)` landet auf `(2, 1)` -> Besucht!
              - Alle anderen 7 Sprünge liegen außerhalb der Grenzen. Schleife endet.
          - Backtrack: `board[0][2] = -1`. Gebe False zurück.
      - Alle Sprünge von `(2, 1)` erschöpft.
    - Backtrack: `board[2][1] = -1`. Gebe False zurück.
- Alle Sprünge von `(0, 0)` erschöpft.
Gebe False zurück.

Ergebnis: `[]` (Keine Tour existiert für ein 3x3 Brett).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(8^(N^2)$) | $O(N^2)$ |
| **Schlechtester Fall** | $O(8^(N^2)$) | $O(N^2)$ |

Auf jedem Feld hat der Springer bis zu 8 Möglichkeiten. Die Tour erfordert N^2 Schritte.
Die obere Schranke der Zeitkomplexität für Brute-Force ist ein astronomisches $O(8^{N^2})$. Für ein 8 x 8 Brett ist 8^{64} rechnerisch unmöglich durch reines Brute-Force zu lösen, ohne extremes Glück bei der Reihenfolge der Verzweigungen.
Die Platzkomplexität beträgt $O(N^2)$ für das Brett und die Tiefe des Rekursions-Stacks.

## Varianten & Optimierungen

- **Warnsdorff-Heuristik:** Dies ist der Zaubertrick, der die Knight's Tour in Echtzeit lösbar macht! Anstatt blind durch die 8 Sprünge in einer statischen Reihenfolge zu iterieren, sollten Sie die **8 Sprünge sortieren**, basierend darauf, *wie viele weiterführende Sprünge von dort aus verfügbar sind*. Sie müssen gierig auf das Feld springen, das die WENIGSTEN weiteren Optionen bietet! Dadurch wird der Springer gezwungen, zuerst die Ränder und Ecken zu besuchen, was verhindert, dass er in eine Sackgasse gerät. Dies senkt die praktische Zeitkomplexität auf nahezu $O(N^2)$!

## Anwendungen in der Praxis

- **Kryptographie:** Wird beim Entwurf von Verschlüsselungsalgorithmen und Pseudozufallszahlengeneratoren verwendet, bei denen eine maximale räumliche Diffusion über ein Speichergitter ohne Wiederholung von Zuständen erforderlich ist.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_05 - Rat in a Maze](backtrack_05_rat-in-a-maze.md)** — Das grundlegende 2D-Tracking-Problem mit nur 4 Richtungen und statischen Wänden.
- **[backtrack_02 - Permutations](backtrack_02_permutations.md)** — Das Generieren einer Knight's Tour ist mathematisch äquivalent zur Erzeugung einer spezifischen Permutation der N^2 Felder, eingeschränkt durch L-Sprünge.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Competitive Programming verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*