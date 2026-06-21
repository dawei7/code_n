# Quick Sort

| | |
|---|---|
| **ID** | `sort_05` |
| **Kategorie** | Sortieren |
| **Komplexität (erforderlich)** | $O(n log n)$ |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Quicksort](https://en.wikipedia.org/wiki/Quicksort) |

## Problemstellung

Gegeben sei ein Array von Integern `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge unter Verwendung des Quick-Sort-Algorithmus.

**Eingabe:** Ein unsortiertes Array von Integern `arr`.
**Ausgabe:** Das Array, sortiert in strikt aufsteigender Reihenfolge.

**Beispiel:**
| Eingabe `arr` | Ausgabe |
|---|---|
| `[10, 80, 30, 90, 40, 50, 70]` | `[10, 30, 40, 50, 70, 80, 90]` |

## Wann man es verwendet

- Wenn Sie einen hocheffizienten Allzweck-Sortieralgorithmus benötigen. Er ist der Standard-Sortieralgorithmus (`std::sort`) in C++ und vielen anderen Sprachen, da sein Overhead durch konstante Faktoren extrem gering ist.
- Wenn der Speicherplatz begrenzt ist. Im Gegensatz zu Merge Sort, das $O(n)$ zusätzlichen Speicherplatz benötigt, ist Quick Sort ein **in-place** Sortierverfahren, das nur $O(log n)$ Platz für den rekursiven Aufruf-Stack benötigt.
- Wenn Caching und Speicherlokalität wichtig sind. Der Partitionierungsschritt durchläuft den Speicher sequenziell, was hervorragend mit CPU-Hardware-Caches harmoniert.

## Ansatz

Quick Sort ist ein **Divide and Conquer**-Algorithmus, der auf dem Konzept der Partitionierung basiert.

1. **Wähle ein Pivot-Element:** Wählen Sie ein Element aus dem Array als Pivot. Gängige Strategien sind die Wahl des letzten Elements, des ersten Elements, eines zufälligen Elements oder des Medians aus drei Elementen.
2. **Partitionierung:** Ordnen Sie das Array so um, dass alle Elemente, die kleiner als das Pivot sind, links davon stehen, und alle Elemente, die größer als das Pivot sind, rechts davon. Am Ende dieses Schrittes befindet sich das Pivot-Element dauerhaft an seiner korrekten sortierten Position.
3. **Rekursion:** Wenden Sie die oben genannten Schritte rekursiv auf das Sub-Array der Elemente kleiner als das Pivot und auf das Sub-Array der Elemente größer als das Pivot an.

Das gebräuchlichste Partitionierungsschema ist das **Lomuto-Partitionsschema** (einfacher, verwendet das letzte Element) oder das **Hoare-Partitionsschema** (schneller, verwendet zwei Pointer, die sich aufeinander zubewegen).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_05: Quick Sort.

Three-way (Dutch National Flag) partition so duplicate keys are
handled in O(n) instead of O(n^2), then drive the recursion
iteratively. Three-way partition is the standard textbook fix
for quicksort's classic "all-equal" infinite loop with Lomuto
partition + the <= comparator, and it also halves the op count
on real data with duplicates.
"""


def solve(data, n):
    def partition_3way(items, low, high):
        # Dutch National Flag partition: items[low..lt-1] are < pivot,
        # items[lt..i-1] are == pivot, items[gt+1..high] are > pivot.
        pivot = items[high]
        lt = low
        i = low
        gt = high
        while i <= gt:
            if items[i] < pivot:
                items[lt], items[i] = items[i], items[lt]
                lt += 1
                i += 1
            elif items[i] > pivot:
                items[i], items[gt] = items[gt], items[i]
                gt -= 1
            else:
                i += 1
        return lt, gt

    stack = [(0, n - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            lt, gt = partition_3way(data, low, high)
            # Both halves may be non-empty.
            if lt - 1 > low:
                stack.append((low, lt - 1))
            if gt + 1 < high:
                stack.append((gt + 1, high))

    return data
```

</details>

## Ablaufbeispiel

Sei `arr = [10, 80, 30, 90, 40, 50, 70]`. `low = 0`, `high = 6`.

**Partitionierung (Pivot = 70):**
- `i = -1`
- `j=0` (10): `10 < 70`. `i=0`. Tausche `arr[0]` mit `arr[0]`. `[10, 80, 30, 90, 40, 50, 70]`
- `j=1` (80): `80 > 70`. Keine Aktion.
- `j=2` (30): `30 < 70`. `i=1`. Tausche `arr[1]` (80) mit `arr[2]` (30). `[10, 30, 80, 90, 40, 50, 70]`
- `j=3` (90): `90 > 70`. Keine Aktion.
- `j=4` (40): `40 < 70`. `i=2`. Tausche `arr[2]` (80) mit `arr[4]` (40). `[10, 30, 40, 90, 80, 50, 70]`
- `j=5` (50): `50 < 70`. `i=3`. Tausche `arr[3]` (90) mit `arr[5]` (50). `[10, 30, 40, 50, 80, 90, 70]`
- Schleife endet. Tausche `arr[i+1]` (80) mit `pivot` (70).
- Finales partitioniertes Array: `[10, 30, 40, 50, 70, 90, 80]`.
- Rückgabe des Pivot-Index `4`.

Das Pivot-Element `70` ist perfekt platziert. Wir führen nun rekursiv `quick_sort` auf dem linken Sub-Array `[10, 30, 40, 50]` und dem rechten Sub-Array `[90, 80]` aus.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n log n)$ | $O(log n)$ |
| **Durchschnittlicher Fall** | $O(n log n)$ | $O(log n)$ |
| **Schlechtester Fall** | $O(n^2)$ | $O(n)$ |

