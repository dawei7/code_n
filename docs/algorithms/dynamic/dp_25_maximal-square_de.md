# Maximales Quadrat

| | |
|---|---|
| **ID** | `dp_25` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(M * N)$ Zeit, $O(N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Maximal Square](https://leetcode.com/problems/maximal-square/) |

## Aufgabenstellung

Gegeben sei eine `m x n` binäre Matrix, die mit `0` und `1` gefüllt ist. Finde das größte Quadrat, das ausschließlich aus `1` besteht, und gib dessen Fläche zurück.

**Eingabe:** Eine `m x n`-Matrix `matrix`, deren Elemente die Zeichen `'0'` oder `'1'` sind.
**Ausgabe:** Eine ganze Zahl, die die Fläche des größten Quadrats angibt.

## Wann man es verwenden sollte

- Ein klassisches 2D-Gitter-DP-Problem, bei dem man lernt, wie man nach OBEN, LINKS und DIAGONAL-OBEN-LINKS schaut, um den Zustand der aktuellen Zelle zu bestimmen.
- Der perfekte Einstieg, bevor man sich an das viel schwierigere `Maximal Rectangle`-Problem wagt.

## Vorgehensweise

**1. Den Zustand definieren:**
Sei `dp[i][j]` die **Seitenlänge** des größten Quadrats, dessen *rechte untere Ecke* genau in der Zelle `(i, j)` liegt.

**2. Die Basisfälle ermitteln:**
Befinden wir uns in der ersten Zeile (`i = 0`) oder der ersten Spalte (`j = 0`), ist das größte Quadrat, das dort enden kann, auf die Zelle selbst beschränkt!
Wenn `matrix[i][j] == '1'`, dann `dp[i][j] = 1`.
Wenn `matrix[i][j] == '0'`, dann `dp[i][j] = 0`.

**3. Finde den Übergang (die Rekursionsbeziehung):**
Was bestimmt für jede innere Zelle `(i, j)`, ob sie ein größeres Quadrat bilden kann?
Zunächst MUSS `matrix[i][j]` `'1'` sein. Ist es `'0'`, wird das Quadrat sofort unterbrochen, und `dp[i][j] = 0`.
Ist sie `'1'`, kann sie als rechte untere Ecke eines größeren Quadrats fungieren, WENN UND NUR WENN die drei benachbarten Zellen (links, oben, diagonal oben links) EBENFALLS Quadrate von mindestens einer bestimmten Größe bilden!
Die Größe des Quadrats, das bei `(i, j)` endet, wird durch das **kleinste** dieser drei umgebenden Quadrate begrenzt.
`dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`

Wir verfolgen den Wert von `max_side` global über die gesamte DP-Matrix hinweg. Die endgültige Fläche ist `max_side * max_side`.

**4. Speicherplatz optimieren:**
Beachte, dass `dp[i][j]` nur von der aktuellen Zeile `i` und der vorherigen Zeile `i-1` abhängt. Wir können dies vom $O(M \times N)$-Speicherplatz auf ein eindimensionales Array der Größe N optimieren!
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

## Schritt-für-Schritt-Anleitung

`matrix = [["1","0","1","0"], ["1","1","1","1"], ["1","1","1","1"]]`
M = 3, N = 4. `dp` wird auf `[0, 0, 0, 0, 0]` initialisiert.

1. **i = 1 (Zeile 0: `1 0 1 0`):**
   - `j=1 ('1')`: `dp[1] = min(0, 0, 0) + 1 = 1`. `max=1`.
   - `j=2 ('0')`: `dp[2] = 0`.
   - `j=3 ('1')`: `dp[3] = min(0, 0, 0) + 1 = 1`.
   - `j=4 ('0')`: `dp[4] = 0`.
   - `dp` Zustand: `[0, 1, 0, 1, 0]`.

2. **i = 2 (Zeile 1: `1 1 1 1`):**
   - `j=1 ('1')`: `dp[1] = min(1(up), 0(left), 0(diag)) + 1 = 1`.
   - `j=2 ('1')`: `dp[2] = min(0(up), 1(left), 1(diag)) + 1 = 1`.
   - `j=3 ('1')`: `dp[3] = min(1(up), 1(left), 0(diag)) + 1 = 1`.
   - `j=4 ('1')`: `dp[4] = min(0(up), 1(left), 1(diag)) + 1 = 1`.
   - `dp`-Zustand: `[0, 1, 1, 1, 1]`.

3. **i = 3 (Zeile 2: `1 1 1 1`):**
   - `j=1 ('1')`: `dp[1] = 1`.
   - `j=2 ('1')`: `dp[2] = min(1, 1, 1) + 1 = 2`. `max=2`.
   - `j=3 ('1')`: `dp[3] = min(1, 2, 1) + 1 = 2`.
   - `j=4 ('1')`: `dp[4] = min(1, 2, 1) + 1 = 2`.
   - `dp`-Zustand: `[0, 1, 2, 2, 2]`.

Das Endergebnis `max_side` ist 2. Die Fläche beträgt 2 × 2 = 4. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M * N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(M * N)$ | $O(N)$ |

Die verschachtelten Schleifen durchlaufen jede Zelle der M × N-Matrix genau einmal und führen dabei $O(1)$ Operationen durch. Die Laufzeit beträgt genau $O(M \times N)$.
Durch die Verwendung des eindimensionalen rollenden Arrays beträgt der Speicherbedarf $O(N)$ (wobei N die Anzahl der Spalten ist).

## Varianten & Optimierungen

- **Anzahl der Quadrat-Submatrizen mit lauter Einsen:** Anstatt die MAXIMALE Fläche zurückzugeben, gib die GesamtANZAHL der gültigen Quadrate zurück! Die Logik ist absolut identisch. Der Wert `dp[i][j]` gibt genau an, wie viele gültige Quadrate ihre rechte untere Ecke bei `(i, j)` haben. Man summiert einfach alle `dp[i][j]`-Werte über die gesamte Matrix!
- **Maximales Rechteck:** Was ist, wenn die Form kein perfektes Quadrat sein muss? Die `min()`-Logik bricht dann völlig zusammen. Dies erfordert einen völlig anderen Ansatz unter Verwendung monotoner Stacks! (`dp_26`).

## Praktische Anwendungen

- **Computer Vision:** Schnelle Identifizierung von Begrenzungsrahmen für dichte, einfarbige Bereiche (wie eine durchgehend weiße Wand oder einen Textblock) in einer Bildverarbeitungs-Pipeline.

## Verwandte Algorithmen in cOde(n)

- **[dp_12 – Minimum Path Sum](dp_12_min-cost-path.md)** — Ein weiteres 2D-Gitter-DP, bei dem man ein eindimensionales Zeilenarray optimiert, wobei man hier zusätzlich den diagonalen Zustand im Auge behalten muss!
- **[dp_26 – Maximal Rectangle](dp_26_maximal-rectangle.md)** – Die wesentlich schwierigere Variante, bei der Breite und Höhe voneinander abweichen können.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
