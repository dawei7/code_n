# Quickhull (Konvexe Hülle)

| | |
|---|---|
| **ID** | `dc_16` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(\log N)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Interview-Relevanz** | 2/10 |
| **Wikipedia** | [Quickhull](https://en.wikipedia.org/wiki/Quickhull) |

## Problemstellung

Gegeben ist eine Menge von N Punkten in einer 2D-Ebene. Gesucht ist die konvexe Hülle (Convex Hull) dieser Punkte.
Die konvexe Hülle ist das kleinste konvexe Polygon, das alle Punkte vollständig umschließt.
*Bedingung:* Lösen Sie dies mit dem Quickhull-Algorithmus.

**Eingabe:** Ein Array von `Points`, wobei `Point` die Eigenschaften `x` und `y` besitzt.
**Ausgabe:** Ein Array von `Points`, das die konvexe Hülle repräsentiert.

## Wann man es verwendet

- Um das räumliche geometrische Äquivalent zu Quicksort zu verstehen.
- Während die reine Divide-and-Conquer-Methode (`dc_15`) Punkte willkürlich anhand der X-Koordinate in der Mitte teilt, verwendet Quickhull Extrempunkte als "Pivots", um geometrisch große Mengen innerer Punkte sofort zu verwerfen.

## Ansatz

**1. Die initiale "Pivot"-Aufteilung:**
Finden Sie den Punkt mit der minimalen X-Koordinate (P_{min}) und den Punkt mit der maximalen X-Koordinate (P_{max}).
Da dies die horizontal am weitesten entfernten Punkte sind, MÜSSEN sie mathematisch gesehen Eckpunkte der konvexen Hülle sein!
Zeichnen Sie eine Linie zwischen ihnen. Diese Linie teilt alle verbleibenden Punkte in zwei Mengen: Punkte "oberhalb" der Linie und Punkte "unterhalb" der Linie.

**2. Die geometrische "Partitionierung" (Verwerfen von Punkten):**
Betrachten wir die Punkte "oberhalb" der Linie.
Finden Sie den Punkt P_{far} in dieser Menge, der den **größten senkrechten Abstand** zur Linie P_{min} - P_{max} aufweist.
Da P_{far} der absolute Scheitelpunkt der Kurve auf dieser Seite der Linie ist, MUSS er ebenfalls ein Eckpunkt der konvexen Hülle sein!
Nun haben wir ein Dreieck, das durch P_{min}, P_{max} und P_{far} gebildet wird.
*Die magische Optimierung:* Jeder Punkt, der sich aktuell INNERHALB dieses Dreiecks befindet, kann unmöglich auf der äußeren Begrenzung der konvexen Hülle liegen. Wir können alle diese Punkte dauerhaft verwerfen!

**3. Der rekursive Schritt (Decrease and Conquer):**
Die ursprüngliche Linie P_{min} - P_{max} wurde nun durch zwei neue äußere Linien ersetzt, die ein "Zelt" bilden:
Linie 1: P_{min} zu P_{far}
Linie 2: P_{far} zu P_{max}

Wir rufen unsere Quickhull-Funktion rekursiv zweimal auf!
- Einmal für die Punkte, die "außerhalb" von Linie 1 liegen.
- Einmal für die Punkte, die "außerhalb" von Linie 2 liegen.
Die Rekursion endet, wenn keine Punkte mehr "außerhalb" einer gegebenen Linie liegen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_16: Quickhull Convex Hull.

Given n points in the plane, return the vertices of
"""


def _line_side(p1, p2, p):
    """+1 / -1 / 0 for the side of p w.r.t. the line p1->p2."""
    val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

def _line_dist(p1, p2, p):
    return abs((p[1] - p1[1]) * (p2[0] - p1[0]) -
               (p2[1] - p1[1]) * (p[0] - p1[0]))

def solve(points, n):
    """Convex hull via Quickhull. Return as a Python set."""
    if n < 3:
        return set(points)
    # Find leftmost and rightmost points.
    min_x = max_x = 0
    for i in range(1, n):
        if points[i][0] < points[min_x][0]:
            min_x = i
        if points[i][0] > points[max_x][0]:
            max_x = i
    a, b = points[min_x], points[max_x]
    hull = set()

    # quickHull re-scans the full set and selects points on
    # `side` of the line p1->p2, exactly like the GfG reference
    # implementation. Average O(n log n), worst O(n^2).
    def quickHull(pts, p1, p2, side):
        ind = -1
        max_dist = 0
        for i, p in enumerate(pts):
            if _line_side(p1, p2, p) == side:
                d = _line_dist(p1, p2, p)
                if d > max_dist:
                    ind = i
                    max_dist = d
        if ind == -1:
            hull.add(p1)
            hull.add(p2)
            return
        P = pts[ind]
        quickHull(pts, P, p1, -_line_side(P, p1, p2))
        quickHull(pts, P, p2, -_line_side(P, p2, p1))

    quickHull(points, a, b, 1)
    quickHull(points, a, b, -1)
    return hull
```

</details>

## Ablauf

*(Konzeptionell)*
1. Finden Sie P_{min} (ganz links) und P_{max} (ganz rechts). Fügen Sie diese zur `hull` hinzu.
2. Zeichnen Sie eine Linie zwischen ihnen. Teilen Sie alle anderen Punkte in `left_set` (oberhalb) und `right_set` (unterhalb) auf.
3. **Verarbeitung von `left_set`:**
   - Finden Sie den Punkt P_{top} mit der größten vertikalen Höhe relativ zur Linie. Fügen Sie P_{top} zur `hull` hinzu.
   - Die Linie P_{min} \rightarrow P_{max} wird durch ein Dreieck ersetzt.
   - Alle Punkte innerhalb des Dreiecks (unterhalb von P_{top}) werden dauerhaft verworfen!
   - Wir erstellen eine neue Menge `s1` für Punkte außerhalb der Linie P_{min} \rightarrow P_{top}.
   - Wir erstellen eine neue Menge `s2` für Punkte außerhalb der Linie P_{top} \rightarrow P_{max}.
   - Rekursion auf `s1` und `s2`!
4. **Verarbeitung von `right_set`:**
   - Gleicher Prozess, aber Suche nach P_{bottom}.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(N)$ |

Genau wie bei Quicksort gilt: Wenn der Pivot-Punkt (P_{far}) die verbleibenden Punkte relativ gleichmäßig aufteilt (ein "fettes" Dreieck, das viele Punkte verwirft), beträgt die Rekursionstiefe $O(\log N)$ und der Aufwand pro Ebene $O(N)$, was zu einer durchschnittlichen Zeitkomplexität von $O(N \log N)$ führt.
Wenn jedoch alle Punkte perfekt auf einem Kreis angeordnet sind, werden durch die Dreiecke niemals Punkte verworfen! Der Algorithmus verkommt dazu, pro Ebene nur 1 Punkt zu verarbeiten, was im schlimmsten Fall zu einer Zeitkomplexität von $O(N^2)$ führt.
Die Platzkomplexität beträgt im Durchschnitt $O(\log N)$ für den Rekursions-Stack.

## Varianten & Optimierungen

- **Graham Scan:** Wie immer garantiert der Graham Scan eine Zeitkomplexität von $O(N \log N)$ im schlechtesten Fall, indem die Punkte zuerst nach ihrem Polarwinkel sortiert werden, wodurch die Anfälligkeit von Quickhull für den schlechtesten Fall vollständig vermieden wird.
- **Chan's Algorithmus:** Ein verblüffender Algorithmus, der mathematisch Graham Scan und Jarvis March kombiniert, um eine strikte Zeitkomplexität von $O(N \log H)$ zu erreichen, wobei H die Anzahl der Punkte ist, die tatsächlich auf der Hülle liegen!

## Anwendungen in der Praxis

- **Computergrafik (Hitboxen):** Erzeugung der vereinfachten 2D-konvexen Kollisions-Hitbox für ein hochkomplexes Sprite. Quickhull ist in der Praxis bei zufällig verteilten Punkten im Allgemeinen schneller als Graham Scan, da es aggressiv und fast sofort innere Pixel verwirft.

## Verwandte Algorithmen in cOde(n)

- **[dc_15 - Convex Hull Divide & Conquer](dc_15_convex-hull-divide-and-conquer.md)** — Die strikte $O(N \log N)$ rekursive Merge-Methode.
- **[sort_02 - Quick Sort](../sorting/sort_02_quick-sort.md)** — Das 1D-Array-Analogon, das unter exakt derselben $O(N^2)$ Pivot-Anfälligkeit im schlechtesten Fall leidet.

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*