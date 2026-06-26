# Maximal Square

| | |
|---|---|
| **ID** | `dp_25` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(M * N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Maximal Square](https://leetcode.com/problems/maximal-square/) |

## Problemstellung

Gegeben ist eine `m x n` Binärmatrix, die mit `0` und `1` gefüllt ist. Finde das größte Quadrat, das nur `1` enthält, und gib dessen Fläche zurück.

**Eingabe:** Eine `m x n` Matrix `matrix`, deren Elemente die Zeichen `'0'` oder `'1'` sind.
**Ausgabe:** Eine Ganzzahl, die die Fläche des größten Quadrats repräsentiert.

## Wann man es verwendet

- Ein klassisches 2D-Grid-DP-Problem, das lehrt, wie man nach OBEN, LINKS und DIAGONAL-OBEN-LINKS schaut, um den Zustand der aktuellen Zelle zu bestimmen.
- Der perfekte Ausgangspunkt, bevor man das deutlich schwierigere `Maximal Rectangle`-Problem angeht.

## Ansatz

**1. Den Zustand definieren:**
Sei `dp[i][j]` die **Seitenlänge** des maximalen Quadrats, dessen *untere rechte Ecke* sich genau an der Zelle `(i, j)` befindet.

**2. Die Basisfälle finden:**
Wenn wir uns in der ersten Zeile (`i = 0`) oder der ersten Spalte (`j = 0`) befinden, ist das maximale Quadrat, das dort enden kann, auf die Zelle selbst begrenzt!
Wenn `matrix[i][j] == '1'`, dann ist `dp[i][j] = 1`.
Wenn `matrix[i][j] == '0'`, dann ist `dp[i][j] = 0`.

**3. Den Übergang finden (Die Rekursionsgleichung):**
Was bestimmt für eine interne Zelle `(i, j)`, ob sie ein größeres Quadrat bilden kann?
Zuerst MUSS `matrix[i][j]` gleich `'1'` sein. Wenn es `'0'` ist, wird das Quadrat sofort unterbrochen und `dp[i][j] = 0`.
Wenn es `'1'` IST, kann es genau dann als untere rechte Ecke eines größeren Quadrats fungieren, wenn die drei benachbarten Zellen (Links, Oben, Diagonal-Oben-Links) ebenfalls Quadrate einer bestimmten Mindestgröße bilden!
Die Größe des Quadrats, das bei `(i, j)` endet, wird durch das **Minimum** dieser drei umliegenden Quadrate begrenzt.
`dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`

Wir verfolgen den globalen `max_side`-Wert über die gesamte DP-Matrix hinweg. Die endgültige Fläche ist `max_side * max_side`.

**4. Platzkomplexität optimieren:**
Beachte, dass `dp[i][j]` nur von der aktuellen Zeile `i` und der vorherigen Zeile `i-1` abhängt. Wir können dies von $O(M \times N)$ Platz auf ein 1D-Array der Größe N optimieren!
Wir benötigen lediglich eine temporäre Variable, um `dp[i-1][j-1]` zu speichern, bevor es überschrieben wird.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_25: Maximal Square.

dp[i][j] = side length of the largest square whose bottom-
right corner is at (i, j). Recurrence:
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
if matrix[i][j] == '1', else 0. Space-optimized to O(N).
"""


def solve(matrix, m, n):
    if m == 0 or n == 0:
        return 0
    dp = [0] * (n + 1)
    max_side = 0
    prev = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            temp = dp[j]
            if matrix[i - 1][j - 1] == "1":
                dp[j] = min(dp[j], dp[j - 1], prev) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0
            prev = temp
        prev = 0
    return max_side * max_side
```

</details>

## Durchlauf

`matrix = [["1","0","1","0"], ["1","1","1","1"], ["1","1","1","1"]]`
M=3, N=4. `dp` initialisiert mit `[0, 0, 0, 0, 0]`.

1. **i = 1 (Zeile 0: `1 0 1 0`):**
   - `j=1 ('1')`: `dp[1] = min(0, 0, 0) + 1 = 1`. `max=1`.
   - `j=2 ('0')`: `dp[2] = 0`.
   - `j=3 ('1')`: `dp[3] = min(0, 0, 0) + 1 = 1`.
   - `j=4 ('0')`: `dp[4] = 0`.
   - `dp`-Zustand: `[0, 1, 0, 1, 0]`.

2. **i = 2 (Zeile 1: `1 1 1 1`):**
   - `j=1 ('1')`: `dp[1] = min(1(oben), 0(links), 0(diag)) + 1 = 1`.
   - `j=2 ('1')`: `dp[2] = min(0(oben), 1(links), 1(diag)) + 1 = 1`.
   - `j=3 ('1')`: `dp[3] = min(1(oben), 1(links), 0(diag)) + 1 = 1`.
   - `j=4 ('1')`: `dp[4] = min(0(oben), 1(links), 1(diag)) + 1 = 1`.
   - `dp`-Zustand: `[0, 1, 1, 1, 1]`.

3. **i = 3 (Zeile 2: `1 1 1 1`):**
   - `j=1 ('1')`: `dp[1] = 1`.
   - `j=2 ('1')`: `dp[2] = min(1, 1, 1) + 1 = 2`. `max=2`.
   - `j=3 ('1')`: `dp[3] = min(1, 2, 1) + 1 = 2`.
   - `j=4 ('1')`: `dp[4] = min(1, 2, 1) + 1 = 2`.
   - `dp`-Zustand: `[0, 1, 2, 2, 2]`.

Das endgültige `max_side` ist 2. Die Fläche ist 2 x 2 = 4. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M * N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(M * N)$ | $O(N)$ |

Die verschachtelten Schleifen besuchen jede Zelle in der M x N Matrix exakt einmal und führen $O(1)$ Operationen aus. Die Zeitkomplexität ist strikt $O(M \times N)$.
Durch die Verwendung des 1D-Rolling-Arrays beträgt die Platzkomplexität $O(N)$ (wobei N die Anzahl der Spalten ist).

## Varianten & Optimierungen

- **Count Square Submatrices with All Ones:** Anstatt die MAXIMALE Fläche zurückzugeben, gib die Gesamtzahl der gültigen Quadrate zurück! Die Logik ist absolut identisch. Der Wert `dp[i][j]` repräsentiert exakt, wie viele gültige Quadrate ihre untere rechte Ecke bei `(i, j)` haben. Man summiert einfach alle `dp[i][j]`-Werte über die gesamte Matrix auf!
- **Maximal Rectangle:** Was, wenn die Form kein perfektes Quadrat sein muss? Die `min()`-Logik funktioniert hier nicht mehr. Dies erfordert einen völlig anderen Ansatz unter Verwendung von Monotonic Stacks! (`dp_26`).

## Anwendungen in der Praxis

- **Computer Vision:** Schnelle Identifizierung von Bounding Boxes für dichte, einfarbige Regionen (wie eine solide weiße Wand oder ein Textblock) in einer Bildverarbeitungspipeline.

## Verwandte Algorithmen in cOde(n)

- **[dp_12 - Minimum Path Sum](dp_12_min-cost-path.md)** — Ein weiteres 2D-Grid-DP-Problem, bei dem man ein 1D-Zeilen-Array optimiert, aber hier muss man zusätzlich den diagonalen Zustand verfolgen!
- **[dp_26 - Maximal Rectangle](dp_26_maximal-rectangle.md)** — Die deutlich schwierigere Variante, bei der Breite und Höhe unterschiedlich sein können.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*