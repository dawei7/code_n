# Counting Sort

| | |
|---|---|
| **ID** | `sort_07` |
| **Kategorie** | sorting |
| **Komplexität (erforderlich)** | $O(n + k)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **Wikipedia** | [Counting sort](https://en.wikipedia.org/wiki/Counting_sort) |

## Problemstellung

Gegeben sei ein Array von Integern `arr`, wobei alle Elemente nicht-negativ sind und durch einen relativ kleinen Maximalwert `k` begrenzt sind. Sortieren Sie das Array in aufsteigender Reihenfolge unter Verwendung des Counting-Sort-Algorithmus.

**Eingabe:** Ein unsortiertes Array von nicht-negativen Integern `arr` und der Maximalwert `k` im Array.
**Ausgabe:** Das Array, sortiert in strikt aufsteigender Reihenfolge.

**Beispiel:**
| Eingabe `arr` | `k` | Ausgabe |
|---|---|---|
| `[4, 2, 2, 8, 3, 3, 1]` | 8 | `[1, 2, 2, 3, 3, 4, 8]` |

## Wann man es verwendet

- Wenn die Eingabedaten Integer sind, die einen **kleinen, bekannten Bereich** abdecken (z. B. das Sortieren von Altersangaben von Personen, die strikt zwischen 0 und 150 liegen).
- Wenn Sie eine **lineare Zeitkomplexität $O(n)$** benötigen. Da Counting Sort die Elemente nicht miteinander vergleicht, durchbricht es die für vergleichsbasierte Sortierverfahren mathematisch bewiesene untere Schranke von $O(n \log n)$!
- Als stabile Subroutine für **Radix Sort**.

## Ansatz

Counting Sort verzichtet vollständig auf die Idee, `a` mit `b` zu vergleichen.
Stattdessen zählt es die absolute Häufigkeit jedes Integers im Array.

1. **Häufigkeiten zählen:** Erstellen Sie ein `count`-Array der Größe `k + 1` (initialisiert mit 0). Iterieren Sie durch das Eingabe-Array `arr`. Wenn Sie die Zahl `4` sehen, inkrementieren Sie `count[4]`.
2. **Präfixsummen berechnen:** Modifizieren Sie das `count`-Array so, dass jeder Index nun die Summe aller vorangegangenen Zählwerte speichert: `count[i] += count[i-1]`. Dieser brillante Schritt transformiert das Array von "Häufigkeiten" zu "tatsächlichen Startpositionen" im finalen sortierten Array.
3. **Ausgabe aufbauen:** Iterieren Sie *rückwärts* durch das ursprüngliche `arr` (um die Stabilität zu wahren). Finden Sie die Position des Elements im `count`-Array, platzieren Sie es an diesem exakten Index `- 1` in einem `output`-Array und dekrementieren Sie den Zählwert.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_07: Counting Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n) time.
"""


def solve(data, n):
    if n == 0:
        return data
    min_val = min(data)
    max_val = max(data)
    span = max_val - min_val + 1
    counts = [0] * span
    for value in data:
        counts[value - min_val] += 1
    # Rewrite data in place by walking the count array.
    index = 0
    for offset, count in enumerate(counts):
        for _ in range(count):
            data[index] = offset + min_val
            index += 1
    return data
```

</details>

## Durchlauf

Sei `arr = [2, 1, 1, 0, 2]` und `k = 2`.

**1. Häufigkeiten:**
`count = [0, 0, 0]`
- Lese 2 -> `count = [0, 0, 1]`
- Lese 1 -> `count = [0, 1, 1]`
- Lese 1 -> `count = [0, 2, 1]`
- Lese 0 -> `count = [1, 2, 1]`
- Lese 2 -> `count = [1, 2, 2]`

**2. Präfixsummen:**
`count[0]` bleibt `1`.
`count[1] = count[1] + count[0]` = `2 + 1 = 3`.
`count[2] = count[2] + count[1]` = `2 + 3 = 5`.
Das `count`-Array ist nun `[1, 3, 5]`. Das bedeutet, die letzte `0` kommt an Index 0, die letzte `1` an Index 2, die letzte `2` an Index 4.

**3. Ausgabe aufbauen (rückwärts):**
- Lese `2`. `count[2]` ist 5. Platziere an Index 4. `count[2]` wird 4. `output = [_, _, _, _, 2]`
- Lese `0`. `count[0]` ist 1. Platziere an Index 0. `count[0]` wird 0. `output = [0, _, _, _, 2]`
- Lese `1`. `count[1]` ist 3. Platziere an Index 2. `count[1]` wird 2. `output = [0, _, 1, _, 2]`
- Lese `1`. `count[1]` ist 2. Platziere an Index 1. `count[1]` wird 1. `output = [0, 1, 1, _, 2]`
- Lese `2`. `count[2]` ist 4. Platziere an Index 3. `count[2]` wird 3. `output = [0, 1, 1, 2, 2]`

Sortiert! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n + k)$ | $O(n + k)$ |
| **Durchschnittlicher Fall** | $O(n + k)$ | $O(n + k)$ |
| **Schlechtester Fall** | $O(n + k)$ | $O(n + k)$ |

Der Algorithmus iteriert zweimal durch das Eingabe-Array (Größe `n`) und zweimal durch das `count`-Array (Größe `k`). Daher ist die Zeitkomplexität strikt `O(n + k)`. Wenn `k` klein ist (z. B. `k <= n`), ist dies ein echtes lineares `O(n)`-Sortierverfahren!
Die Platzkomplexität beträgt jedoch ebenfalls `O(n + k)`. Wenn Sie versuchen, ein Array `[1, 1000000000]` zu sortieren, wird der Algorithmus blind ein Array mit einer Milliarde Elementen allokieren, nur um zwei Zahlen zu sortieren, was zu einem katastrophalen Out-Of-Memory-Absturz führt.

## Varianten & Optimierungen

- **Negative Zahlen:** Counting Sort setzt inhärent voraus, dass Indizes bei 0 beginnen. Wenn das Array negative Zahlen enthält, finden Sie den absoluten Minimalwert und verschieben das gesamte Array einheitlich durch Addition von `abs(min)`. Nach dem Sortieren subtrahieren Sie diesen Wert wieder.

## Anwendungen in der Praxis

- **Grundlage für Radix Sort:** Wird als stabiler Integer-Sortiermechanismus hinter Radix Sort verwendet, wodurch Radix Sort Zahlen Ziffer für Ziffer sequenziell sortieren kann.
- **Suffix-Arrays:** Fortgeschrittene Algorithmen zur String-Verarbeitung nutzen Counting Sort, um die Präfix-Sortierphasen stark zu optimieren und so Suchen nach Teilstrings zu beschleunigen.

## Verwandte Algorithmen in cOde(n)

- **[sort_08 - Radix Sort](sort_08_radix-sort.md)** — Löst das massive Speicherproblem von Counting Sort, indem extrem große Zahlen Ziffer für Ziffer statt alle auf einmal sortiert werden.
- **[sort_09 - Bucket Sort](sort_09_bucket-sort.md)** — Ein eng verwandtes, nicht-vergleichsbasiertes Sortierverfahren, das Gleitkommazahlen anstelle von Integern verarbeitet.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den enzyklopädischen Standardeintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*