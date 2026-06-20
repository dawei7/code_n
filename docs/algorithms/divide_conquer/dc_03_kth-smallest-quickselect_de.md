# Das k-kleinste Element (Quickselect)

| | |
|---|---|
| **ID** | `dc_03` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [K-größtes Element in einem Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) |

## Aufgabenstellung

Gegeben sei ein unsortiertes Ganzzahl-Array `nums` und eine Ganzzahl `k`. Gib das k-kleinste Element im Array zurück.
Beachte, dass es sich um das k-kleinste Element in der sortierten Reihenfolge handelt, nicht um das k-te unterschiedliche Element.
Sie müssen die Aufgabe mit einer durchschnittlichen Zeitkomplexität von $O(N)$ lösen.

*(Hinweis: Das Ermitteln des k-ten **größten** Elements erfolgt auf identische Weise; orientieren Sie sich einfach am Index `len(nums) - k`).*

**Eingabe:** Ein Ganzzahl-Array `nums` und eine Ganzzahl `k`.
**Ausgabe:** Eine Ganzzahl, die das k-kleinste Element darstellt.

## Wann man es verwendet

- Wenn Sie einen bestimmten Rang (Median, Min, Max, 10. Perzentil) in einem Array ermitteln müssen, OHNE den Aufwand $O(N \log N)$ für eine vollständige Sortierung zu betreiben.
- **Quickselect** ist der klassische „Teile und herrsche“-Algorithmus.

## Vorgehensweise

**1. Der Nachteil einer vollständigen Sortierung:**
Wenn man `nums.sort()` ausführt und `nums[k-1]` zurückgibt, dauert dies $O(N \log N)$ Zeit.
Aber die Reihenfolge der anderen Elemente ist uns egal! Uns interessiert NUR das Element, das genau am Index `k-1` landet.

**2. Die Quicksort-Partitionierung:**
Erinnerst du dich, wie Quicksort funktioniert? Man wählt einen „Pivot“ aus. Alle Zahlen, die kleiner als der Pivot sind, werden links davon abgelegt, alle größeren rechts davon.
Die magische Eigenschaft von Quicksort ist, dass nach genau einer Partition **der Pivot an seiner absoluten, endgültigen, global sortierten Position fixiert ist!**
Nehmen wir an, der Pivot landet am Index `P`.
- Wenn `P == k - 1`: Wir haben ihn gefunden! Der Pivot IST das k-kleinste Element! Wir können sofort aufhören!
- Wenn `P > k - 1`: Das k-kleinste Element MUSS sich irgendwo im linken Teil befinden. Wir verwerfen den rechten Teil vollständig und führen die Rekursion NUR auf der linken Seite durch!
- Wenn `P < k - 1`: Das k-kleinste Element MUSS sich irgendwo im rechten Teil befinden. Wir verwerfen den linken Teil und führen die Rekursion NUR auf der rechten Seite durch!

**3. „Decrease and Conquer“ vs. „Divide and Conquer“:**
Im Gegensatz zu Quicksort, das sowohl die linke als auch die rechte Hälfte rekursiv aufruft („Divide and Conquer“), verwirft Quickselect jedes Mal die Hälfte des Arrays.
Die benötigte Zeit beträgt N + N/2 + N/4 + N/8 \dots
Diese geometrische Reihe konvergiert mathematisch genau gegen 2N. Daher beträgt die durchschnittliche Zeitkomplexität streng $O(N)$!

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

## Schritt-für-Schritt-Anleitung

`nums = [3, 2, 1, 5, 6, 4]`, `k = 2` (zweitkleinste). `target_index = 1`.

1. `quickselect(0, 5)`:
   - Zufälliger Pivot: Wähle Index 5 (Wert `4`).
   - `partition`:
     - Alle mit `4` vergleichen.
 - `3 < 4` (tauschen, speichern=1)
 - `2 < 4` (tauschen, speichern=2)
     - `1 < 4` (Tauschen, Speichern=3)
 - `5`, `6` > 4 (kein Tauschen).
     - Tauschen Sie den Pivot zurück zu `store=3`.
 - `nums` ist nun `[3, 2, 1, 4, 6, 5]`. Der Pivot `4` befindet sich am Index 3.
   - `final_pivot_index = 3`.
   - `target_index (1) < 3`. Rechte Seite verwerfen! Links rekursiv weiterverarbeiten.
2. `quickselect(0, 2)`: (Fokus auf `[3, 2, 1]`)
   - Zufälliger Drehpunkt: Wähle Index 1 (Wert `2`).
   - `partition`:
 - Vergleiche alle mit `2`.
     - `nums` wird zu `[1, 2, 3]`. Der Drehpunkt `2` befindet sich am Index 1.
   - `final_pivot_index = 1`.
   - `target_index (1) == 1`. ÜBEREINSTIMMUNG!

Gibt `nums[1]` zurück, was `2` ist. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechteste** | $O(N^2)$ | $O(1)$ |

Die durchschnittliche Laufzeit beträgt $O(N)$, da sich die Array-Größe jedes Mal ungefähr halbiert (N + N/2 + N/4 ~= 2N).
Sollte man jedoch unglaubliches Pech haben und der zufällige Pivot IMMER das Element mit dem absoluten Maximalwert sein, verringert sich die Größe des Arrays jedes Mal um genau 1 Element (N + N-1 + N-2 \dots). Dies löst den verheerenden $O(N^2)$-Worst-Case-Fall aus. (Der „Median-of-Medians“-Algorithmus kann den $O(N)$-Worst-Case garantieren, ist jedoch für Vorstellungsgespräche zu komplex).
Die Platzkomplexität beträgt $O(1)$ Hilfsraum bei iterativer Ausführung oder $O(\log N)$ für die Stapeltiefe der Rekursion.

## Varianten & Optimierungen

- **Min-Heap (Priority Queue):** Die pragmatische, nicht-D&C-basierte Alternative. Elemente in einen Max-Heap mit einer strikten Größe von K einfügen. Wenn der Heap die Größe K überschreitet, das oberste (größte) Element entfernen. Am Ende ist das oberste Element des Heaps das k-kleinste Element! Die Laufzeit beträgt $O(N log K)$, was technisch gesehen schlechter ist als $O(N)$, aber den $O(N^2)$-Worst-Case-Fall vermeidet und deutlich einfacher fehlerfrei zu programmieren ist.

## Praktische Anwendungen

- **Datenbank-Abfrageplaner:** Wird in SQL-Datenbanken intensiv genutzt, um `PERCENTILE_CONT(0.5)`-Abfragen (Ermittlung des Medians) über riesige unstrukturierte Tabellen hinweg zu beantworten, ohne den Arbeitsspeicher durch das Sortieren der gesamten Tabelle zu überlasten.

## Verwandte Algorithmen in cOde(n)

- **[sort_02 – Quick Sort](../sorting/sort_02_quick-sort.md)** — Die Grundlage dieses Algorithmus, der auf BEIDEN Hälften rekursiv angewendet wird.
- **[heap_01 – K-größtes Element](../heap/heap_01_kth-largest.md)** — Der alternative $O(N log K)$-Ansatz unter Verwendung einer Priority Queue.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
