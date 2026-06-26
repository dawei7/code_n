# Largest Rectangle in Histogram

| | |
|---|---|
| **ID** | `stack_04` |
| **Kategorie** | stack |
| **Komplexität (erforderlich)** | $O(N)$ |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) |

## Problemstellung

Gegeben ist ein Array von Integern `heights`, das die Höhe der Balken eines Histogramms darstellt, wobei die Breite jedes Balkens 1 beträgt. Geben Sie die Fläche des größten Rechtecks im Histogramm zurück.

**Eingabe:** Ein Integer-Array `heights`.
**Ausgabe:** Ein Integer, der die maximale rechteckige Fläche repräsentiert.

**Beispiel:**
`heights = [2, 1, 5, 6, 2, 3]`
Ausgabe: `10`.
*(Das größte Rechteck wird durch die Balken der Höhe 5 und 6 gebildet, was ein Rechteck der Höhe 5 und Breite 2 ergibt: `5 * 2 = 10`).*

## Wann man es verwendet

- Gilt als der "Endgegner" der Datenstruktur Monotonic Stack.
- Wird ausgiebig bei Problemen der dynamischen Programmierung in 2D-Matrizen verwendet (wie z. B. Maximal Rectangle).

## Ansatz

Wenn wir ein Rechteck bilden wollen, wird die Höhe dieses Rechtecks durch den **kürzesten** Balken innerhalb seiner Breite begrenzt.
Daher können wir für jeden einzelnen Balken `i` im Histogramm fragen: *"Wenn dieser Balken `i` der absolut kürzeste Balken in einem Rechteck ist, wie weit kann ich dieses Rechteck nach links und rechts ausdehnen?"*
Das Rechteck kann sich nach links ausdehnen, bis es auf einen Balken trifft, der *kürzer* als `heights[i]` ist.
Das Rechteck kann sich nach rechts ausdehnen, bis es auf einen Balken trifft, der *kürzer* als `heights[i]` ist.

Das bedeutet, wir müssen für jeden Balken das **Previous Smaller Element (PSE)** und das **Next Smaller Element (NSE)** finden!
Dies können wir in einem einzigen Durchlauf mit einem **Monotonically Increasing Stack** erreichen.

Während wir über die Balken iterieren:
- Wir pushen Indizes auf den Stack, solange die Höhen streng monoton steigend sind.
- Wenn wir auf einen Balken `curr` stoßen, der *kürzer* ist als der Balken an der Spitze des Stacks, bedeutet dies, dass `curr` das **NSE** für das Element an der Stack-Spitze ist!
- Wir führen ein `pop` auf der Stack-Spitze aus. Ihre Höhe ist bekannt. Ihr **NSE** ist der aktuelle Index `i`. Ihr **PSE** ist das *neue* Element an der Spitze des Stacks (da der Stack monoton steigend ist, muss das darunter liegende Element streng kleiner sein).
- Die Breite des Rechtecks für den entfernten Balken ist `NSE - PSE - 1`.
- Fläche = `height * width`. Aktualisiere die maximale Fläche.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for stack_04: Largest Rectangle in Histogram.

Monotonic stack of bar indices with increasing heights. For each
bar popped, the rectangle extends from the previous-smaller on
the left to the current on the right. Track the max area across
all pops.
"""


def solve(heights, n):
    if n == 0:
        return 0
    stack = []
    best = 0
    for i in range(n + 1):
        cur_h = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > cur_h:
            top = stack.pop()
            h = heights[top]
            left = stack[-1] + 1 if stack else 0
            right = i - 1
            area = h * (right - left + 1)
            if area > best:
                best = area
        stack.append(i)
    return best
```

</details>

## Durchlauf

`heights = [2, 1, 5, 6, 2, 3, 0]` *(0 angehängt)*

1. `i=0 (2)`. Push. `stack=[0]`.
2. `i=1 (1)`. `1 < 2`. **Pop `0` (Höhe 2)**.
   - NSE ist `i=1`. PSE ist keines (Stack leer). `w = 1`.
   - Fläche = 2 x 1 = 2. `max=2`.
   - Push `1`. `stack=[1]`.
3. `i=2 (5)`. Push. `stack=[1, 2]`.
4. `i=3 (6)`. Push. `stack=[1, 2, 3]`.
5. `i=4 (2)`.
   - `2 < 6`. **Pop `3` (Höhe 6)**. NSE=`4`. PSE=`2` (Stack-Spitze). `w = 4 - 2 - 1 = 1`. Fläche = 6 x 1 = 6. `max=6`.
   - `2 < 5`. **Pop `2` (Höhe 5)**. NSE=`4`. PSE=`1` (Stack-Spitze). `w = 4 - 1 - 1 = 2`. Fläche = 5 x 2 = 10. `max=10`.
   - `2 < 1` ist falsch.
   - Push `4`. `stack=[1, 4]`.
6. `i=5 (3)`. Push. `stack=[1, 4, 5]`.
7. `i=6 (0)`. Erzwingt, dass alles gepopt wird.
   - **Pop `5` (Höhe 3)**. `w = 6 - 4 - 1 = 1`. Fläche = 3.
   - **Pop `4` (Höhe 2)**. `w = 6 - 1 - 1 = 4`. Fläche = 8.
   - **Pop `1` (Höhe 1)**. `w = 6`. Fläche = 6.

Ausgabe: `10`. ✓

## Komplexität

| | Zeitkomplexität | Platzkomplexität |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Jeder Index wird genau einmal auf den Stack gepusht und genau einmal gepopt. Die Zeitkomplexität ist streng auf $O(N)$ begrenzt, was sie der $O(N^2)$ Brute-Force-Expansion weit überlegen macht.
Die Platzkomplexität beträgt $O(N)$ für den Stack.

## Varianten & Optimierungen

- **Maximal Rectangle in 2D Binary Matrix:** Gegeben eine 2D-Matrix aus `0`en und `1`en, finde das größte Rechteck aus `1`en. Dies wird gelöst, indem jede Zeile als Basis eines Histogramms betrachtet wird. Man führt ein Array von Höhen, das inkrementiert wird, wenn die Zelle `1` ist, und auf `0` zurückgesetzt wird, wenn die Zelle `0` ist. Man führt diesen $O(N)$ Histogramm-Algorithmus auf jeder Zeile aus, was zu einer $O(ROWS x COLS)$ Lösung führt!

## Anwendungen in der Praxis

- **Computer Vision:** Finden des größten nicht verdeckten Begrenzungsrahmens innerhalb eines Bitmasken-Bildes für die Partitionierung bei der optischen Zeichenerkennung (OCR).

## Verwandte Algorithmen in cOde(n)

- **[stack_02 - Next Greater Element](stack_02_next-greater-element.md)** — Erklärt das grundlegende Monotonic Stack-Muster, das hier verwendet wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*