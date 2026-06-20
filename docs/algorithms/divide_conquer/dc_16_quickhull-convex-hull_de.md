# Quickhull (Konvexhülle)

| | |
|---|---|
| **ID** | `dc_16` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(\log N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Quickhull](https://en.wikipedia.org/wiki/Quickhull) |

## Aufgabenstellung

Gegeben sei eine Menge von N Punkten in einer 2D-Ebene. Bestimme die konvexe Hülle dieser Punkte.
Die konvexe Hülle ist das kleinste konvexe Polygon, das alle Punkte vollständig umschließt.
*Einschränkung:* Lösen Sie diese Aufgabe mithilfe des Quickhull-Algorithmus.

**Eingabe:** Ein Array von `Points`, wobei `Point` die Eigenschaften `x` und `y` aufweist.
**Ausgabe:** Ein Array von `Points`, das die konvexe Hülle darstellt.

## Wann man es verwendet

- Um das räumlich-geometrische Äquivalent von Quicksort zu verstehen.
- Während die reine „Teile und herrsche“-Methode (`dc_15`) Punkte willkürlich anhand der X-Koordinate in der Mitte teilt, nutzt Quickhull Extrempunkte als „Pivots“, um große Teile der inneren Punkte geometrisch sofort auszusortieren.

## Vorgehensweise

**1. Die anfängliche Teilung anhand der „Pivots“:**
Finde den Punkt mit der kleinsten X-Koordinate (P_{min}) und den Punkt mit der größten X-Koordinate (P_{max}).
Da dies die horizontal absolut am weitesten entfernten Punkte sind, MÜSSEN sie mathematisch gesehen Eckpunkte der konvexen Hülle sein!
Zeichne eine Gerade zwischen ihnen. Diese Gerade teilt alle verbleibenden Punkte in zwei Mengen auf: Punkte „oberhalb“ der Geraden und Punkte „unterhalb“ der Geraden.

**2. Die geometrische „Partition“ (Punkte verwerfen):**
Konzentrieren wir uns auf die Punkte „oberhalb“ der Geraden.
Finde in dieser Menge den Punkt P_{far}, der den **größten senkrechten Abstand** zur Linie P_{min} – P_{max} aufweist.
Da P_{far} der absolute Höchstwert der Kurve auf dieser Seite der Linie ist, MUSS er ebenfalls ein Eckpunkt der konvexen Hülle sein!
Nun haben wir ein Dreieck, das durch P_{min}, P_{max} und P_{far} gebildet wird.
*Die magische Optimierung:* Jeder Punkt, der sich derzeit INNERHALB dieses Dreiecks befindet, kann unmöglich auf der Außengrenze der konvexen Hülle liegen. Wir können sie alle endgültig verwerfen!

**3. Der rekursive Schritt (Reduzieren und Erobern):**
Die ursprüngliche Linie P_{min} – P_{max} wurde nun durch zwei neue Außenlinien ersetzt, die ein „Zelt“ bilden:
Linie 1: P_{min} bis P_{far}
Linie 2: P_{far} bis P_{max}

Wir rufen unsere Quickhull-Funktion rekursiv zweimal auf!
- Einmal für die Punkte, die „außerhalb“ von Linie 1 liegen.
- Einmal für die Punkte, die „außerhalb“ von Linie 2 liegen.
Die Rekursion endet, wenn keine Punkte mehr „außerhalb“ einer bestimmten Linie liegen.

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
1. Finde P_{min} (ganz links) und P_{max} (ganz rechts). Füge sie zu `hull` hinzu.
2. Zeichne eine Linie zwischen ihnen. Teile alle anderen Punkte in `left_set` (oberhalb) und `right_set` (unterhalb) auf.
3. **Schritt `left_set`:**
   - Finde den Punkt P_{top} mit der höchsten vertikalen Höhe relativ zur Linie. Füge P_{top} zu `hull` hinzu.
   - Die Linie P_{min} \rightarrow P_{max} wird durch ein Dreieck ersetzt.
   - Alle Punkte innerhalb des Dreiecks (unterhalb von P_{top}) werden endgültig verworfen!
   - Wir erstellen eine neue Menge `s1` für Punkte außerhalb der Linie P_{min} \rightarrow P_{top}.
   - Wir erstellen eine neue Menge `s2` für Punkte außerhalb der Linie P_{top} \rightarrow P_{max}.
   - Rekursion auf `s1` und `s2`!
4. **Verfahren `right_set`:**
   - Gleiches Verfahren, jedoch zur Ermittlung von P_{bottom}.

## Komplexität

| | Zeit | Speicher |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlimmster Fall** | $O(N^2)$ | $O(N)$ |

Genau wie bei Quicksort gilt: Wenn der Pivot-Punkt (P_{far}) die verbleibenden Punkte relativ gleichmäßig aufteilt (ein „dickes“ Dreieck, das viele Punkte aussortiert), beträgt die Rekursionstiefe $O(\log N)$ und der Aufwand pro Ebene beträgt $O(N)$, was zu einer durchschnittlichen Laufzeit von $O(N \log N)$ führt.
Sind jedoch alle Punkte perfekt kreisförmig angeordnet, werden durch die Dreiecke niemals Punkte verworfen! Der Algorithmus läuft dann darauf hinaus, dass pro Ebene 1 Punkt verarbeitet wird, was zu einer Katastrophe führt, bei der die $O(N^2)$-Zeitgrenze im schlimmsten Fall überschritten wird.
Die Platzkomplexität beträgt im Durchschnittlicher Fall $O(\log N)$ für den Rekursionsstapel.

## Varianten & Optimierungen

- **Graham-Scan:** Wie immer garantiert der Graham-Scan eine Laufzeit von $O(N \log N)$ im schlimmsten Fall, indem er die Punkte zunächst nach Polarkoordinaten sortiert und so die Schwachstelle des Quickhull-Algorithmus im schlimmsten Fall vollständig umgeht.
- **Chan-Algorithmus:** Ein verblüffender Algorithmus, der Graham-Scan und Jarvis-March mathematisch kombiniert, um eine strenge $O(N log H)$-Zeit zu erreichen, wobei H die Anzahl der Punkte ist, die tatsächlich auf der Hülle landen!

## Praktische Anwendungen

- **Computergrafik (Hitboxen):** Erzeugung einer vereinfachten konvexen 2D-Kollisions-Hitbox für ein hochkomplexes Sprite. Quickhull ist in der Praxis bei zufällig verteilten Punkten im Allgemeinen schneller als der Graham-Scan, da es innere Pixel fast augenblicklich aggressiv verworfen.

## Verwandte Algorithmen in cOde(n)

- **[dc_15 – Convex Hull Divide & Conquer](dc_15_convex-hull-divide-and-conquer.md)** — Die rekursive Merge-Methode mit strikter $O(N \log N)$-Laufzeit.
- **[sort_02 – Quick Sort](../sorting/sort_02_quick-sort.md)** – Das 1D-Array-Analogon, das genau dieselbe $O(N^2)$ Pivot-Schwachstelle im Worst-Case-Szenario aufweist.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
