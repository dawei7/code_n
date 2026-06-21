# Kth Smallest Element in a Sorted Matrix

| | |
|---|---|
| **ID** | `heap_06` |
| **Kategorie** | heap |
| **Komplexität (erforderlich)** | $O(K log N)$ oder $O(N log(Max-Min)$) |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) |

## Problemstellung

Gegeben ist eine $N \times N$ Matrix, in der jede Zeile und jede Spalte in aufsteigender Reihenfolge sortiert ist. Geben Sie das K-te kleinste Element in der Matrix zurück.
Beachten Sie, dass es sich um das K-te kleinste Element in der sortierten Reihenfolge handelt, nicht um das K-te eindeutige Element.
Sie müssen einen Algorithmus finden, der effizienter ist als das Extrahieren aller $N^2$ Elemente und deren Sortierung ($O(N^2 log(N^2)$)).

**Eingabe:** Eine $N \times N$ Matrix und eine Ganzzahl K.
**Ausgabe:** Die K-te kleinste Ganzzahl.

## Wann man es verwendet

- Ein klassisches Problem in Vorstellungsgesprächen, das eine elegante Brücke zwischen Heaps (Priority Queues) und binärer Suche schlägt.
- Der Heap-Ansatz wird im Allgemeinen bevorzugt, wenn K klein ist. Der Ansatz mit binärer Suche wird bevorzugt, wenn K groß ist (nahe bei $N^2$).

## Ansatz

**Ansatz 1: Min-Heap (Zusammenführen von N sortierten Listen) — $O(K log N)$**
Betrachten Sie die Matrix als N unabhängige sortierte Listen (die Zeilen). Das Finden des K-ten kleinsten Elements über N sortierte Listen hinweg ist ein Standardalgorithmus für Priority Queues.
1. Initialisieren Sie einen Min-Heap.
2. Fügen Sie das erste Element *jeder Zeile* in den Heap ein. Speichern Sie ein Tupel: `(value, row, col)`.
3. Entfernen Sie das kleinste Element aus dem Heap mittels `pop`.
4. Da wir `(value, r, c)` entfernt haben, betrachten wir sofort das *nächste* Element in derselben Zeile `(r, c+1)`. Falls es existiert, fügen Sie es dem Heap hinzu!
5. Wiederholen Sie den `pop`- und `push`-Vorgang K-mal. Das K-te entfernte Element ist Ihre Antwort.

**Ansatz 2: Binäre Suche über den Wertebereich — $O(N log(\text{Max} - \text{Min})$)**
Wir suchen nicht nach Indizes, wir suchen nach *Werten*!
1. Der absolut kleinste Wert ist `matrix[0][0]`. Der absolut größte ist `matrix[N-1][N-1]`.
2. Führen Sie eine binäre Suche nach einem `mid`-Wert durch.
3. Wie viele Elemente in der Matrix sind $\le mid$?
   - Da die Spalten sortiert sind, können wir dies in $O(N)$ Zeit zählen! Beginnen Sie an der unteren linken Ecke. Wenn der Wert > mid ist, bewegen Sie sich NACH OBEN. Wenn er $\le mid$ ist, bedeutet dies, dass *alles darüber in dieser Spalte* ebenfalls $\le mid$ ist! Addieren Sie `row + 1` zum Zähler und bewegen Sie sich NACH RECHTS.
4. Wenn `count < k`, muss das K-te Element größer sein. `low = mid + 1`.
5. Wenn `count >= k`, könnte das K-te Element `mid` oder kleiner sein. `high = mid`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for heap_06: Kth Smallest in a Sorted Matrix.

