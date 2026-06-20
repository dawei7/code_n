# Punkt im Polygon (Ray-Casting)

| | |
|---|---|
| **ID** | `geometric_04` |
| **Kategorie** | Geometrie |
| **Komplexität (erforderlich)** | $O(V)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Punkt in einem Polygon](https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm) |

## Aufgabenstellung

Gegeben sei ein Polygon, das durch ein Array von V Knoten in der Reihenfolge ihrer Anordnung dargestellt wird, sowie ein einzelner Testpunkt P.
Bestimme, ob der Punkt P streng innerhalb des Polygons, auf der Grenze oder außerhalb des Polygons liegt. Das Polygon kann konvex oder sehr komplex/konkav sein.
Implementiere den **Ray-Casting-Algorithmus (Even-Odd)**.

**Eingabe:** Eine Liste von `(x, y)` Koordinatentupeln, die die Polygonkanten definieren, und ein `(x, y)` Testpunkt.
**Ausgabe:** Ein Boolescher Wert: `True`, wenn der Punkt innerhalb des Polygons oder auf der Grenze liegt, andernfalls `False`.

## Wann wird es verwendet?

- Um festzustellen, ob der Mausklick eines Benutzers innerhalb eines bestimmten UI-Elements oder eines geografischen Kartenbereichs gelandet ist.
- Ray-Casting funktioniert bei *jedem* Polygon (konvex oder konkav), während einfachere mathematische Verfahren (wie die Überprüfung, ob der Punkt „links“ von jeder Kante liegt) NUR bei streng konvexen Polygonen funktionieren.

## Vorgehensweise

Stellen Sie sich vor, Sie stehen am Testpunkt P. Sie feuern einen Laserstrahl (einen Strahl) direkt horizontal nach rechts ab, der sich bis ins Unendliche erstreckt.
- Wenn Sie außerhalb eines Polygons stehen, wird der Strahl das Polygon entweder vollständig verfehlen (0 Schnittpunkte) oder es durchdringen, also eintreten und wieder austreten. (2, 4 oder 6 Schnittpunkte).
- Wenn du INNERHALB des Polygons stehst, MUSS der Strahl die Polygongrenze durchdringen, um hinauszugelangen! (1, 3 oder 5 Schnittpunkte).

**Die Gerade-Ungerade-Regel:**
Zähle, wie oft der von P ausgehende horizontale Strahl die Kanten des Polygons schneidet.
- Ist die Anzahl der Schnittpunkte **UNGERADE**, befindet sich der Punkt INNERHALB.
- Ist die Anzahl der Schnittpunkte **GERADE**, befindet sich der Punkt AUSSERHALB.

**Grenzfälle & mathematische Tricks:**
1. Um Fließkommaarithmetik und komplexe Gleichungen für unendliche Strahlen zu vermeiden, erstellen wir einfach ein endliches Liniensegment von P=(x, y) zu einem Extrempunkt weit außerhalb des Begrenzungsrahmens des Polygons, z. B. Extreme=(1000000, y).
2. Anschließend durchlaufen wir alle benachbarten Eckpunktpaare im Polygon-Array (die dessen Kanten bilden) und verwenden unsere `do_intersect()`-Funktion aus `geometric_03`!
3. Liegt der Punkt genau auf einer Kante, versagt die „Even-Odd“-Logik. Wir müssen explizit prüfen, ob P kollinear zur Kante und innerhalb ihres Begrenzungsraums liegt (`on_segment`), um sofort „True“ zurückzugeben.

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
Quadratisches Polygon: `(0,0)`, `(10,0)`, `(10,10)`, `(0,10)`.

**Testpunkt P(5, 5):**
- Strahl: `(5,5)` nach `(INF, 5)`.
- Kante 1 `(0,0)->(10,0)`: Der Strahl verfehlt die Kante.
- Kante 2 `(10,0)->(10,10)`: Der Strahl kreuzt die Kante! (Schneidet genau bei `10,5`). `count = 1`.
- Kante 3 `(10,10)->(0,10)`: Strahl verfehlt.
- Kante 4 `(0,10)->(0,0)`: Strahl verfehlt.
- Anzahl ist 1 (UNGERADE). True zurückgeben! ✓

