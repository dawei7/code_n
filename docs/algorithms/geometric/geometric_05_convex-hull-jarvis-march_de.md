# Convex Hull (Jarvis March / Gift Wrapping)

| | |
|---|---|
| **ID** | `geometric_05` |
| **Category** | geometric |
| **Complexity (required)** | $O(N * H)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Gift wrapping algorithm](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm) |

## Problem statement

Gegeben ist ein Array von $N$ Punkten in einer 2D-Ebene. Gesucht ist die **Convex Hull** (konvexe Hülle): das kleinste konvexe Polygon, das alle Punkte vollständig umschließt.
Während der Graham Scan (`geo_02`) eine strikte Zeitkomplexität von $O(N \log N)$ aufweist, implementieren wir hier den **Jarvis March** Algorithmus (oft auch als Gift Wrapping Algorithmus bezeichnet).
Dieser Algorithmus hat eine Zeitkomplexität von $O(N \cdot H)$, wobei $H$ die Anzahl der Punkte ist, die tatsächlich auf der Hülle liegen. Dies macht ihn zu einem ausgabesensitiven Algorithmus!

**Input:** Eine Liste von `(x, y)` Koordinaten-Tupeln.
**Output:** Eine Liste von `(x, y)` Tupeln, welche die Eckpunkte der Convex Hull darstellen.

## Wann sollte man ihn verwenden?

- Wenn Sie stark vermuten, dass die Convex Hull im Vergleich zur Gesamtzahl der Punkte nur sehr wenige Eckpunkte besitzt (z. B. $10^6$ Punkte, die dicht in einem Quadrat gepackt sind. $H$ wäre 4, also läuft der Jarvis March in $O(4N)$, was den Graham Scan mit $O(N \log N)$ massiv schlägt).
- Er ist konzeptionell wesentlich einfacher zu implementieren als der Graham Scan, da er keine initiale Sortierung und keine Stack-Logik erfordert.

## Ansatz

Stellen Sie sich vor, Sie fahren mit einem Auto um den Umfang der Punktwolke herum.
Sie beginnen am absolut linkesten Punkt (niedrigster X-Wert). Sie wissen, dass dieser Punkt zwingend auf der Convex Hull liegen MUSS.
Nun möchten Sie Ihr Auto so drehen, dass es auf den *nächsten* Eckpunkt der Hülle zeigt. Um dies zu tun, betrachten Sie jeden einzelnen Punkt in der Wolke und wählen denjenigen aus, der Sie dazu zwingt, die größtmögliche **Rechtskurve** zu machen!
Sobald Sie diesen Punkt gefunden haben, fahren Sie zu ihm und wiederholen den Vorgang, bis Sie wieder an Ihrem Startpunkt angekommen sind.

1. **Anker finden:** Finden Sie den linkesten Punkt. Sei `current_point` dieser Anker.
2. **Hülle initialisieren:** Fügen Sie `current_point` zur Hülle hinzu.
3. **Die Schleife:** Wir nehmen an, der nächste Punkt auf der Hülle sei `next_point = points[0]`.
4. **Scan:** Iterieren Sie durch jeden Punkt `p` im Array:
   - Verwenden Sie das **Kreuzprodukt** (Cross Product), um die Orientierung von `current_point -> next_point -> p` zu prüfen.
   - Wenn `p` weiter rechts (im Gegenuhrzeigersinn) liegt als unser aktueller `next_point`-Tipp, aktualisieren Sie `next_point = p`.
   - *(Sonderfall: Wenn `p` und `next_point` perfekt kollinear mit `current_point` sind, wählen Sie denjenigen, der weiter entfernt ist).*
5. **Aktualisierung:** Nach der Überprüfung aller Punkte ist mathematisch garantiert, dass `next_point` der nächste Eckpunkt auf der Hülle ist. Fügen Sie ihn der Hülle hinzu.
6. Setzen Sie `current_point = next_point`. Wiederholen Sie die Schritte 3-6, bis `next_point` unserem ursprünglichen Anker entspricht.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for geometric_05: Convex Hull (Jarvis March).

