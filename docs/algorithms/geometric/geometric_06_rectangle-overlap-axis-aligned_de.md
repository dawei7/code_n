# Überlappung von Rechtecken (achsenparallel)

| | |
|---|---|
| **ID** | `geometric_06` |
| **Kategorie** | Geometrie |
| **Komplexität (erforderlich)** | $O(1)$ |
| **Schwierigkeitsgrad** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Rechtecküberlappung](https://leetcode.com/problems/rectangle-overlap/) |

## Aufgabenstellung

Gegeben sind zwei achsenparallele Rechtecke (Rechtecke, deren Kanten exakt parallel zur X- und Y-Achse verlaufen).
Jedes Rechteck wird durch zwei Koordinaten dargestellt: seine linke untere Ecke `(x1, y1)` und seine rechte obere Ecke `(x2, y2)`.
Stelle fest, ob sich die beiden Rechtecke überlappen. Eine Berührung an einer Ecke oder die gemeinsame Nutzung eines mathematischen Liniensegments als Kante stellt *keine* Überlappung dar (die überlappende Fläche muss streng positiv sein).

**Eingabe:** Zwei Arrays, die die Rechtecke darstellen: `rect1 = [x1, y1, x2, y2]` und `rect2 = [x1, y1, x2, y2]`.
**Ausgabe:** Ein boolescher Wert: `True`, wenn sie sich überlappen, `False` andernfalls.

## Wann man es verwendet

- Wird in FAANG-Vorstellungsgesprächen regelmäßig als grundlegender Test für das Schreiben sauberer, logischer und fehlerfreier Bedingungsprüfungen abgefragt.
- Die Grundlage der 2D-Kollisionserkennung in Spielen (AABB – Axis-Aligned Bounding Box).

## Vorgehensweise

Ein naiver Ansatz versucht, alle Möglichkeiten zu definieren, wie sich Rechtecke *überlappen können* (Ecken innen, ein Kreuz bildend, eines umschließt das andere vollständig). Dies führt zu massiven, unlesbaren und fehleranfälligen `if/else`-Ketten.

**Der Trick mit der umgekehrten Logik:**
Anstatt zu prüfen, ob sie sich überlappen, ist es wesentlich einfacher zu prüfen, **ob sie sich NICHT überlappen!**
Zwei Rechtecke können sich absolut nicht überlappen, wenn eines vollständig und streng links, rechts, oben oder unten vom anderen liegt.

1. **Links:** Befindet sich `rect1` vollständig links von `rect2`?
   - `rect1_right_x <= rect2_left_x`
2. **Rechts:** Befindet sich `rect1` vollständig rechts von `rect2`?
   - `rect1_left_x >= rect2_right_x`
3. **Unten:** Befindet sich `rect1` vollständig unterhalb von `rect2`?
   - `rect1_top_y <= rect2_bottom_y`
4. **Oben:** Befindet sich `rect1` vollständig über `rect2`?
   - `rect1_bottom_y >= rect2_top_y`

Wenn **IRGENDEINE** dieser 4 Bedingungen wahr ist, überlappen sich die Rechtecke nicht!
Wenn also **ALLE** diese Bedingungen falsch sind, MÜSSEN sie sich überlappen!

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

## Schritt-für-Schritt-Anleitung

`rect1 = [0, 0, 2, 2]` (Ein 2 × 2-Quadrat am Ursprung).
`rect2 = [1, 1, 3, 3]` (Ein um 1 versetztes 2 × 2-Quadrat).

1. `is_left`: `2 <= 1`? Falsch.
2. `is_right`: `0 >= 3`? Falsch.
3. `is_bottom`: `2 <= 1`? Falsch.
4. `is_top`: `0 >= 3`? Falsch.

Alle Bedingungen sind falsch. Die Überlappung beträgt `True`. ✓

**Fläche berechnen:**
`overlap_left_x = max(0, 1) = 1`
`overlap_right_x = min(2, 3) = 2`
`width = max(0, 2 - 1) = 1`
`overlap_bottom_y = max(0, 1) = 1`
`overlap_top_y = min(2, 3) = 2`
`height = max(0, 2 - 1) = 1`
Fläche = 1 × 1 = 1. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Der Algorithmus führt eine konstante Anzahl von Ganzzahlvergleichen und Zuweisungen durch. Zeit- und Speicherbedarf sind streng $O(1)$.

## Varianten & Optimierungen

- **Sweep-Line (Suche nach Schnittpunkten zwischen N Rechtecken):** Bei 10.000 Rechtecken ist es zu langsam, sich überschneidende Paare durch Überprüfung jeder $O(N^2)$ Kombination zu finden. Man kann die Rechtecke als „Start“- und „End“-Ereignisse auf die X-Achse projizieren, eine vertikale Linie über die X-Achse ziehen und die aktiven Y-Intervalle mithilfe eines Segmentbaums verwalten! Dadurch reduziert sich die Zeit auf $O(N log N + I)$, wobei I die Anzahl der tatsächlichen Überlappungen ist.

## Anwendungen in der Praxis

- **Web-Rendering-Engines:** Browser berechnen den Schnittpunkt von HTML-`<div>`-Begrenzungsrechtecken mit dem Sichtbereichsrechteck des Benutzers, um zu bestimmen, ob ein Element gerendert oder ausgeblendet werden soll (Lazy Loading).

## Verwandte Algorithmen in cOde(n)

- **[geometric_03 – Linienschnitt](geometric_03_line-segment-intersection.md)** — Die entsprechende Logik für 1D-Linien.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
