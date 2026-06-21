# Selection Sort

| | |
|---|---|
| **ID** | `sort_02` |
| **Kategorie** | sorting |
| **Komplexität (erforderlich)** | $O(n^2)$ |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Selection sort](https://en.wikipedia.org/wiki/Selection_sort) |

## Problemstellung

Gegeben sei ein Array von Integern `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge unter Verwendung des Selection Sort Algorithmus.

**Eingabe:** Ein unsortiertes Array von Integern `arr`.
**Ausgabe:** Das Array, sortiert in strikt aufsteigender Reihenfolge.

**Beispiel:**
| Eingabe `arr` | Ausgabe |
|---|---|
| `[64, 25, 12, 22, 11]` | `[11, 12, 22, 25, 64]` |

## Wann sollte man es verwenden

- Beim Schreiben von Daten in Flash-Speicher oder EEPROMs, bei denen **Schreiboperationen extrem kostspielig sind oder die Hardware verschleißen**, während Leseoperationen praktisch kostenlos sind. Selection Sort führt die absolut minimale Anzahl an Schreibvorgängen/Swaps durch: genau $O(n)$.
- Als pädagogisches Werkzeug, um quadratische algorithmische Komplexität zu lehren.

## Ansatz

Das Array wird logisch in zwei Teile unterteilt:
1. Den sortierten Teil am Anfang.
2. Den unsortierten Teil am Ende.

Anfangs ist der sortierte Teil leer und der unsortierte Teil umfasst das gesamte Array.
Wir durchsuchen den gesamten unsortierten Teil, um das absolute Minimum zu finden. Sobald wir es gefunden haben, tauschen wir es mit dem am weitesten links stehenden Element des unsortierten Teils, wodurch unser sortierter Teil effektiv um 1 wächst.

Wir wiederholen diesen Prozess: das Minimum der verbleibenden Elemente finden, es an den Anfang der verbleibenden Elemente platzieren und so weiter.

Im Gegensatz zu Bubble Sort, das kontinuierlich benachbarte Elemente im gesamten Array tauscht, führt Selection Sort pro Durchlauf genau einen Swap durch.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_02: Selection Sort.

For each index i, find the minimum element in data[i..n-1] and
swap it into position i. O(n^2) time, O(1) extra space, at most n
swaps.
"""


def solve(data, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
    return data
```

</details>

## Ablaufbeispiel

Sei `arr = [29, 10, 14, 37, 13]`.

**Durchlauf 1 (`i = 0`):**
- Unsortierter Bereich: `[29, 10, 14, 37, 13]`
- Gefundenes Minimum: `10` (an Index 1)
- Tausche `arr[0]` (29) mit `arr[1]` (10).
- Array ist nun: `[10, 29, 14, 37, 13]`

**Durchlauf 2 (`i = 1`):**
- Unsortierter Bereich: `[29, 14, 37, 13]`
- Gefundenes Minimum: `13` (an Index 4)
- Tausche `arr[1]` (29) mit `arr[4]` (13).
- Array ist nun: `[10, 13, 14, 37, 29]`

**Durchlauf 3 (`i = 2`):**
- Unsortierter Bereich: `[14, 37, 29]`
- Gefundenes Minimum: `14` (an Index 2)
- Tausch: Nicht erforderlich (min_idx == i).
- Array ist nun: `[10, 13, 14, 37, 29]`

**Durchlauf 4 (`i = 3`):**
- Unsortierter Bereich: `[37, 29]`
- Gefundenes Minimum: `29` (an Index 4)
- Tausche `arr[3]` (37) mit `arr[4]` (29).
- Array ist nun: `[10, 13, 14, 29, 37]`

Das letzte Element befindet sich nun automatisch an der richtigen Stelle. Array sortiert! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n^2)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(n^2)$ | $O(1)$ |
| **Schlechtester Fall** | $O(n^2)$ | $O(1)$ |

Die Zeitkomplexität ist in allen Fällen (Bestfall, Durchschnitt, Schlechtester Fall) strikt $O(n^2)$. Selbst wenn das Array bereits perfekt sortiert ist, muss Selection Sort bei jedem Durchlauf den gesamten unsortierten Rest des Arrays scannen, nur um zu *verifizieren*, dass das aktuelle Element das Minimum ist. Dies macht ihn Insertion Sort bei nahezu sortierten Daten deutlich unterlegen. Der Platzbedarf ist $O(1)$ (in-place).

## Varianten & Optimierungen

- **Bingo Sort:** Eine optimierte Version von Selection Sort, bei der Elemente mit identischen Werten gruppiert und gemeinsam verschoben werden.
- **Heap Sort:** Konzeptionell ist Heap Sort lediglich ein optimierter Selection Sort! Anstatt $O(n)$ für die lineare Suche nach dem Minimum während jedes Durchlaufs zu benötigen, verwendet Heap Sort eine Binary Heap Datenstruktur, um das Minimum in $O(1)$ Zeit zu finden und den verbleibenden Heap in $O(log n)$ Zeit zu aktualisieren, was die gesamte Zeitkomplexität drastisch von $O(n^2)$ auf $O(n log n)$ reduziert.

## Praxisanwendungen

- Extrem eingeschränkte eingebettete Mikrocontroller, bei denen Flash-Speicher-Schreibvorgänge die Hardware verschleißen. Selection Sort garantiert genau `n` Schreibvorgänge (Swaps), um das Array zu sortieren – das absolute theoretische Minimum für ein in-place Sortierverfahren.

## Verwandte Algorithmen in cOde(n)

- **[sort_06 - Heap Sort](sort_06_heap-sort.md)** — Der massiv optimierte $O(n log n)$ geistige Nachfolger von Selection Sort.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*