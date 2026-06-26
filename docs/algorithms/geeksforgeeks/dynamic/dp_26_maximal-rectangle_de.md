# Maximal Rectangle

| | |
|---|---|
| **ID** | `dp_26` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(M * N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) |

## Problemstellung

Gegeben ist eine `rows x cols` große binäre Matrix, die mit `0` und `1` gefüllt ist. Finde das größte Rechteck, das nur aus `1` besteht, und gib dessen Fläche zurück.

**Eingabe:** Eine `m x n` Matrix `matrix`, wobei die Elemente die Zeichen `'0'` oder `'1'` sind.
**Ausgabe:** Eine Ganzzahl, die die Fläche des größten Rechtecks repräsentiert.

## Wann man es verwendet

- Um die Beherrschung der Kombination von Dynamic Programming (zur Komprimierung von 2D-Daten in 1D-Histogramme) mit Monotonic Stacks (zur Lösung der 1D-Histogramme) zu demonstrieren.
- Man kann NICHT den einfachen `min(Up, Left, Diagonal)`-Trick aus Maximal Square (`dp_25`) verwenden. Rechtecke skalieren nicht symmetrisch.

## Ansatz

**1. Die mathematische Reduktion:**
Stellen Sie sich vor, Sie schneiden die Matrix horizontal Zeile für Zeile auf.
Wenn Sie die `1`en, die sich von der aktuellen Zeile nach oben erstrecken, als "Gebäude" betrachten, bildet jede Zeile eine Skyline oder ein Histogramm!
Zum Beispiel:
```
1 0 1 0  -> Histogramm: [1, 0, 1, 0]
1 1 1 1  -> Histogramm: [2, 1, 2, 1]  (Gebäude wachsen in die Höhe!)
1 1 1 0  -> Histogramm: [3, 2, 3, 0]  (Eine '0' lässt das Gebäude sofort auf Höhe 0 fallen)
```
Wenn wir die Matrix Zeile für Zeile in eine Sequenz von Histogrammen umwandeln können, reduziert sich das Problem perfekt darauf, den Algorithmus für das **"Largest Rectangle in Histogram"** auf jede einzelne Zeile anzuwenden!

**2. Dynamic Programming (Aufbau der Histogramme):**
Wir führen ein 1D-DP-Array `heights` der Größe `N`.
Für jede Zeile `i` iterieren wir durch jede Spalte `j`:
- Wenn `matrix[i][j] == '1'`, dann `heights[j] += 1` (das Gebäude wächst höher).
- Wenn `matrix[i][j] == '0'`, dann `heights[j] = 0` (das Fundament des Gebäudes wird zerstört).

**3. Monotonic Stack (Lösung des Histogramms):**
Wie finden wir für das aktuelle `heights`-Array das größte Rechteck?
Wir iterieren durch das Histogramm. Wir führen einen Monotonic Increasing Stack von Indizes.
Wenn wir auf einen Balken `heights[k]` stoßen, der *kürzer* ist als der Balken an der Spitze des Stacks, bedeutet dies, dass der höhere Balken im Stack nicht weiter nach rechts expandieren kann!
Wir entfernen den höheren Balken vom Stack.
- Seine Höhe `H` ist `heights[popped_index]`.
- Seine Breite `W` wird durch seine Grenzen bestimmt: Die linke Grenze ist die neue Spitze des Stacks (der nächstgelegene kürzere Balken zur Linken). Die rechte Grenze ist `k` (der nächstgelegene kürzere Balken zur Rechten).
- Fläche = `H * W`.
Wir verfolgen die `max_area` über alle Entfernungen hinweg, über alle Zeilen!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_26: Maximal Rectangle.

