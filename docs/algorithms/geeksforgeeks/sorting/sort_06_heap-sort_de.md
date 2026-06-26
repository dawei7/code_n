# Heap Sort

| | |
|---|---|
| **ID** | `sort_06` |
| **Kategorie** | sorting |
| **Komplexität (erforderlich)** | $O(n log n)$ |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **Wikipedia** | [Heapsort](https://de.wikipedia.org/wiki/Heapsort) |

## Problemstellung

Gegeben sei ein Array von Integern `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge unter Verwendung des Heap-Sort-Algorithmus.

**Eingabe:** Ein unsortiertes Array von Integern `arr`.
**Ausgabe:** Das Array, sortiert in strikt aufsteigender Reihenfolge.

**Beispiel:**
| Eingabe `arr` | Ausgabe |
|---|---|
| `[12, 11, 13, 5, 6, 7]` | `[5, 6, 7, 11, 12, 13]` |

## Wann man es verwendet

- Wenn eine strikt garantierte Zeitkomplexität im Schlechtesten Fall von **$O(n log n)$** erforderlich ist, man sich aber den zusätzlichen Speicherbedarf von **$O(n)$** bei Merge Sort nicht leisten kann. Heap Sort ist ein perfekter In-Place-Algorithmus ($O(1)$ Platzkomplexität).
- Als Fallback-Mechanismus in Algorithmen wie Introsort, wenn der Rekursionsbaum von Quicksort pathologisch tief wird.
- In Schedulern von Betriebssystemen (wie in älteren Linux-Kerneln), bei denen strikte Grenzen für die Ausführungszeit und den Speicherbedarf kritisch sind.

## Ansatz

Heap Sort ist im Grunde eine optimierte Version von **Selection Sort**.
Bei Selection Sort durchsuchen wir das gesamte Array in `O(n)`, um das maximale Element zu finden, was zu einer Gesamtlaufzeit von `O(n^2)` führt.
Bei Heap Sort organisieren wir das Array in einer **Max-Heap**-Datenstruktur. Ein Max-Heap stellt sicher, dass das absolute Maximum immer an der Wurzel (Index 0) steht. Das Finden des Maximums ist somit `O(1)`.

Der Algorithmus besteht aus zwei Hauptphasen:
1. **Heapify (Max-Heap aufbauen):** Das flache Array wird in einen gültigen Max-Heap umorganisiert. Dies benötigt mathematisch gesehen `O(n)` Zeit, wenn es von unten nach oben (bottom-up) durchgeführt wird.
2. **Extrahieren und Sortieren:** Wir tauschen das maximale Element (an der Wurzel) mit dem allerletzten Element des unsortierten Segments. Dann reduzieren wir die logische Größe des Heaps um 1 und lassen die neue Wurzel "nach unten sinken" (sift down), um die Max-Heap-Eigenschaft wiederherzustellen. Dies benötigt `O(log n)` Zeit. Diesen Vorgang wiederholen wir `n` Mal.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_06: Heap Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n log n) time.
"""


def solve(data, n):
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

    # Pop the root into the last position, one at a time.
    for end in range(n - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        sift_down(0, end)
    return data
```

</details>

## Ablaufbeispiel

Sei `arr = [4, 10, 3]`.

**Phase 1: Max-Heap aufbauen**
- `n = 3`. Letzter Nicht-Blatt-Knoten `i = 3 // 2 - 1 = 0`.
- Aufruf von `heapify(arr, 3, 0)`:
  - `largest = 0` (Wert 4). Linkes Kind ist Index 1 (Wert 10). Rechtes ist Index 2 (Wert 3).
  - 10 > 4, also `largest = 1`.
  - Tausche Index 0 und 1: `[10, 4, 3]`.
- Das Array ist nun ein gültiger Max-Heap! Das Maximum (10) steht an der Wurzel.

**Phase 2: Extrahieren & Sortieren**
- **Iteration 1 (`i = 2`):**
  - Tausche `arr[0]` (10) mit `arr[2]` (3). Array: `[3, 4, 10]`. (10 ist permanent am Ende sortiert!)
  - Aufruf von `heapify(arr, 2, 0)`, um die Wurzel (3) zu korrigieren.
  - Linkes Kind ist 4. `4 > 3`, tausche. Array: `[4, 3, 10]`.
- **Iteration 2 (`i = 1`):**
  - Tausche `arr[0]` (4) mit `arr[1]` (3). Array: `[3, 4, 10]`. (4 ist permanent sortiert!)
  - Aufruf von `heapify(arr, 1, 0)`. Linkes Kind ist außerhalb der Grenzen. Nichts zu tun.
- **Iteration 3 (`i = 0`):**
  - Schleife beendet.

Endgültiges Array: `[3, 4, 10]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n log n)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(n log n)$ | $O(1)$ |
| **Schlechtester Fall** | $O(n log n)$ | $O(1)$ |

Der anfängliche Aufbau des Heaps benötigt strikt `O(n)` Zeit. Die Extraktionsphase läuft `n` Mal durch, und jede `heapify`-Operation benötigt `O(log n)` Zeit, da die Höhe eines binären Heaps `log n` beträgt. Daher ist die gesamte Zeitkomplexität immer `O(n log n)`. Es handelt sich um eine In-Place-Sortierung, die keinen zusätzlichen Speicher benötigt, daher ist die Platzkomplexität `O(1)`.

## Varianten & Optimierungen

- **Bottom-up Heapsort:** Eine hochoptimierte Variante, die die Anzahl der Vergleiche reduziert. Anstatt während des `sift_down` Kinder zu vergleichen und dann gegen die Wurzel zu prüfen, lässt man die Wurzel blind bis zu einem Blatt hinunterwandern und führt sie dann wieder nach oben. Dies halbiert die Anzahl der Vergleiche nahezu.

## Anwendungen in der Praxis

- **Eingebettete Systeme:** Perfekt für Sortieraufgaben in Umgebungen ohne Möglichkeiten zur dynamischen Speicherallokation.
- **Priority Queues:** Die zugrunde liegende Max-Heap-Struktur ist derselbe Mechanismus, der für die Aufgabenplanung in Betriebssystemen oder Pfadfindungsalgorithmen wie Dijkstra verwendet wird.

## Verwandte Algorithmen in cOde(n)

- **[sort_02 - Selection Sort](sort_02_selection-sort.md)** — Der konzeptionell identische, aber strukturell nicht optimierte `O(n^2)`-Vorgänger.
- **[heap_01 - Min Heap Implementation](../heap/heap_01_min-heap.md)** — Ein tieferer Einblick in die eigentliche binäre Heap-Datenstruktur.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*