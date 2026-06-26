# Min Cost Path

| | |
|---|---|
| **ID** | `dp_12` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Shortest path problem](https://en.wikipedia.org/wiki/Shortest_path_problem) |

## Problemstellung

Gegeben ist ein `m × n` Grid aus **nicht-negativen** Ganzzahlen (die "Kosten" jeder Zelle). Finde einen Pfad von oben links nach unten rechts, der die **Gesamtkosten minimiert**. Man darf sich nur **nach rechts oder nach unten** bewegen.

**Eingabe:** Ein 2D-Grid aus nicht-negativen Ganzzahlen.
**Ausgabe:** Die minimalen Gesamtkosten eines Pfades von `grid[0][0]` nach `grid[m-1][n-1]`.

**Beispiel:**

```
  1  3  1
  1  5  1
  4  2  1

Min-cost path: 1 → 1 → 1 → 1 → 1 = 5
  (right, down, right, down, right;
   cells: (0,0)→(0,1)→(0,2)→(1,2)→(2,2) = 1+3+1+1+1 = 7
   actually that's 7; the minimum is:
   (0,0)→(1,0)→(2,0)→(2,1)→(2,2) = 1+1+4+2+1 = 9 (worse))
   
   Let me retrace: 1+1+1+1+1 = 5 with cells (0,0),(1,0),(1,1),(1,2),(2,2)? No, (1,0)→(1,1) is "right" not "down". Movement is right or down.
   (0,0)→(0,1)→(0,2)→(1,2)→(2,2) = 1+3+1+1+1 = 7
   (0,0)→(0,1)→(1,1)→(2,1)→(2,2) = 1+3+5+2+1 = 12
   (0,0)→(0,1)→(1,1)→(1,2)→(2,2) = 1+3+5+1+1 = 11
   (0,0)→(1,0)→(1,1)→(1,2)→(2,2) = 1+1+5+1+1 = 9
   (0,0)→(1,0)→(2,0)→(2,1)→(2,2) = 1+1+4+2+1 = 9
   (0,0)→(0,1)→(1,1)→(2,1)→(2,2) = 1+3+5+2+1 = 12
   (0,0)→(0,1)→(0,2)→(1,2)→(2,2) = 1+3+1+1+1 = 7
   Hmm 7 seems best. Let me try:
   (0,0)→(1,0)→(1,1)→(1,2)→(2,2) = 1+1+5+1+1 = 9
   (0,0)→(0,1)→(1,1)→(1,2)→(2,2) = 1+3+5+1+1 = 11
   So the answer is 7.
```

| Grid | Min cost |
|---|---:|
| `[[1, 3, 1], [1, 5, 1], [4, 2, 1]]` | 7 |
| `[[1, 2, 3], [4, 5, 6]]` | 12 (1+2+3+6) |
| `[[1]]` | 1 |

## Anwendung

- Das klassische DP-Problem zum "**Zählen von Pfaden mit Kosten**". Wird häufig in Telefoninterviews abgefragt, oft mit kleinen Variationen (Hindernisse, mit Diagonalen, mit Bewegungen nach oben/unten/links/rechts).
- Grundlage für die **Roboter-Bewegungsplanung** auf gewichteten Grids, **Routen mit geringstem Aufwand** in der Geländeanalyse und viele Varianten des **kostengünstigsten Pfades**.

## Ansatz

Sei `dp[i][j]` = die minimalen Kosten, um die Zelle `(i, j)` von `(0, 0)` aus zu erreichen.

**Rekurrenz:** Um `(i, j)` zu erreichen, müssen wir entweder von `(i-1, j)` (unten) oder von `(i, j-1)` (rechts) gekommen sein. Wir wählen das Minimum der beiden und addieren die Kosten der aktuellen Zelle:
```
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
```

**Induktionsanfang:** `dp[0][0] = grid[0][0]`.
`dp[0][j] = grid[0][j] + dp[0][j-1]` (nur Bewegungen nach rechts).
`dp[i][0] = grid[i][0] + dp[i-1][0]` (nur Bewegungen nach unten).

**Antwort:** `dp[m-1][n-1]`.

**Platzoptimierung:** `dp[i][j]` hängt nur von der Zelle darüber und der Zelle links davon ab, daher kann die 2D-Tabelle auf ein 1D-Array der Größe `n` reduziert werden. Wir iterieren von links nach rechts; die Zelle "darüber" ist `dp[j]` (aktuell), während die Zelle "links" `dp[j-1]` (gerade aktualisiert) ist:
```
dp[j] = grid[i][j] + min(dp[j], dp[j-1])
```

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_12: Min Cost Path.

Minimum-cost path from (0,0) to (m-1, n-1), right/down only.
"""


def solve(grid, m, n):
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]
```

</details>

## Durchlauf

Grid: `[[1, 3, 1], [1, 5, 1], [4, 2, 1]]`.

Nach Zeile 0: `dp = [1, 4, 5]`.

**i = 1:**
- `dp[0] += grid[1][0]` → `dp[0] = 1 + 1 = 2`.
- `dp[1] = 5 + min(4, 2) = 7`.
- `dp[2] = 1 + min(5, 7) = 6`.

Nach Zeile 1: `dp = [2, 7, 6]`.

**i = 2:**
- `dp[0] += grid[2][0]` → `dp[0] = 2 + 4 = 6`.
- `dp[1] = 2 + min(7, 6) = 8`.
- `dp[2] = 1 + min(6, 8) = 7`.

Nach Zeile 2: `dp = [6, 8, 7]`.

Antwort: `dp[2] = 7`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(m·n)$ | $O(n)$ mit Rolling Array |
| **Durchschnittlicher Fall** | $O(m·n)$ | $O(n)$ |
| **Schlechtester Fall** | $O(m·n)$ | $O(n)$ |

Die erforderliche Komplexität ist $O(n²)$ für die cOde(n)-Engine, wobei `n = max(m, n)`.

## Varianten & Optimierungen

- **Mit Hindernissen** — blockierte Zellen als unendlich behandeln.
- **Mit Diagonalen** — `(i-1, j-1)` zu den Kandidaten hinzufügen.
- **Pfad mit maximalen Kosten** — `min` durch `max` ersetzen.
- **Mit Bewegungen nach oben/unten/links/rechts** — in Dijkstra auf dem Grid-Graphen umwandeln (da alle Kosten nicht-negativ sind).
- **Pfad rekonstruieren** — ein `parent[i][j]` (oder `parent[j]` in der Rolling-Version) speichern und zurückverfolgen.
- **Min-Cost-Pfad mit K Kurven** — die Anzahl der Richtungswechsel ist begrenzt. Eine Zustandsdimension hinzufügen.

## Anwendungen in der Praxis

- **Roboter-Bewegungsplanung** — den günstigsten Pfad durch ein gewichtetes Gelände finden.
- **Routen mit geringstem Energieverbrauch** in einem Straßennetz (wobei die Gewichte Treibstoff oder Zeit sind).
- **Game AI** — Pfadfindung auf einem Kostengrid.
- **Bildverarbeitung** — Seam Carving (den Pfad mit den geringsten Kosten von oben nach unten finden).
- **Logistik** — günstigste Lieferroute.
- **Bioinformatik** — Sequenzalignment mit nicht-negativen Scores (die gewichtete Editierdistanz für Proteine).

## Verwandte Algorithmen in cOde(n)

- **[dp_10 — Unique Paths](dp_10_unique-paths.md)** — *zählt* alle Pfade; dieses Problem findet den *günstigsten*. (d=4/10, r=9/10)
- **[dp_23 — Min Cost Climbing Stairs](dp_23_min-cost-climbing-stairs.md)** — 1D-Version. (d=3/10, r=9/10)
- **[graph_04 — Dijkstra](graph_04_dijkstra.md)** — Min-Cost-Pfad auf einem allgemeinen Graphen mit gewichteten Kanten. (d=5/10, r=8/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*