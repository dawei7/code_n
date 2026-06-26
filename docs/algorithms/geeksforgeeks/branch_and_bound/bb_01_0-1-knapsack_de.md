# 0-1 Knapsack (Branch and Bound)

| | |
|---|---|
| **ID** | `bb_01` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(2^N)$ Schlechtester Fall |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Branch and bound](https://de.wikipedia.org/wiki/Branch-and-Bound-Verfahren) |

## Problemstellung

Gegeben sind $N$ Gegenstände, jeweils mit einem `weight` (Gewicht) und einem `value` (Wert), sowie ein Rucksack mit einer maximalen `capacity` (Kapazität). Ziel ist es, den maximalen Gesamtwert zu finden, den man transportieren kann. Man muss einen Gegenstand entweder vollständig mitnehmen oder zurücklassen (0-1-Eigenschaft).
Im Gegensatz zur Lösung mittels Dynamischer Programmierung, die eine pseudo-polynomielle Zeitkomplexität von $O(N \cdot W)$ aufweist und bei sehr großen $W$ versagt, muss dieses Problem mittels **Branch and Bound** gelöst werden. Hierbei wird der exponentielle Zustandsraum systematisch durchsucht, wobei ungültige oder suboptimale Pfade aggressiv beschnitten (pruning) werden, um eine schnelle durchschnittliche Performance zu erzielen.

**Eingabe:** Eine Liste von `(value, weight)`-Paaren und eine `capacity`.
**Ausgabe:** Der maximal mögliche Wert.

## Wann sollte man es verwenden?

- Wenn die Rucksackkapazität $W$ astronomisch groß ist (z. B. Millionen), wodurch die Standard-DP-Tabelle nicht mehr in den Arbeitsspeicher passt.
- Branch and Bound ist der absolute Industriestandard für die Lösung exakter NP-harter kombinatorischer Optimierungsprobleme (wie der Ganzzahligen Linearen Programmierung).

## Ansatz

Ein Standard-Backtracking-Algorithmus erkundet jede mögliche Kombination aus Mitnehmen oder Zurücklassen eines Gegenstands und bildet einen massiven Binärbaum der Höhe $N$. Dies benötigt $O(2^N)$ Zeit.

**Branch and Bound** verbessert dies, indem Zweige, von denen wir mathematisch wissen, dass sie unsere aktuell beste Lösung nicht übertreffen können, sofort abgebrochen (beschnitten) werden!

1. **Sortieren:** Sortieren Sie die Gegenstände nach ihrem `value/weight`-Verhältnis in absteigender Reihenfolge. Dies stellt sicher, dass wir die "besten" Gegenstände zuerst bewerten und früh eine starke Lösung finden, um den Rest des Baumes effizienter zu beschneiden.
2. **Der Zustand:** Ein Knoten in unserem Suchbaum speichert:
   - `level`: der aktuelle Index des Gegenstands.
   - `profit`: der bisher gesammelte Gesamtwert.
   - `weight`: das bisher gesammelte Gesamtgewicht.
3. **Die Schranke (Upper Bound):** Was ist für einen beliebigen Knoten das absolute *mathematische Maximum* an Profit, das wir erzielen könnten, wenn wir diesen Zweig weiterverfolgen würden?
   - Wir berechnen dies mithilfe des **Greedy Fractional Knapsack**-Algorithmus! Wir nehmen den aktuellen `profit` und fügen dann gierig die verbleibenden Gegenstände (auch bruchstückhaft) hinzu, bis die Kapazität vollständig ausgeschöpft ist.
   - Wenn diese `upper_bound` **kleiner oder gleich** unserem bisher gefundenen globalen `max_profit` ist, hören wir sofort auf, diesen Knoten zu untersuchen! Selbst in einer mathematisch perfekten, fraktionierten Welt kann dieser Zweig unser aktuelles Optimum nicht schlagen.
4. **Traversierung:** Wir verwenden eine einfache Queue (BFS/FIFO), um den Baum zu durchsuchen. (Für einen noch schnelleren Ansatz unter Verwendung von Priority Queues, siehe `bb_03`).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bb_01: 0/1 Knapsack.

Each item is either in the knapsack or not. Recursive choice
with a capacity check. Setup keeps n small (n <= 8) so
exhaustive search is feasible; a real solver would use DP or
branch-and-bound with a fractional-relaxation upper bound.
"""


def solve(values, weights, capacity, n):
    best = 0

    def helper(i, value, weight):
        nonlocal best
        if i == n:
            if value > best:
                best = value
            return
        # Skip item i.
        helper(i + 1, value, weight)
        # Take item i (only if it fits).
        if weight + weights[i] <= capacity:
            helper(i + 1, value + values[i], weight + weights[i])

    helper(0, 0, 0)
    return best
```

</details>

## Ablaufbeispiel

*(Konzeptionell)*
`capacity = 10`
`Gegenstände (sortiert nach Verhältnis): (v:40, w:4), (v:50, w:5), (v:20, w:5)`

1. **Wurzelknoten:** Level -1. `profit=0`, `weight=0`. Theoretische Obergrenze: Nimm Gegenstand 0 (w=4), Gegenstand 1 (w=5) und 1/5 von Gegenstand 2 (w=1). Schranke = 40 + 50 + (1/5 * 20) = 94.
2. **Untersuche "Nimm Gegenstand 0":** `profit=40`, `weight=4`. Schranke = 94. Gültiger Zweig! `max_profit = 40`.
3. **Untersuche "Überspringe Gegenstand 0":** `profit=0`, `weight=0`. Schrankenberechnung: Nimm Gegenstand 1 (w=5), Gegenstand 2 (w=5). Schranke = 50 + 20 = 70. Gültiger Zweig, aber eine deutlich niedrigere Schranke!
4. **Tief im Baum:** Wenn wir schließlich eine Lösung finden, die Gegenstand 0 und 1 nimmt, `profit=90`, `max_profit = 90`.
5. Nun gehen wir zurück, um einen Knoten im Zweig "Überspringe Gegenstand 0" zu bewerten. Dessen Schranke ist 70. Ist 70 > 90? Nein! Wir beschneiden (PRUNE) sofort diesen gesamten Teil des Suchbaums!

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | Viel schneller als 2^N | $O(2^N)$ |
| **Schlechtester Fall** | $O(2^N)$ | $O(2^N)$ |

Im mathematisch schlechtesten Fall, in dem die Schranken den Algorithmus perfekt täuschen, degeneriert er zur Überprüfung jeder Teilmenge, was $O(2^N)$ Zeit und Platz benötigt (da die Queue die breite BFS-Ebene speichert).
In durchschnittlichen, praxisnahen Fällen beschneidet Branch and Bound jedoch über 99 % des Baumes, was ihn unglaublich schnell macht.

## Varianten & Optimierungen

- **Best-First Search (LC-Search):** Anstatt eine Standard-FIFO-Queue zu verwenden (die den Baum schichtweise auswertet), verwenden wir eine Priority Queue (Max-Heap), sortiert nach der `bound`! Das bedeutet, dass wir immer die mathematisch vielversprechendsten Zweige zuerst untersuchen. Dadurch finden wir den optimalen `max_profit` viel früher, was das Beschneiden massiv verstärkt! (Siehe `bb_03`).

## Anwendungen in der Praxis

- **Solver für Ganzzahlige Lineare Programmierung:** Werkzeuge wie Gurobi und CPLEX verwenden hochoptimierte Branch-and-Bound-Engines, um Planungs- und Logistikprobleme für Fortune-500-Unternehmen zu lösen.

## Verwandte Algorithmen in cOde(n)

- **[approx_05 - Fractional Knapsack](../approximation/approx_05_fractional-knapsack-greedy.md)** — Die $O(N)$-Berechnung, die als Schrankenfunktion verwendet wird.
- **[bb_03 - Least Cost B&B Knapsack](bb_03_0-1-knapsack-least-cost-b-b.md)** — Die Optimierung mittels Priority Queue.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den enzyklopädischen Standardeintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*