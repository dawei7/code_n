# Schnittpunkt von Liniensegmenten

| | |
|---|---|
| **ID** | `geometric_03` |
| **Kategorie** | geometrisch |
| **Komplexität (erforderlich)** | $O(1)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Line–line intersection](https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line) |

## Problemstellung

Gegeben sind zwei Liniensegmente, die durch ihre Endpunkte definiert sind: Segment 1 von P_1 nach P_2 und Segment 2 von P_3 nach P_4.
Bestimmen Sie, ob sich die beiden Liniensegmente strikt oder tangential schneiden.
Sie müssen dies ausschließlich unter Verwendung von Ganzzahl-Arithmetik (der **Kreuzprodukt-Orientierungsprüfung**) lösen, wobei Gleitkomma-Steigungen, Division durch Null oder der Umgang mit unendlichen y=mx+b-Gleichungen vermieden werden.

**Eingabe:** Vier `(x, y)` Koordinaten-Tupel: `p1`, `p2`, `p3`, `p4`.
**Ausgabe:** Ein Boolean: `True`, wenn sich die Segmente schneiden, andernfalls `False`.

## Anwendungsbereiche

- Um zu bestimmen, ob eine Sichtlinie in einem 2D-Spiel durch eine Wand blockiert wird.
- Als grundlegender Baustein für den "Punkt-im-Polygon"-Ray-Casting-Algorithmus (`geo_04`).

## Ansatz

Wir verwenden dasselbe Konzept der **Kreuzprodukt-Orientierung** wie beim Graham Scan.
`orientation(A, B, C)` gibt Folgendes zurück:
- `1`, wenn der Pfad A \to B \to C im Uhrzeigersinn verläuft.
- `2`, wenn der Pfad gegen den Uhrzeigersinn verläuft.
- `0`, wenn A, B, C perfekt kollinear sind.

**Die Schnittregel:**
Zwei Segmente (P_1, P_2) und (P_3, P_4) schneiden sich genau dann, wenn:
1. P_3 und P_4 auf **entgegengesetzten Seiten** der durch (P_1, P_2) definierten Linie liegen.
   - Das bedeutet, `orientation(p1, p2, p3)` unterscheidet sich von `orientation(p1, p2, p4)`.
2. **UND** P_1 und P_2 auf **entgegengesetzten Seiten** der durch (P_3, P_4) definierten Linie liegen.
   - Das bedeutet, `orientation(p3, p4, p1)` unterscheidet sich von `orientation(p3, p4, p2)`.

Wenn beide Bedingungen erfüllt sind, bilden die Segmente eine X-Form und müssen sich schneiden!

**Der kollineare Spezialfall:**
Was ist, wenn die Linien kein X bilden, sondern perfekt übereinander liegen (kollinear)?
Wenn `orientation == 0` ist, müssen wir prüfen, ob der Punkt tatsächlich direkt *zwischen* den Endpunkten auf den X/Y-Achsen liegt (unter Verwendung einer einfachen Bounding-Box-Prüfung). Wenn er innerhalb der Bounding Box liegt, überlappen sie sich und schneiden sich somit!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for geometric_03: Line Segment Intersection.

Given two line segments, each as ((x1, y1), (x2, y2)). They
intersect iff the orientations of the two endpoint triples
straddle each other. Standard cross-product trick.
"""


def solve(seg1, seg2):
    def orient(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    def on_segment(a, b, c):
        return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and
                min(a[1], b[1]) <= c[1] <= max(a[1], b[1]))

    (p1, q1) = seg1
    (p2, q2) = seg2
    o1 = orient(p1, q1, p2)
    o2 = orient(p1, q1, q2)
    o3 = orient(p2, q2, p1)
    o4 = orient(p2, q2, q1)
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
    if o1 == 0 and on_segment(p1, q1, p2):
        return True
    if o2 == 0 and on_segment(p1, q1, q2):
        return True
    if o3 == 0 and on_segment(p2, q2, p1):
        return True
    if o4 == 0 and on_segment(p2, q2, q1):
        return True
    return False
```

</details>

## Durchlauf

*(Konzeptionell)*
`L1: p1(1,1) bis p2(10,1)` (Eine horizontale Linie bei y=1).
`L2: p3(1,2) bis p4(10,2)` (Eine horizontale Linie bei y=2).

1. `o1 = orient(p1, p2, p3)` -> `(1,1)` bis `(10,1)` bis `(1,2)`. Dreht gegen den Uhrzeigersinn. `o1 = 2`.
2. `o2 = orient(p1, p2, p4)` -> `(1,1)` bis `(10,1)` bis `(10,2)`. Dreht gegen den Uhrzeigersinn. `o2 = 2`.
3. Allgemeine Prüfung: `o1 != o2`? Nein! (Beide sind 2). P_3 und P_4 liegen auf der *gleichen Seite* von L1.
4. Ergebnis: `False`. Sie schneiden sich nicht. ✓

`L1: p1(10,0) bis p2(0,10)`
`L2: p3(0,0) bis p4(10,10)`
1. `o1 = orient((10,0), (0,10), (0,0))` -> Uhrzeigersinn (`1`).
2. `o2 = orient((10,0), (0,10), (10,10))` -> Gegen den Uhrzeigersinn (`2`).
3. `o3 = orient((0,0), (10,10), (10,0))` -> Uhrzeigersinn (`1`).
4. `o4 = orient((0,0), (10,10), (0,10))` -> Gegen den Uhrzeigersinn (`2`).
5. Allgemeine Prüfung: `(o1 != o2)` UND `(o3 != o4)`. True UND True!
6. Ergebnis: `True`. Sie bilden ein X! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Der Algorithmus führt genau 4 Kreuzproduktberechnungen und bis zu 4 Bounding-Box-Prüfungen durch. Alles basiert auf reiner $O(1)$ arithmetischer Multiplikation und Subtraktion. Die Zeitkomplexität ist strikt $O(1)$.

## Varianten & Optimierungen

- **Sweep Line (Bentley-Ottmann):** Was ist, wenn Sie N Liniensegmente gegeben haben und herausfinden müssen, ob sich *irgendwelche* zwei schneiden? Der Vergleich aller Paare ist $O(N^2)$. Der Bentley-Ottmann Sweep-Line-Algorithmus verwendet einen balancierten BST, um dies in $O((N + I) \log N)$ Zeit zu lösen, wobei I die Anzahl der Schnittpunkte ist!

## Anwendungen in der Praxis

- **Computer Aided Design (CAD):** Sicherstellen, dass sich Leiterbahnen auf einer gedruckten Leiterplatte (PCB) nicht überlappen und einen Kurzschluss verursachen.
- **Geofencing:** Validierung, dass eine vom Benutzer gezeichnete polygonale Lieferzone sich nicht selbst schneidet (was ein komplexes Polygon bilden würde).

## Verwandte Algorithmen in cOde(n)

- **[geometric_02 - Graham Scan](geometric_02_convex-hull-graham-scan.md)** — Basiert auf derselben Kreuzprodukt-Mathematik, um Drehungen zu bestimmen.
- **[geometric_04 - Punkt im Polygon](geometric_04_point-in-polygon-ray-casting.md)** — Wirft einen Strahl (ein Liniensegment) und zählt mithilfe dieser exakten Funktion, wie viele Polygonkanten er schneidet!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Wettbewerbsprogrammierungs-Referenzseiten verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*