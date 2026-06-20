# Das am nächsten beieinander liegende Punktpaar

| | |
|---|---|
| **ID** | `dc_05` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **GeeksForGeeks-Äquivalent** | [Nächstgelegenes Punktpaar](https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/) |

## Aufgabenstellung

Gegeben ist ein Array mit N Punkten in einer 2D-Ebene, wobei jeder Punkt durch seine `(x, y)`-Koordinaten definiert ist. Finde das Punktpaar, zwischen dem der kleinste euklidische Abstand besteht.
Gib diesen minimalen Abstand zurück.

**Eingabe:** Ein Array von `Points`, wobei `Point` die Eigenschaften `x` und `y` aufweist.
**Ausgabe:** Eine Gleitkommazahl, die den minimalen Abstand angibt.

## Wann man es verwendet

- Das typische Problem der Computational Geometry für die „Teile und herrsche“-Strategie.
- Zeigt, wie das Sortieren den „Herrsche“-Schritt (Zusammenführen) räumlicher Algorithmen stark optimiert, um $O(N^2)$-Prüfungen zu umgehen.

## Vorgehensweise

**1. Der naive Ansatz:**
Berechne den euklidischen Abstand zwischen jedem möglichen Punktpaar. Bei \frac{N(N-1)}{2} Paaren handelt es sich um eine streng $O(N^2)$-Zeitaufwendung.

**2. Teile und herrsche:**
Sortieren wir alle Punkte nach ihrer `x`-Koordinate.
Wir können die Punkte in eine linke und eine rechte Hälfte unterteilen, indem wir eine vertikale Linie `L` genau durch die Mitte der `x`-Koordinate ziehen.
Finde rekursiv das nächstgelegene Paar in der linken Hälfte (d_{left}) und das nächstgelegene Paar in der rechten Hälfte (d_{right}).
Sei d = \min(d_{left}, d_{right}).
Ist d der absolute Mindestabstand? Nicht unbedingt! Was ist, wenn sich ein Punkt am äußersten rechten Rand der linken Hälfte und der andere Punkt am äußersten linken Rand der rechten Hälfte befindet? Sie liegen beiderseits der Trennlinie `L` und könnten näher beieinander liegen als d!

**3. Der „Streifen“ (Eroberungsschritt):**
Uns interessieren nur Punkte, die näher an der Trennlinie `L` liegen als der Abstand d. Liegt ein Punkt weiter als d von der Linie entfernt, ist es mathematisch unmöglich, dass er ein Paar über die Linie hinweg bildet, dessen Abstand kleiner als d ist.
1. Erstelle ein Array `strip`, das nur die Punkte enthält, deren `x`-Koordinate innerhalb von d zur Trennlinie `L` liegt.
2. **Sortiere das `strip`-Array nach den `y`-Koordinaten.**
3. Durchlaufe das `strip`. Vergleiche für jeden Punkt diesen mit den nächsten Punkten im Streifen.
   *Die geniale Optimierung:* Da die Punkte im Streifen durch eine Breite von 2d begrenzt sind und wir sie nach `y` sortiert haben, ist mathematisch bewiesen, dass wir NUR die nächsten **7 Punkte** vor ihm im sortierten Array überprüfen müssen! Jeder Punkt, der weiter als 7 Stellen entfernt ist, hat definitiv einen `y`-Abstand, der größer als d ist.
   Dadurch reduziert sich der Zusammenführungsschritt von einem $O(N^2)$-Quervergleich auf einen $O(N)$-linearen Scan!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_05: Closest Pair of Points.