Die Zeitkomplexität hängt stark von der Wahl des Pivot-Elements ab. Wenn das Pivot das Array jedes Mal exakt halbiert, ist der Rekursionsbaum `log n` tief und wir leisten auf jeder Ebene `n` Arbeit, was zu $O(n log n)$ führt.
Wenn das Array jedoch bereits sortiert ist und wir das letzte Element als Pivot wählen, isoliert die Partitionierung nur 1 Element pro Ebene. Dies führt zu einem katastrophalen Rekursionsbaum der Tiefe `n`, was eine Zeitkomplexität von $O(n^2)$ und das Risiko einer Stack-Overflow-Exception aufgrund von $O(n)$ Platzbedarf zur Folge hat.
Um dies abzumildern, werden randomisierte Pivots oder die "Median-of-3"-Strategie verwendet, um im Durchschnitt $O(n log n)$ zu garantieren.

## Varianten & Optimierungen

- **3-Way Quicksort (Dutch National Flag):** Anstatt in zwei Gruppen (< Pivot, > Pivot) zu partitionieren, wird in drei Gruppen (<, ==, >) unterteilt. Dies eliminiert das $O(n^2)$-Worst-Case-Verhalten von Quicksort bei Arrays, die viele doppelte Elemente enthalten, vollständig.
- **Introsort:** Beginnt als Quicksort, überwacht jedoch die Rekursionstiefe. Wenn die Tiefe `2 * log n` überschreitet, geht der Algorithmus davon aus, dass die Pivots ungünstig gewählt wurden, und wechselt vollständig zu **Heap Sort**, um strikt eine $O(n log n)$-Worst-Case-Garantie zu bieten.

## Anwendungen in der Praxis

- **Standardbibliotheken von Programmiersprachen:** Variationen von Quicksort (meist Introsort) bilden das Rückgrat von C++ `std::sort`, Go's `sort.Slice` und vielen Java-Primitive-Arrays (`Arrays.sort(int[])` verwendet Dual-Pivot Quicksort).

## Verwandte Algorithmen in cOde(n)

- **[sort_04 - Merge Sort](sort_04_merge-sort.md)** — Die stabile $O(n log n)$-Alternative, die $O(n)$ Speicherplatz opfert, um den $O(n^2)$-Worst-Case von Quicksort zu vermeiden.
- **[sort_14 - Introsort](sort_14_intro-sort-simplified.md)** — Der produktive Algorithmus, der die Schwachstellen von Quicksort im Worst-Case behebt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*