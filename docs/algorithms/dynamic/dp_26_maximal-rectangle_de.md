# Maximales Rechteck

| | |
|---|---|
| **ID** | `dp_26` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(M * N)$ Zeit, $O(N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Maximales Rechteck](https://leetcode.com/problems/maximal-rectangle/) |

## Aufgabenstellung

Gegeben ist eine `rows x cols` binäre Matrix, die mit `0` und `1` gefüllt ist. Finde das größte Rechteck, das ausschließlich `1` enthält, und gib dessen Fläche zurück.

**Eingabe:** Eine `m x n`-Matrix `matrix`, deren Elemente Zeichen `'0'` oder `'1'` sind.
**Ausgabe:** Eine ganze Zahl, die die Fläche des größten Rechtecks angibt.

## Wann man diese Aufgabe einsetzen sollte

- Um zu zeigen, dass man die Kombination aus dynamischer Programmierung (zur Komprimierung von 2D-Daten in 1D-Histogramme) und monotonen Stacks (zur Lösung der 1D-Histogramme) beherrscht.
- Du darfst den einfachen `min(Up, Left, Diagonal)`-Trick aus „Maximal Square“ (`dp_25`) NICHT verwenden. Rechtecke lassen sich nicht symmetrisch skalieren.

## Vorgehensweise

**1. Die mathematische Reduktion:**
Stell dir vor, du schneidest die Matrix horizontal Zeile für Zeile auf.
Wenn du die `1`s, die sich von der aktuellen Zeile nach oben erstrecken, als „Gebäude“ betrachtest, bildet jede Zeile eine Skyline oder ein Histogramm!
Zum Beispiel:
```
1 0 1 0  -> Histogram: [1, 0, 1, 0]
1 1 1 1  -> Histogram: [2, 1, 2, 1]  (Buildings grow taller!)
1 1 1 0  -> Histogram: [3, 2, 3, 0]  (A '0' instantly drops the building to height 0)
```
Wenn wir die Matrix zeilenweise in eine Folge von Histogrammen umwandeln können, lässt sich das Problem perfekt darauf reduzieren, den Algorithmus **„Größtes Rechteck im Histogramm“** auf jede einzelne Zeile anzuwenden!

**2. Dynamische Programmierung (Erstellen der Histogramme):**
Wir verwalten ein 1D-DP-Array `heights` der Größe `N`.
Für jede Zeile `i` durchlaufen wir jede Spalte `j`:
- Wenn `matrix[i][j] == '1'`, dann `heights[j] += 1` (das Gebäude wird höher).
- Wenn `matrix[i][j] == '0'`, dann `heights[j] = 0` (das Fundament des Gebäudes wird zerstört).

**3. Monotoner Stack (Lösung des Histogramms):**
Wie finden wir für das aktuelle `heights`-Array das größte Rechteck?
Wir durchlaufen das Histogramm. Dabei führen wir einen monoton steigenden Stack von Indizes.
Wenn wir auf einen Balken `heights[k]` stoßen, der *kürzer* ist als der Balken an der Spitze des Stacks, bedeutet dies, dass sich der höhere Balken im Stack nicht mehr nach rechts ausdehnen kann!
Wir entfernen den höheren Balken vom Stack.
- Seine Höhe `H` beträgt `heights[popped_index]`.
- Seine Breite `W` wird durch seine Begrenzungen bestimmt: Die linke Begrenzung ist die neue Spitze des Stapels (der nächstgelegene kürzere Balken auf der linken Seite). Die rechte Begrenzung ist `k` (der nächstgelegene kürzere Balken auf der rechten Seite).
- Fläche = `H * W`.
Wir verfolgen den `max_area` über alle Entnahmen hinweg, über alle Zeilen hinweg!

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

## Schritt-für-Schritt-Anleitung

`matrix = [["1","0","1","0"], ["1","1","1","1"]]`.
M=2, N=4. `heights = [0, 0, 0, 0, 0]`.

1. **Zeile 0 (`1 0 1 0`):**
   - `heights` wird zu `[1, 0, 1, 0, 0]`.
   - Stapelausführung:
 - `j=0` (h=1): `0` auf den Stack legen. Stack=`[0]`.
     - `j=1` (h=0): `0 < heights[0]`. `0` vom Stack nehmen. h=1, w=1-0=1. Fläche=1. `max_area=1`. `1` auf den Stack legen. Stack=`[1]`.
 - `j=2` (h=1): `2` auf den Stack legen. Stack=`[1, 2]`.
     - `j=3` (h=0): `0 < heights[2]`. Entnehmen `2`. h=1, w=3-1-1=1. Fläche=1. Auf den Stack legen `3`.
     - ... (Leert den Stack). `max_area = 1`.

2. **Zeile 1 (`1 1 1 1`):**
   - `heights` wird zu `[2, 1, 2, 1, 0]`. (Beachte, dass der Index 1 von 0 auf 1 und der Index 0 von 1 auf 2 gewachsen ist).
   - Stapelausführung:
 - `j=0` (h=2): `0` auf den Stack legen.
     - `j=1` (h=1): `1 < 2`. Pop `0`. h=2, w=1-0=1. Fläche=2. `max=2`. `1` auf den Stack legen. Stack=`[1]`.
 - `j=2` (h=2): `2` auf den Stack legen. Stack=`[1, 2]`.
     - `j=3` (h=1): `1 < 2`. Pop `2`. h=2, w=3-1-1=1. Fläche=2. `3` auf den Stack legen. Stack=`[1, 3]`.
 - `j=4` (h=0): `0 < 1`. `3` entnehmen. h=1, w=4-1-1=2. Fläche=2.
 - `1` entnehmen (h=1). w=4-0=4. Fläche = 1 × 4 = 4. `max=4`!
   - `max_area = 4`.

Das Ergebnis `max_area` ist 4. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M * N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(N)$ |
| **Schlechteste** | $O(M * N)$ | $O(N)$ |

Die äußere Schleife läuft M-mal. Die innere DP-Schleife läuft N-mal. Die Monotonic-Stack-Schleife verarbeitet jeden Index j genau zweimal (ein Push, ein Pop). Die Gesamtzeit beträgt streng $O(M \times N)$.
Die Platzkomplexität beträgt streng $O(N)$ für das `heights`-Array und das `stack`-Array.

## Varianten & Optimierungen

- **Optimierung nur mit DP-Arrays:** Man kann den monotonen Stack tatsächlich vollständig durch zwei weitere DP-Arrays ersetzen: `left[j]` und `right[j]`. Für jede Zeile führen Sie einen Durchlauf von links nach rechts durch, um die linke Begrenzung des Gebäudes bei `j` zu ermitteln, sowie einen Durchlauf von rechts nach links, um die rechte Begrenzung zu ermitteln. Dies bleibt $O(M \times N)$-zeitlich, ist jedoch rein mathematisch und läuft in der Praxis oft schneller, da der Overhead durch Stack-Push/Pop vermieden wird.

## Anwendungen in der Praxis

- **VLSI-Design:** Ermittlung der größten zusammenhängenden rechteckigen Fläche auf einem Wafer, auf der ein großer Logikblock (wie ein CPU-Kern) platziert werden kann, ohne dass es zu Überschneidungen mit bereits verlegten Leiterbahnen kommt.

## Verwandte Algorithmen in cOde(n)

- **[dp_25 – Maximal Square](dp_25_maximal-square.md)** — Die streng quadratische, rein auf dynamischer Programmierung (DP) basierende Variante dieses Problems.
- **[stack_02 - Largest Rectangle in Histogram](../stacks/stack_02_largest-rectangle-in-histogram.md)** — Der 1D-Monotonic-Stack-Algorithmus, der als Kern dieser 2D-Lösung dient.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
