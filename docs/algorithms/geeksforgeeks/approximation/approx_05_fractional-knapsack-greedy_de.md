# Fractional Knapsack (Greedy Bound)

| | |
|---|---|
| **ID** | `approx_05` |
| **Kategorie** | approximation |
| **Komplexität (erforderlich)** | $O(N \log N)$ |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **Wikipedia** | [Continuous knapsack problem](https://en.wikipedia.org/wiki/Continuous_knapsack_problem) |

## Problemstellung

Gegeben sind $N$ Elemente, jedes mit einem `weight` und einem `value`, sowie ein Rucksack mit einer maximalen `capacity`. Finde den maximalen Gesamtwert, den du transportieren kannst.
Im Gegensatz zum 0-1 Knapsack-Problem, bei dem man ein Element entweder ganz nehmen oder zurücklassen muss, ist es hier erlaubt, **Bruchteile** eines Elements zu nehmen (z. B. ergeben 50 % eines Elements 50 % seines Gewichts und 50 % seines Wertes).

Obwohl dieses Problem *exakt* mit einem Greedy-Ansatz gelöst werden kann, wird das Ergebnis dieser exakten fraktionalen Lösung häufig als **obere Schranke (Upper Bound Approximation)** für das NP-schwere 0-1 Knapsack-Problem in Branch-and-Bound-Algorithmen verwendet.

**Eingabe:** Eine Liste von `(value, weight)`-Paaren und eine `capacity`.
**Ausgabe:** Der maximal mögliche Wert (oft als Float).

## Wann man es verwendet

- Zur Lösung von Ressourcenallokationsproblemen mit kontinuierlichen Materialien (Goldstaub, Flüssigkeiten, Getreide).
- Entscheidend ist die Verwendung als `Bounding`-Funktion in der Branch-and-Bound-Lösung für das 0-1 Knapsack-Problem. Durch die Berechnung des fraktionalen Knapsack-Wertes kennt man das absolute theoretische Maximum eines Zweigs. Wenn dieses fraktionale Maximum schlechter ist als die aktuell beste 0-1 Lösung, kann man den Zweig sofort abschneiden (Pruning)!

## Ansatz

Da wir Bruchteile von Elementen nehmen können, müssen wir uns nie Sorgen machen, Platz zu "verschwenden". Wir können den Rucksack immer bis zum Rand füllen (sofern wir genug Gesamtgewicht zur Verfügung haben).
Daher ist die logischste Greedy-Entscheidung, immer das Element zu wählen, das den **höchsten Wert pro Gewichtseinheit** bietet.

1. Berechne das Verhältnis `value / weight` für jedes Element.
2. Sortiere die Elemente in **absteigender Reihenfolge** dieses Verhältnisses.
3. Iteriere durch die sortierten Elemente:
   - Wenn das gesamte Element in die verbleibende Kapazität passt, nimm es komplett! Ziehe sein Gewicht von der Kapazität ab und addiere seinen Wert zum Gesamtwert.
   - Wenn das gesamte Element *nicht* hineinpasst, nimm genau den Bruchteil davon, der die verbleibende Kapazität perfekt ausfüllt. Addiere den proportionalen Wert zum Gesamtwert und **brich** die Schleife ab (da der Rucksack nun exakt voll ist).
4. Gib den Gesamtwert zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for approx_05: Fractional Knapsack (Greedy).

Given n items each with a value and a weight, and a
"""


def solve(values, weights, n, capacity):
    """Fractional knapsack via greedy by value/weight ratio."""
    if capacity <= 0 or n == 0:
        return 0.0
    items = sorted(
        range(n),
        key=lambda i: values[i] / weights[i],
        reverse=True,
    )
    remaining = capacity
    total = 0.0
    for i in items:
        if remaining <= 0:
            break
        if weights[i] <= remaining:
            total += values[i]
            remaining -= weights[i]
        else:
            total += values[i] * (remaining / weights[i])
            remaining = 0
    return total
```

</details>

## Durchlauf

`capacity = 50`
`items = [(V:60, W:10), (V:100, W:20), (V:120, W:30)]`

1. **Verhältnisse berechnen:**
   - Element 1: 60 / 10 = 6.0
   - Element 2: 100 / 20 = 5.0
   - Element 3: 120 / 30 = 4.0
2. **Sortieren:** Bereits sortiert `[Element 1, Element 2, Element 3]`.
3. **Iterieren:**
   - **Element 1:** Gewicht 10 <= 50. Alles nehmen! `capacity = 40`, `total_value = 60`.
   - **Element 2:** Gewicht 20 <= 40. Alles nehmen! `capacity = 20`, `total_value = 60 + 100 = 160`.
   - **Element 3:** Gewicht 30 > 20. Kann nicht alles nehmen. Bruchteil nehmen!
     - `fraction = 20 / 30 = 2/3`.
     - `value added = 120 * (2/3) = 80`.
     - `total_value = 160 + 80 = 240`.
     - `capacity = 0`. Schleife abbrechen.

Ausgabe: 240.0. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(1)$ |

Das Sortieren der Elemente benötigt $O(N \log N)$ Zeit. Die Greedy-Iteration benötigt exakt $O(N)$ Zeit. Der Flaschenhals ist das Sortieren, was die gesamte Zeitkomplexität strikt auf $O(N \log N)$ festlegt.
Die Platzkomplexität beträgt $O(1)$ zusätzlichen Speicherplatz, wenn in-place sortiert wird (oder $O(N)$, abhängig von der Implementierung des Sortieralgorithmus).

## Varianten & Optimierungen

- **$O(N)$ Auswahlalgorithmus:** Wenn $N$ riesig ist, muss man nicht das gesamte Array sortieren! Man kann einen deterministischen QuickSelect-Algorithmus (Median of Medians) verwenden, um das "Pivot"-Element, das die Kapazitätsgrenze überschreitet, in exakt $O(N)$ Zeit zu finden. Man nimmt alles mit einem höheren Verhältnis als das Pivot und einen Bruchteil des Pivots selbst.

## Anwendungen in der Praxis

- **Rohstoffhandel:** Maximierung des Geldwerts eines Frachtschiffs, das kontinuierliche Schüttgüter (Getreide, Rohöl, flüssige Chemikalien) transportiert.

## Verwandte Algorithmen in cOde(n)

- **[bb_03 - 0-1 Knapsack Branch and Bound](../branch_and_bound/bb_03_0-1-knapsack-least-cost-b-b.md)** — Verwendet diesen exakten Fractional Knapsack-Algorithmus intern, um die theoretische obere Schranke eines Zweigs zu berechnen!
- **[greedy_02 - Fractional Knapsack](../greedy/greedy_02_fractional-knapsack.md)** — Der identische Kernalgorithmus.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*