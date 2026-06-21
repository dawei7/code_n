# K-th Largest Element

| | |
|---|---|
| **ID** | `heap_02` |
| **Kategorie** | heap |
| **Komplexität (erforderlich)** | $O(N log K)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) |

## Problemstellung

Gegeben ist ein unsortiertes Array von Integern `nums` und ein Integer `k`. Geben Sie das `k`-größte Element im Array zurück.
Beachten Sie, dass es sich um das `k`-größte Element in der sortierten Reihenfolge handelt, nicht um das `k`-te eindeutige Element.
Während das Sortieren des Arrays $O(N \log N)$ Zeit in Anspruch nimmt, müssen Sie eine Priority Queue (Heap) verwenden, um eine Zeitkomplexität von $O(N log K)$ zu erreichen.

**Eingabe:** Ein unsortiertes Array von Integern und ein Integer K.
**Ausgabe:** Der Integer, der das K-größte Element repräsentiert.

## Wann man es verwendet

- Dies ist eine der am häufigsten gestellten grundlegenden Fragen in Vorstellungsgesprächen.
- Verwenden Sie diesen spezifischen $O(N log K)$ Min-Heap-Ansatz bei Problemen mit **Streaming-Daten**, bei denen N praktisch unendlich ist und Sie nicht das gesamte Array im Arbeitsspeicher halten können.

## Ansatz

Ein naiver Heap-Ansatz fügt alle N Elemente in $O(N)$ Zeit in einen Max-Heap ein (`heap_01`) und entnimmt dann K-mal das maximale Element, was $O(K log N)$ dauert. Dies ist schnell, erfordert jedoch, dass Speicher für alle N Elemente gleichzeitig reserviert wird.

**Die Min-Heap-Strategie ($O(N log K)$):**
Wenn wir nur das K-größte Element suchen, interessieren uns alle kleineren Elemente nicht!
Wir können einen **Min-Heap** mit einer strikten Größe von K verwalten. Dieser Heap fungiert als "VIP-Club", der nur die K größten Elemente enthält, die wir bisher gesehen haben.
Da es sich um einen Min-Heap handelt, befindet sich das *kleinste* Element in diesem VIP-Club immer an der Spitze (`heap[0]`).

1. Iterieren Sie durch das Array.
2. Fügen Sie jedes Element in den Min-Heap ein.
3. Wenn die Größe des Heaps K überschreitet, führen wir sofort ein `pop()` aus! Der Min-Heap garantiert, dass wir gerade das kleinste Element aus dem VIP-Club entfernt haben.
4. Wenn die Schleife endet, enthält der Heap genau die K größten Elemente aus dem gesamten Array.
5. Das Element an der Spitze des Min-Heaps (`heap[0]`) ist das kleinste dieser K größten Elemente... was exakt dem **K-größten Element insgesamt** entspricht!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for heap_02: Kth Largest Element.

Maintain a min-heap of size k. For each element, push it onto
the heap and pop the smallest if the heap is over k. At the end
the heap contains the k largest elements; the smallest of those
(the heap top) is the kth largest. O(n log k).
"""


def solve(data, n, k):
    import heapq
    if k <= 0 or k > n:
        return -1
    heap = []
    for value in data:
        if len(heap) < k:
            heapq.heappush(heap, value)
        elif value > heap[0]:
            heapq.heapreplace(heap, value)
    return heap[0]
```

</details>

## Durchlauf

`nums = [3, 2, 1, 5, 6, 4]`, `k = 2`.

1. **Push 3:** `min_heap = [3]`. (Größe 1 \le 2).
2. **Push 2:** `min_heap = [2, 3]`. (Größe 2 \le 2).
3. **Push 1:** `min_heap = [1, 3, 2]`. (Größe 3 > 2).
   - Pop! Das kleinste Element `1` wird entfernt. `min_heap = [2, 3]`.
4. **Push 5:** `min_heap = [2, 3, 5]`. (Größe 3 > 2).
   - Pop! Das kleinste Element `2` wird entfernt. `min_heap = [3, 5]`.
5. **Push 6:** `min_heap = [3, 5, 6]`. (Größe 3 > 2).
   - Pop! Das kleinste Element `3` wird entfernt. `min_heap = [5, 6]`.
6. **Push 4:** `min_heap = [4, 6, 5]`. (Größe 3 > 2).
   - Pop! Das kleinste Element `4` wird entfernt. `min_heap = [5, 6]`.

Die Schleife endet! Der Heap ist `[5, 6]`. Das zweitgrößte Element insgesamt befindet sich an der Spitze des Min-Heaps: `5`! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N log K)$ | $O(K)$ |
| **Durchschnittlicher Fall** | $O(N log K)$ | $O(K)$ |
| **Schlechtester Fall** | $O(N log K)$ | $O(K)$ |

Wir iterieren durch N Elemente. Für jedes Element führen wir ein Push und möglicherweise ein Pop auf einem Heap der maximalen Größe K aus. Heap-Operationen bei Größe K benötigen $O(log K)$. Die Gesamtlaufzeit beträgt exakt $O(N log K)$.
Die Platzkomplexität beträgt strikt $O(K)$, um die VIP-Elemente zu speichern. Dies macht den Ansatz perfekt für massive Datenströme, bei denen N in die Milliarden geht, K aber nur 100 beträgt.

## Varianten & Optimierungen

- **Quickselect ($O(N)$ Durchschnitt):** Der in der Praxis absolut schnellste Algorithmus, wenn alle Daten im Arbeitsspeicher verfügbar sind. Er verwendet die Partitionierungslogik von Quick Sort. Wenn Sie zufällig ein Pivot-Element wählen und das Array partitionieren, wissen Sie genau, wie viele Elemente größer als das Pivot sind. Wenn es exakt K-1 größere Elemente gibt, ist das Pivot das K-größte Element! Er benötigt im Durchschnitt $O(N)$ Zeit, verschlechtert sich jedoch im schlechtesten Fall auf $O(N^2)$.
- **Max-Heap ($O(N + K log N)$):** Wie besprochen benötigt `build_max_heap` $O(N)$ und K Pops benötigen $O(K log N)$. Wenn K sehr klein ist, ist dies mathematisch gesehen schneller als der $O(N log K)$ Min-Heap-Ansatz! Er benötigt jedoch $O(N)$ Platz.

## Praxisanwendungen

- **Twitter Trending Topics:** Ein Streaming-Aggregator, der die K meistdiskutierten Hashtags aus Millionen von Live-Tweets identifiziert.
- **Aktienmarkt:** Ermittlung der 10 meistgehandelten Aktien in Echtzeit.

## Verwandte Algorithmen in cOde(n)

- **[heap_03 - Top K Frequent Elements](heap_03_top-k-frequent-elements.md)** — Eine direkte Erweiterung dieses VIP-Club-Musters, angewendet auf Häufigkeits-Maps.
- **[sort_04 - Quick Sort](../sorting/sort_04_quick-sort.md)** — Die Grundlage der $O(N)$ Quickselect-Alternative.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*