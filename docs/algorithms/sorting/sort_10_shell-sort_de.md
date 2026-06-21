# Shell Sort

| | |
|---|---|
| **ID** | `sort_10` |
| **Kategorie** | Sortieren |
| **Komplexität (erforderlich)** | $O(N^{4/3})$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 1/10 |
| **Wikipedia** | [Shellsort](https://en.wikipedia.org/wiki/Shellsort) |

## Problemstellung

Gegeben ist ein Array von Ganzzahlen `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge.
Sie müssen einen In-Place-Algorithmus verwenden, der die schlechte $O(N^2)$-Performance von Insertion Sort drastisch verbessert, ohne den rekursiven Platzbedarf von Merge Sort oder Quick Sort zu verursachen.

**Eingabe:** Ein unsortiertes Array von Ganzzahlen `arr`.
**Ausgabe:** Ein sortiertes Array (in-place modifiziert).

## Einsatzgebiete

- Primär von historischem und akademischem Interesse.
- Verwendung in eingebetteten Systemen, in denen der Speicher-Stack für Rekursion zu klein ist (was Quicksort ausschließt), das Array aber zu groß für $O(N^2)$ Insertion Sort ist.

## Ansatz

**1. Der entscheidende Nachteil von Insertion Sort (`sort_03`):**
Insertion Sort ist unglaublich schnell, wenn ein Array *fast sortiert* ist. Sein entscheidender Nachteil ist, dass Elemente immer nur um EINEN Index verschoben werden können. Wenn das absolut kleinste Element `1` am Ende eines Arrays der Größe 1000 gefangen ist, benötigt Insertion Sort 999 einzelne Tauschoperationen, nur um es langsam an den Index 0 zu befördern!

**2. Die "Gap"-Strategie (Donald Shell, 1959):**
Anstatt Elemente zu vergleichen, die direkt nebeneinander liegen (`gap = 1`), was passiert, wenn wir Elemente vergleichen, die extrem weit auseinander liegen (`gap = N/2`)?
Wir führen einen modifizierten Insertion Sort aus, der in riesigen Sprüngen durch das Array geht. Dies ermöglicht es kleinen Elementen, die am Ende gefangen sind, in einem einzigen Tauschvorgang sofort an den Anfang des Arrays zu springen!
Sobald das Array durch die große Lücke "grob" sortiert ist, verkleinern wir die Lücke! `gap = gap / 2`. Wir führen Insertion Sort erneut aus.
Schließlich führen wir den Algorithmus mit `gap = 1` aus. Da das Array durch die vorherigen Durchläufe bereits praktisch sortiert ist, erreicht der abschließende $O(N^2)$ Insertion Sort seinen Bestfall und wird in strikter $O(N)$ linearer Zeit ausgeführt!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_10: Shell Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n²) time.
"""


def solve(data, n):
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1
    while gap >= 1:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 3
    return data
```

</details>

## Durchlauf

`arr = [23, 29, 15, 19, 31, 7, 9, 5, 2]`. Länge `9`.
`gap = 9 // 2 = 4`.

**Durchlauf 1 (`gap = 4`):**
Teil-Arrays, die sortiert werden:
- `[23, 31, 2]` (Indizes 0, 4, 8) -> Sortiert zu `[2, 23, 31]`! Die `2` sprang sofort 8 Plätze!
- `[29, 7]` (Indizes 1, 5) -> Sortiert zu `[7, 29]`.
- `[15, 9]` (Indizes 2, 6) -> Sortiert zu `[9, 15]`.
- `[19, 5]` (Indizes 3, 7) -> Sortiert zu `[5, 19]`.
Das Array ist nun: `[2, 7, 9, 5, 23, 29, 15, 19, 31]`. (Grob sortiert!)

**Durchlauf 2 (`gap = 4 // 2 = 2`):**
Teil-Arrays:
- `[2, 9, 23, 15, 31]` -> Sortiert zu `[2, 9, 15, 23, 31]`.
- `[7, 5, 29, 19]` -> Sortiert zu `[5, 7, 19, 29]`.
Das Array ist nun: `[2, 5, 9, 7, 15, 19, 23, 29, 31]`. (Sehr nah an der perfekten Sortierung!)

**Durchlauf 3 (`gap = 2 // 2 = 1`):**
Standard Insertion Sort.
Nur `7` und `9` müssen getauscht werden! Alles andere ist bereits an der richtigen Position.
Das Array ist sortiert! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N^{4/3})$ oder $O(N^{3/2})$ | $O(1)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(1)$ |

Die Komplexität von Shell Sort ist mathematisch bekanntermaßen schwer zu berechnen, da sie strikt von der gewählten "Gap-Sequenz" abhängt.
Die klassische Shell-Sequenz (`N/2, N/4, N/8...`) ist tatsächlich ziemlich schlecht und führt zu einem $O(N^2)$ Schlechtester-Fall.
Wenn die **Hibbard-Sequenz** (2^k - 1 -> 1, 3, 7, 15...) verwendet wird, sinkt der Schlechtester-Fall mathematisch auf $O(N^{3/2})$.
Wenn die **Sedgewick-Sequenz** (4^k + 3 \cdot 2^{k-1} + 1) verwendet wird, sinkt der Schlechtester-Fall beeindruckend auf $O(N^{4/3})$.
Die Platzkomplexität ist bedingungslos $O(1)$ konstanter Platz, da Elemente strikt in-place getauscht werden.

## Varianten & Optimierungen

- **Knuth-Gap-Sequenz:** h = 3h + 1 -> 1, 4, 13, 40, 121... Eine sehr beliebte und einfach zu implementierende Sequenz, die eine $O(N^{3/2})$-Performance liefert.

## Anwendungen in der Praxis

- **uClibc (Micro C Library):** Wird in der Standard-`qsort()`-Implementierung für eingebettete Linux-Systeme verwendet. Die Bibliothek bevorzugt Shell Sort gegenüber Quicksort, da die Speicher-Stacks eingebetteter Systeme zu klein sind, um das Risiko eines Stack-Überlaufs durch tiefe Rekursion einzugehen, und der Code-Umfang von Shell Sort unglaublich gering ist.

## Verwandte Algorithmen in cOde(n)

- **[sort_03 - Insertion Sort](sort_03_insertion-sort.md)** — Der grundlegende Baustein, den Shell Sort aggressiv optimiert.
- **[sort_13 - Tim Sort](sort_13_tim-sort-simplified.md)** — Der moderne, überlegene Algorithmus, der teilweise sortierte Daten mittels Insertion Sort effizient nutzt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*