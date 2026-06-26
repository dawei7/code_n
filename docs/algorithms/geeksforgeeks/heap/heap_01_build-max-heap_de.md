# Build Max Heap (Heapify)

| | |
|---|---|
| **ID** | `heap_01` |
| **Kategorie** | heap |
| **Komplexität (erforderlich)** | $O(N)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Binary heap](https://en.wikipedia.org/wiki/Binary_heap#Building_a_heap) |

## Problemstellung

Gegeben ist ein unsortiertes Array von N Ganzzahlen. Ordnen Sie die Elemente in-place so um, dass sie die **Max-Heap-Eigenschaft** erfüllen: Für jeden Knoten i ist der Wert des Knotens i größer oder gleich den Werten seiner Kinder.
Sie müssen diesen Heap in strikter $O(N)$-Zeit aufbauen, nicht in $O(N \log N)$.

**Eingabe:** Ein unsortiertes Array von Ganzzahlen.
**Ausgabe:** Dasselbe Array, das in-place in einen gültigen Max-Heap umgewandelt wurde.

## Wann man es verwendet

- Als grundlegender erster Schritt des Heap Sort-Algorithmus.
- Wenn Sie eine Priority Queue benötigen, aber die gesamte Datenmenge vorab erhalten, anstatt sie als Stream zu verarbeiten. Der Aufbau eines Heaps in $O(N)$ ist mathematisch schneller, als N Elemente einzeln nacheinander in einen leeren Heap einzufügen ($O(N \log N)$).

## Ansatz

Ein Binary Heap wird typischerweise als vollständiger Binärbaum visualisiert, aber er lässt sich perfekt effizient in einem flachen Array speichern!
Wenn sich ein Knoten am Index `i` befindet (0-basiert):
- Befindet sich sein linkes Kind an `2*i + 1`.
- Befindet sich sein rechtes Kind an `2*i + 2`.
- Befindet sich sein Elternknoten an `(i - 1) // 2`.

**Die `sift_down`-Operation:**
Wenn Sie einen Knoten haben, der kleiner als seine Kinder ist, verletzt er die Max-Heap-Eigenschaft. Sie beheben dies, indem Sie ihn „nach unten sieben“ (sift down): Tauschen Sie ihn mit seinem *größten* Kind und wiederholen Sie dies rekursiv, bis er größer als beide Kinder ist oder den Boden erreicht (ein Blatt wird).

**Die $O(N)$-Aufbaustrategie (Floyd-Algorithmus):**
Ein naiver Weg, einen Heap aufzubauen, besteht darin, `sift_up` für jedes Element von links nach rechts aufzurufen. Dies benötigt $O(N \log N)$.
Um $O(N)$ zu erreichen, müssen wir **bottom-up** arbeiten und `sift_down` aufrufen!
1. Die untere Hälfte des Arrays repräsentiert die Blattknoten des Baums. Blätter haben keine Kinder, daher erfüllen sie die Heap-Eigenschaft bereits trivial! (Wir können sie überspringen).
2. Der letzte Nicht-Blatt-Knoten befindet sich am Index `N // 2 - 1`.
3. Wir laufen rückwärts von diesem Index bis `0`.
4. Für jeden Knoten rufen wir `sift_down` auf. Da wir rückwärts gehen, garantieren wir mathematisch, dass die Teilbäume unterhalb des aktuellen Knotens bereits perfekte Max-Heaps sind! Die `sift_down`-Operation führt diese mühelos zusammen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for heap_01: Build Max Heap.

Treat the input as a 0-indexed binary heap and sift-down from
the last non-leaf to the root. Bottom-up heapify is O(n) - faster
than the O(n log n) naive "insert" approach.
"""


def solve(data, n):
    # Sift down ``start`` in [0, n).
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child >= end:
                break
            if child + 1 < end and data[child + 1] > data[child]:
                child += 1
            if data[child] > data[root]:
                data[root], data[child] = data[child], data[root]
                root = child
            else:
                break
    # Build the max-heap.
    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n)
    return data
```

</details>

## Durchlauf

`arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]`
N = 11. Der letzte Nicht-Blatt-Knoten ist `11 // 2 - 1 = 4`.
*(Blätter: `13, 10, 9, 8, 15, 17` werden ignoriert).*

1. **i = 4 (Wert 6):** Kinder sind an Position 9 (Wert 15) und 10 (Wert 17). Das größte Kind ist 17. Tausche 6 und 17!
   - `arr = [1, 3, 5, 4, 17, 13, 10, 9, 8, 15, 6]`.
2. **i = 3 (Wert 4):** Kinder an Position 7 (Wert 9) und 8 (Wert 8). Das größte ist 9. Tausche 4 und 9!
   - `arr = [1, 3, 5, 9, 17, 13, 10, 4, 8, 15, 6]`.
3. **i = 2 (Wert 5):** Kinder an Position 5 (Wert 13) und 6 (Wert 10). Das größte ist 13. Tausche 5 und 13!
   - `arr = [1, 3, 13, 9, 17, 5, 10, 4, 8, 15, 6]`.
4. **i = 1 (Wert 3):** Kinder an Position 3 (Wert 9) und 4 (Wert 17). Das größte ist 17. Tausche 3 und 17!
   - `arr = [1, 17, 13, 9, 3, 5, 10, 4, 8, 15, 6]`.
   - Knoten 3 wurde auf Index 4 nach unten gesiebt. Seine neuen Kinder sind 15 und 6. Tausche 3 und 15!
   - `arr = [1, 17, 13, 9, 15, 5, 10, 4, 8, 3, 6]`.
5. **i = 0 (Wert 1):** Kinder an Position 1 (Wert 17) und 2 (Wert 13). Tausche 1 und 17!
   - `arr = [17, 1, 13, 9, 15, 5, 10, 4, 8, 3, 6]`.
   - Knoten 1 kaskadiert den Baum hinunter, genau wie Knoten 3 es tat.
   - Tausche 1 mit 15. Dann tausche 1 mit 6.
   - Finales `arr = [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]`.

Das maximale Element (17) befindet sich nun perfekt an `arr[0]`! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Warum ist der Aufbau eines Heaps $O(N)$, wenn das Nach-unten-Sieben $O(\log N)$ dauert?
Die meisten Knoten in einem Baum befinden sich am Boden! Die Hälfte der Knoten sind Blätter (Höhe 0, Siebdistanz 0). Ein Viertel der Knoten befindet sich auf Höhe 1 (Siebdistanz 1). Nur der einzelne Wurzelknoten muss die volle Distanz von $\log N$ zurücklegen.
Die mathematische Summe der Reihe \sum \frac{h}{2^h} konvergiert exakt gegen $O(N)$!
Die Platzkomplexität beträgt $O(1)$ an zusätzlichem Speicher, wenn iterativ gearbeitet wird (der obige rekursive Pseudocode verwendet $O(\log N)$ Aufruf-Stack-Speicher, was leicht in eine `while`-Schleife umgewandelt werden kann).

## Varianten & Optimierungen

- **Heap Sort ($O(N \log N)$):** Sobald der Max-Heap aufgebaut ist, tauschen Sie `arr[0]` (das maximale Element) mit dem letzten Element des Arrays. Rufen Sie dann `sift_down(0)` auf die reduzierte Array-Größe auf. Wiederholen Sie dies, bis die Array-Größe 1 ist. Das Array ist nun perfekt in aufsteigender Reihenfolge sortiert!

## Anwendungen in der Praxis

- **Betriebssystem-Task-Scheduler:** Verwaltung einer Queue von Prozessen, bei der der Prozess mit der höchsten Priorität immer als nächster ausgeführt wird.

## Verwandte Algorithmen in cOde(n)

- **[heap_02 - K-th Largest Element](heap_02_kth-largest-element.md)** — Verwendet genau diesen Max-Heap-Aufbau, um schnell die obersten Elemente zu extrahieren.
- **[sort_04 - Quick Sort](../sorting/sort_04_quick-sort.md)** — Heap Sort bietet eine garantierte $O(N \log N)$ Zeitkomplexität im schlechtesten Fall, im Gegensatz zu Quick Sort, das auf $O(N^2)$ degradieren kann; Quick Sort ist jedoch aufgrund der CPU-Cache-Lokalität im Allgemeinen schneller.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*