A matrix where every row and every column is sorted. The first
column is not necessarily sorted, but the matrix has the property
that the smallest element is in [0][0]. Use a min-heap of
(value, row, col) and pop k times.
"""


def solve(matrix, n, k):
    if n == 0 or k <= 0:
        return -1
    import heapq
    heap = [(matrix[0][0], 0, 0)]
    seen = {(0, 0)}
    popped = 0
    while heap:
        v, r, c = heapq.heappop(heap)
        popped += 1
        if popped == k:
            return v
        for dr, dc in [(0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc
            if nr < n and nc < n and (nr, nc) not in seen:
                heapq.heappush(heap, (matrix[nr][nc], nr, nc))
                seen.add((nr, nc))
    return -1
```

</details>

## Durchlauf

*(Heap-Ansatz)*
Matrix:
`[ 1,  5,  9]`
`[10, 11, 13]`
`[12, 13, 15]`
`K = 8`.

1. **Heap initialisieren:** `[(1, 0,0), (10, 1,0), (12, 2,0)]`.
2. **Pop 1:** `1` entfernt. `matrix[0][1]=5` hinzufügen. Heap: `[5, 10, 12]`.
3. **Pop 2:** `5` entfernt. `matrix[0][2]=9` hinzufügen. Heap: `[9, 10, 12]`.
4. **Pop 3:** `9` entfernt. Nichts mehr in Zeile 0. Heap: `[10, 12]`.
5. **Pop 4:** `10` entfernt. `11` hinzufügen. Heap: `[11, 12]`.
6. **Pop 5:** `11` entfernt. `13` hinzufügen. Heap: `[12, 13]`.
7. **Pop 6:** `12` entfernt. `13` hinzufügen. Heap: `[13, 13]`.
8. **Pop 7:** `13` (aus Zeile 1) entfernt. `15` hinzufügen (HALT, Zeile 1 endet bei 13). Kein `push`. Heap: `[13]`.
9. **Pop 8:** `13` (aus Zeile 2) entfernt. FERTIG!
Ergebnis = 13. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall (Heap)** | $O(K log(min(N, K)$)) | $O(min(N, K)$) |
| **Bestfall (BS)** | $O(N log(Max - Min)$) | $O(1)$ |

**Heap:** Der Heap enthält maximal $\min(N, K)$ Elemente. Wir führen genau K `pop`/`push`-Operationen durch. Die Zeitkomplexität beträgt $O(K log(\min(N, K)))$. Die Platzkomplexität beträgt $O(\min(N, K))$ für das Heap-Array.
**Binäre Suche:** Der Wertebereich ist $W = Max - Min$. Die binäre Suche halbiert diesen Bereich, was $log_2 W$ Schritte erfordert. Jeder Schritt durchläuft die Treppenstruktur der Matrix in genau $O(N)$ Zeit. Die Zeitkomplexität beträgt $O(N log W)$. Die Platzkomplexität ist strikt $O(1)$.

## Varianten & Optimierungen

- **Selektion in X+Y:** Gegeben zwei unsortierte Arrays X und Y der Größe N, finden Sie die K-te kleinste Summe $X[i] + Y[j]$. Wenn Sie X und Y sortieren, transformiert sich das Problem sofort perfekt in das Finden des K-ten kleinsten Elements in einer impliziten sortierten Matrix, wobei `matrix[i][j] = X[i] + Y[j]` gilt! Sie müssen die Matrix nicht einmal explizit erstellen, sondern können den Heap-Ansatz mathematisch anwenden.

## Anwendungen in der Praxis

- **Multi-Sensor-Fusion:** Aggregation paralleler, unabhängig sortierter Datenströme von zeitgestempelten Telemetriedaten und Extraktion des K-ten historischen Ereignisses über alle Ströme hinweg.

## Verwandte Algorithmen in cOde(n)

- **[heap_02 - Kth Largest Element](heap_02_kth-largest-element.md)** — Die 1D-Variante.
- **[sort_03 - Merge Sort](../sorting/sort_03_merge-sort.md)** — Der Heap-Ansatz entspricht buchstäblich dem `Merge`-Schritt eines K-Wege-Merge-Sorts.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*