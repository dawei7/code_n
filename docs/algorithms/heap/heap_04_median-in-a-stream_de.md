# Find Median from Data Stream

| | |
|---|---|
| **ID** | `heap_04` |
| **Category** | heap |
| **Complexity (required)** | $O(\log N)$ insert, $O(1)$ query |
| **Difficulty** | 7/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) |

## Problem statement

Entwerfen Sie eine Datenstruktur, die die folgenden Operationen unterstützt:
1. `addNum(int num)`: Fügt eine Ganzzahl `num` aus einem Datenstrom zur Datenstruktur hinzu.
2. `findMedian()`: Gibt den Median aller bisherigen Elemente zurück. Der Median ist der mittlere Wert in einer sortierten Liste von Ganzzahlen. Wenn die Größe der Liste gerade ist, gibt es keinen einzelnen mittleren Wert; in diesem Fall ist der Median der Mittelwert der beiden mittleren Werte.

Sie müssen einen endlosen Strom eingehender Ganzzahlen verarbeiten und dabei die Fähigkeit beibehalten, den exakten Median in $O(1)$ Zeit zurückzugeben und neue Zahlen in $O(\log N)$ Zeit einzufügen.

**Input:** Ein Strom von Zahlen, bei dem `addNum` aufgerufen wird, durchsetzt mit `findMedian`-Abfragen.
**Output:** Fließkommazahlen, die den aktuellen Median repräsentieren.

## Wann man es verwendet

- Eine klassische Interview-Frage zum Systemdesign bzw. zu Datenstrukturen.
- Immer dann, wenn Sie dynamischen Zugriff auf die exakte Mitte eines sich ändernden Datensatzes benötigen, ohne das gesamte Array zu sortieren ($O(N \log N)$) oder einen balancierten BST zu pflegen (was komplex in der Implementierung ist).

## Ansatz

**Das Zwei-Heap-Muster:**
Stellen Sie sich die sortierte Version unseres Datenstroms vor. Wir möchten eine Linie exakt durch die Mitte ziehen.
Alle Zahlen in der linken Hälfte der Linie sind \le dem Median. Alle Zahlen in der rechten Hälfte sind \ge dem Median.
Wenn wir die absolut **größte** Zahl der linken Hälfte und die absolut **kleinste** Zahl der rechten Hälfte kennen, kennen wir sofort den Median!

Wir können diesen Zustand exakt mit zwei Priority Queues aufrechterhalten:
1. **Max-Heap (`lo`):** Speichert die kleinere Hälfte der Zahlen. Die Wurzel ist das *größte* Element der kleinen Zahlen.
2. **Min-Heap (`hi`):** Speichert die größere Hälfte der Zahlen. Die Wurzel ist das *kleinste* Element der großen Zahlen.

**Der Balanceakt:**
Um den Median zu wahren, müssen wir zwei strikte Regeln durchsetzen:
1. **Werteintegrität:** JEDE Zahl im `lo` Max-Heap muss \le JEDER Zahl im `hi` Min-Heap sein.
2. **Größenbalance:** Die Größen der beiden Heaps dürfen sich um maximal 1 unterscheiden. Wir legen willkürlich fest, dass bei einer ungeraden Gesamtzahl der `lo` Max-Heap das zusätzliche Element enthält.

**Einfügelogik:**
1. Fügen Sie die neue Zahl immer zuerst in den `lo` Max-Heap ein.
2. Aber Vorsicht! Die Zahl, die wir gerade eingefügt haben, gehört möglicherweise eigentlich in die `hi`-Hälfte (sie könnte größer sein als das minimale Element in `hi`). Um dies zu korrigieren, führen wir bedingungslos ein `pop` des größten Elements aus `lo` durch und `push` es in `hi`!
3. Nun haben `lo` und `hi` eine perfekte Werteintegrität. Aber was ist mit der Größenbalance?
4. Wenn `hi` plötzlich mehr Elemente als `lo` hat, führen wir ein `pop` des kleinsten Elements aus `hi` durch und `push` es zurück in `lo`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for heap_04: Median in a Stream.

