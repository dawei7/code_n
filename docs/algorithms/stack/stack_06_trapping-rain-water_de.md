# Trapping Rain Water

| | |
|---|---|
| **ID** | `stack_06` |
| **Kategorie** | stack |
| **Komplexität (erforderlich)** | $O(N)$ |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 10/10 |
| **LeetCode-Äquivalent** | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) |

## Problemstellung

Gegeben ist ein Array aus `n` nicht-negativen Ganzzahlen, das eine Höhenkarte darstellt, wobei die Breite jedes Balkens 1 beträgt. Berechnen Sie, wie viel Wasser nach einem Regen darin gespeichert werden kann.

**Input:** Ein Integer-Array `height`.
**Output:** Ein Integer, der die gesamte Menge an gespeichertem Wasser repräsentiert.

**Beispiel:**
`height = [0,1,0,2,1,0,1,3,2,1,2,1]`
Output: `6`.
*(Gespeichertes Wasser: 1 Einheit an Index 2. 1 Einheit an Index 4. 2 Einheiten an Index 5. 1 Einheit an Index 6. 1 Einheit an Index 9. Gesamt = 6).*

## Wann man es verwendet

- Gilt weithin als die berühmteste FAANG-Interviewfrage.
- Kann mittels Dynamic Programming, Two Pointers oder einem **Monotonic Stack** gelöst werden. Wir behandeln hier den Stack-Ansatz, um dessen Stärke bei der Auflösung horizontaler Begrenzungen zu demonstrieren.

## Ansatz

Wasser wird in einem "Tal" gespeichert. Ein Tal benötigt eine linke Wand, einen Boden und eine rechte Wand.
Wenn wir einen **Monotonically Decreasing Stack** verwenden, können wir diese Täler finden!

Wir iterieren durch das Array. Der Stack speichert die *Indizes* der Balken.
- Solange der aktuelle Balken kleiner oder gleich dem Balken an der Spitze des Stacks ist, führen wir einen `push` aus. Wir bewegen uns in ein Tal hinab!
- In dem Moment, in dem wir einen Balken `curr_height` finden, der *höher* ist als die Spitze des Stacks, haben wir die rechte Wand eines Tals erreicht!
- Wir führen einen `pop` auf der Stack-Spitze aus. Dieses entfernte Element ist der **Boden** des Tals (`bottom_height`).
- Nun betrachten wir die *neue* Spitze des Stacks. Dies ist die **linke Wand** des Tals.
- Die Höhe des gespeicherten Wassers, das durch diese drei Elemente begrenzt wird, ist `min(left_wall_height, right_wall_height) - bottom_height`.
- Die Breite des gespeicherten Wassers ist `right_wall_index - left_wall_index - 1`.
- Addieren Sie `height * width` zum gesamten gespeicherten Wasser.
- Wiederholen Sie den `pop`-Prozess, bis der Stack leer ist oder `curr_height` nicht mehr höher ist als die Stack-Spitze. Führen Sie dann einen `push` von `curr_index` aus.

Dies berechnet das Wasser in horizontalen "Schichten" von unten nach oben!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for stack_06: Trapping Rain Water.

Given a non-negative integer array heights where each
"""


def solve(heights, n):
    """Trapping Rain Water via monotonic stack."""
    if n <= 2:
        return 0
    stack = []  # indices with increasing heights
    water = 0
    for i in range(n):
        while stack and heights[i] > heights[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            # Distance between current and new top of stack.
            dist = i - stack[-1] - 1
            # Bounded by min of the two walls minus the popped bottom.
            bounded = min(heights[i], heights[stack[-1]]) - heights[top]
            water += dist * bounded
        stack.append(i)
    return water
```

</details>

## Durchlauf

`height = [2, 1, 0, 2]`

1. `i=0, h=2`. `push`. `stack=[0]`.
2. `i=1, h=1`. `1 < 2`. `push`. `stack=[0, 1]`. (Abstieg).
3. `i=2, h=0`. `0 < 1`. `push`. `stack=[0, 1, 2]`. (Abstieg).
4. `i=3, h=2`. 
   - `2 > height[stack[-1]] (0)`. Rechte Wand gefunden!
   - `pop` `2`. Bodenhöhe ist 0.
   - Linke Wand ist Stack-Spitze `1`. Linke Höhe ist 1.
   - Begrenzte Höhe = `min(1, 2) - 0 = 1`.
   - Breite = `3 - 1 - 1 = 1`.
   - Wasser += 1 x 1 = 1. (Füllte den Boden des Tals).
   - Stack ist nun `[0, 1]`.
   - `2 > height[stack[-1]] (1)`. Immer noch rechte Wand!
   - `pop` `1`. Bodenhöhe ist 1.
   - Linke Wand ist Stack-Spitze `0`. Linke Höhe ist 2.
   - Begrenzte Höhe = `min(2, 2) - 1 = 1`.
   - Breite = `3 - 0 - 1 = 2`.
   - Wasser += 1 x 2 = 2. (Füllte die obere horizontale Schicht).
   - Stack ist nun `[0]`.
   - `2 > height[stack[-1]] (2)`? Falsch.
   - `push` `3`. `stack=[0, 3]`.

Gesamtes Wasser = `1 + 2 = 3`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Jedes Element wird genau einmal auf den Stack gepusht und höchstens einmal gepoppt. Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität beträgt $O(N)$, da das Array streng abnehmend sein könnte (z. B. `[5, 4, 3, 2, 1]`), was dazu führt, dass alle N Elemente auf den Stack gepusht werden, ohne jemals einen `pop` auszuführen.

## Varianten & Optimierungen

- **Two Pointers ($O(1)$ Platz):** Sie können dies ohne Stack lösen, indem Sie einen linken und einen rechten Pointer verwenden, die sich nach innen bewegen. Sie verwalten `max_left` und `max_right`. Da das Wasser durch das Minimum der beiden Gipfel bestimmt wird, verarbeiten Sie einfach die Seite mit dem *kleineren* maximalen Gipfel! Wenn `max_left < max_right`, können Sie sicher `max_left - height[left]` zur Gesamtsumme addieren und den linken Pointer bewegen. Dies erreicht $O(N)$ Zeit und $O(1)$ Platz.
- **Dynamic Programming ($O(N)$ Platz):** Erstellen Sie zwei Arrays, `left_max` und `right_max`, die in zwei linearen Durchläufen vorberechnet werden. Das Wasser an Index `i` ist einfach `min(left_max[i], right_max[i]) - height[i]`. Am einfachsten zu verstehen, benötigt aber 3 Durchläufe.

## Anwendungen in der Praxis

- **Topologische Datenanalyse:** Identifizierung von Persistenzhomologie und lokalen Minima/Maxima-Becken in 2D-Höhenkarten oder LIDAR-Geländescans.

## Verwandte Algorithmen in cOde(n)

- **[stack_04 - Largest Rectangle in Histogram](stack_04_largest-rectangle-in-histogram.md)** — Verwendet exakt dieselbe Monotonic-Stack-Logik, berechnet jedoch die Fläche unter dem Balken anstatt darüber.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*