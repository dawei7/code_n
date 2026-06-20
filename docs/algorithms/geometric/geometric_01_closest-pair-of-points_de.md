# Das am nächsten beieinanderliegende Punktpaar

| | |
|---|---|
| **ID** | `geometric_01` |
| **Kategorie** | Geometrie |
| **Komplexität (erforderlich)** | $O(N \log N)$ |
| **Schwierigkeitsgrad** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Problem des nächstgelegenen Punktpaares](https://en.wikipedia.org/wiki/Closest_pair_of_points_problem) |

## Aufgabenstellung

Gegeben ist ein Array mit N Punkten in einer 2D-Ebene. Finde die beiden Punkte, die einander am nächsten liegen, und gib den euklidischen Abstand zwischen ihnen zurück.
Ein naiver Ansatz vergleicht jedes Punktpaar, was $O(N^2)$ Zeit in Anspruch nimmt. Sie müssen einen **Divide-and-Conquer**-Algorithmus implementieren, der die Zeitkomplexität auf streng $O(N \log N)$ senkt.

**Eingabe:** Eine Liste von `(x, y)` Koordinatentupeln.
**Ausgabe:** Ein Float-Wert, der den minimalen euklidischen Abstand angibt.

## Wann man ihn einsetzt

- In räumlichen Clustering-Algorithmen, Kollisionserkennungs-Engines oder Flugsicherungssimulationen, bei denen N \ge 10^5 gilt.
- Eine klassische, wunderbar elegante Anwendung des „Teile und herrsche“-Prinzips in der computergestützten Geometrie.

## Vorgehensweise

1. **Nach X sortieren:** Sortiere zunächst alle Punkte nach ihrer X-Koordinate.
2. **Teilen:** Das Punkte-Array wird rekursiv in zwei Hälften geteilt (durch Ziehen einer vertikalen Trennlinie). Der Basisfall liegt vor, wenn die Teilmenge \le 3 Punkte enthält (in diesem Fall wird der Abstand einfach mit Brute-Force berechnet).
3. **Beherrschen:** Die rekursiven Aufrufe geben `min_left` und `min_right` zurück. Der bisher gefundene minimale Abstand ist `d = min(min_left, min_right)`.
4. **Das grenzüberschreitende Problem:** Das absolut nächstgelegene Punktpaar könnte einen Punkt auf der linken Seite der Trennlinie und einen Punkt auf der rechten Seite haben! Dies MUSS überprüft werden.
5. **Der Streifen (die $O(N)$-Magie):**
   - Uns interessieren nur grenzüberschreitende Punkte, die *näher* als `d` liegen. Daher müssen wir nur Punkte betrachten, deren X-Koordinate streng innerhalb des Abstands `d` zur vertikalen Trennlinie liegt. Dies bildet einen vertikalen „Streifen“ der Breite `2d`.
   - **Sortiere den Streifen nach der Y-Koordinate.**
   - Durchlaufe für jeden Punkt im Streifen die *nächsten* paar Punkte im sortierten Streifen.
   - **Die geometrische Garantie:** Mathematisch gesehen kann ein Punkt in diesem Streifen aufgrund der Herleitung von `d` höchstens **7** andere Punkte haben, die sich in einem Abstand von `d` zu ihm befinden! Daher wird die innere Schleife höchstens 7 Mal durchlaufen, wodurch diese Grenzüberschreitungsprüfung streng $O(N)$ ist!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for geometric_01: Closest Pair of Points.

Brute-force O(n^2) for the test gauntlet. Check every pair;
return the smallest squared distance and the sorted pair.
"""


def solve(points, n):
    if n < 2:
        return -1, [(0, 0), (0, 0)]
    best_d = float("inf")
    best_pair = (points[0], points[1])
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            d = dx * dx + dy * dy
            if d < best_d:
                best_d = d
                best_pair = (points[i], points[j])
    return best_d, sorted(best_pair)
```

</details>

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
Punkte: `(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)`

1. **Nach X sortieren:** `(2,3), (3,4), (5,1), (12,10), (12,30), (40,50)`.
2. **Teilen:** In der Mitte teilen `(5,1)`.
   - Links: `(2,3), (3,4), (5,1)`. Das Minimum bei der Brute-Force-Methode liegt bei `d = 1.41` (zwischen `2,3` und `3,4`).
   - Rechts: `(12,10), (12,30), (40,50)`. Brute-Force-Methode `d = 20`.
3. **Erobern:** Das beste `d` ist `1.41`.
4. **Entfernen:** Die Linie liegt bei `X = 5`.
   - Gibt es Punkte mit `X` zwischen `5 - 1.41` und `5 + 1.41`? (Bereich von `3.59` bis `6.41`).
   - Nur `(5,1)` liegt im Streifen.
   - Da es nur einen Punkt gibt, kann kein grenzüberschreitendes Paar `1.41` übertreffen.
5. Gib `1.41` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlechteste** | $O(N log^2 N)$ | $O(N)$ |

*Hinweis: Der obige Pseudocode verwendet innerhalb der Rekursion ein Python-`sort()`. Pythons Timsort ist bei nahezu sortierten Daten schnell, aber theoretisch dauert das Sortieren des Streifens auf jeder Ebene $O(N \log N)$ innerhalb eines $O(\log N)$-Baums, was im schlimmsten Fall eine Laufzeit von $O(N log^2 N)$ ergibt.*
Um striktes $O(N \log N)$ zu erreichen, musst du alle Punkte zu Beginn einmal nach ihrer Y-Koordinate vorsortieren und sie sorgfältig in die linken und rechten rekursiven Aufrufe filtern.
Die Platzkomplexität ist durch $O(N)$ für das Array-Slicing bzw. die Zuweisung des Streifens begrenzt.

## Varianten & Optimierungen

- **Sweep-Line-Algorithmus:** Sie können diese Aufgabe ohne „Teile und herrsche“ lösen! Verwalten Sie ein aktives Fenster mit Punkten, die nach ihrer Y-Koordinate in einem ausgeglichenen BST sortiert sind. Während eine vertikale Linie nach rechts verläuft, entfernen Sie Punkte, die weiter als `d` hinter der Linie liegen, und überprüfen Sie den neuen Punkt anhand des BST. Auch hier gilt striktes $O(N \log N)$.

## Praktische Anwendungen

- **LIDAR-Verarbeitung:** Schnelles Auffinden der nächstgelegenen physischen Hindernisse durch Analyse umfangreicher Punktwolken, die von Sensoren autonomer Fahrzeuge erzeugt werden.

## Verwandte Algorithmen in cOde(n)

- **[sort_03 – Merge-Sort](../sorting/sort_03_merge-sort.md)** — Die Partitionierungslogik von „Teile und herrsche“ ist mathematisch identisch mit dem Merge-Sort!
- **[geometric_06 – Rechtecküberlappung](geometric_06_rectangle-overlap-axis-aligned.md)** — Eine weitere räumliche Abfrage, die durch Sweep-Line-Algorithmen stark optimiert wurde.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