Compute the convex hull of n points using Jarvis
"""


def solve(points, n):
    """Convex hull via Jarvis March (gift wrapping)."""
    if n < 3:
        return sorted(points)
    # Find the leftmost point.
    leftmost = min(range(n), key=lambda i: (points[i][0], points[i][1]))
    hull = []
    cur = leftmost
    while True:
        hull.append(cur)
        # Find the next hull vertex: the most counterclockwise
        # point with respect to the current edge.
        candidate = None
        for j in range(n):
            if j == cur:
                continue
            if candidate is None:
                candidate = j
                continue
            # We want (candidate - cur) to be the most
            # counterclockwise of all points. Cross product
            # positive means j is more CCW than candidate.
            cross = ((points[candidate][0] - points[cur][0])
                     * (points[j][1] - points[cur][1])
                     - (points[candidate][1] - points[cur][1])
                     * (points[j][0] - points[cur][0]))
            if cross < 0:
                candidate = j
        # If the next candidate is the leftmost, we're done.
        if candidate == leftmost:
            break
        cur = candidate
        # Safety: avoid infinite loop on degenerate inputs.
        if len(hull) > n:
            break
    return [points[i] for i in hull]
```

</details>

## Walk-through

*(Konzeptionell)*
Punkte: `A(0,0)`, `B(1,1)`, `C(2,0)`, `D(1,2)`

1. **Linkester Punkt:** `A(0,0)`. `hull = [A]`.
2. **Aktuell:** `A`. Tipp `next_idx = B`.
   - Prüfe `C`: `A -> B -> C` ergibt eine Rechtskurve. `C` liegt weiter "außen" als `B`. Aktualisiere `next_idx = C`.
   - Prüfe `D`: `A -> C -> D` ergibt eine Linkskurve. Behalte `next_idx = C`.
3. **Bewegung:** `next_idx` ist `C`. `hull = [A, C]`.
4. **Aktuell:** `C`. Tipp `next_idx = A`.
   - Prüfe `B`: `C -> A -> B` ergibt eine Linkskurve. Behalte `next_idx = A`.
   - Prüfe `D`: `C -> A -> D` ergibt eine Rechtskurve. `D` liegt weiter außen! Aktualisiere `next_idx = D`.
5. **Bewegung:** `next_idx` ist `D`. `hull = [A, C, D]`.
6. **Aktuell:** `D`. Tipp `next_idx = A`.
   - Prüfe `B`: `D -> A -> B` ergibt eine Linkskurve. Behalte `A`.
   - Prüfe `C`: `D -> A -> C` ergibt eine Linkskurve. Behalte `A`.
7. **Bewegung:** `next_idx` ist `A`. Dies ist der Startpunkt! Die Schleife bricht ab!
Ergebnis: `[A, C, D]`. ✓ (`B` lag strikt im Inneren!).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N * H)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(1)$ |

*Wobei H die Anzahl der Eckpunkte auf der Hülle ist.*
Wenn jeder einzelne Punkt auf der Hülle liegt (z. B. wenn sie einen riesigen Kreis bilden), läuft die Schleife $N$-mal durch und prüft jedes Mal $N$ Punkte, was zu $O(N^2)$ führt. Dies ist schlechter als der Graham Scan!
Wenn $H$ jedoch klein ist, läuft er unglaublich schnell.
Die Platzkomplexität beträgt strikt $O(1)$ an zusätzlichem Speicher (exklusive des Ausgabe-Arrays), was ihn sehr speichereffizient macht.

## Varianten & Optimierungen

- **Chan's Algorithm:** Der ultimative Algorithmus für die Convex Hull. Er kombiniert den Graham Scan und den Jarvis March, um eine ausgabesensitive Zeitkomplexität von exakt $O(N \log H)$ zu erreichen. Er funktioniert, indem die Punkte in Blöcke der Größe $H$ unterteilt werden, der Graham Scan auf jedem Block ausgeführt wird und anschließend der Jarvis March auf den resultierenden Teil-Hüllen angewendet wird!

## Anwendungen in der Praxis

- **Robotik:** Bestimmung der absoluten äußeren Begrenzung eines Schwarms von Robotern, um die Mindestgröße eines umschließenden Netzes zu berechnen.

## Verwandte Algorithmen in cOde(n)

- **[geometric_02 - Graham Scan](geometric_02_convex-hull-graham-scan.md)** — Das $O(N \log N)$ Gegenstück.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*