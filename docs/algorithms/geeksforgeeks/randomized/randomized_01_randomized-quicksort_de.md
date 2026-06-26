# Randomized Quicksort

| | |
|---|---|
| **ID** | `randomized_01` |
| **Kategorie** | randomized |
| **Komplexität (erforderlich)** | $O(N \log N)$ erwartet |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **Wikipedia** | [Quicksort (Randomized)](https://en.wikipedia.org/wiki/Quicksort#Randomized_quicksort) |

## Problemstellung

Sortieren Sie ein Array mit N Elementen unter Verwendung des Quicksort-Algorithmus, garantieren Sie jedoch explizit eine erwartete Zeitkomplexität von $O(N \log N)$, unabhängig von der ursprünglichen Anordnung des Eingabe-Arrays.

**Eingabe:** Ein unsortiertes Array von Integern.
**Ausgabe:** Dasselbe Array, in-place sortiert.

## Wann man es verwendet

- Sie benötigen den schnellsten praktischen In-Place-Sortieralgorithmus und müssen sich gegen gegnerische Eingaben absichern, die bei einem Standard-Quicksort zu einer Verschlechterung auf $O(N^2)$ führen würden.
- Wird in Vorstellungsgesprächen häufig explizit gefordert, um das Verständnis für algorithmische Worst-Case-Szenarien zu prüfen.

## Ansatz

Standard-Quicksort funktioniert, indem ein "Pivot" (oft das letzte oder erste Element) gewählt wird, das Array so partitioniert wird, dass kleinere Elemente links und größere rechts stehen, und anschließend rekursiv fortgefahren wird.
Der fatale Fehler des Standard-Quicksort besteht darin, dass bei einer *bereits sortierten* (oder umgekehrt sortierten) Eingabe die Wahl des letzten Elements als Pivot zu Partitionen der Größe 0 und N-1 führt. Die Rekursionstiefe wird zu N, was eine Zeitkomplexität von $O(N^2)$ zur Folge hat!

Um dies zu beheben, führen wir eine **Las-Vegas-Randomisierung** ein.
Bevor wir ein Segment `[low...high]` partitionieren, wählen wir zufällig einen Index `r` zwischen `low` und `high` aus.
Wir tauschen das Element an Position `r` mit dem Element an Position `high`.
Anschließend fahren wir mit der exakten Standard-Partitionierungslogik fort und verwenden `high` als Pivot!

Da der Pivot gleichverteilt zufällig gewählt wird, wird die Wahrscheinlichkeit, bei jedem Rekursionsschritt konsequent den absolut schlechtesten Pivot zu wählen, astronomisch gering. Die *erwarteten* Partitionsgrößen sind ausgeglichen, was eine erwartete Zeitkomplexität von $O(N \log N)$ garantiert, unabhängig von der Eingabepermutation!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for randomized_01: Randomized Quicksort.

Quicksort with a random pivot. Each partition picks a random
index in [lo, hi], swaps it to the end, then Lomuto-partitions.
Expected O(n log n); with adversarial input, expected
O(n log n) - the random pivot breaks the bad case.
"""


def solve(data, n):
    import random
    work = list(data)

    def partition(lo, hi):
        pivot_idx = random.randint(lo, hi)
        work[pivot_idx], work[hi] = work[hi], work[pivot_idx]
        pivot = work[hi]
        i = lo
        for j in range(lo, hi):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi] = work[hi], work[i]
        return i

    def sort(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            sort(lo, p - 1)
            sort(p + 1, hi)

    if n > 1:
        sort(0, n - 1)
    return work
```

</details>

## Ablaufbeispiel

`arr = [1, 2, 3, 4, 5]` (Bereits sortiert - Worst Case für Standard-Quicksort!)
`low = 0, high = 4`.

**Standard Quicksort:**
- Pivot ist `arr[4] = 5`.
- Partitionierung in `[1, 2, 3, 4]` und `[]`.
- Nächster Pivot ist `arr[3] = 4`. Partitionierung in `[1, 2, 3]` und `[]`.
- $O(N^2)$ Verschlechterung!

**Randomized Quicksort:**
- `random.randint(0, 4)` ergibt `2`.
- Tausche `arr[2]` mit `arr[4]`. Das Array ist nun `[1, 2, 5, 4, 3]`.
- Pivot ist `arr[4] = 3`.
- `partition` gruppiert `<3` nach links, `>3` nach rechts.
- Das Array wird zu `[1, 2, 3, 4, 5]`. Pivot `3` landet an Index `2`.
- Perfekte Partitionierung in `[1, 2]` und `[4, 5]`!
- Die Rekursionstiefe beträgt log N.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ erwartet | $O(\log N)$ |
| **Schlechtester Fall** | $O(N^2)$ (Mathematisch möglich, praktisch null) | $O(N)$ |

Der theoretische Schlechteste Fall ist weiterhin $O(N^2)$, falls der Zufallszahlengenerator auf wundersame Weise bei jedem einzelnen Schritt den schlechtestmöglichen Pivot wählt, aber die Wahrscheinlichkeit dafür liegt bei 1 / N!, was praktisch 0 ist. Die erwartete Zeitkomplexität ist nachweislich $O(N \log N)$.
Die Platzkomplexität beträgt im Erwartungswert $O(\log N)$ für den rekursiven Aufruf-Stack.

## Varianten & Optimierungen

- **Median-of-Three:** Anstatt einen Zufallszahlengenerator aufzurufen (was in Systembibliotheken langsam sein kann), wählt man drei Elemente (erstes, mittleres, letztes) und verwendet deren Median als Pivot. Dies umgeht deterministisch den "bereits sortiert"-Worst-Case und vermeidet gleichzeitig den Overhead durch Zufallszahlen.
- **IntroSort:** Der Algorithmus, der in C++ `std::sort` verwendet wird. Er beginnt mit Randomized Quicksort, aber falls die Rekursionstiefe 2 log N überschreitet, wechselt er abrupt zu HeapSort, um absolut eine Worst-Case-Zeitkomplexität von $O(N \log N)$ zu garantieren!

## Anwendungen in der Praxis

- **Systembibliotheken:** Allzweck-Sortierfunktionen in dynamisch typisierten Sprachen, bei denen die Eingabeverteilung unbekannt ist und Schutz gegen böswillige, gegnerische Eingaben erforderlich ist (z. B. DDOS-Angriffe, die auf Sortierroutinen abzielen).

## Verwandte Algorithmen in cOde(n)

- **[sorting_03 - Quicksort](../sorting/sorting_03_quicksort.md)** — Der deterministische Vorläufer.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*