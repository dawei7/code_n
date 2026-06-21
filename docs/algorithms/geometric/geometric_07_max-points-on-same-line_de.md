# Max Points on a Line

| | |
|---|---|
| **ID** | `geometric_07` |
| **Kategorie** | geometric |
| **Komplexität (erforderlich)** | $O(N^2)$ |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) |

## Problemstellung

Gegeben ist ein Array von N Punkten in einer 2D-Ebene. Finden Sie die maximale Anzahl an Punkten, die exakt auf derselben geraden Linie liegen.
Ein naiver Ansatz würde eine Linie durch jedes Punktepaar definieren $O(N^2)$ und anschließend jeden anderen Punkt darauf prüfen, ob er auf dieser Linie liegt $O(N)$, was zu einem $O(N^3)$-Algorithmus führt.
Sie müssen dies in $O(N^2)$ unter Verwendung einer Hash Map und einer Steigungsrepräsentation lösen.

**Eingabe:** Eine Liste von `(x, y)`-Koordinatentupeln.
**Ausgabe:** Eine Ganzzahl, die die maximale Anzahl kollinearer Punkte repräsentiert.

## Wann man es verwendet

- Eine klassische technische Interviewfrage, die darauf ausgelegt ist, Kandidaten in die Falle zu locken, die Gleitkommadivision (`y / x`) zur Darstellung von Steigungen verwenden, was aufgrund von Präzisionsfehlern unweigerlich scheitert.

## Ansatz

Wenn wir einen spezifischen Punkt A als Ankerpunkt wählen, können wir eine Linie von A zu jedem anderen Punkt B, C, D... ziehen.
Wenn die Linie A \to B exakt dieselbe **Steigung** aufweist wie die Linie A \to C, dann müssen A, B und C kollinear sein!
Daher gilt für einen fixierten Ankerpunkt A:
1. Berechnen Sie die Steigung zu jedem anderen Punkt.
2. Speichern Sie die Anzahl jeder Steigung in einer Hash Map.
3. Die maximale Anzahl in der Hash Map (plus 1 für den Ankerpunkt selbst) ist die maximale Anzahl kollinearer Punkte, die durch A verlaufen.
Wiederholen Sie dies für jeden Punkt als Anker, was $O(N^2)$ Zeit in Anspruch nimmt.

**Die Gleitkomma-Falle:**
Die Steigung ist M = \frac{\Delta Y}{\Delta X} = \frac{y_2 - y_1}{x_2 - x_1}.
Bei einer Gleitkommadivision könnte `0.3333333333333333` anders gehasht werden als `0.3333333333333334`. Zudem führen vertikale Linien zu einem Fehler durch Division durch Null!
**Die Lösung:** Repräsentieren Sie die Steigung als irreduziblen Bruch (als String oder Tupel aus zwei Ganzzahlen).
Um einen Bruch irreduzibel zu machen, teilen Sie sowohl \Delta Y als auch \Delta X durch ihren größten gemeinsamen Teiler (GCD)!
Beispiel: \frac{6}{4} wird zu \frac{3}{2} gekürzt. \frac{-9}{-6} wird zu \frac{3}{2} gekürzt. Wir speichern das Tupel `(3, 2)` als Dictionary-Key!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for geometric_07: Max Points on Same Line.

Given n points in the plane, find the maximum
"""


def solve(points, n):
    """Max points on the same line via slope hashing."""
    from math import gcd
    if n < 2:
        return n
    best = 0
    for i in range(n):
        slopes = {}
        duplicates = 0
        vertical = 0
        for j in range(n):
            if i == j:
                continue
            if points[i] == points[j]:
                duplicates += 1
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0:
                # Vertical line.
                vertical += 1
            else:
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                # Normalize sign: force dx > 0 (or both zero).
                if dx < 0:
                    dx = -dx
                    dy = -dy
                key = (dy, dx)
                slopes[key] = slopes.get(key, 0) + 1
        local_max = vertical
        for c in slopes.values():
            if c > local_max:
                local_max = c
        total = local_max + duplicates + 1  # +1 for the pivot itself
        if total > best:
            best = total
    return best
```

</details>

## Durchlauf

`points = [(1,1), (2,2), (3,3), (4,5)]`

**Iteration 1: Anker `(1,1)`**
- vs `(2,2)`: dx=1, dy=1. GCD=1. Steigung `(1, 1)`. `counts[(1,1)] = 1`.
- vs `(3,3)`: dx=2, dy=2. GCD=2. Steigung `(1, 1)`. `counts[(1,1)] = 2`.
- vs `(4,5)`: dx=3, dy=4. GCD=1. Steigung `(3, 4)`. `counts[(3,4)] = 1`.
- Die maximale Steigungsanzahl ist 2 (für Steigung `1,1`).
- Linienlänge = 2 (\text{Steigungsübereinstimmung}) + 1 (\text{Anker}) = 3.
- `global_max = 3`.

**Iteration 2: Anker `(2,2)`**
- vs `(3,3)`: Steigung `(1, 1)`.
- vs `(4,5)`: dx=2, dy=3. Steigung `(2, 3)`.
- Maximale Linienlänge = 2.

**Endergebnis:** `global_max = 3`. ✓

*(Beachten Sie, wie wir die innere Schleife bei `j = i + 1` beginnen können. Wir müssen nicht rückwärts schauen, da jede Linie, die `points[i]` und vorherige Punkte einbezieht, bereits vollständig gezählt wurde, als der vorherige Punkt der Anker war!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^2)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N^2 log M)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N^2 log M)$ | $O(N)$ |

Die Doppelschleife iteriert $O(N^2)$ mal. Innerhalb der inneren Schleife benötigt die Berechnung des GCD logarithmische Zeit in Bezug auf die Koordinatenwerte M. Technisch gesehen also $O(N^2 log(\max(|dx|, |dy|)))$. Da Koordinaten üblicherweise begrenzt sind, wird dies in Interviews effektiv als $O(N^2)$ betrachtet.
Die Platzkomplexität ist $O(N)$, da das Dictionary im schlechtesten Fall N verschiedene Steigungs-Keys für einen einzelnen Anker speichert.

## Varianten & Optimierungen

- **Hough-Transformation:** Wenn N in die Millionen geht (wie Pixel in einem Bild) und Sie die längsten Linien finden möchten (Kantenerkennung), ist $O(N^2)$ zu langsam. Computer-Vision-Engines verwenden die Hough-Transformation, bei der Punkte in einen parametrischen (r, \theta)-Raum abgebildet werden und Schnittpunkte über eine Voting-Akkumulatormatrix gefunden werden, was Geschwindigkeiten nahe $O(N)$ erreicht!

## Anwendungen in der Praxis

- **Autonomes Fahren:** Verarbeitung von LIDAR-Punktwolken und Erkennung massiver Sequenzen kollinearer Punkte, um die physischen Grenzen einer Fahrspur oder Mauer mathematisch zu definieren.

## Verwandte Algorithmen in cOde(n)

- **[math_01 - GCD/LCM](../math/math_01_gcd-lcm-euclidean.md)** — Der Euklidische Algorithmus, der die Bruchreduktion ermöglicht und Gleitkommafehler vermeidet.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*