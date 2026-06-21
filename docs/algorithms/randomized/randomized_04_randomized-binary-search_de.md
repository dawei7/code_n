# Randomized Binary Search

| | |
|---|---|
| **ID** | `randomized_04` |
| **Kategorie** | randomized |
| **Komplexität (erforderlich)** | $O(\log N)$ erwartet |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **LeetCode-Äquivalent** | N/A (theoretische Variation) |

## Problemstellung

Gegeben ist ein sortiertes Array aus eindeutigen Integern `nums` und ein `target`. Finde den Index von `target`.
Anstatt der standardmäßigen Binary Search, die strikt den exakten `mid`-Index prüft, implementiere eine **Randomized Binary Search**, die einen zufälligen Index innerhalb der aktuellen Grenzen wählt.

**Eingabe:** Ein sortiertes Integer-Array `nums` und ein Integer `target`.
**Ausgabe:** Der Index von `target` oder `-1`, falls nicht gefunden.

## Wann ist es zu verwenden?

- Primär eine akademische Übung, um probabilistische Leistungsschranken zu untersuchen.
- In der Praxis ist die standardmäßige Binary Search weitaus überlegen, da die Berechnung von `mid = (L + R) / 2` deterministisch ist und im Schlechtesten Fall $O(\log N)$ garantiert. Randomisierung bietet hier keine defensiven Vorteile, da Binary Search bei keiner Eingabepermutation schlechter als $O(\log N)$ abschneidet (im Gegensatz zu Quicksort).

## Ansatz

Bei der standardmäßigen Binary Search reduzieren wir den Suchraum, indem wir `mid = left + (right - left) // 2` wählen. Dies garantiert, dass der Suchraum exakt halbiert wird.
Bei der Randomized Binary Search wählen wir `random_idx = random.randint(left, right)`.

1. Initialisiere `left = 0`, `right = len(nums) - 1`.
2. Solange `left <= right`:
   - Wähle einen zufälligen Index `r` zwischen `left` und `right`.
   - Wenn `nums[r] == target`, gib `r` zurück.
   - Wenn `nums[r] < target`, muss sich das `target` rechts befinden! `left = r + 1`.
   - Wenn `nums[r] > target`, muss sich das `target` links befinden! `right = r - 1`.
3. Wenn die Schleife ohne Rückgabewert endet, gib `-1` zurück.

**Warum läuft dies immer noch in $O(\log N)$ erwarteter Zeit?**
Wenn man einen zufälligen Index wählt, ist die Wahrscheinlichkeit, einen Index nahe der Mitte zu wählen (gut), genauso hoch wie einen nahe der Ränder (schlecht).
Im Durchschnitt teilt ein zufällig gewählter Punkt ein Segment der Größe N in zwei Segmente der erwarteten Größe N/2 und N/2. Über mehrere Iterationen bleibt der erwartete Reduktionsfaktor geometrisch, was eine erwartete Höhe von $O(\log N)$ für den Rekursionsbaum ergibt.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for randomized_04: Randomized Binary Search.

Given a sorted list of n distinct integers and a
"""


def solve(arr, n, target):
    """Randomized binary search.

    Pick a uniformly random pivot in [lo, hi], then narrow
    the range based on whether arr[pivot] is less than,
    greater than, or equal to target. Expected O(log n).
    """
    import random
    if n == 0:
        return -1
    lo, hi = 0, n - 1
    while lo <= hi:
        pivot = random.randint(lo, hi)
        if arr[pivot] == target:
            return pivot
        if arr[pivot] < target:
            lo = pivot + 1
        else:
            hi = pivot - 1
    return -1
```

</details>

## Durchlauf

`nums = [10, 20, 30, 40, 50, 60]`, `target = 50`.
`L = 0, R = 5`.

1. **Iteration 1:** `random.randint(0, 5)` ergibt `1`.
   - `nums[1] = 20`. `20 < 50`.
   - `target` liegt rechts. `L = 2, R = 5`.
2. **Iteration 2:** `random.randint(2, 5)` ergibt `4`.
   - `nums[4] = 50`. `50 == 50`. `target` gefunden!
   - Gib `4` zurück. ✓

*Hinweis: Wenn der Zufallszahlengenerator `0`, dann `1`, dann `2`... würfeln würde, würde es zu einer linearen Suche mit $O(N)$ degenerieren. Aber die Wahrscheinlichkeit dafür ist verschwindend gering.*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ erwartet | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Der Bestfall ist das Finden des `target` beim ersten zufälligen Tipp $O(1)$.
Der durchschnittliche Fall ist $O(\log N)$, da der erwartete Reduktionsfaktor ein Bruchteil ist.
Der absolute Schlechteste Fall ist $O(N)$, wenn der RNG konsistent den absoluten Randwert wählt (z. B. immer `left` wählt, wenn das `target` bei `right` liegt).
Die Platzkomplexität ist $O(1)$ für den iterativen Ansatz.

## Varianten & Optimierungen

- **Interpolation Search:** Anstatt einen zufälligen Punkt oder den exakten Mittelpunkt zu wählen, sagt die Interpolation Search den Index basierend auf den Werten an den Rändern voraus: `pos = L + ((target - arr[L]) * (R - L) / (arr[R] - arr[L]))`. Bei gleichmäßig verteilten Daten ist die Interpolation Search $O(log log N)$!

## Anwendungen in der Praxis

- **Theoretische Analyse:** Wird häufig in Informatik-Lehrplänen verwendet, um randomisierte Algorithmen und die Herleitung von Erwartungswerten einzuführen, bevor schwierigere Algorithmen wie Randomized Treaps oder Skip Lists behandelt werden.

## Verwandte Algorithmen in cOde(n)

- **[searching_01 - Binary Search](../searching/searching_01_binary-search.md)** — Der deterministische und weitaus überlegene Standardansatz.
- **[randomized_01 - Randomized Quicksort](randomized_01_randomized-quicksort.md)** — Ein Szenario, in dem die Randomisierung des Pivots tatsächlich sehr vorteilhaft ist.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*