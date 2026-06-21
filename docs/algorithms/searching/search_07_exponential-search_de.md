# Exponential Search (Galloping Search)

| | |
|---|---|
| **ID** | `search_07` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Exponential search](https://en.wikipedia.org/wiki/Exponential_search) |

## Problemstellung

Gegeben ist ein sortiertes Array `arr` und ein `target`-Wert.
Finde den Index des `target` im Array. Falls das `target` nicht vorhanden ist, gib `-1` zurück.
Optimiere die Suche für Szenarien, in denen das Array UNBEGRENZT (unendliche Größe) ist oder wenn erwartet wird, dass sich das `target` sehr nah am Anfang des Arrays befindet.

**Eingabe:** Ein sortiertes Array `arr` und ein `target`-Wert.
**Ausgabe:** Eine Ganzzahl, die den Index repräsentiert.

## Wann sollte man es verwenden?

- **Unendliche Arrays:** Wenn die Größe des Arrays buchstäblich unbekannt ist (z. B. beim Lesen eines aktiven, endlosen Datenstroms), kann man mathematisch KEINE Binary Search verwenden, da man nicht weiß, wo der `right`-Pointer platziert werden soll!
- **Daten mit Fokus auf den Anfang:** Wenn statistische Analysen zeigen, dass sich das `target` normalerweise in den ersten 5 % eines riesigen Arrays befindet, verschwendet eine Binary Search Operationen durch das Prüfen der Mitte/des Endes.

## Ansatz

**1. Die Galloping-Phase:**
Wir beginnen bei Index `1`. Wir prüfen, ob das Element dort $\ge$ unserem `target` ist.
Wenn es kleiner ist, verdoppeln wir unseren Index! `1 -> 2 -> 4 -> 8 -> 16...`
Wir verdoppeln den Index exponentiell weiter, bis `arr[index] >= target` (oder wir die Grenzen des Arrays überschreiten).
Da das Array sortiert ist, wissen wir in dem Moment, in dem wir das `target` überschreiten, dass das `target` ZWISCHEN unserem vorherigen Sprung `index / 2` und unserem aktuellen `index` liegen MUSS!

**2. Die Binary-Search-Phase:**
Nachdem wir erfolgreich eine geschlossene Schranke `[index / 2, min(index, N-1)]` identifiziert haben, übergeben wir diese Grenzen einfach an eine Standard-Binary Search!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_07: Exponential Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(log n) time.
"""


def solve(data, target, n):
    if n == 0 or data[0] > target:
        return -1
    bound = 1
    while bound < n and data[bound] <= target:
        bound *= 2
    # Binary search in [bound/2, min(bound, n-1)].
    low, high = bound // 2, min(bound, n - 1)
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

</details>

## Durchlauf

`arr = [10, 20, 40, 50, 70, 90, 100, 120, 150]`, `target = 90`. Länge 9.

1. `arr[0] = 10 == 90`? Falsch.
2. **Gallop:**
   - `i = 1`: `arr[1] = 20 <= 90`. `i = 1 * 2 = 2`.
   - `i = 2`: `arr[2] = 40 <= 90`. `i = 2 * 2 = 4`.
   - `i = 4`: `arr[4] = 70 <= 90`. `i = 4 * 2 = 8`.
   - `i = 8`: `arr[8] = 150 <= 90` ist FALSCH! Gallop endet.
3. **Binary-Search-Bereich:**
   - `left = 8 // 2 = 4`.
   - `right = min(8, 8) = 8`.
   - Aufruf `binary_search(arr, left=4, right=8, target=90)`.
4. **Binary Search:**
   - `mid = (4 + 8) // 2 = 6`. `arr[6] = 100 > 90`. `right = 5`.
   - `mid = (4 + 5) // 2 = 4`. `arr[4] = 70 < 90`. `left = 5`.
   - `mid = (5 + 5) // 2 = 5`. `arr[5] = 90 == 90`! Treffer gefunden!

Ergebnis: `5`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log I)$ | $O(1)$ |
| **Schlechtester Fall** | $O(\log I)$ | $O(1)$ |

Sei I der Index, an dem sich das `target` tatsächlich befindet.
Die Galloping-Phase verdoppelt i, bis es I überschreitet. Dies benötigt $O(\log I)$ Schritte.
Die Binary-Search-Phase durchsucht dann einen Bereich der Größe $\frac{I}{2}$. Die binäre Suche in diesem Bereich benötigt $O(\log(I/2)) = O(\log I - 1) = O(\log I)$ Schritte.
Daher ist die gesamte Zeitkomplexität strikt $O(\log I)$.
Wenn sich das `target` an Index 10 befindet, findet die Exponential Search es in $\approx \log_2(10) = 3$ Operationen, selbst wenn das Array 1 Milliarde Elemente enthält! Eine Standard-Binary Search würde $\approx \log_2(10^9) = 30$ Operationen benötigen.
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Unbounded Binary Search:** Wenn man es mit Funktionen statt mit Arrays zu tun hat (z. B. "Finde die erste positive Ganzzahl X, für die f(X) > 1000 gilt"), kann man mathematisch keine Standard-Binary Search verwenden, da es keine obere Schranke gibt. Man MUSS die Exponential Search verwenden, um zuerst die obere Schranke zu finden!

## Anwendungen in der Praxis

- **Pythons Timsort:** Der Standard-Sortieralgorithmus in Python (`list.sort()`) und Java (`Arrays.sort()`). Timsort verwendet intern eine hochoptimierte Variante der Exponential Search (speziell "Galloping" genannt), um beim Zusammenführen zweier Arrays, deren Größen stark unausgewogen sind, schnell Einfügepunkte zu finden!

## Verwandte Algorithmen in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — Der Algorithmus für die zweite Phase, der verwendet wird, sobald der Suchbereich eingegrenzt wurde.
- **[search_06 - Jump Search](search_06_jump-search.md)** — Verwendet eine ähnliche Logik des Überspringens von Elementen, nutzt jedoch arithmetische Sprünge fester Größe ($\sqrt{N}$) anstelle von exponentiellen geometrischen Sprüngen (x 2).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*