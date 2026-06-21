# Kth Smallest Element (Quickselect)

| | |
|---|---|
| **ID** | `dc_03` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) |

## Problem statement

Gegeben ist ein unsortiertes Array `nums` von Ganzzahlen und eine Ganzzahl `k`. Geben Sie das k-te kleinste Element im Array zurück.
Beachten Sie, dass es sich um das k-te kleinste Element in der sortierten Reihenfolge handelt, nicht um das k-te eindeutige Element.
Sie müssen das Problem mit einer durchschnittlichen Zeitkomplexität von $O(N)$ lösen.

*(Hinweis: Das Finden des k-ten **Größten** ist identisch; zielen Sie einfach auf den Index `len(nums) - k` ab).*

**Input:** Ein Array `nums` von Ganzzahlen und eine Ganzzahl `k`.
**Output:** Eine Ganzzahl, die das k-te kleinste Element repräsentiert.

## Wann man es verwendet

- Wenn Sie einen bestimmten Rang (Median, Minimum, Maximum, 10. Perzentil) in einem Array finden müssen, OHNE die Kosten von $O(N \log N)$ für eine vollständige Sortierung zu tragen.
- **Quickselect** ist der kanonische "Decrease and Conquer"-Algorithmus.

## Ansatz

**1. Der Nachteil der vollständigen Sortierung:**
Wenn Sie `nums.sort()` ausführen und `nums[k-1]` zurückgeben, benötigt dies $O(N \log N)$ Zeit.
Aber die Reihenfolge der anderen Elemente ist uns egal! Wir interessieren uns NUR für das Element, das exakt an Index `k-1` landet.

**2. Die Quicksort-Partitionierung:**
Erinnern Sie sich, wie Quicksort funktioniert? Sie wählen ein "Pivot"-Element. Sie verschieben alle Zahlen, die kleiner als das Pivot sind, nach links und alle Zahlen, die größer sind, nach rechts.
Die magische Eigenschaft von Quicksort ist, dass nach genau einer Partitionierung **das Pivot an seiner absoluten, endgültigen, global sortierten Position fixiert ist!**
Nehmen wir an, das Pivot landet an Index `P`.
- Wenn `P == k - 1`: Wir haben es gefunden! Das Pivot IST das k-te kleinste Element! Wir können sofort abbrechen!
- Wenn `P > k - 1`: Das k-te kleinste Element MUSS irgendwo im linken Teilbereich liegen. Wir verwerfen den rechten Teilbereich vollständig und führen die Rekursion NUR auf dem linken Teil aus!
- Wenn `P < k - 1`: Das k-te kleinste Element MUSS irgendwo im rechten Teilbereich liegen. Wir verwerfen den linken Teilbereich und führen die Rekursion NUR auf dem rechten Teil aus!

**3. Decrease and Conquer vs. Divide and Conquer:**
Im Gegensatz zu Quicksort, das rekursiv BEIDE Hälften aufruft (Divide and Conquer), verwirft Quickselect jedes Mal die Hälfte des Arrays.
Die benötigte Zeit beträgt N + N/2 + N/4 + N/8 \dots
Diese geometrische Reihe konvergiert mathematisch exakt gegen 2N. Daher ist die durchschnittliche Zeitkomplexität strikt $O(N)$!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_03: Kth Smallest (Quickselect).

Quickselect: partition the array around a pivot (Lomuto-style),
then only recurse into the half that contains the kth smallest.
O(n) average case, O(n^2) worst case on pathological data.
The setup shuffles the array first to keep the worst case rare.
"""


def solve(arr, k, n):
    if k < 1 or k > n:
        return -1
    work = list(arr)
    target = k - 1  # 0-indexed

    def select(lo, hi):
        if lo == hi:
            return work[lo]
        pivot = work[hi]
        i = lo
        for j in range(lo, hi):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi] = work[hi], work[i]
        if i == target:
            return work[i]
        if i < target:
            return select(i + 1, hi)
        return select(lo, i - 1)

    return select(0, n - 1)
```

</details>

## Durchlauf

`nums = [3, 2, 1, 5, 6, 4]`, `k = 2` (2. kleinstes). `target_index = 1`.

1. `quickselect(0, 5)`:
   - Zufälliges Pivot: wähle Index 5 (Wert `4`).
   - `partition`:
     - Vergleiche alle mit `4`.
     - `3 < 4` (Tausch, store=1)
     - `2 < 4` (Tausch, store=2)
     - `1 < 4` (Tausch, store=3)
     - `5`, `6` > 4 (kein Tausch).
     - Tausche Pivot zurück an `store=3`.
     - `nums` ist jetzt `[3, 2, 1, 4, 6, 5]`. Pivot `4` ist an Index 3.
   - `final_pivot_index = 3`.
   - `target_index (1) < 3`. Verwirf rechts! Rekursion links.
2. `quickselect(0, 2)`: (Fokus auf `[3, 2, 1]`)
   - Zufälliges Pivot: wähle Index 1 (Wert `2`).
   - `partition`:
     - Vergleiche alle mit `2`.
     - `nums` wird zu `[1, 2, 3]`. Pivot `2` ist an Index 1.
   - `final_pivot_index = 1`.
   - `target_index (1) == 1`. TREFFER!

Gibt `nums[1]` zurück, was `2` ist. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(1)$ |

Die durchschnittliche Zeit ist $O(N)$, da sich die Arraygröße jedes Mal etwa halbiert (N + N/2 + N/4 ~= 2N).
Wenn Sie jedoch extrem viel Pech haben und das zufällige Pivot IMMER das absolut größte Element ist, verringert sich die Arraygröße jedes Mal um genau 1 Element (N + N-1 + N-2 \dots). Dies führt zum verheerenden $O(N^2)$ Schlechtesten Fall. (Der Median-of-Medians-Algorithmus kann einen $O(N)$ Schlechtesten Fall garantieren, ist aber für Vorstellungsgespräche zu komplex).
Die Platzkomplexität beträgt $O(1)$ zusätzlichen Speicherplatz bei iterativer Implementierung oder $O(\log N)$ für die Tiefe des Rekursions-Stacks.

## Varianten & Optimierungen

- **Min-Heap (Priority Queue):** Die pragmatische Alternative ohne Divide and Conquer. Fügen Sie Elemente in einen Max-Heap mit einer strikten Größe von K ein. Wenn der Heap die Größe K überschreitet, entfernen Sie das oberste (größte) Element. Am Ende ist das oberste Element des Heaps das k-te kleinste Element! Die Zeit beträgt $O(N \log K)$, was technisch schlechter als $O(N)$ ist, aber den $O(N^2)$ Schlechtesten Fall vermeidet und deutlich einfacher fehlerfrei zu implementieren ist.

## Anwendungen in der Praxis

- **Datenbank-Abfrageplaner:** Wird häufig in SQL-Datenbanken verwendet, um `PERCENTILE_CONT(0.5)`-Abfragen (Finden des Medians) über riesige, unstrukturierte Tabellen hinweg zu beantworten, ohne den Arbeitsspeicher durch das Sortieren der gesamten Tabelle zu erschöpfen.

## Verwandte Algorithmen in cOde(n)

- **[sort_02 - Quick Sort](../sorting/sort_02_quick-sort.md)** — Die Grundlage dieses Algorithmus, der auf BEIDE Hälften rekursiv zugreift.
- **[heap_01 - Kth Largest Element](../heap/heap_01_kth-largest.md)** — Der alternative $O(N \log K)$-Ansatz unter Verwendung einer Priority Queue.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*