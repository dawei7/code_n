# Schnittpunkt von Liniensegmenten

| | |
|---|---|
| **ID** | `geometric_03` |
| **Kategorie** | Geometrie |
| **Komplexität (erforderlich)** | $O(1)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Schnittpunkt zweier Geraden](https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line) |

## Aufgabenstellung

Gegeben sind zwei Liniensegmente, die durch ihre Endpunkte definiert sind: Segment 1 von P_1 nach P_2 und Segment 2 von P_3 nach P_4.
Bestimme, ob sich die beiden Liniensegmente streng oder tangential schneiden.
Du musst dies ausschließlich mit ganzzahliger Arithmetik lösen (die Prüfung der **Orientierung des Kreuzprodukts**), wobei du die Berechnung von Gleitkomma-Steigungen, Division durch Null oder den Umgang mit unendlichen y=mx+b-Gleichungen vermeiden musst.

**Eingabe:** Vier `(x, y)`-Koordinatentupel: `p1`, `p2`, `p3`, `p4`.
**Ausgabe:** Ein boolescher Wert: `True`, wenn sich die Segmente schneiden, andernfalls `False`.

## Anwendungsfälle

- Um festzustellen, ob eine Sichtlinie in einem 2D-Spiel durch eine Wand blockiert wird.
- Als grundlegender Baustein für den Ray-Casting-Algorithmus „Point in Polygon“ (`geo_04`).

## Vorgehensweise

Wir verwenden dasselbe Konzept der **Vektororientierung** wie beim Graham-Scan.
`orientation(A, B, C)` gibt Folgendes zurück:
- `1`, wenn der Pfad A \to B \to C im Uhrzeigersinn verläuft.
- `2`, wenn der Pfad gegen den Uhrzeigersinn verläuft.
- `0`, wenn A, B und C exakt auf einer Geraden liegen.

**Die Schnittregel:**
Zwei Segmente (P_1, P_2) und (P_3, P_4) schneiden sich genau dann, wenn:
1. P_3 und P_4 auf **entgegengesetzten Seiten** der durch (P_1, P_2) gebildeten Geraden liegen.
   – Das bedeutet, dass `orientation(p1, p2, p3)` sich von `orientation(p1, p2, p4)` unterscheidet.
2. **UND** P_1 und P_2 liegen auf **entgegengesetzten Seiten** der durch (P_3, P_4) gebildeten Geraden.
   – Das bedeutet, dass `orientation(p3, p4, p1)` sich von `orientation(p3, p4, p2)` unterscheidet.

Sind beide Bedingungen erfüllt, bilden die Segmente eine X-Form und müssen sich schneiden!

**Der Fall der kollinearen Kanten:**
Was ist, wenn die Geraden kein X bilden, sondern genau übereinander liegen (kollinear)?
Wenn `orientation == 0`, müssen wir prüfen, ob der Punkt tatsächlich direkt *zwischen* den Endpunkten auf der X- und Y-Achse liegt (mithilfe einer einfachen Begrenzungsrahmenprüfung). Liegt er innerhalb des Begrenzungsrahmens, überlappen sie sich und schneiden sich daher!

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
`L1: p1(1,1) to p2(10,1)` (Eine horizontale Gerade bei y=1).
`L2: p3(1,2) to p4(10,2)` (Eine horizontale Gerade bei y=2).

1. `o1 = orient(p1, p2, p3)` -> `(1,1)` zu `(10,1)` zu `(1,2)`. Dreht sich gegen den Uhrzeigersinn. `o1 = 2`.
2. `o2 = orient(p1, p2, p4)` -> `(1,1)` zu `(10,1)` zu `(10,2)`. Drehung gegen den Uhrzeigersinn. `o2 = 2`.
3. Allgemeine Überprüfung: `o1 != o2`? Nein! (Beide sind 2). P_3 und P_4 liegen auf der *gleichen Seite* von L1.
4. Ergebnis: `False`. Sie schneiden sich nicht. ✓

`L1: p1(10,0) to p2(0,10)`
`L2: p3(0,0) to p4(10,10)`
1. `o1 = orient((10,0), (0,10), (0,0))` -> im Uhrzeigersinn (`1`).
2. `o2 = orient((10,0), (0,10), (10,10))` -> Gegen den Uhrzeigersinn (`2`).
3. `o3 = orient((0,0), (10,10), (10,0))` -> Im Uhrzeigersinn (`1`).
4. `o4 = orient((0,0), (10,10), (0,10))` -> Gegen den Uhrzeigersinn (`2`).
5. Allgemeine Überprüfung: `(o1 != o2)` UND `(o3 != o4)`. Wahr UND Wahr!
6. Ergebnis: `True`. Sie bilden ein X! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(1)$ | $O(1)$ |
| **Schlechtester Fall** | $O(1)$ | $O(1)$ |

Der Algorithmus führt genau 4 Kreuzproduktberechnungen und bis zu 4 Begrenzungsrahmenprüfungen durch. Alles basiert auf reiner $O(1)$ arithmetischer Multiplikation und Subtraktion. Die Zeitkomplexität beträgt streng $O(1)$.

## Varianten & Optimierungen

- **Sweep-Line-Verfahren (Bentley-Ottmann):** Was ist, wenn man N Liniensegmente erhält und herausfinden muss, ob sich *beliebige* zwei davon schneiden? Der Vergleich aller Paare ist $O(N^2)$. Der Bentley-Ottmann-Sweep-Line-Algorithmus verwendet einen ausgeglichenen BST, um das Problem in $O((N + I)$ log N) Zeit zu lösen, wobei I die Anzahl der Schnittpunkte ist!

## Anwendungen in der Praxis

- **Computer Aided Design (CAD):** Sicherstellen, dass sich Leiterbahnen auf einer Leiterplatte (PCB) nicht überlappen und keinen Kurzschluss verursachen.
- **Geofencing:** Überprüfen, ob sich ein vom Nutzer gezeichnetes polygonales Liefergebiet nicht selbst schneidet (und so ein komplexes Polygon bildet).

## Verwandte Algorithmen in cOde(n)

- **[geometric_02 – Graham-Scan](geometric_02_convex-hull-graham-scan.md)** — Nutzt genau dieselbe Vektorprodukt-Mathematik, um Wendepunkte zu bestimmen.
- **[geometric_04 – Punkt im Polygon](geometric_04_point-in-polygon-ray-casting.md)** – Werft einen Strahl (ein Liniensegment) und zählt mithilfe genau dieser Funktion, wie viele Polygonkanten er schneidet!

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
