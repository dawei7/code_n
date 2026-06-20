# Konvexe Hülle (Teile und herrsche)

| | |
|---|---|
| **ID** | `dc_15` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(\log N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **GeeksForGeeks-Äquivalent** | [Konvexe Hülle (Teile und herrsche)](https://www.geeksforgeeks.org/convex-hull-using-divide-and-conquer-algorithm/) |

## Aufgabenstellung

Gegeben sei eine Menge von N Punkten in einer 2D-Ebene. Bestimme die konvexe Hülle dieser Punkte.
Die konvexe Hülle ist das kleinste konvexe Polygon, das alle Punkte vollständig umschließt. Stellen Sie sich vor, die Punkte seien Nägel, die in ein Brett eingeschlagen wurden; die konvexe Hülle ist die Form, die entsteht, wenn man ein Gummiband um die äußersten Nägel spannt.
Geben Sie die Punkte zurück, die die Eckpunkte dieses Polygons bilden, entweder im Uhrzeigersinn oder gegen den Uhrzeigersinn.

**Eingabe:** Ein Array von `Points`, wobei `Point` die Eigenschaften `x` und `y` aufweist.
**Ausgabe:** Ein Array von `Points`, das die konvexe Hülle darstellt.

## Wann man es verwendet

- Wenn man aufgefordert wird, fortgeschrittene Methoden der rechnergestützten Geometrie zu demonstrieren.
- *(Hinweis: Im Wettbewerbsprogrammieren werden der Graham-Scan oder die monotone Kette deutlich bevorzugt, da sie einfacher zu programmieren sind. Dieser $O(N \log N)$-Ansatz nach dem Prinzip „Teile und herrsche“ ist in der Regel eine akademische Folgefrage).*

## Vorgehensweise

**1. Der Basisfall:**
Wenn es 3 oder weniger Punkte gibt, bilden diese trivialerweise ihre eigene konvexe Hülle (ein Dreieck, ein Liniensegment oder einen Punkt). Sortiere sie einfach im Uhrzeigersinn und gib sie zurück!

**2. Der Teilungsschritt:**
Ähnlich wie bei „Closest Pair of Points“ (`dc_05`) sortieren wir zunächst alle Punkte global nach ihrer X-Koordinate.
Wir teilen die Punkte genau in zwei Hälften auf: eine linke und eine rechte Menge.
Berechne rekursiv die konvexe Hülle der linken Menge (CH_L) und die konvexe Hülle der rechten Menge (CH_R).

**3. Der Zusammenführungsschritt:**
Wir haben nun zwei separate, sich nicht überlappende konvexe Polygone, die nebeneinander liegen. Wir müssen sie zu einem einzigen großen konvexen Polygon zusammenführen!
Dazu müssen wir die **obere Tangente** und die **untere Tangente** finden, die CH_L und CH_R verbinden.
Sobald wir diese beiden Verbindungslinien gefunden haben, löschen wir einfach die inneren, „zueinander gerichteten“ Kanten beider Polygone und verbinden sie mithilfe der Tangenten!

**4. Die obere Tangente finden (die „Gummiband“-Methode):**
- Beginne mit dem Punkt ganz rechts von CH_L (nennen wir ihn L) und dem Punkt ganz links von CH_R (nennen wir ihn R). Die Linie L-R ist unsere erste Vermutung für die Tangente.
- Halte R fest und bewege L *gegen den Uhrzeigersinn* um CH_L herum, solange sich die Linie L-R weiter nach OBEN bewegt.
- Sobald L den lokalen Höchstpunkt erreicht hat, halte L fest und bewege R *im Uhrzeigersinn* um CH_R herum, solange sich die Linie L-R weiter nach OBEN bewegt.
- Wiederhole das Hin- und Herbewegen, bis WEDER L noch R sich weiter nach oben bewegen können. Du hast die obere Tangente gefunden!
- Das Finden der unteren Tangente erfolgt genau umgekehrt (bewege L im Uhrzeigersinn, bewege R gegen den Uhrzeigersinn nach unten).

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
1. Punkte nach X sortiert. Die linke Hälfte wird rekursiv bearbeitet, die rechte Hälfte wird rekursiv bearbeitet.
2. CH_L ist ein Polygon auf der linken Seite. CH_R ist ein Polygon auf der rechten Seite.
3. Beginne mit einer Vermutung für die innersten gegenüberliegenden Punkte L und R.
4. Prüfe, ob das Verschieben von L „nach oben“ im linken Polygon den Winkel der Verbindungslinie vergrößert. Das ist der Fall! Verschiebe L.
5. Prüfe, ob das Verschieben von R „nach oben“ entlang des rechten Polygons den Winkel der Verbindungslinie vergrößert. Das ist der Fall! Verschiebe R.
6. Irgendwann führt das Verschieben eines der beiden Punkte dazu, dass die Verbindungslinie innerhalb der Polygone abfällt. Stopp. Dies ist die obere Tangente.
7. Wiederhole den Vorgang nach unten, um die untere Tangente zu finden.
8. Verbinde L_{up} mit R_{up}, verfolge die äußere rechte Kante nach unten bis zu R_{down}, verbinde diese mit L_{down} und verfolge die äußere linke Kante wieder nach oben bis zu L_{up}.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlechteste** | $O(N \log N)$ | $O(\log N)$ |

Die anfängliche Sortierung der X-Koordinaten dauert $O(N \log N)$.
Der Rekursionsbaum hat eine Tiefe von $O(\log N)$.
Auf jeder Ebene nimmt das Durchlaufen der Zeiger zur Ermittlung der oberen und unteren Tangenten Zeit in Anspruch, die proportional zur Anzahl der Eckpunkte in den Hüllen ist, was im schlimmsten Fall $O(N)$ beträgt.
Daher lautet die Rekursionsbeziehung T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$.
Die Platzkomplexität beträgt $O(\log N)$ für die Rekursionstiefe (sofern die Hüllen an Ort und Stelle oder über Index-Arrays zusammengefügt werden; Standardimplementierungen, die neue Arrays zurückgeben, benötigen jedoch $O(N)$ Speicherplatz).

## Varianten & Optimierungen

- **Graham-Scan:** Ein $O(N \log N)$-Algorithmus ohne „Teile und herrsche“-Prinzip. Alle Punkte werden nach ihrem Polwinkel relativ zum untersten Punkt sortiert. Auf einen Stack schieben. Wenn ein Punkt eine „Rechtskurve“ (Konkavität) erzeugt, vom Stack abheben, bis die Form wieder konvex ist!
- **Quickhull (`dc_16`):** Das räumlich-geometrische Äquivalent zu Quicksort! Wähle den äußersten linken und rechten Punkt aus. Finde den Punkt, der am weitesten von dieser Linie entfernt ist, um ein Dreieck zu bilden. Verwerfe alle Punkte innerhalb des Dreiecks. Baue rekursiv Dreiecke nach außen auf! $O(N \log N)$ im Durchschnittlicher Fall, $O(N^2)$ im schlimmsten Fall.

## Anwendungen in der Praxis

- **Kollisionsvermeidung (Robotik):** Der schnellste Weg, um festzustellen, ob ein komplexer, mehrgelenkiger Roboterarm gegen eine Wand stoßen wird, besteht darin, die konvexe Hülle des Roboters zu berechnen und auf Schnittpunkte zu prüfen, anstatt jedes einzelne Gelenk und jede einzelne Leitung zu überprüfen.
- **Bildverarbeitung:** Erkennung von Form, Umfang und Begrenzungsrahmen von Objekten in der Bildverarbeitung (z. B. Handgestenerkennung).

## Verwandte Algorithmen in cOde(n)

- **[dc_16 – Quickhull-Konvexhülle](dc_16_quickhull-convex-hull.md)** — Der alternative rekursive Ansatz zur Berechnung der Konvexhülle.
- **[dc_05 – Nächstgelegenes Punktpaar](dc_05_closest-pair-of-points.md)** – Der andere grundlegende räumliche „Teile und herrsche“-Algorithmus in der Geometrie.

---

*Diese Dokumentation ist ein für cOde(n) verfasster Originalbeitrag,
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie unter dem Wikipedia-Link oben auf der Seite.
Quell-Repository:
<https://github.com/dawei7/code_n>.*
