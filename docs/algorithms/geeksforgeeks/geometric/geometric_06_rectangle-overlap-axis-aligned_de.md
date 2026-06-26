# Rectangle Overlap (Axis-Aligned)

| | |
|---|---|
| **ID** | `geometric_06` |
| **Kategorie** | geometric |
| **Komplexität (erforderlich)** | $O(1)$ |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/) |

## Problemstellung

Gegeben sind zwei achsenparallele Rechtecke (Rechtecke, deren Kanten perfekt parallel zu den X- und Y-Achsen verlaufen).
Jedes Rechteck wird durch zwei Koordinaten repräsentiert: die untere linke Ecke `(x1, y1)` und die obere rechte Ecke `(x2, y2)`.
Bestimmen Sie, ob sich die beiden Rechtecke überschneiden. Das Berühren an einer Ecke oder das Teilen eines mathematischen Liniensegments als Kante gilt *nicht* als Überschneidung (die überschneidende Fläche muss strikt positiv sein).

**Eingabe:** Zwei Arrays, die die Rechtecke repräsentieren: `rect1 = [x1, y1, x2, y2]` und `rect2 = [x1, y1, x2, y2]`.
**Ausgabe:** Ein Boolean: `True`, wenn sie sich überschneiden, andernfalls `False`.

## Anwendung

- Wird in FAANG-Vorstellungsgesprächen ständig als grundlegender Test für das Schreiben von sauberem, logischem und fehlerfreiem Code zur Überprüfung von Bedingungen abgefragt.
- Die Grundlage für die Kollisionserkennung in 2D-Spielen (AABB - Axis-Aligned Bounding Box).

## Ansatz

Ein naiver Ansatz versucht, alle Möglichkeiten zu definieren, wie sich Rechtecke überschneiden *können* (Ecken innerhalb, ein Kreuz bildend, eines umschließt das andere vollständig). Dies führt zu massiven, unleserlichen und fehleranfälligen `if/else`-Ketten.

**Der Trick der invertierten Logik:**
Anstatt zu prüfen, ob sie sich überschneiden, ist es wesentlich einfacher zu prüfen, **ob sie sich NICHT überschneiden!**
Zwei Rechtecke können sich absolut nicht überschneiden, wenn eines vollständig und strikt links, rechts, oberhalb oder unterhalb des anderen liegt.

1. **Links:** Liegt `rect1` vollständig links von `rect2`?
   - `rect1_right_x <= rect2_left_x`
2. **Rechts:** Liegt `rect1` vollständig rechts von `rect2`?
   - `rect1_left_x >= rect2_right_x`
3. **Unten:** Liegt `rect1` vollständig unterhalb von `rect2`?
   - `rect1_top_y <= rect2_bottom_y`
4. **Oben:** Liegt `rect1` vollständig oberhalb von `rect2`?
   - `rect1_bottom_y >= rect2_top_y`

Wenn **EINE** dieser 4 Bedingungen wahr ist, überschneiden sich die Rechtecke nicht!
Wenn daher **ALLE** diese Bedingungen falsch sind, MÜSSEN sie sich überschneiden!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for geometric_06: Rectangle Overlap (Axis-Aligned).

Given two axis-aligned rectangles (each given by its
"""


def solve(l1, r1, l2, r2):
    """Two rectangles do not overlap iff one is entirely left
    of the other, or one is entirely above the other.
    l1 = top-left, r1 = bottom-right (y-axis points up).
    """
    # If rectangle 1 is to the right of rectangle 2, no overlap.
    if l1[0] > r2[0] or l2[0] > r1[0]:
        return False
    # If rectangle 1 is above rectangle 2, no overlap.
    # "Above" means l1.y > r2.y (r1.y is the lower y-bound of rect 1).
    if r1[1] > l2[1] or r2[1] > l1[1]:
        return False
    return True
```

</details>

## Durchlauf

`rect1 = [0, 0, 2, 2]` (Ein 2 x 2 Quadrat am Ursprung).
`rect2 = [1, 1, 3, 3]` (Ein 2 x 2 Quadrat, um 1 verschoben).

1. `is_left`: `2 <= 1`? False.
2. `is_right`: `0 >= 3`? False.
3. `is_bottom`: `2 <= 1`? False.
4. `is_top`: `0 >= 3`? False.

Alle Bedingungen sind False. Die Überschneidung ist `True`. ✓

**Fläche berechnen:**
`overlap_left_x = max(0, 1) = 1`
`overlap_right_x = min(2, 3) = 2`
`width = max(0, 2 - 1) = 1`
`overlap_bottom_y = max(0, 1) = 1`
`overlap_top_y = min(2, 3) = 2`
`height = max(0, 2 - 1) = 1`
Fläche = 1 x 1 = 1. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Der Algorithmus führt eine konstante Anzahl von Ganzzahlvergleichen und Zuweisungen durch. Zeit- und Platzkomplexität sind strikt $O(1)$.

## Varianten & Optimierungen

- **Sweep Line (Schnittpunkte unter N Rechtecken finden):** Wenn Sie 10.000 Rechtecke haben, ist das Finden überschneidender Paare durch das Prüfen jeder $O(N^2)$-Kombination zu langsam. Sie können die Rechtecke als "Start"- und "End"-Ereignisse auf die X-Achse projizieren, eine vertikale Linie über die X-Achse ziehen und die aktiven Y-Intervalle mithilfe eines Segment Tree verwalten! Dies reduziert die Zeit auf $O(N log N + I)$, wobei I die Anzahl der tatsächlichen Überschneidungen ist.

## Praxisanwendungen

- **Web-Rendering-Engines:** Browser berechnen die Schnittmenge von HTML `<div>`-Begrenzungsrechtecken mit dem Viewport-Rechteck des Benutzers, um zu bestimmen, ob ein Element gerendert oder verworfen (Lazy Loading) werden soll.

## Verwandte Algorithmen in cOde(n)

- **[geometric_03 - Line Intersection](geometric_03_line-segment-intersection.md)** — Die Logik für das 1D-Linien-Äquivalent.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*