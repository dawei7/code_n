# N-Queen (Branch and Bound)

| | |
|---|---|
| **ID** | `bb_05` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(N!)$ Schlechtester Fall |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **Wikipedia** | [Damenproblem](https://de.wikipedia.org/wiki/Damenproblem) |

## Problemstellung

Das N-Damen-Problem besteht darin, N Schachdamen auf einem N x N Schachbrett so zu platzieren, dass sich keine zwei Damen gegenseitig bedrohen.
Das bedeutet, dass keine zwei Damen in derselben Zeile, Spalte oder Diagonale stehen dürfen.
Während dies klassischerweise mittels Backtracking gelöst wird, kann der Schritt zur Überprüfung der Nebenbedingungen durch einen array-basierten **Branch and Bound**-Zustandsverfolger drastisch optimiert werden.

**Eingabe:** Eine Ganzzahl N.
**Ausgabe:** Die Anzahl der gültigen, unterschiedlichen Lösungen (oder die Liste der Brettkonfigurationen).

## Wann man es einsetzt

- Wenn man aufgefordert wird, Standard-Backtracking-Code zu optimieren. Eine naive Backtracking-Lösung iteriert durch das Brett-Array, um zu prüfen, ob ein Angriff einer Dame gültig ist, was $O(N)$ Zeit pro Platzierung in Anspruch nimmt. Branch and Bound verwendet vorberechnete Hash-Arrays, um Nebenbedingungen in strikter $O(1)$-Zeit zu validieren!

## Ansatz

Der klassische Backtracking-Ansatz platziert eine Dame in Zeile r, Spalte c und ruft dann eine Funktion `is_safe(r, c)` auf. Diese Funktion durchsucht die gesamte Zeile, Spalte und die beiden Diagonalen, was $O(N)$ Zeit benötigt.

**Die Branch and Bound-Optimierung ($O(1)$-Prüfungen):**
Anstatt das Brett manuell zu scannen, können wir vier "Bound"-Arrays führen.
1. `cols_taken[N]`: True, wenn sich irgendwo in dieser Spalte eine Dame befindet.
2. `rows_taken[N]`: True, wenn sich irgendwo in dieser Zeile eine Dame befindet.
3. `diag1_taken[2N-1]`: Die Hauptdiagonalen (von oben links nach unten rechts). Beachten Sie eine mathematische Invariante: Für jede Zelle (r, c) auf derselben Hauptdiagonale ist der Wert **r - c immer konstant**! (Wir verschieben ihn um +N-1, damit die Array-Indizes nicht negativ werden).
4. `diag2_taken[2N-1]`: Die Nebendiagonalen (von oben rechts nach unten links). Für jede Zelle auf derselben Nebendiagonale ist der Wert **r + c immer konstant**!

Durch das Verfolgen dieser Invarianten wird `is_safe(r, c)` zu einer einfachen $O(1)$-Prüfung:
`if not cols_taken[c] and not diag1_taken[r - c + N - 1] and not diag2_taken[r + c]: place_queen()`

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bb_05: N-Queen (Branch and Bound).

Place N queens on an N x N board so that no two
"""


def solve(n):
    """N-queen via branch and bound (column-by-column with
    O(1) row/diagonal lookups)."""
    if n <= 0:
        return []
    row_used = [False] * n
    # / diagonal: r + c. backslash diagonal: c - r + (n - 1).
    slash = [False] * (2 * n - 1)
    backslash = [False] * (2 * n - 1)
    placement = []                        # list of (row, col)
    found = []

    def dfs(col):
        if col == n:
            found.extend(placement)
            return True
        for r in range(n):
            si = r + col
            bi = col - r + (n - 1)
            if row_used[r] or slash[si] or backslash[bi]:
                continue
            row_used[r] = True
            slash[si] = True
            backslash[bi] = True
            placement.append((r, col))
            if dfs(col + 1):
                return True
            placement.pop()
            row_used[r] = False
            slash[si] = False
            backslash[bi] = False
        return False

    dfs(0)
    return sorted(found)
```

</details>

## Ablaufbeispiel

`N = 4`.
Start `row = 0`.
- Versuche `col = 0`.
  - `d1_id = 0 - 0 + 3 = 3`. `d2_id = 0 + 0 = 0`.
  - Frei? Ja. Platziere Dame bei `(0,0)`.
  - Zustand: `cols[0]=T`, `diag1[3]=T`, `diag2[0]=T`.

Rekursion `row = 1`.
- Versuche `col = 0`: `cols[0]` ist True. Blockiert!
- Versuche `col = 1`: `d1_id = 1 - 1 + 3 = 3`. `diag1[3]` ist True! (Bedroht durch 0,0 auf der Hauptdiagonale). Blockiert!
- Versuche `col = 2`: `d1_id = 1 - 2 + 3 = 2`, `d2_id = 1 + 2 = 3`. Alles frei!
  - Platziere Dame bei `(1,2)`.
  - Zustand: `cols[2]=T`, `diag1[2]=T`, `diag2[3]=T`.

Rekursion `row = 2`... (Wenn alle Spalten blockiert sind, kehrt die Funktion zurück, baut den Call-Stack ab, löst das Zurücksetzen der `False`-Markierungen aus und versucht die nächste Spalte auf der vorherigen Ebene. Dies ist das Wesen des Backtrackings mit Schranken!)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N!)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N!)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N!)$ | $O(N)$ |

Die Zeitkomplexität bleibt im absolut schlechtesten Fall der Baumsuche $O(N!)$, da wir N Spalten, dann N-1 usw. iterieren. Das Ersetzen der $O(N)$-Schleife innerhalb von `is_safe` durch einen $O(1)$-Array-Zugriff reduziert jedoch die Gesamtzahl der Operationen um einen Faktor N, was die tatsächliche Ausführungszeit massiv beschleunigt.
Die Platzkomplexität beträgt $O(N)$ für den Rekursions-Stack und die Constraint-Arrays.

## Varianten & Optimierungen

- **Bitmasking:** Anstatt boolesche Arrays zu verwenden, können Sie rohe bitweise Ganzzahlen verwenden, um die belegten Spalten und Diagonalen zu verfolgen! Das Verschieben der Ganzzahl `(diag1 >> 1)` überträgt den Zustand sofort auf die nächste Zeile. Dies ist die legendärste und am stärksten optimierte Art, das N-Damen-Problem zu lösen, da sie vollständig in CPU-Registern abläuft.

## Anwendungen in der Praxis

- **Constraint Satisfaction Problems (CSP):** Die Mathematik der Zuweisung physischer Frequenzen an Mobilfunkmasten, sodass sich überlappende Bereiche nicht stören, ist direkt analog zu nicht-bedrohenden Damen.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_01 - N-Queens](../backtracking/backtrack_01_n-queens.md)** — Die klassische Backtracking-Version ohne die mathematischen $O(1)$-Schranken-Arrays.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*