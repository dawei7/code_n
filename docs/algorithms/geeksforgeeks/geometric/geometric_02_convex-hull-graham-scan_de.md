# Convex Hull (Graham Scan)

| | |
|---|---|
| **ID** | `geometric_02` |
| **Kategorie** | geometric |
| **Komplexität (erforderlich)** | $O(N \log N)$ |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **Wikipedia** | [Graham scan](https://en.wikipedia.org/wiki/Graham_scan) |

## Problemstellung

Gegeben ist ein Array von $N$ Punkten in einer 2D-Ebene. Finde die **Convex Hull** (konvexe Hülle): das kleinste konvexe Polygon, das alle Punkte vollständig umschließt.
Stellen Sie sich vor, Sie spannen ein Gummiband um die gesamte Punktwolke und lassen es zuschnappen. Die Punkte, die das Gummiband berührt, sind die Eckpunkte der Convex Hull.
Implementieren Sie den **Graham Scan** Algorithmus, um diese Eckpunkte in strikter $O(N \log N)$ Zeit zu finden.

**Eingabe:** Eine Liste von `(x, y)` Koordinaten-Tupeln.
**Ausgabe:** Eine Liste von `(x, y)` Tupeln, die die Eckpunkte der Convex Hull darstellen, typischerweise in gegen den Uhrzeigersinn verlaufender Reihenfolge.

## Wann man es verwendet

- Um die Begrenzungsfläche einer Form zu finden, Ausreißer in einem Datensatz zu erkennen oder als vorbereitender Schritt zur Bestimmung des Durchmessers einer Punktwolke (Rotating Calipers Algorithmus).
- Der Graham Scan ist der Standard-Algorithmus und die eleganteste $O(N \log N)$ Lösung für dieses Problem.

## Ansatz

Der Kern des Graham Scan ist ein Stack und ein mathematisches Konzept namens **Kreuzprodukt** (Cross Product).
Das Kreuzprodukt von drei Punkten A, B, C gibt uns die "Orientierung" der Drehung vom Liniensegment AB zum Liniensegment BC an:
- Wenn das Kreuzprodukt > 0 ist, handelt es sich um eine **Linkskurve** (gegen den Uhrzeigersinn).
- Wenn es < 0 ist, handelt es sich um eine **Rechtskurve** (im Uhrzeigersinn).
- Wenn es 0 ist, sind die Punkte kollinear (eine gerade Linie).

Ein konvexes Polygon, das gegen den Uhrzeigersinn durchlaufen wird, MUSS ausschließlich aus Linkskurven bestehen!

**Die Schritte:**
1. **Ankerpunkt finden:** Finde den Punkt mit der niedrigsten Y-Koordinate (bei Gleichstand den mit der niedrigsten X-Koordinate). Dieser Punkt liegt mathematisch garantiert auf der Hülle. Nennen wir ihn P_0.
2. **Nach Winkel sortieren:** Sortiere alle anderen Punkte basierend auf dem Polarwinkel, den sie mit P_0 relativ zur X-Achse bilden. (Wenn zwei Punkte denselben Winkel haben, behalte denjenigen, der am weitesten von P_0 entfernt ist).
3. **Der Stack:** Lege P_0 und den ersten sortierten Punkt auf einen Stack.
4. **Scan:** Iteriere durch den Rest der sortierten Punkte.
   - Betrachte für jeden neuen Punkt P_i die obersten zwei Punkte auf dem Stack (top und second\_top).
   - Bildet die Sequenz `second_top -> top -> P_i` eine Linkskurve?
   - Falls NEIN (es ist eine Rechtskurve oder eine gerade Linie), haben wir gerade eine "Delle" in unserer Hülle erzeugt! Das bedeutet, dass top nicht auf der Convex Hull liegen kann. Entferne ihn vom Stack (pop)! Wiederhole diese Prüfung, bis eine Linkskurve gebildet wird.
   - Sobald eine Linkskurve vorliegt, lege P_i auf den Stack (push).
5. Der Stack enthält nun exakt die Eckpunkte der Convex Hull!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for geometric_02: Convex Hull (Graham Scan).

Bottom-most, then leftmost point is the pivot. Sort the rest
by polar angle to the pivot. Walk the sorted list, pushing to
a stack; pop the stack while the top two and the new point
make a non-left turn. O(n log n).
"""


def solve(points, n):
    import math
    if n < 3:
        return sorted(points)
    pivot = min(points)

    def angle_key(p):
        if p == pivot:
            return (-math.inf,)
        dx = p[0] - pivot[0]
        dy = p[1] - pivot[1]
        return (math.atan2(dy, dx), dx * dx + dy * dy)

    rest = [p for p in points if p != pivot]
    rest.sort(key=angle_key)
    hull = [pivot]
    for p in rest:
        while len(hull) >= 2:
            o, a = hull[-2], hull[-1]
            cross = (a[0] - o[0]) * (p[1] - o[1]) - (a[1] - o[1]) * (p[0] - o[0])
            if cross <= 0:
                hull.pop()
            else:
                break
        hull.append(p)
    return sorted(hull)
```

</details>

## Durchlauf

*(Konzeptionell)*
Punkte: `A(0,0)`, `B(3,1)`, `C(1,2)`, `D(0,3)`, `E(-2,1)`

1. **Anker:** Niedrigstes Y ist `A(0,0)`.
2. **Nach Winkel sortieren:**
   - `B` hat etwa 18 Grad.
   - `C` hat etwa 63 Grad.
   - `D` hat 90 Grad.
   - `E` hat etwa 153 Grad.
   - Reihenfolge: `B, C, D, E`.
3. **Stack:** `[A, B]`.
4. **Scan C:** `A -> B -> C`. Bildet eine Linkskurve! Stack: `[A, B, C]`.
5. **Scan D:** `B -> C -> D`. Bildet eine Linkskurve! Stack: `[A, B, C, D]`.
6. **Scan E:** `C -> D -> E`. Bildet eine Linkskurve! Stack: `[A, B, C, D, E]`.

Was wäre, wenn wir einen Punkt `X(1, 1)` hätten?
- Der Winkel von `X` beträgt 45 Grad. Reihenfolge: `B, X, C, D, E`.
- Stack: `[A, B]`.
- Scan X: `A -> B -> X` ist eine Linkskurve. Stack `[A, B, X]`.
- Scan C: `B -> X -> C` ist eine **Rechtskurve**! Wir beulen nach innen ein!
  - Pop `X`! Stack ist `[A, B]`.
  - Prüfe nun `A -> B -> C`. Linkskurve! Push `C`. Stack `[A, B, C]`.
  - `X` wurde erfolgreich von der Hülle ausgeschlossen! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Das anfängliche Sortieren der Punkte nach Polarwinkel benötigt strikt $O(N \log N)$ Zeit.
Die Scan-Schleife verarbeitet jeden Punkt genau einmal. Ein Punkt wird genau einmal auf den Stack gelegt (push) und höchstens einmal entfernt (pop). Daher benötigen die Stack-Operationen insgesamt strikt $O(N)$ Zeit. Der Flaschenhals ist das Sortieren, was die Gesamtlaufzeit auf exakt $O(N \log N)$ festlegt.
Die Platzkomplexität beträgt $O(N)$, um das sortierte Array und den Stack zu speichern.

## Varianten & Optimierungen

- **Monotone Chain Algorithmus:** Eine sehr beliebte Alternative zum Graham Scan. Anstatt nach Polarwinkel zu sortieren (was aufwendige `math.atan2` Fließkommaberechnungen erfordert), sortiert er die Punkte einfach nach der X-Koordinate. Er erstellt eine "obere Hülle" (Upper Hull) und eine "untere Hülle" (Lower Hull) unter Verwendung derselben Linkskurven-Stack-Logik und fügt diese dann zusammen! Er wird in der wettbewerbsorientierten Programmierung meist bevorzugt, da er nur Ganzzahl-Arithmetik verwendet.

## Anwendungen in der Praxis

- **Kollisionserkennung:** Berechnung der "Hitbox" komplexer 3D-Objekte in Physik-Engines von Videospielen durch Reduktion auf deren Convex Hull.
- **Geoinformationssysteme (GIS):** Bestimmung der territorialen Grenzen von Tierhabitaten anhand von GPS-Tracking-Daten.

## Verwandte Algorithmen in cOde(n)

- **[geometric_05 - Jarvis March](geometric_05_convex-hull-jarvis-march.md)** — Die $O(N \cdot H)$ "Gift Wrapping" Alternative zur Bestimmung der Convex Hull.
- **[stack_01 - Next Greater Element](../stacks/stack_01_next-greater-element.md)** — Die identische Monotonic-Stack-Logik, die verwendet wird, um ungültige innere Elemente zu entfernen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für wettbewerbsorientierte Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*