# Closest Pair of Points

| | |
|---|---|
| **ID** | `dc_05` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **GeeksForGeeks Äquivalent** | [Closest Pair of Points](https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/) |

## Problemstellung

Gegeben ist ein Array von N Punkten in einer 2D-Ebene, wobei jeder Punkt durch seine `(x, y)`-Koordinaten definiert ist. Finden Sie das Punktepaar mit dem kleinsten euklidischen Abstand zueinander.
Geben Sie diesen minimalen Abstand zurück.

**Eingabe:** Ein Array von `Points`, wobei `Point` die Eigenschaften `x` und `y` besitzt.
**Ausgabe:** Eine Fließkommazahl, die den minimalen Abstand repräsentiert.

## Wann man es verwendet

- Das klassische Problem der Computergeometrie für Divide and Conquer.
- Zeigt, wie Sortieren den "Conquer"-Schritt (Merge-Schritt) von räumlichen Algorithmen massiv optimiert, um $O(N^2)$-Prüfungen zu umgehen.

## Ansatz

**1. Der naive Ansatz:**
Berechnen Sie den euklidischen Abstand zwischen jedem möglichen Punktepaar. \frac{N(N-1)}{2} Paare bedeuten, dass dies strikt $O(N^2)$ Zeit benötigt.

**2. Divide and Conquer:**
Sortieren wir alle Punkte nach ihrer `x`-Koordinate.
Wir können die Punkte in eine linke und eine rechte Hälfte unterteilen, indem wir eine vertikale Linie `L` genau durch die mittlere `x`-Koordinate ziehen.
Finden Sie rekursiv das nächste Paar in der linken Hälfte (d_{left}) und das nächste Paar in der rechten Hälfte (d_{right}).
Sei d = \min(d_{left}, d_{right}).
Ist d der absolute minimale Abstand? Nicht unbedingt! Was, wenn ein Punkt am äußersten rechten Rand der linken Hälfte liegt und der andere Punkt am äußersten linken Rand der rechten Hälfte? Sie liegen beidseitig der Trennlinie `L` und könnten näher beieinander liegen als d!

**3. Der "Streifen" (Conquer-Schritt):**
Wir betrachten nur Punkte, die näher an der Trennlinie `L` liegen als der Abstand d. Wenn ein Punkt weiter als d von der Linie entfernt ist, ist es mathematisch unmöglich, dass er ein Paar über die Linie hinweg bildet, dessen Abstand kleiner als d ist.
1. Erstellen Sie ein Array `strip`, das nur die Punkte enthält, deren `x`-Koordinate innerhalb von d zur Trennlinie `L` liegt.
2. **Sortieren Sie das `strip`-Array nach den `y`-Koordinaten.**
3. Iterieren Sie durch den `strip`. Vergleichen Sie jeden Punkt mit den nachfolgenden Punkten im Streifen.
   *Die magische Optimierung:* Da die Punkte im Streifen durch eine Breite von 2d begrenzt sind und wir sie nach `y` sortiert haben, ist mathematisch bewiesen, dass wir NUR die nächsten **7 Punkte** im sortierten Array prüfen müssen! Jeder Punkt, der weiter als 7 Stellen entfernt ist, wird definitiv einen `y`-Abstand größer als d haben.
   Dies reduziert den Merge-Schritt von einem $O(N^2)$-Kreuzvergleich auf einen linearen $O(N)$-Durchlauf!

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

## Ablauf

*(Konzeptionell aufgrund der räumlichen Anordnung)*

1. Punkte werden nach X sortiert. Die linke Hälfte wird rekursiv verarbeitet, die rechte Hälfte ebenfalls.
2. Angenommen `d_left = 5` und `d_right = 7`.
3. Das aktuelle absolute Minimum ist `d = 5`.
4. Die Trennlinie `L` liegt bei `X = 10`.
5. Wir scannen die Punkte. Jeder Punkt, dessen X-Koordinate zwischen `5` und `15` liegt, wird dem `strip` hinzugefügt.
6. Wir sortieren den `strip` nach der Y-Koordinate (z. B. von unten nach oben).
7. Wir iterieren durch den `strip`. Für Punkt P_1 prüfen wir P_2, P_3 \dots
8. Wenn der vertikale Abstand zwischen P_1 und P_k `5` übersteigt, brechen wir die innere Schleife SOFORT ab, da kein weiter oben liegender Punkt näher als `5` sein kann.
9. Die innere Schleife wird nie öfter als 7 Mal pro Punkt ausgeführt, was den Vergleich extrem schnell macht.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N log^2 N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N log^2 N)$ | $O(N)$ |

Der obige Code benötigt $O(N log^2 N)$ Zeit. Warum? Die Rekursionstiefe beträgt $O(\log N)$. Auf jeder Ebene benötigt das Erstellen des Streifens $O(N)$, aber das Sortieren des Streifens nach Y benötigt $O(k log k)$, wobei k \le N. Die innere While-Schleife ist insgesamt strikt $O(N)$. Daher dominiert das Sortieren den Merge-Schritt: T(N) = 2T(N/2) + $O(N \log N)$ -> $O(N log^2 N)$.
**Optimierung auf strikt $O(N \log N)$:** Wenn wir die Punkte zu Beginn global nach Y vorsortieren (`points_sorted_y`) und dieses Y-sortierte Array während des Divide-Schritts sorgfältig in linke und rechte Hälften aufteilen, müssen wir den Streifen nicht erneut sortieren! Der Merge-Schritt wird rein $O(N)$, was T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$ erfüllt.
Die Platzkomplexität beträgt $O(N)$, um die Arrays während der Rekursion zu speichern.

## Varianten & Optimierungen

- **Sweep-Line-Algorithmus:** Ein Ansatz, der vollständig ohne Divide and Conquer auskommt und einen Binary Search Tree (wie `std::set` in C++) verwendet. Man bewegt eine vertikale Linie von links nach rechts und verwaltet ein "aktives Fenster" von Punkten innerhalb des Abstands d, sortiert nach Y. Er erreicht $O(N \log N)$, ist aber in der Praxis oft viel schneller und einfacher zu implementieren.

## Anwendungen in der Praxis

- **Flugsicherung:** Erkennung, ob sich zwei Flugzeuge auf Kollisionskurs befinden (Verletzung der minimalen Sicherheitsabstände) im 3D-Radarraum.
- **Physik-Simulatoren (Kollisionserkennung):** Identifizierung, welche Partikel im aktuellen Frame interagieren oder abprallen, ohne jedes einzelne Atompaar in der Simulation prüfen zu müssen.

## Verwandte Algorithmen in cOde(n)

- **[dc_02 - Majority Element](dc_02_majority-element.md)** — Ein weiterer Algorithmus, bei dem der Conquer-Schritt die Validierung von Elementen gegen einen dynamisch abgeleiteten Schwellenwert erfordert.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*