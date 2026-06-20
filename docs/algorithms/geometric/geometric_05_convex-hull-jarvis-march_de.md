# Konvexhülle (Jarvis March / Geschenkverpackung)

| | |
|---|---|
| **ID** | `geometric_05` |
| **Kategorie** | geometrisch |
| **Komplexität (erforderlich)** | $O(N * H)$ |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Gift-Wrapping-Algorithmus](https://en.wikipedia.org/wiki/Gift_wrapping_algorithm) |

## Aufgabenstellung

Gegeben ist ein Array mit N Punkten in einer 2D-Ebene. Bestimme die **konvexe Hülle**: das kleinste konvexe Polygon, das alle Punkte vollständig umschließt.
Während der Graham-Scan (`geo_02`) genau $O(N \log N)$ Zeit benötigt, implementiere den **Jarvis-March**-Algorithmus (oft auch als „Gift-Wrapping“-Algorithmus bezeichnet).
Dieser Algorithmus benötigt $O(N \cdot H)$ Zeit, wobei H die Anzahl der Punkte ist, die tatsächlich auf der Hülle liegen. Damit handelt es sich um einen ausgabeabhängigen Algorithmus!

**Eingabe:** Eine Liste von `(x, y)` Koordinatentupeln.
**Ausgabe:** Eine Liste von `(x, y)` Tupeln, die die Eckpunkte der konvexen Hülle darstellen.

## Wann man ihn verwenden sollte

- Wenn du stark vermutest, dass die konvexe Hülle im Vergleich zur Gesamtzahl der Punkte nur sehr wenige Eckpunkte haben wird (z. B. 10^6 Punkte, die dicht in einem Quadrat gepackt sind. H wäre dann 4, sodass Jarvis-March in $O(4N)$ läuft und damit den Graham-Scan $O(N \log N)$).
- Die Implementierung ist konzeptionell viel einfacher als beim Graham-Scan, da auf eine anfängliche Sortierung und Stack-Logik verzichtet wird.

## Vorgehensweise

Stell dir vor, du fährst mit einem Auto um den Umfang der Punktwolke herum.
Du startest am absolut linken Punkt (niedrigster X-Wert). Man weiß, dass dieser Punkt auf der konvexen Hülle liegen MUSS.
Nun möchte man das Auto so lenken, dass es auf den *nächsten* Eckpunkt der Hülle zeigt. Dazu betrachtet man einfach jeden einzelnen Punkt in der Wolke und wählt denjenigen aus, der einen zu einer möglichst weiten **Rechtskurve** zwingt!
Sobald du diesen Punkt gefunden hast, fährst du dorthin und wiederholst den Vorgang, bis du wieder an deinem Ausgangspunkt angekommen bist.

1. **Ankerpunkt finden:** Finde den Punkt ganz links. Sei `current_point` dieser Ankerpunkt.
2. **Hülle initialisieren:** Füge `current_point` zur Hülle hinzu.
3. **Die Schleife:** Nehmen wir an, der nächste Punkt auf der Hülle ist `next_point = points[0]`.
4. **Durchsuchen:** Durchlaufe jeden Punkt `p` im Array:
   - Verwende das **Vektorprodukt**, um die Ausrichtung von `current_point -> next_point -> p` zu überprüfen.
   - Wenn `p` weiter rechts (gegen den Uhrzeigersinn) liegt als unsere aktuelle Vermutung `next_point`, aktualisiere `next_point = p`.
   - *(Randfall: Wenn `p` und `next_point` perfekt kollinear mit `current_point` sind, wähle den Punkt aus, der weiter entfernt ist).*
5. **Aktualisierung:** Nachdem alle Punkte überprüft wurden, ist `next_point` mathematisch garantiert der nächste Eckpunkt auf der Hülle. Füge ihn zur Hülle hinzu.
6. Setze `current_point = next_point`. Wiederhole die Schritte 3–6, bis `next_point` unserem ursprünglichen Anker entspricht.

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
Punkte: `A(0,0)`, `B(1,1)`, `C(2,0)`, `D(1,2)`

1. **Ganz links:** `A(0,0)`. `hull = [A]`.
2. **Aktuell:** `A`. Vermutung `next_idx = B`.
   - Überprüfe `C`: `A -> B -> C` biegt nach rechts ab. `C` liegt „äußerer“ als `B`. Aktualisiere `next_idx = C`.
   - Überprüfe `D`: `A -> C -> D` dreht sich nach links. Behalte `next_idx = C`.
3. **Bewegung:** `next_idx` ist `C`. `hull = [A, C]`.
4. **Aktuell:** `C`. Vermutung `next_idx = A`.
   - Überprüfung `B`: `C -> A -> B` dreht sich nach links. Behalte `next_idx = A`.
   - Überprüfung `D`: `C -> A -> D` dreht sich nach rechts. `D` ist weiter außen! Aktualisiere `next_idx = D`.
5. **Zug:** `next_idx` ist `D`. `hull = [A, C, D]`.
6. **Aktuell:** `D`. Vermutung `next_idx = A`.
   - Überprüfe `B`: `D -> A -> B` dreht nach links. `A` beibehalten.
   - `C` prüfen: `D -> A -> C` biegt nach links ab. `A` beibehalten.
7. **Zug:** `next_idx` ist `A`. Dies ist der Startpunkt! Die Schleife wird unterbrochen!
Ergebnis: `[A, C, D]`. ✓ (`B` befand sich streng genommen innerhalb!).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N * H)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(1)$ |

*Dabei ist H die Anzahl der Eckpunkte auf der Hülle.*
Wenn sich jeder einzelne Punkt auf der Hülle befindet (z. B. wenn sie einen riesigen Kreis bilden), wird die Schleife N-mal durchlaufen, wobei jedes Mal N Punkte überprüft werden, was zu $O(N^2)$ führt. Dies ist schlechter als der Graham-Scan!
Ist H jedoch klein, läuft er unglaublich schnell.
Die Platzkomplexität beträgt streng genommen $O(1)$ Hilfsraum (ohne das Ausgabearray), was ihn äußerst speichereffizient macht.

## Varianten & Optimierungen

- **Chan-Algorithmus:** Der ultimative Algorithmus für die konvexe Hülle. Er kombiniert den Graham-Scan und den Jarvis-March-Algorithmus, um eine ausgababhängige Laufzeit von genau $O(N log H)$ zu erreichen. Dabei werden die Punkte in Blöcke der Größe H aufgeteilt, auf jedem Block wird der Graham-Scan ausgeführt und anschließend wird Jarvis-March auf die resultierenden Teilhüllen angewendet!

## Praktische Anwendungen

- **Robotik:** Bestimmung der absoluten Außengrenze eines Roboterschwarms, um die minimale Größe eines Begrenzungsnetzes zu berechnen.

## Verwandte Algorithmen in cOde(n)

- **[geometric_02 – Graham-Scan](geometric_02_convex-hull-graham-scan.md)** — Das $O(N \log N)$-Pendant.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