**Testpunkt P(15, 5):**
- Strahl: `(15,5)` nach `(INF, 5)`.
- Verfehlt alle Kanten (da alle X-Koordinaten des Polygons \le 10 sind).
- Zählstand ist 0 (GERADE). „False“ zurückgeben! ✓

*(Hinweis: Der oben gezeigte naive Ray-Casting-Algorithmus weist einen bekannten Randfall auf: Wenn der Strahl genau durch einen Scheitelpunkt verläuft, könnte dies als Schnitt mit ZWEI Kanten gewertet werden! Im Produktionscode wird der Strahl oft leicht geneigt (z. B. unter einem epsilon-Winkel abgefeuert), um Knoten-Treffer zu vermeiden, oder es werden explizite Ausschlussregeln für `y`-Koordinaten-Endpunkte hinzugefügt).*

## Komplexität

| | Zeit | Speicher |
|---|---|---|
| **Bestfall** | $O(V)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(V)$ | $O(1)$ |
| **Schlechtester Fall** | $O(V)$ | $O(1)$ |

Der Algorithmus durchläuft jede Kante des Polygons genau einmal.
Innerhalb der Schleife benötigt die `do_intersect`-Prüfung streng $O(1)$ Zeit.
Die gesamte Zeitkomplexität beträgt $O(V)$, wobei V die Anzahl der Eckpunkte ist.
Die Platzkomplexität beträgt $O(1)$, da wir lediglich Schnittpunktzähler verwalten.

## Varianten & Optimierungen

- **Winding-Number-Algorithmus:** Eine Alternative zum Ray-Casting. Stellen Sie sich eine Schnur vor, die an P befestigt ist und sich bis zu einem Punkt erstreckt, der den Umfang des Polygons durchläuft. Die „Winding-Number“ zählt, wie viele vollständige 360-Grad-Umwicklungen die Schnur um P vollführt. Ist W = 0, liegt der Punkt außerhalb. Ist W ≠ 0, liegt der Punkt innerhalb. Die Winding-Number behandelt den Randfall „Strahl trifft einen Eckpunkt“ einwandfrei und ist der Industriestandard für GIS-Kartierungs-Engines.
- **Binary-Search nur für konvexe Polygone:** Ist das Polygon streng konvex, kann man einen Mittelpunkt ermitteln, die Eckpunkte nach dem Winkel sortieren und mithilfe der binären Suche herausfinden, in welchen „Schnitt“ des Polygons P der Punkt fällt, wodurch sich die Abfragezeit auf $O(log V)$ reduziert!

## Praktische Anwendungen

- **Computergrafik:** Rendern von Vektorgrafiken (SVG) durch Ermittlung der Pixel, die innerhalb der Pfadbefehle liegen.
- **Geofencing:** Auslösen einer mobilen Benachrichtigung, wenn eine GPS-Koordinate eine vorab festgelegte geometrische Zone überschreitet (z. B. beim Betreten eines Flughafens).

## Verwandte Algorithmen in cOde(n)

- **[geometric_03 – Linienschnitt](geometric_03_line-segment-intersection.md)** — Die Engine, die die Ray-Casting-Prüfungen unterstützt.
- **[geometric_02 – Konvexhülle](geometric_02_convex-hull-graham-scan.md)** — Ein Konvexhüllen-Algorithmus wird häufig verwendet, um schnell eine „Bounding Box / Bounding Hull“ um ein komplexes Polygon zu berechnen. Befindet sich ein Punkt außerhalb der Hülle, weiß man sofort, dass er außerhalb des Polygons liegt, ohne Ray-Casting ausführen zu müssen!

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
