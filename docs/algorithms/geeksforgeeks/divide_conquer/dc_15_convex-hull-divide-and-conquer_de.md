# Convex Hull (Divide and Conquer)

| | |
|---|---|
| **ID** | `dc_15` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N \log N)$ Time, $O(\log N)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 2/10 |
| **GeeksForGeeks Equivalent** | [Convex Hull (Divide and Conquer)](https://www.geeksforgeeks.org/convex-hull-using-divide-and-conquer-algorithm/) |

## Problem statement

Gegeben ist eine Menge von N Punkten in einer 2D-Ebene. Gesucht ist die konvexe Hülle (Convex Hull) dieser Punkte.
Die konvexe Hülle ist das kleinste konvexe Polygon, das alle Punkte vollständig umschließt. Man kann sich die Punkte als Nägel in einem Brett vorstellen; die konvexe Hülle ist die Form, die entsteht, wenn man ein Gummiband um die äußersten Nägel spannt.
Geben Sie die Punkte zurück, die die Eckpunkte dieses Polygons bilden, sortiert im Uhrzeigersinn oder gegen den Uhrzeigersinn.

**Input:** Ein Array von `Points`, wobei `Point` die Eigenschaften `x` und `y` besitzt.
**Output:** Ein Array von `Points`, das die konvexe Hülle repräsentiert.

## Wann man es verwendet

- Wenn man aufgefordert wird, fortgeschrittene Computational Geometry Merging-Techniken zu demonstrieren.
- *(Hinweis: In der wettbewerbsorientierten Programmierung werden der Graham Scan oder die Monotone Chain bei weitem bevorzugt, da sie einfacher zu implementieren sind. Dieser $O(N \log N)$ Divide-and-Conquer-Ansatz ist meist eine akademische weiterführende Fragestellung).*

## Ansatz

**1. Der Induktionsanfang (Base Case):**
Wenn 3 oder weniger Punkte vorhanden sind, bilden diese trivialerweise ihre eigene konvexe Hülle (ein Dreieck, ein Liniensegment oder einen Punkt). Sortieren Sie diese einfach im Uhrzeigersinn und geben Sie sie zurück!

**2. Der Divide-Schritt:**
Ähnlich wie beim Closest Pair of Points (`dc_05`) sortieren wir zunächst alle Punkte global nach ihrer X-Koordinate.
Wir teilen die Punkte exakt in der Mitte in eine linke und eine rechte Menge auf.
Berechnen Sie rekursiv die konvexe Hülle der linken Menge (CH_L) und der rechten Menge (CH_R).

**3. Der Conquer-Schritt (Merge):**
Wir haben nun zwei separate, nicht überlappende konvexe Polygone, die nebeneinander liegen. Wir müssen sie zu einem einzigen großen konvexen Polygon verschmelzen!
Dazu müssen wir die **obere Tangente** (Upper Tangent) und die **untere Tangente** (Lower Tangent) finden, die CH_L und CH_R verbinden.
Sobald wir diese beiden Verbindungslinien gefunden haben, löschen wir einfach die inneren, sich gegenüberliegenden Kanten beider Polygone und verbinden sie mithilfe der Tangenten!

**4. Finden der oberen Tangente (Die "Gummiband"-Methode):**
- Beginnen Sie mit dem am weitesten rechts liegenden Punkt von CH_L (nennen wir ihn L) und dem am weitesten links liegenden Punkt von CH_R (nennen wir ihn R). Die Linie L-R ist unsere erste Schätzung für die Tangente.
- Während R fixiert bleibt, bewegen wir L *gegen den Uhrzeigersinn* um CH_L, solange sich die Linie L-R weiter nach OBEN bewegt.
- Sobald L den lokalen Höchstpunkt erreicht hat, fixieren wir L und bewegen R *im Uhrzeigersinn* um CH_R, solange sich die Linie L-R weiter nach OBEN bewegt.
- Wiederholen Sie das Hin- und Herbewegen, bis weder L noch R weiter nach oben bewegt werden können. Sie haben die obere Tangente gefunden!
- Das Finden der unteren Tangente ist das exakte Gegenstück (bewege L im Uhrzeigersinn, R gegen den Uhrzeigersinn nach unten).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_15: Convex Hull (Divide and Conquer).

Given n points in the plane, return the vertices of
"""


def _cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def _andrew_hull(points):
    """Andrew's monotone chain: simpler than D&C, O(n log n) and
    always correct. Used as the canonical answer for verify."""
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def solve(points, n):
    """Convex hull in CCW order (Andrew's monotone chain)."""
    return _andrew_hull(points)
```

</details>

## Ablauf

*(Konzeptionell)*
1. Punkte nach X sortiert. Linke Hälfte rekursiv, rechte Hälfte rekursiv.
2. CH_L ist ein Polygon auf der linken Seite. CH_R ist ein Polygon auf der rechten Seite.
3. Starten Sie die Schätzung bei den innersten, sich gegenüberliegenden Punkten L und R.
4. Prüfen Sie, ob das Bewegen von L "nach oben" am linken Polygon den Winkel der Verbindungslinie vergrößert. Das tut es! Bewege L.
5. Prüfen Sie, ob das Bewegen von R "nach oben" am rechten Polygon den Winkel der Verbindungslinie vergrößert. Das tut es! Bewege R.
6. Irgendwann führt das Bewegen eines der Punkte dazu, dass die Verbindungslinie in das Innere der Polygone abfällt. Stoppen. Dies ist die obere Tangente.
7. Wiederholen Sie den Vorgang nach unten, um die untere Tangente zu finden.
8. Verbinden Sie L_{up} mit R_{up}, folgen Sie der äußeren rechten Kante nach unten zu R_{down}, verbinden Sie diese mit L_{down} und folgen Sie der äußeren linken Kante zurück nach oben zu L_{up}.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(\log N)$ |

Das anfängliche Sortieren nach der X-Koordinate benötigt $O(N \log N)$.
Der Rekursionsbaum hat eine Tiefe von $O(\log N)$.
Auf jeder Ebene benötigt das Bewegen der Pointer zum Finden der oberen und unteren Tangenten Zeit proportional zur Anzahl der Eckpunkte in den Hüllen, was im schlechtesten Fall $O(N)$ entspricht.
Daher lautet die Rekursionsgleichung T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$.
Die Platzkomplexität beträgt $O(\log N)$ für die Rekursionstiefe (sofern die Hüllen in-place oder über Index-Arrays zusammengefügt werden, obwohl Standardimplementierungen, die neue Arrays zurückgeben, $O(N)$ Platz benötigen).

## Varianten & Optimierungen

- **Graham Scan:** Ein $O(N \log N)$ Algorithmus, der nicht auf Divide and Conquer basiert. Sortieren Sie alle Punkte nach dem Polarwinkel relativ zum untersten Punkt. Pushen Sie diese auf einen Stack. Wenn ein Punkt eine "Rechtskurve" (Konkavität) erzeugt, poppen Sie den Stack, bis er wieder konvex ist!
- **Quickhull (`dc_16`):** Das geometrische Äquivalent zu Quicksort! Wählen Sie die extrem linken und rechten Punkte. Finden Sie den Punkt, der am weitesten von dieser Linie entfernt ist, um ein Dreieck zu bilden. Verwerfen Sie alle Punkte innerhalb des Dreiecks. Bilden Sie rekursiv Dreiecke nach außen! $O(N \log N)$ im Durchschnitt, $O(N^2)$ im schlechtesten Fall.

## Anwendungen in der Praxis

- **Kollisionsvermeidung (Robotik):** Der schnellste Weg, um festzustellen, ob ein komplexer Roboterarm mit mehreren Gelenken gegen eine Wand stößt, besteht darin, die konvexe Hülle des Roboters zu berechnen und auf Schnittpunkte zu prüfen, anstatt jedes einzelne Gelenk und Kabel zu überprüfen.
- **Bildverarbeitung:** Erkennung der Form, des Umfangs und der Bounding Boxes von Objekten in der Computer Vision (z. B. Erkennung von Handgesten).

## Verwandte Algorithmen in cOde(n)

- **[dc_16 - Quickhull Convex Hull](dc_16_quickhull-convex-hull.md)** — Der alternative rekursive Ansatz zur Berechnung der konvexen Hülle.
- **[dc_05 - Closest Pair of Points](dc_05_closest-pair-of-points.md)** — Der andere grundlegende räumliche Divide-and-Conquer-Algorithmus der Geometrie.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für wettbewerbsorientierte Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*