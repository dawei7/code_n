# Fractional Knapsack Problem

| | |
|---|---|
| **ID** | `greedy_02` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **GeeksForGeeks Äquivalent** | [Fractional Knapsack Problem](https://www.geeksforgeeks.org/fractional-knapsack-problem/) |

## Problemstellung

Gegeben sind `N` Gegenstände, wobei jeder Gegenstand einen `value` (Wert) und ein `weight` (Gewicht) besitzt. Sie haben einen Rucksack mit einer maximalen Gewichtskapazität `W`.
Ihr Ziel ist es, den Gesamtwert im Rucksack zu maximieren.
Entscheidend ist, dass Sie Gegenstände in kleinere Bruchteile zerlegen dürfen (z. B. ergibt die Entnahme von 50 % des Gewichts eines Gegenstands 50 % seines Wertes).

**Eingabe:** Maximale Kapazität `W` und ein Array von Objekten `items` mit `value`- und `weight`-Eigenschaften.
**Ausgabe:** Eine Fließkommazahl, die den maximal erreichbaren Gesamtwert darstellt.

## Wann ist dieser Ansatz zu verwenden?

- Nur wenn das Problem explizit besagt, dass Gegenstände unendlich teilbar sind (z. B. Goldstaub, Sand, Flüssigkeiten).
- *Einschränkung:* Wenn Gegenstände NICHT zerlegt werden können (z. B. ein massiver Goldbarren, ein Laptop), SCHEITERT dieser Greedy-Ansatz vollständig. In diesem Fall müssen Sie den $O(N \times W)$ Algorithmus der Dynamischen Programmierung für das "0/1 Knapsack Problem" verwenden!

## Ansatz

**1. Die Greedy-Metrik:**
Wenn wir den Wert maximieren und das Gewicht minimieren wollen, sollten wir die Gegenstände basierend auf ihrer "Dichte" bewerten!
Berechnen Sie das `value-to-weight ratio` (Wert-Gewicht-Verhältnis) für jeden Gegenstand (`ratio = value / weight`).
Ein Gegenstand mit einem Verhältnis von 10/kg ist weitaus wertvoller als ein Gegenstand mit einem Verhältnis von 2/kg.

**2. Die Sortierung:**
Sortieren Sie alle Gegenstände in absteigender Reihenfolge basierend auf ihrem `ratio`.

**3. Das Packen:**
Iterieren Sie durch die sortierten Gegenstände.
- Wenn der gesamte Gegenstand in die verbleibende Kapazität des Rucksacks passt, nehmen Sie ihn vollständig! Subtrahieren Sie sein Gewicht von der Kapazität und addieren Sie seinen vollen Wert zu Ihrem Gesamtwert.
- Wenn der Gegenstand schwerer ist als die verbleibende Kapazität, nehmen Sie einen BRUCHTEIL davon! Nehmen Sie spezifisch `remaining_capacity` kg davon. Addieren Sie `remaining_capacity * ratio` zu Ihrem Gesamtwert. Der Rucksack ist nun exakt voll! Brechen Sie die Schleife ab.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_02: Fractional Knapsack.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(values, weights, capacity, n):
    # Sort items by value-to-weight ratio (descending). Pair indices
    # so we can sort on the ratio without losing the alignment.
    order = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    remaining = capacity
    total = 0.0
    for index in order:
        w = weights[index]
        if remaining >= w:
            total += values[index]
            remaining -= w
        else:
            total += values[index] * (remaining / w)
            break
    return total
```

</details>

## Durchlauf

`W = 50`. Gegenstände: `I1(v=60, w=10)`, `I2(v=100, w=20)`, `I3(v=120, w=30)`.

1. Verhältnisse berechnen:
   - `I1`: 60 / 10 = 6.0
   - `I2`: 100 / 20 = 5.0
   - `I3`: 120 / 30 = 4.0
2. Absteigend nach Verhältnis sortieren: `[I1, I2, I3]`.
3. `I1` bewerten (Gewicht 10):
   - 0 + 10 \le 50. Alles nehmen!
   - `total = 60`. `current_weight = 10`.
4. `I2` bewerten (Gewicht 20):
   - 10 + 20 \le 50. Alles nehmen!
   - `total = 60 + 100 = 160`. `current_weight = 30`.
5. `I3` bewerten (Gewicht 30):
   - 30 + 30 = 60 > 50. Zu schwer! Einen Bruchteil nehmen.
   - `remaining_capacity = 50 - 30 = 20`.
   - 20 Gewichtseinheiten von den 30 verfügbaren nehmen.
   - `fractional_value = 120 * (20 / 30) = 80`.
   - `total = 160 + 80 = 240`.
   - Abbruch.

Ergebnis `240.0`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(1)$ oder $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(1)$ oder $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(1)$ oder $O(N)$ |

Die Zeitkomplexität wird maßgeblich durch das $O(N \log N)$ Sortieren des Gegenstände-Arrays basierend auf dem Verhältnis bestimmt. Die anschließende Pack-Schleife ist ein einfacher linearer Durchlauf in $O(N)$.
Die Platzkomplexität beträgt $O(1)$, wenn wir das Array der Gegenstände in-place sortieren, oder $O(N)$, wenn wir ein neues Array von Objekten erstellen müssen, um die Verhältnisse zu speichern, ohne die Eingabe zu verändern.

## Varianten & Optimierungen

- **0/1 Knapsack Problem (`dp_01`):** Die nicht-teilbare DP-Version. Warum scheitert Greedy bei 0/1? Betrachten Sie `W=50`. Gegenstände: `A(v=60, w=10)`, `B(v=100, w=20)`, `C(v=120, w=30)`. Greedy nimmt A und B (Gesamtwert 160, Gewicht 30). Es kann C nicht mehr aufnehmen und endet mit 20 Einheiten freiem Platz. Die optimale Wahl wäre jedoch gewesen, A komplett auszulassen und B und C zu nehmen! (Gesamtwert 220, Gewicht 50).

## Anwendungen in der Praxis

- **Rohstoffhandel:** Bestimmung der optimalen Mischung von losen Schüttgütern (wie Getreide, Sand oder Flüssigkeiten), um ein Frachtschiff mit begrenzter Tonnage zu beladen und den Gewinn bei der Lieferung zu maximieren.

## Verwandte Algorithmen in cOde(n)

- **[dp_01 - 0/1 Knapsack Problem](../dynamic/dp_01_0-1-knapsack.md)** — Das DP-Gegenstück, das erforderlich ist, wenn Bruchteile nicht zulässig sind.
- **[greedy_01 - Activity Selection](greedy_01_activity-selection.md)** — Der andere grundlegende einführende Greedy-Algorithmus, der auf dem Sortieren nach einer benutzerdefinierten Metrik basiert.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*