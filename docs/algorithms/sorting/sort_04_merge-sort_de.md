# Merge Sort

| | |
|---|---|
| **ID** | `sort_04` |
| **Kategorie** | sorting |
| **Komplexität (erforderlich)** | $O(n log n)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Merge sort](https://en.wikipedia.org/wiki/Merge_sort) |

## Problemstellung

Gegeben sei ein Array von Integern `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge unter Verwendung des Merge-Sort-Algorithmus.

**Eingabe:** Ein unsortiertes Array von Integern `arr`.
**Ausgabe:** Das Array, sortiert in strikt aufsteigender Reihenfolge.

**Beispiel:**
| Eingabe `arr` | Ausgabe |
|---|---|
| `[38, 27, 43, 3, 9, 82, 10]` | `[3, 9, 10, 27, 38, 43, 82]` |

## Wann man es verwendet

- Wenn Sie einen garantierten $O(n log n)$ Sortieralgorithmus benötigen, der **stabil** ist (d. h. die relative Reihenfolge von gleichen Elementen bleibt erhalten).
- Beim Sortieren riesiger Datensätze, die nicht in den RAM passen. Merge Sort ist die Grundlage für **External Sorting**, da es ermöglicht, Datenblöcke von einer Festplatte zu lesen, zu sortieren und sauber wieder auf die Festplatte zurückzuführen.
- Beim Sortieren von Linked Lists. Da Merge Sort sequenziell traversiert und keinen wahlfreien Zugriff (wie Heap Sort oder Quick Sort) benötigt, sortiert es Linked Lists optimal in $O(n log n)$ Zeit und mit strikt $O(1)$ zusätzlichem Speicherplatz!

## Ansatz

Merge Sort ist das Lehrbuchbeispiel für einen **Divide and Conquer**-Algorithmus.

1. **Divide (Teilen):** Teilen Sie das Array rekursiv in zwei Hälften, bis jedes Sub-Array genau 1 Element enthält. Ein Array der Länge 1 ist mathematisch gesehen bereits sortiert!
2. **Conquer (Mischen):** Nehmen Sie zwei benachbarte sortierte Sub-Arrays und führen Sie diese zu einem einzigen, größeren sortierten Array zusammen. Dies erreichen wir, indem wir zwei Pointer am Anfang beider Sub-Arrays führen, wiederholt das kleinere der beiden Elemente auswählen und es in ein temporäres Array einfügen.
3. Wiederholen Sie den Mischvorgang entlang des Rekursionsbaums, bis das gesamte Array wieder zusammengesetzt ist.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_04: Merge Sort.

Divide the array in half, sort each half recursively, then merge
the two sorted halves. O(n log n) time, O(n) extra space.
"""


def solve(data, n):
    def merge_sort(items):
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left = merge_sort(items[:mid])
        right = merge_sort(items[mid:])
        return _merge(left, right)

    def _merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    sorted_items = merge_sort(data)
    # Copy back into the player's list so the in-place contract
    # is satisfied. Each `data[i] = value` counts as one write
    # in the AST op count.
    for i, value in enumerate(sorted_items):
        data[i] = value
    return data
```

</details>

## Ablaufbeispiel

Sei `arr = [38, 27, 43, 3]`.

**1. Divide-Phase (Rekursion nach unten)**
- `[38, 27, 43, 3]` wird in `[38, 27]` und `[43, 3]` aufgeteilt.
- `[38, 27]` wird in `[38]` und `[27]` aufgeteilt.
- `[43, 3]` wird in `[43]` und `[3]` aufgeteilt.

**2. Conquer-Phase (Mischen nach oben)**
- Mische `[38]` und `[27]`. Vergleiche 38 und 27. 27 ist kleiner. Das Array wird zu `[27, 38]`.
- Mische `[43]` und `[3]`. Vergleiche 43 und 3. 3 ist kleiner. Das Array wird zu `[3, 43]`.
- Mische `[27, 38]` und `[3, 43]`:
  - Pointer bei `27` und `3`. `3` ist kleiner. Füge `3` hinzu.
  - Pointer bei `27` und `43`. `27` ist kleiner. Füge `27` hinzu.
  - Pointer bei `38` und `43`. `38` ist kleiner. Füge `38` hinzu.
  - Linkes Array ist leer. Füge das verbleibende rechte Element `43` hinzu.
- Finales Array: `[3, 27, 38, 43]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n log n)$ | $O(n)$ |
| **Durchschnittlicher Fall** | $O(n log n)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n log n)$ | $O(n)$ |

Das Array wird wiederholt halbiert, was zu einem Rekursionsbaum der Tiefe `log n` führt. Auf jeder Ebene des Baums erfordert das Mischen der Arrays, dass alle `n` Elemente genau einmal berührt werden ($O(n)$). Daher ist die Zeitkomplexität strikt `O(n) * O(log n) = O(n log n)`.
Im Gegensatz zu Quicksort oder Heapsort erfordert Merge Sort die Zuweisung eines temporären Arrays während der Mischphase, um die sortierten Elemente zu halten. Dies führt zu einer zusätzlichen Platzkomplexität von $O(n)$.

## Varianten & Optimierungen

- **Bottom-Up Merge Sort:** Anstatt einer rekursiven Teilung betrachtet man das Array als `n` Sub-Arrays der Größe 1. Man iteriert durch das Array und mischt Paare zu Arrays der Größe 2, dann 4, dann 8 usw. Dies eliminiert den Overhead des Rekursions-Stacks vollständig.
- **In-Place Merge Sort:** Eine hochkomplexe Variante, die es schafft, Arrays mit $O(1)$ zusätzlichem Speicherplatz zu mischen, meist durch Block-Swapping (wie beim *WikiSort*-Algorithmus). Der konstante Zeit-Overhead ist jedoch massiv, was ihn in der Praxis unbrauchbar macht.

## Anwendungen in der Praxis

- **External Sorting / Datenbanken:** Wenn eine Postgres-Datenbank eine Tabelle mit einer Größe von 500 GB sortieren muss (`ORDER BY`), passt diese nicht in 16 GB RAM. Sie streamt Blöcke in den RAM, sortiert diese, schreibt sie als "Runs" auf die Festplatte und liest und *mischt* die Runs dann sequenziell wieder auf die Festplatte zurück.
- **Timsort-Grundlage:** Der Standard-Sortieralgorithmus für Python und Java ist im Wesentlichen ein optimierter Bottom-Up Merge Sort!

## Verwandte Algorithmen in cOde(n)

- **[sort_05 - Quick Sort](sort_05_quick-sort.md)** — Der andere berühmte $O(n log n)$ Divide-and-Conquer-Algorithmus.
- **[sort_13 - Timsort](sort_13_tim-sort-simplified.md)** — Der moderne Produktionsalgorithmus, der stark von Merge Sort abgeleitet ist.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den enzyklopädischen Standardeintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*