Given n points in the plane, return the smallest
"""


def solve(points, n):
    """Closest pair of points via D&C plane sweep."""
    if n < 2:
        return 0.0
    px = sorted(points, key=lambda p: (p[0], p[1]))
    return _closest(px, 0, n - 1)

def _dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def _brute(pts, lo, hi):
    best = float("inf")
    for i in range(lo, hi + 1):
        for j in range(i + 1, hi + 1):
            d = _dist(pts[i], pts[j])
            if d < best:
                best = d
    return best

def _closest(px, lo, hi):
    n = hi - lo + 1
    if n <= 3:
        return _brute(px, lo, hi)
    mid = (lo + hi) // 2
    mid_x = px[mid][0]
    dl = _closest(px, lo, mid)
    dr = _closest(px, mid + 1, hi)
    d = min(dl, dr)
    strip = [px[k] for k in range(lo, hi + 1) if abs(px[k][0] - mid_x) < d]
    strip.sort(key=lambda p: p[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) ** 2 >= d * d:
                break
            cand = _dist(strip[i], strip[j])
            if cand < d:
                d = cand
    return d
```

</details>

## Schritt-für-Schritt-Anleitung

*(Konzeptionell aufgrund der räumlichen Anordnung)*

1. Die Punkte werden nach X sortiert. Die linke Hälfte wird rekursiv bearbeitet, die rechte Hälfte wird rekursiv bearbeitet.
2. Angenommen, `d_left = 5` und `d_right = 7`.
3. Das aktuelle absolute Minimum ist `d = 5`.
4. Die Trennlinie `L` liegt bei `X = 10`.
5. Wir durchlaufen die Punkte. Jeder Punkt, dessen X-Koordinate zwischen `5` und `15` liegt, wird zu `strip` hinzugefügt.
6. Wir sortieren die `strip` nach ihrer Y-Koordinate (z. B. von unten nach oben).
7. Wir durchlaufen die `strip`. Für den Punkt P_1 prüfen wir P_2, P_3 \dots
8. Wenn der vertikale Abstand zwischen P_1 und P_k `5` überschreitet, brechen wir die innere Schleife SOFORT ab, da kein höher gelegener Punkt näher als `5` sein kann.
9. Die innere Schleife wird pro Punkt nie öfter als 7 Mal ausgeführt, wodurch der Vergleich blitzschnell bleibt.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N log^2 N)$ | $O(N)$ |
| **Schlechteste** | $O(N log^2 N)$ | $O(N)$ |

Der obige Code benötigt $O(N log^2 N)$ Zeit. Warum? Die Rekursionstiefe beträgt $O(\log N)$. Auf jeder Ebene dauert das Erstellen des Streifens $O(N)$, das Sortieren des Streifens nach Y jedoch $O(k log k)$, wobei k \le N gilt. Die innere while-Schleife ist streng $O(N)$ total. Somit dominiert die Sortierung den Zusammenführungsschritt: T(N) = 2T(N/2) + $O(N \log N)$ -> $O(N log^2 N)$.
**Optimierung auf streng $O(N \log N)$:** Wenn wir die Punkte ganz am Anfang global nach Y vorsortieren (`points_sorted_y`) und dieses nach Y sortierte Array während des Divide-Schritts sorgfältig in eine linke und eine rechte Hälfte aufteilen, müssen wir den Streifen nicht erneut sortieren! Der Merge-Schritt wird zu reinem $O(N)$, womit T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$ erfüllt ist.
Die Platzkomplexität beträgt $O(N)$, um die Arrays während der Rekursion zu speichern.

## Varianten & Optimierungen

- **Sweep-Line-Algorithmus:** Ein Ansatz, der gänzlich ohne „Teile und herrsche“ auskommt und einen Binary Search Tree verwendet (wie `std::set` in C++). Man fegt eine vertikale Linie von links nach rechts und behält dabei ein „aktives Fenster“ von Punkten innerhalb der Entfernung d bei, sortiert nach Y. Er erreicht $O(N \log N)$, ist in der Praxis jedoch oft viel schneller und einfacher zu programmieren.

## Praktische Anwendungen

- **Flugsicherung:** Erkennung, ob sich zwei Flugzeuge im 3D-Radarraum auf Kollisionskurs befinden (und damit die Mindestabstände für einen sicheren Flug verstoßen).
- **Physiksimulatoren (Kollisionserkennung):** Ermittlung, welche Partikel im aktuellen Bild miteinander interagieren oder voneinander abprallen, ohne jedes einzelne Atompaar in der Simulation zu überprüfen.

## Verwandte Algorithmen in cOde(n)

- **[dc_02 – Majority Element](dc_02_majority-element.md)** — Ein weiterer Algorithmus, bei dem im „Conquer“-Schritt Elemente anhand eines dynamisch abgeleiteten Schwellenwerts validiert werden müssen.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
