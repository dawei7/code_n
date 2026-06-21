# Insertion Sort

| | |
|---|---|
| **ID** | `sort_03` |
| **Kategorie** | sorting |
| **Komplexität (erforderlich)** | $O(n^2)$ |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort) |

## Problemstellung

Gegeben sei ein Array von Integern `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge unter Verwendung des Insertion-Sort-Algorithmus.

**Eingabe:** Ein unsortiertes Array von Integern `arr`.
**Ausgabe:** Das Array, sortiert in strikt aufsteigender Reihenfolge.

**Beispiel:**
| Eingabe `arr` | Ausgabe |
|---|---|
| `[12, 11, 13, 5, 6]` | `[5, 6, 11, 12, 13]` |

## Wann man es verwendet

- **Als Subroutine in modernen Produktions-Sortier-Engines** wie Timsort (verwendet in Python und Java) oder Introsort (verwendet in C++ `std::sort`). Wenn ein rekursiver Quicksort oder Mergesort das Array in sehr kleine Abschnitte unterteilt (typischerweise < 16 Elemente), ist der Overhead der Rekursion zu hoch und sie wechseln zu Insertion Sort.
- Wenn die Daten **nahezu sortiert** sind. Insertion Sort arbeitet in $O(n)$ Zeit, wenn das Array bereits größtenteils geordnet ist.
- Beim Sortieren eines Datenstroms, der **online** (Element für Element) eintrifft.

## Ansatz

Insertion Sort ahmt die Art und Weise nach, wie Menschen eine Hand voll Spielkarten sortieren.
Wir iterieren über das Array von links nach rechts. An jeder Position `i` betrachten wir das Element `arr[i]` als die „Karte“, die wir gerade aufgenommen haben.

Alles links von `i` ist bereits sortiert. Wir vergleichen unsere „Karte“ mit den Karten links davon und verschieben die größeren Karten nach rechts, um Platz zu schaffen. Sobald wir eine Karte finden, die kleiner ist als unsere aktuelle Karte (oder den Anfang des Arrays erreichen), legen wir unsere Karte in die neu entstandene Lücke.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_03: Insertion Sort.

For each element, shift larger elements right to make room, then
drop the element into the gap. O(n^2) worst case, O(n) on nearly
sorted data.
"""


def solve(data, n):
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
```

</details>

## Ablaufbeispiel

Sei `arr = [4, 3, 2, 10, 12, 1, 5, 6]`. Wir verfolgen nur die ersten paar Schritte.

**Durchlauf 1 (`i = 1`, `key = 3`):**
- Array: `[4, | 3, 2, 10, ...]`
- `arr[0]` (4) > 3, also verschiebe 4 nach rechts.
- Füge 3 ein.
- Array: `[3, 4, | 2, 10, ...]`

**Durchlauf 2 (`i = 2`, `key = 2`):**
- Array: `[3, 4, | 2, 10, ...]`
- `arr[1]` (4) > 2, verschiebe 4 nach rechts.
- `arr[0]` (3) > 2, verschiebe 3 nach rechts.
- Füge 2 ein.
- Array: `[2, 3, 4, | 10, ...]`

**Durchlauf 3 (`i = 3`, `key = 10`):**
- Array: `[2, 3, 4, | 10, ...]`
- `arr[2]` (4) ist NICHT > 10. Die `while`-Schleife wird gar nicht erst ausgeführt!
- Array bleibt: `[2, 3, 4, 10, | ...]`

*Beachten Sie, dass es absolut nichts ($O(1)$) kostet, ein Element an seinem Platz zu belassen, wenn es von Natur aus größer als seine sortierten Nachbarn ist. Deshalb ist Insertion Sort bei nahezu sortierten Daten so schnell.*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(n^2)$ | $O(1)$ |
| **Schlechtester Fall** | $O(n^2)$ | $O(1)$ |

Der schlechteste Fall $O(n^2)$ tritt ein, wenn das Array in umgekehrter Reihenfolge vorliegt, was bedeutet, dass jedes neue Element bis ganz an den Anfang des Arrays verschoben werden muss. Der Bestfall $O(n)$ tritt ein, wenn das Array bereits sortiert ist – die Bedingung der inneren `while`-Schleife `arr[j] > key` schlägt bei jedem Durchlauf sofort fehl, wodurch der Algorithmus auf einen einzigen linearen $O(n)$-Durchlauf reduziert wird. Der Platzbedarf ist $O(1)$ (in-place).

## Varianten & Optimierungen

- **Binary Insertion Sort:** Verwenden Sie Binäre Suche, um die exakte Position zum Einfügen von `key` in $O(log n)$ Zeit zu finden. Da Arrays jedoch zusammenhängende Speicherstrukturen sind, müssen Sie dennoch alle Elemente physisch nach rechts verschieben, was eine $O(n)$-Operation pro Element bleibt. Daher bleibt die gesamte Zeitkomplexität bei $O(n^2)$.

## Anwendungen in der Praxis

- **Timsort (Python / Java):** Der Standard-Sortieralgorithmus in modernen Programmiersprachen. Timsort unterteilt riesige Arrays in kleine „Runs“ von ca. 32 bis 64 Elementen, sortiert diese kleinen Abschnitte mittels Insertion Sort und fügt sie dann wieder zusammen.
- **Introsort (C++ `std::sort`):** C++ verwendet nativ Quicksort, wechselt jedoch zu Heapsort, wenn die Rekursion zu tief wird, und greift auf Insertion Sort zurück, wenn die partitionierten Sub-Arrays unter 16 Elemente fallen.

## Verwandte Algorithmen in cOde(n)

- **[sort_10 - Shell Sort](sort_10_shell-sort.md)** — Eine brillante Optimierung von Insertion Sort, die weit voneinander entfernte Elemente vergleicht, um sie schnell durch das Array zu bewegen, und so die Schwäche von Insertion Sort überwindet, nur um 1 zu verschieben.
- **[sort_13 - Timsort](sort_13_tim-sort-simplified.md)** — Der Produktionsalgorithmus, der auf Insertion Sort als Rückgrat basiert.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*