For each row, build a heights[] histogram. Run the largest-
rectangle-in-histogram algorithm (monotonic stack) on each
row. Track the global maximum area across all rows.
"""


def solve(matrix, m, n):
    if m == 0 or n == 0:
        return 0
    heights = [0] * (n + 1)  # Extra sentinel 0 at end
    max_area = 0
    for i in range(m):
        for j in range(n):
            heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
        stack = [-1]
        for k in range(n + 1):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[k]:
                h = heights[stack.pop()]
                w = k - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(k)
    return max_area
```

</details>

## Durchlauf

`matrix = [["1","0","1","0"], ["1","1","1","1"]]`.
M=2, N=4. `heights = [0, 0, 0, 0, 0]`.

1. **Zeile 0 (`1 0 1 0`):**
   - `heights` wird zu `[1, 0, 1, 0, 0]`.
   - Stack-Ausführung:
     - `j=0` (h=1): Push `0`. Stack=`[0]`.
     - `j=1` (h=0): `0 < heights[0]`. Pop `0`. h=1, w=1-0=1. Fläche=1. `max_area=1`. Push `1`. Stack=`[1]`.
     - `j=2` (h=1): Push `2`. Stack=`[1, 2]`.
     - `j=3` (h=0): `0 < heights[2]`. Pop `2`. h=1, w=3-1-1=1. Fläche=1. Push `3`.
     - ... (Leeren). `max_area = 1`.

2. **Zeile 1 (`1 1 1 1`):**
   - `heights` wird zu `[2, 1, 2, 1, 0]`. (Beachten Sie, dass Index 1 von 0 auf 1 wuchs, Index 0 von 1 auf 2 wuchs).
   - Stack-Ausführung:
     - `j=0` (h=2): Push `0`.
     - `j=1` (h=1): `1 < 2`. Pop `0`. h=2, w=1-0=1. Fläche=2. `max=2`. Push `1`. Stack=`[1]`.
     - `j=2` (h=2): Push `2`. Stack=`[1, 2]`.
     - `j=3` (h=1): `1 < 2`. Pop `2`. h=2, w=3-1-1=1. Fläche=2. Push `3`. Stack=`[1, 3]`.
     - `j=4` (h=0): `0 < 1`. Pop `3`. h=1, w=4-1-1=2. Fläche=2.
       - Pop `1` (h=1). w=4-0=4. Fläche = 1 x 4 = 4. `max=4`!
   - `max_area = 4`.

Das Ergebnis `max_area` ist 4. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M * N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(M * N)$ | $O(N)$ |

Die äußere Schleife läuft M-mal. Die innere DP-Schleife läuft N-mal. Die Monotonic Stack-Schleife verarbeitet jeden Index j exakt zweimal (einmal Push, einmal Pop). Die Gesamtlaufzeit beträgt strikt $O(M \times N)$.
Die Platzkomplexität beträgt strikt $O(N)$ für das `heights`-Array und den `stack`.

## Varianten & Optimierungen

- **DP-Only Array-Optimierung:** Sie können den Monotonic Stack tatsächlich vollständig durch zwei weitere DP-Arrays ersetzen: `left[j]` und `right[j]`. Für jede Zeile führen Sie einen Durchlauf von links nach rechts durch, um die linke Grenze des Gebäudes bei `j` zu finden, und einen Durchlauf von rechts nach links, um die rechte Grenze zu finden. Dies bleibt bei $O(M \times N)$ Zeit, ist aber rein mathematisch und läuft in der Praxis oft schneller, da der Overhead durch Stack-Push/Pop vermieden wird.

## Anwendungen in der Praxis

- **VLSI-Design:** Finden der größten zusammenhängenden rechteckigen Fläche aus leerem Silizium auf einem Wafer, um einen massiven Logikblock (wie einen CPU-Kern) zu platzieren, ohne bestehende Leiterbahnen zu überlappen.

## Verwandte Algorithmen in cOde(n)

- **[dp_25 - Maximal Square](dp_25_maximal-square.md)** — Die rein quadratische, rein DP-basierte Variante dieses Problems.
- **[stack_02 - Largest Rectangle in Histogram](../stacks/stack_02_largest-rectangle-in-histogram.md)** — Der 1D Monotonic Stack-Algorithmus, der als Kern-Engine für diese 2D-Lösung dient.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*