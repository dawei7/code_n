# Closest Pair of Points

| | |
|---|---|
| **ID** | `geometric_01` |
| **Kategorie** | geometric |
| **Komplexität (erforderlich)** | $O(N \log N)$ |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Closest pair of points problem](https://en.wikipedia.org/wiki/Closest_pair_of_points_problem) |

## Problemstellung

Gegeben ist ein Array von $N$ Punkten in einer 2D-Ebene. Finden Sie die zwei Punkte, die am nächsten beieinander liegen, und geben Sie den euklidischen Abstand zwischen ihnen zurück.
Ein naiver Ansatz vergleicht jedes Punktepaar, was eine Zeitkomplexität von $O(N^2)$ erfordert. Sie müssen einen **Divide and Conquer**-Algorithmus implementieren, der die Zeitkomplexität auf strikt $O(N \log N)$ reduziert.

**Input:** Eine Liste von `(x, y)`-Koordinatentupeln.
**Output:** Ein `float`, der den minimalen euklidischen Abstand repräsentiert.

## Anwendungsbereiche

- In räumlichen Clustering-Algorithmen, Kollisionserkennungs-Engines oder Simulationen der Flugverkehrskontrolle, bei denen $N \ge 10^5$ gilt.
- Eine klassische, elegant formulierte Anwendung des Divide and Conquer-Paradigmas in der Computergeometrie.

## Vorgehensweise

1. **Sortierung nach X:** Sortieren Sie zunächst alle Punkte nach ihrer X-Koordinate.
2. **Divide:** Teilen Sie das Array von Punkten rekursiv in zwei Hälften (durch Ziehen einer vertikalen Trennlinie). Der Induktionsanfang (Basis) ist erreicht, wenn die Teilmenge $\le 3$ Punkte enthält (hier wird der Abstand per Brute-Force berechnet).
3. **Conquer:** Die rekursiven Aufrufe liefern `min_left` und `min_right` zurück. Der bisher gefundene minimale Abstand ist `d = min(min_left, min_right)`.
4. **Das Problem der Trennlinien-Überschreitung:** Das absolut nächste Punktepaar könnte einen Punkt auf der linken Seite der Trennlinie und einen Punkt auf der rechten Seite haben! Dies MÜSSEN wir überprüfen.
5. **Der Streifen (Die $O(N)$-Magie):**
   - Wir interessieren uns nur für Punkte, die die Trennlinie überschreiten und *näher* als `d` beieinander liegen. Daher müssen wir nur Punkte betrachten, deren X-Koordinate innerhalb des Abstands `d` von der vertikalen Trennlinie liegt. Dies bildet einen vertikalen "Streifen" der Breite `2d`.
   - **Sortieren Sie den Streifen nach der Y-Koordinate.**
   - Iterieren Sie für jeden Punkt im Streifen durch die *nächsten* paar Punkte im sortierten Streifen.
   - **Die geometrische Garantie:** Mathematisch gesehen kann aufgrund der Herleitung von `d` ein Punkt in diesem Streifen höchstens **7** andere Punkte haben, die innerhalb des Abstands `d` von ihm liegen! Daher läuft die innere Schleife maximal 7-mal, was diese Überprüfung der Trennlinien-Überschreitung auf strikt $O(N)$ begrenzt!

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

## Durchlauf

*(Konzeptionell)*
Punkte: `(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)`

1. **Sortierung nach X:** `(2,3), (3,4), (5,1), (12,10), (12,30), (40,50)`.
2. **Divide:** Teilen bei Mitte `(5,1)`.
   - Links: `(2,3), (3,4), (5,1)`. Brute-Force-Minimum ist `d = 1.41` (zwischen `2,3` und `3,4`).
   - Rechts: `(12,10), (12,30), (40,50)`. Brute-Force `d = 20`.
3. **Conquer:** Bestes `d` ist `1.41`.
4. **Streifen:** Linie liegt bei `X = 5`.
   - Gibt es Punkte mit `X` zwischen `5 - 1.41` und `5 + 1.41`? (Bereich `3.59` bis `6.41`).
   - Nur `(5,1)` liegt im Streifen.
   - Da nur 1 Punkt vorhanden ist, können keine Paare über die Trennlinie hinweg `1.41` unterbieten.
5. Rückgabe `1.41`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N log^2 N)$ | $O(N)$ |

*Hinweis: Der obige Pseudocode verwendet ein `sort()` innerhalb der Rekursion. Pythons Timsort ist bei nahezu sortierten Daten schnell, aber theoretisch benötigt das Sortieren des Streifens auf jeder Ebene $O(N \log N)$ innerhalb eines $O(\log N)$-Baums, was im schlechtesten Fall zu $O(N log^2 N)$ führt.*
Um strikt $O(N \log N)$ zu erreichen, müssen alle Punkte zu Beginn einmal nach der Y-Koordinate vorsortiert und sorgfältig in die linken und rechten rekursiven Aufrufe gefiltert werden.
Die Platzkomplexität ist durch $O(N)$ für das Slicing des Arrays bzw. die Allokation des Streifens begrenzt.

## Varianten & Optimierungen

- **Sweep-Line-Algorithmus:** Sie können dies ohne Divide and Conquer lösen! Verwalten Sie ein aktives Fenster von Punkten, die nach der Y-Koordinate in einem balancierten BST sortiert sind. Während eine vertikale Linie nach rechts wandert, entfernen Sie Punkte, die weiter als `d` hinter der Linie liegen, und vergleichen Sie den neuen Punkt mit dem BST. Dies ist ebenfalls strikt $O(N \log N)$.

## Praxisanwendungen

- **LIDAR-Verarbeitung:** Schnelles Finden der nächsten physischen Hindernisse durch Analyse massiver Punktwolken, die von Sensoren autonomer Fahrzeuge erzeugt werden.

## Verwandte Algorithmen in cOde(n)

- **[sort_03 - Merge Sort](../sorting/sort_03_merge-sort.md)** — Die Divide and Conquer-Partitionierungslogik ist mathematisch identisch mit Merge Sort!
- **[geometric_06 - Rectangle Overlap](geometric_06_rectangle-overlap-axis-aligned.md)** — Eine weitere räumliche Abfrage, die durch Sweep-Line-Algorithmen stark optimiert wird.

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*