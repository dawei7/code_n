# N-Königinnen-Problem (Branch-and-Bound)

| | |
|---|---|
| **ID** | `bb_05` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(N!)$ Worst Case |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **Wikipedia** | [Acht-Königinnen-Rätsel](https://en.wikipedia.org/wiki/Eight_queens_puzzle) |

## Problemstellung

Das N-Königinnen-Rätsel ist das Problem, N Schachköniginnen so auf einem N × N-Schachbrett zu platzieren, dass sich keine zwei Königinnen gegenseitig bedrohen.
Das bedeutet, dass sich keine zwei Königinnen in derselben Zeile, Spalte oder Diagonale befinden dürfen.
Während dieses Problem klassischerweise mit Backtracking gelöst wird, lässt sich der Schritt der Überprüfung der Einschränkungen mithilfe eines arraybasierten **Branch-and-Bound**-Zustandstrackers drastisch optimieren.

**Eingabe:** Eine ganze Zahl N.
**Ausgabe:** Die Anzahl der gültigen, unterschiedlichen Lösungen (oder die Liste der Brettkonfigurationen).

## Wann man es verwenden sollte

- Wenn man aufgefordert wird, Standard-Backtracking-Code zu optimieren. Eine naive Backtracking-Lösung durchläuft das Spielfeld-Array iterativ, um zu prüfen, ob ein Schachangriff gültig ist, was $O(N)$ Zeit pro Platzierung in Anspruch nimmt. „Branch and Bound“ nutzt vorberechnete Hash-Arrays, um die Einschränkungen in strikter $O(1)$ Zeit zu validieren!

## Vorgehensweise

Beim klassischen Backtracking-Ansatz wird eine Dame in Zeile r, Spalte c platziert und anschließend die Funktion `is_safe(r, c)` aufgerufen. Diese Funktion durchsucht die gesamte Zeile, Spalte und zwei Diagonalen, was $O(N)$ Zeit in Anspruch nimmt.

**Die „Branch-and-Bound“-Optimierung ($O(1)$-Prüfungen):**
Anstatt das Spielfeld manuell zu durchsuchen, können wir vier „Bound“-Arrays führen.
1. `cols_taken[N]`: Wahr, wenn sich irgendwo in dieser Spalte eine Dame befindet.
2. `rows_taken[N]`: Wahr, wenn sich irgendwo in dieser Zeile eine Königin befindet.
3. `diag1_taken[2N-1]`: Die primären Diagonalen (oben links nach unten rechts). Beachten Sie eine mathematische Invariante: Für jedes Feld (r, c) auf genau derselben primären Diagonale ist der Wert **r – c immer konstant**! (Wir versetzen ihn um +N-1, damit die Array-Indizes nicht negativ sind).
4. `diag2_taken[2N-1]`: Die sekundären Diagonalen (oben rechts nach unten links). Für jede Zelle auf derselben sekundären Diagonale ist der Wert **r + c immer konstant**!

Durch die Berücksichtigung dieser Invarianzen wird `is_safe(r, c)` zu einer einfachen $O(1)$-Prüfung:
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

## Schritt-für-Schritt-Anleitung

`N = 4`.
Start `row = 0`.
- Versuche `col = 0`.
  - `d1_id = 0 - 0 + 3 = 3`. `d2_id = 0 + 0 = 0`.
  - Frei? Ja. Königin auf `(0,0)` setzen.
  - Zustand: `cols[0]=T`, `diag1[3]=T`, `diag2[0]=T`.

Rekursiv `row = 1`.
- Versuche `col = 0`: `cols[0]` ist wahr. Blockiert!
- Versuche `col = 1`: `d1_id = 1 - 1 + 3 = 3`. `diag1[3]` ist wahr! (Bedroht durch 0,0 auf der Hauptdiagonale). Blockiert!
- Versuche `col = 2`: `d1_id = 1 - 2 + 3 = 2`, `d2_id = 1 + 2 = 3`. Alles frei!
  - Dame auf `(1,2)` setzen.
  - Zustand: `cols[2]=T`, `diag1[2]=T`, `diag2[3]=T`.

Rekursiv `row = 2`... (Wenn alle Spalten blockiert sind, kehrt die Funktion zurück, räumt den Aufrufstapel ab, löst die Aufhebung der Markierungen in `False` aus und versucht es mit der nächsten Spalte auf der vorherigen Ebene. Das ist das Wesen des Backtracking mit Begrenzungen!)

## Komplexität

| | Zeit | Speicher |
|---|---|---|
| **Bestfall** | $O(N!)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N!)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N!)$ | $O(N)$ |

Die Zeitkomplexität bleibt $O(N!)$ im absolut schlimmsten Fall der Baumdurchsuchung, da wir N Spalten durchlaufen, dann N-1 usw. Ersetzt man jedoch die $O(N)$-Schleife innerhalb von `is_safe` durch einen $O(1)$-Array-Lookup, reduziert sich die Gesamtanzahl der Operationen um den Faktor N, was die Ausführungszeit erheblich verkürzt.
Die Platzkomplexität beträgt $O(N)$ für den Rekursionsaufrufstapel und die Einschränkungs-Arrays.

## Varianten & Optimierungen

- **Bitmaskierung:** Anstelle von booleschen Arrays kannst du reine bitweise Ganzzahlen verwenden, um die belegten Spalten und Diagonalen zu verfolgen! Durch Verschieben der Ganzzahl `(diag1 >> 1)` wird der Zustand sofort an die nächste Zeile weitergegeben. Dies ist die legendärste und am stärksten optimierte Methode zur Lösung des N-Königinnen-Problems, die vollständig in CPU-Registern abläuft.

## Praktische Anwendungen

- **Constraint Satisfaction Problems (CSP):** Die mathematischen Grundlagen der Zuweisung physikalischer Frequenzen an Mobilfunkmasten, damit sich überlappende Frequenzbereiche nicht gegenseitig stören, sind direkt analog zum Problem der nicht bedrohlichen Königinnen.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_01 – N-Königinnen](../backtracking/backtrack_01_n-queens.md)** — Die klassische Backtracking-Version ohne die mathematischen $O(1)$ Begrenzungs-Arrays.

---

*Diese Dokumentation ist ein für cOde(n) verfasster Originalinhalt,
der sich an der kanonischen Struktur orientiert, wie sie von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie unter dem Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
