# Point in Polygon (Ray-Casting)

| | |
|---|---|
| **ID** | `geometric_04` |
| **Kategorie** | geometric |
| **Komplexität (erforderlich)** | $O(V)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Point in polygon](https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm) |

## Problemstellung

Gegeben ist ein Polygon, das durch ein Array von $V$ Eckpunkten in der richtigen Reihenfolge repräsentiert wird, sowie ein einzelner Testpunkt $P$.
Bestimmen Sie, ob der Punkt $P$ strikt innerhalb des Polygons, auf dem Rand oder außerhalb des Polygons liegt. Das Polygon kann konvex oder hochkomplex/konkav sein.
Implementieren Sie den **Ray-Casting-Algorithmus (Even-Odd-Algorithmus)**.

**Eingabe:** Eine Liste von `(x, y)`-Koordinatentupeln, die die Kanten des Polygons definieren, und ein `(x, y)`-Testpunkt.
**Ausgabe:** Ein Boolean: `True`, falls der Punkt innerhalb oder auf dem Rand liegt, andernfalls `False`.

## Anwendungsbereiche

- Um zu bestimmen, ob ein Mausklick eines Benutzers innerhalb eines bestimmten UI-Elements oder eines geografischen Gebiets gelandet ist.
- Ray-Casting funktioniert bei *jedem* Polygon (konvex oder konkav), während einfachere mathematische Ansätze (wie die Prüfung, ob der Punkt links von jeder Kante liegt) NUR bei strikt konvexen Polygonen funktionieren.

## Ansatz

Stellen Sie sich vor, Sie stehen am Testpunkt $P$. Sie feuern einen Laserstrahl (einen Strahl) direkt horizontal nach rechts, der sich bis ins Unendliche erstreckt.
- Wenn Sie außerhalb eines Polygons stehen, wird der Strahl das Polygon entweder komplett verfehlen (0 Schnittpunkte) oder es durchdringen, wobei er hinein- und wieder herausgeht (2, 4 oder 6 Schnittpunkte).
- Wenn Sie INNERHALB des Polygons stehen, MUSS der Strahl den Rand des Polygons durchdringen, um zu entkommen! (1, 3 oder 5 Schnittpunkte).

**Die Even-Odd-Regel:**
Zählen Sie, wie oft der horizontale Strahl, der bei $P$ beginnt, die Kanten des Polygons schneidet.
- Wenn die Anzahl der Schnittpunkte **ungerade** (ODD) ist, liegt der Punkt INNERHALB.
- Wenn die Anzahl der Schnittpunkte **gerade** (EVEN) ist, liegt der Punkt AUSSERHALB.

**Spezialfälle & mathematische Tricks:**
1. Um Fließkomma-Arithmetik und komplexe Gleichungen für unendliche Strahlen zu vermeiden, erstellen wir einfach ein endliches Liniensegment von $P=(x, y)$ zu einem extremen Punkt weit außerhalb der Bounding Box des Polygons, z. B. Extreme=(1000000, y).
2. Wir iterieren dann durch alle benachbarten Paare von Eckpunkten im Polygon-Array (die die Kanten bilden) und verwenden unsere `do_intersect()`-Funktion aus `geometric_03`!
3. Wenn der Punkt exakt auf einer Kante liegt, versagt die Even-Odd-Logik. Wir müssen explizit prüfen, ob $P$ kollinear mit der Kante ist und innerhalb ihrer Bounding Box liegt (`on_segment`), um sofort `True` zurückzugeben.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for geometric_04: Point in Polygon (Ray Casting).

