# Weg mit minimalen Kosten

| | |
|---|---|
| **ID** | `dp_12` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Kürzester-Weg-Problem](https://en.wikipedia.org/wiki/Shortest_path_problem) |

## Aufgabenstellung

Gegeben ist ein `m × n`-Gitter aus **nicht-negativen** ganzen Zahlen (die
„Kosten“ jeder Zelle). Finde einen Weg von links oben nach
rechts unten, der **die Gesamtkosten minimiert**. Man darf sich nur
**nach rechts oder nach unten** bewegen.

**Eingabe:** ein zweidimensionales Gitter aus nicht-negativen ganzen Zahlen.
**Ausgabe:** die minimalen Gesamtkosten eines Weges von
`grid[0][0]` nach `grid[m-1][n-1]`.

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

| Gitter | Min. Kosten |
|---|---:|
| `[[1, 3, 1], [1, 5, 1], [4, 2, 1]]` | 7 |
| `[[1, 2, 3], [4, 5, 6]]` | 12 (1+2+3+6) |
| `[[1]]` | 1 |

## Wann man es einsetzt

- Die klassische DP „**Anzahl der Pfade mit bestimmten Kosten**“. Wird in
  Telefon-Vorstellungsgesprächen abgefragt, oft mit einer kleinen Besonderheit (Hindernisse, mit
  Diagonalen, mit Auf/Ab/Links/Rechts).
- Grundlage für die **Bewegungsplanung von Robotern** auf gewichteten
  Gittern, für **Routen mit minimalem Aufwand** in der Geländebewertung und
  viele Varianten der **kostengünstigsten Pfade**.

## Vorgehensweise

Sei `dp[i][j]` = die minimalen Kosten, um die Zelle `(i, j)`
von `(0, 0)` aus zu erreichen.

**Rekursion:** Um `(i, j)` zu erreichen, müssen wir entweder von
`(i-1, j)` (nach unten) oder von `(i, j-1)` (nach rechts) gekommen sein. Man nehme den
günstigeren dieser beiden Wege und addiere die Kosten der aktuellen Zelle hinzu:
```
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
```

**Basisfall:** `dp[0][0] = grid[0][0]`.
`dp[0][j] = grid[0][j] + dp[0][j-1]` (nur Bewegungen nach rechts).
`dp[i][0] = grid[i][0] + dp[i-1][0]` (nur Züge nach unten).

**Antwort:** `dp[m-1][n-1]`.

**Speicheroptimierung:** `dp[i][j]` hängt nur von der Zelle
oberhalb und der Zelle links davon ab, sodass sich die 2D-Tabelle
auf ein 1D-Array der Größe `n` reduzieren lässt. Iteriere von links nach rechts, und
die „obere“ Zelle ist `dp[j]` (aktuell), während die „linke“ Zelle
`dp[j-1]` (gerade aktualisiert) ist:
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

## Schritt-für-Schritt-Anleitung

Raster: `[[1, 3, 1], [1, 5, 1], [4, 2, 1]]`.

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
| **Bestfall** | $O(m·n)$ | $O(n)$ mit rollendem |
| **Durchschnittlicher Fall** | $O(m·n)$ | $O(n)$ |
| **Schlechteste** | $O(m·n)$ | $O(n)$ |

Die erforderliche Komplexität beträgt $O(n²)$ für die cOde(n)-Engine,
wobei `n = max(m, n)`.

## Varianten & Optimierungen

- **Mit Hindernissen** — behandle blockierte Zellen als Unendlichkeit.
- **Mit Diagonalen** — füge `(i-1, j-1)` zu den Kandidaten hinzu.
- **Pfad mit maximalen Kosten** — `min` durch `max` ersetzen.
- **Mit Auf/Ab/Links/Rechts** — wandle es in Dijkstra um
  auf dem Gittergraphen um (da alle Kosten nicht-negativ sind).
- **Den Pfad rekonstruieren** — speichere ein `parent[i][j]` (oder
  `parent[j]` in der „Rolling“-Version) und gehe den Weg zurück.
- **Pfad mit minimalen Kosten und K Richtungswechseln** — die Anzahl der
  Richtungswechsel ist begrenzt. Füge eine Zustandsdimension hinzu.

## Anwendungen in der Praxis

- **Bewegungsplanung für Roboter** — finde den kostengünstigsten Pfad
  durch ein gewichtetes Gelände.
- **Route mit dem geringsten Energieaufwand** in einem Straßennetz (wobei die Gewichte
  Kraftstoff oder Zeit sind).
- **Spiel-KI** – Wegfindung auf einem Kostenraster.
- **Bildverarbeitung** – Seam Carving (Finde den kostengünstigsten
  Pfad von oben nach unten).
- **Logistik** – kostengünstigste Lieferroute.
- **Bioinformatik** – Sequenzabgleich mit nicht-negativen
  Werten (der gewichtete Editierabstand für Proteine).

## Verwandte Algorithmen in cOde(n)

- **[dp_10 — Eindeutige Pfade](dp_10_unique-paths.md)** —
  *zählt* alle Pfade; dieser Algorithmus findet den *kostengünstigsten*. (d=4/10, r=9/10)
- **[dp_23 — Treppensteigen mit minimalen Kosten](dp_23_min-cost-climbing-stairs.md)** —
  1D-Version. (d=3/10, r=9/10)
- **[graph_04 — Dijkstra](graph_04_dijkstra.md)** — Weg mit minimalen Kosten
  in einem allgemeinen Graphen mit gewichteten Kanten. (d=5/10, r=8/10)

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag
finden Sie über den Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
