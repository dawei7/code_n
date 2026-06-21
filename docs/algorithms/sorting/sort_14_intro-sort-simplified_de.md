# Intro Sort (Introspective Sort)

| | |
|---|---|
| **ID** | `sort_14` |
| **Kategorie** | Sortieren |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(\log N)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **Wikipedia** | [Introsort](https://en.wikipedia.org/wiki/Introsort) |

## Problemstellung

Gegeben sei ein Array von Integern `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge.
Sie müssen einen hybriden Algorithmus verwenden, der die exzellente Durchschnittsgeschwindigkeit von Quicksort garantiert, aber physisch verhindert, dass Quicksort jemals in seinen mathematischen $O(N^2)$ Schlechtesten Fall abfällt.

**Eingabe:** Ein unsortiertes Array von Integern `arr`.
**Ausgabe:** Ein sortiertes Array.

## Wann man es verwendet

- Wenn Sie `std::sort()` in C++ aufrufen. Dies IST der Algorithmus, der im Hintergrund ausgeführt wird!
- Wenn Sie zwingend eine In-Place-Sortierung mit $O(\log N)$ Platz benötigen, was Merge Sort und Tim Sort (die $O(N)$ zusätzlichen Speicher für Arrays benötigen) ausschließt.

## Ansatz

**1. Der fatale Fehler von Quicksort (`sort_05`):**
Quicksort ist mathematisch gesehen im Durchschnitt der schnellste vergleichsbasierte Sortieralgorithmus der Welt. Wenn das Array jedoch bereits sortiert (oder umgekehrt sortiert) ist und man ein schlechtes Pivot-Element wählt, wird der Rekursionsbaum extrem unausgewogen. Die Rekursion geht $N$ Ebenen tief, benötigt $O(N^2)$ Zeit und riskiert einen Stack-Overflow-Speicherabsturz!

**2. Die Introspektions-Strategie (Selbstwahrnehmung):**
Intro Sort wurde 1997 von David Musser erfunden und "introspektiert" (beobachtet sein eigenes Verhalten) buchstäblich während der Laufzeit.
Wir beginnen mit der Ausführung von Standard-Quicksort, übergeben jedoch einen `depth_limit`-Parameter an die rekursive Funktion!
Die optimale Tiefe für einen perfekt ausbalancierten Quicksort-Baum beträgt $2 \times \log_2(N)$.
Jedes Mal, wenn Quicksort rekursiv aufgerufen wird, subtrahieren wir 1 vom `depth_limit`.

**3. Der Notfall-Ausstieg (Heap Sort):**
Wenn `depth_limit` den Wert `0` erreicht, erkennt Intro Sort mathematisch: *"Moment! Ich bin zu tief rekursiert! Die Pivot-Wahl schlägt fehl und ich bewege mich in Richtung $O(N^2)$!"*
Anstatt die Rekursion fortzusetzen, bricht der Algorithmus Quicksort für dieses spezifische Teil-Array sofort AB!
Er ruft stattdessen sofort **Heap Sort (`sort_06`)** auf diesem spezifischen Teil-Array auf!
Warum Heap Sort? Weil Heap Sort im Schlechtesten Fall strikt $O(N \log N)$ ist, keinen zusätzlichen Speicher benötigt und keine Rekursion verwendet (was den Call Stack schont)!

**4. Die Optimierung für kleine Arrays (Insertion Sort):**
Genau wie bei Tim Sort lohnt sich der Overhead der Rekursion oder des Heap-Aufbaus nicht, wenn die Größe des Teil-Arrays sehr klein wird (z. B. < 16 Elemente). Intro Sort wechselt zu **Insertion Sort (`sort_03`)**, um die winzigen Abschnitte in blitzschneller $O(1)$ Zeit fertigzustellen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_14: Intro Sort (Simplified).

Quicksort with depth limit; fall back to heapsort.
"""


def solve(data, n):
    if n <= 1:
        return data
    import math
    work = list(data)
    depth_limit = 2 * int(math.log2(n)) if n > 1 else 0

    def sift_down(lo, hi, root):
        while True:
            child = 2 * (root - lo) + 1 + lo
            if child >= hi:
                break
            if child + 1 < hi and work[child + 1] > work[child]:
                child += 1
            if work[child] > work[root]:
                work[root], work[child] = work[child], work[root]
                root = child
            else:
                break

    def heap_sort(lo, hi):
        for start in range((hi - lo) // 2 - 1 + lo, lo - 1, -1):
            sift_down(lo, hi, start)
        for end in range(hi - 1, lo, -1):
            work[lo], work[end] = work[end], work[lo]
            sift_down(lo, end, lo)

    def partition(lo, hi):
        pivot = work[hi - 1]
        i = lo
        for j in range(lo, hi - 1):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi - 1] = work[hi - 1], work[i]
        return i

    def intro_sort(lo, hi, depth):
        if hi - lo <= 1:
            return
        if depth == 0:
            heap_sort(lo, hi)
            return
        p = partition(lo, hi)
        intro_sort(lo, p, depth - 1)
        intro_sort(p + 1, hi, depth - 1)

    intro_sort(0, n, depth_limit)
    return work
```

</details>

## Ablaufbeispiel

Stellen wir uns ein pathologisches Array vor, das speziell dafür entwickelt wurde, Quicksort zu Fall zu bringen: `arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`. `N = 10`.
1. `max_depth = 2 * int(log2(10)) = 2 * 3 = 6`.
2. **`intro_sort_helper` (Tiefe 6):**
   - Die Quicksort-Partition wählt `1`. Das Array bleibt umgekehrt sortiert.
   - Rekursion auf der linken Seite `[10, 9, 8, 7, 6, 5, 4, 3, 2]`. Größe 9.
3. **`intro_sort_helper` (Tiefe 5):**
   - Die Quicksort-Partition wählt `2`.
   - Rekursion auf der linken Seite `[10...3]`. Größe 8.
   ... *(Dies setzt sich fort, und Quicksort scheitert kläglich)* ...
4. **`intro_sort_helper` (Tiefe 0):**
   - `depth_limit == 0`!
   - Intro Sort erkennt das $O(N^2)$-Versagen in Echtzeit!
   - Es bricht Quicksort sofort ab. Es ruft `heap_sort` auf dem verbleibenden Teil-Array auf!
   - Heap Sort wird in strikter $O(N \log N)$ Zeit ohne Rekursion ausgeführt!
5. Alle Rekursionen sind beendet. Das Array ist perfekt sortiert! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(\log N)$ |

Intro Sort erreicht den "Heiligen Gral" des Sortierens:
Es führt zu 99 % der Zeit Quicksort aus und erbt dessen unglaublich niedrige konstante Faktoren sowie die unübertroffene Hardware-Cache-Lokalität (was es in der Praxis schneller macht als fast alles andere).
Aber seine Zeitkomplexität im Schlechtesten Fall ist garantiert $O(N \log N)$, da der Heap-Sort-Notausstieg strikt verhindert, dass sich jemals der $O(N^2)$-Baum bildet!
Die Platzkomplexität beträgt $O(\log N)$, da das Tiefenlimit verhindert, dass der rekursive Call Stack jemals $2 \log_2 N$ Frames überschreitet. Heap Sort läuft strikt mit $O(1)$ Platzbedarf.

## Varianten & Optimierungen

- **Median-of-Three Pivot:** Intro-Sort-Implementierungen optimieren oft die `partition`-Phase von Quicksort, indem sie das linke, rechte und mittlere Element nehmen und deren Median als Pivot verwenden. Dies reduziert die Wahrscheinlichkeit, den Notfall-Ausstieg `depth_limit` überhaupt zu erreichen, massiv!

## Praxisanwendungen

- **C++ Standard Template Library (STL):** Das `std::sort` in C++ wurde komplett neu geschrieben, um Intro Sort zu verwenden, da es zwingend eine $O(N \log N)$ Zeitkomplexität im Schlechtesten Fall erforderte, Entwickler aber den Overhead der Speicherallokation von Merge Sort nicht akzeptieren wollten.
- **.NET Framework:** Microsofts `Array.Sort` verwendet Intro Sort für primitive Datentypen.

## Verwandte Algorithmen in cOde(n)

- **[sort_05 - Quick Sort](sort_05_quick-sort.md)** — Die primäre Engine.
- **[sort_06 - Heap Sort](sort_06_heap-sort.md)** — Die Notfall-Engine.
- **[sort_03 - Insertion Sort](sort_03_insertion-sort.md)** — Die Engine zur Bereinigung kleiner Arrays.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*