Given a simple polygon (as a list of (x, y) vertices
"""


def solve(polygon, point, m):
    """Ray-casting point-in-polygon test."""
    if m < 3:
        return False
    x, y = point
    inside = False
    j = m - 1
    for i in range(m):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        # Edge (xj, yj) -> (xi, yi). Check if the horizontal
        # ray at y=y from the point crosses this edge.
        if ((yi > y) != (yj > y)):
            # The edge straddles the ray. Compute the x
            # intersection and check it's to the right of the
            # point.
            x_int = (xj * (yi - y) + xi * (y - yj)) / (yi - yj)
            if x < x_int:
                inside = not inside
        # Also: if the point lies on this edge, count as inside.
        # We can detect collinearity by checking the cross product
        # and bounding box.
        def _on_seg(a, b, c):
            return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0])
                    and min(a[1], b[1]) <= c[1] <= max(a[1], b[1])
                    and (b[0] - a[0]) * (c[1] - a[1])
                        == (b[1] - a[1]) * (c[0] - a[0]))
        if _on_seg(polygon[i], polygon[j], point):
            return True
        j = i
    return inside
```

</details>

## Durchlauf

*(Konzeptionell)*
Quadratisches Polygon: `(0,0)`, `(10,0)`, `(10,10)`, `(0,10)`.

**Testpunkt P(5, 5):**
- Strahl: `(5,5)` bis `(INF, 5)`.
- Kante 1 `(0,0)->(10,0)`: Strahl verfehlt.
- Kante 2 `(10,0)->(10,10)`: Strahl schneidet! (Schnittpunkt exakt bei `10,5`). `count = 1`.
- Kante 3 `(10,10)->(0,10)`: Strahl verfehlt.
- Kante 4 `(0,10)->(0,0)`: Strahl verfehlt.
- Anzahl ist 1 (ungerade). Rückgabe True! ✓

**Testpunkt P(15, 5):**
- Strahl: `(15,5)` bis `(INF, 5)`.
- Verfehlt alle Kanten (da alle X-Koordinaten des Polygons \le 10 sind).
- Anzahl ist 0 (gerade). Rückgabe False! ✓

*(Hinweis: Der oben gezeigte naive Ray-Casting-Algorithmus hat einen bekannten Spezialfall: Wenn der Strahl exakt durch einen Eckpunkt verläuft, könnte dies als Schnitt mit ZWEI Kanten gezählt werden! In produktivem Code wird der Strahl oft leicht geneigt (z. B. in einem Epsilon-Winkel abgefeuert), um Treffer an Eckpunkten zu verhindern, oder es werden explizite Regeln zum Ausschluss von Endpunkten der `y`-Koordinate hinzugefügt).*

## Komplexität

| | Zeitkomplexität | Platzkomplexität |
|---|---|---|
| **Bestfall** | $O(V)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(V)$ | $O(1)$ |
| **Schlechtester Fall** | $O(V)$ | $O(1)$ |

Der Algorithmus iteriert genau einmal durch jede Kante des Polygons.
Innerhalb der Schleife benötigt die `do_intersect`-Prüfung strikt $O(1)$ Zeit.
Die gesamte Zeitkomplexität beträgt $O(V)$, wobei $V$ die Anzahl der Eckpunkte ist.
Die Platzkomplexität ist $O(1)$, da wir lediglich Schnittpunktzähler verwalten.

## Varianten & Optimierungen

- **Winding-Number-Algorithmus:** Eine Alternative zum Ray-Casting. Stellen Sie sich eine Schnur vor, die an $P$ befestigt ist und zu einem Punkt führt, der den Umfang des Polygons abläuft. Die "Winding Number" zählt, wie viele volle 360-Grad-Umdrehungen die Schnur um $P$ macht. Wenn $W=0$, liegt der Punkt außerhalb. Wenn $W \neq 0$, liegt der Punkt innerhalb. Die Winding Number behandelt den Spezialfall "Strahl trifft Eckpunkt" fehlerfrei und ist der Industriestandard für GIS-Mapping-Engines.
- **Binäre Suche für konvexe Polygone:** Wenn das Polygon strikt konvex ist, können Sie einen Mittelpunkt finden, die Eckpunkte nach Winkel sortieren und eine binäre Suche verwenden, um herauszufinden, in welches "Segment" des Polygons $P$ fällt, wodurch die Abfragezeit auf $O(log V)$ reduziert wird!

## Praxisanwendungen

- **Computergrafik:** Rendern von Vektorgrafiken (SVG) durch Bestimmung, welche Pixel innerhalb der Pfadbefehle liegen.
- **Geofencing:** Auslösen einer mobilen Benachrichtigung, wenn eine GPS-Koordinate in eine vordefinierte geometrische Zone eintritt (z. B. Betreten eines Flughafengeländes).

## Verwandte Algorithmen in cOde(n)

- **[geometric_03 - Line Intersection](geometric_03_line-segment-intersection.md)** — Die Engine, die die Ray-Casting-Prüfungen antreibt.
- **[geometric_02 - Convex Hull](geometric_02_convex-hull-graham-scan.md)** — Ein Algorithmus für die konvexe Hülle wird oft verwendet, um eine schnelle "Bounding Box / Bounding Hull" um ein komplexes Polygon zu berechnen. Wenn ein Punkt außerhalb der Hülle liegt, wissen Sie sofort, dass er außerhalb des Polygons liegt, ohne Ray-Casting ausführen zu müssen!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*