Two heaps: a max-heap of the smaller half, a min-heap of the
larger half. After each insert, rebalance so the two heaps are
within 1 of each other; the median is the top of the larger
heap (odd length) or the average of the two tops (even).
"""


def solve(data, n):
    import heapq
    if n == 0:
        return []
    small = []  # max-heap (inverted)
    large = []  # min-heap
    out = []
    for value in data:
        # Insert into the appropriate heap.
        if not small or value <= -small[0]:
            heapq.heappush(small, -value)
        else:
            heapq.heappush(large, value)
        # Rebalance.
        if len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        elif len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))
        # Compute the median.
        if len(small) > len(large):
            out.append(-small[0])
        else:
            out.append((-small[0] + large[0]) / 2)
    return out
```

</details>

## Durchlauf

Strom: `1, 2, 3`

1. **`addNum(1)`:**
   - Push `-1` zu `lo`. `lo = [-1]`.
   - Pop `lo` -> `1`. Push `1` zu `hi`. `hi = [1]`.
   - Größenprüfung: `len(lo)=0 < len(hi)=1`.
   - Pop `hi` -> `1`. Push `-1` zu `lo`. `lo = [-1]`, `hi = []`.
   - `findMedian()`: Größen ungleich. Median ist `-(-1) = 1.0`. ✓

2. **`addNum(2)`:**
   - Push `-2` zu `lo`. `lo = [-2, -1]`.
   - Pop `lo` (größtes ist `-1`, also `1`). Push `1` zu `hi`. `hi = [1]`. `lo = [-2]`.
   - Größenprüfung: `len(lo)=1 == len(hi)=1`. Keine Aktion.
   - `findMedian()`: Größen gleich. Mittelwert von `2` und `1` = `1.5`. ✓

3. **`addNum(3)`:**
   - Push `-3` zu `lo`. `lo = [-3, -2]`.
   - Pop `lo` (`2`). Push `2` zu `hi`. `hi = [1, 2]`. `lo = [-3]`.
   - Größenprüfung: `len(lo)=1 < len(hi)=2`.
   - Pop `hi` (`1`). Push `-1` zu `lo`. `lo = [-1, -3]`, `hi = [2]`.
   - `findMedian()`: Größen ungleich. Median ist `-(-1) = 2.0`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(N)$ |

Jeder `addNum`-Aufruf löst 2 oder 3 Heap-Operationen aus. `heappush` und `heappop` benötigen exakt $O(\log N)$ Zeit.
Jeder `findMedian`-Aufruf liest lediglich `heap[0]`, was exakt $O(1)$ Zeit benötigt.
Die Platzkomplexität beträgt $O(N)$, da die Heaps permanent alle Elemente des Stroms speichern.

## Varianten & Optimierungen

- **Order Statistic Tree:** Wenn Sie einen Fenwick Tree mit Binary Lifting (`fenwick_07`) verwenden, können Sie *jedes beliebige* Perzentil (K-tes Element) in $O(\log M)$ Zeit finden, wobei M der Maximalwert ist. Der Zwei-Heap-Ansatz ist strikt auf das Finden des exakten 50. Perzentils (Median) ausgelegt, erfordert jedoch keine Begrenzung der Input-Werte!
- **Count Array (Falls Input-Werte klein sind):** Wenn garantiert ist, dass der Strom nur Ganzzahlen von 0 \dots 100 enthält, benötigen Sie keine Heaps! Pflegen Sie einfach ein Array mit 101 Zählern $O(1)$ und eine `total_count`-Variable. Das Finden des Medians benötigt $O(100) = O(1)$, indem Sie durch das Array iterieren, bis der kumulative Zähler `total_count // 2` erreicht.

## Anwendungen in der Praxis

- **Netzwerk-Monitoring:** Dynamische Berechnung der mittleren Ping-Antwortzeit, um eine Basislinie für Warnmeldungen zu etablieren, ohne historische Protokolle neu berechnen zu müssen.

## Verwandte Algorithmen in cOde(n)

- **[heap_05 - Sliding Window Maximum](heap_05_sliding-window-maximum.md)** — Ein weiterer Streaming-Algorithmus, der jedoch das Entfernen abgelaufener Elemente aus dem Arbeitsset handhabt.
- **[fenwick_07 - K-th Smallest / Order Statistic](../fenwick/fenwick_07_k-th-smallest-order-statistic-bit.md)** — Die algebraische Alternative, die das Abfragen beliebiger Perzentile ermöglicht.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*