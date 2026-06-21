# 0-1 Knapsack (Least Cost Branch & Bound)

| | |
|---|---|
| **ID** | `bb_03` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(2^N)$ Schlechtester Fall |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Best-first search](https://en.wikipedia.org/wiki/Best-first_search) |

## Problemstellung

Lösen Sie das 0-1 Knapsack Problem mittels **Least Cost (Best-First) Branch and Bound**.
In `bb_01` haben wir den Zustandsraum-Baum mithilfe einer Standard-FIFO-Queue (Breitensuche) durchsucht. Dies evaluiert alle Knoten auf Ebene 1, dann alle Knoten auf Ebene 2 usw.
Beim Least Cost B&B müssen Sie eine Priority Queue verwenden, um immer den Knoten mit der vielversprechendsten mathematischen Schranke zu expandieren, unabhängig von seiner Tiefe im Baum.

**Eingabe:** Eine Liste von `(value, weight)`-Paaren und eine `capacity`.
**Ausgabe:** Der maximal mögliche Wert.

## Wann man es verwendet

- Dies ist die standardmäßige, vollständig optimierte Version von Branch and Bound. Eine einfache FIFO-Queue wird in produktiven Systemen selten verwendet, da sie enorme Mengen an Zeit damit verschwendet, mathematisch schlechte Zweige zu untersuchen, nur weil sie flach im Baum liegen.
- Durch die Verwendung der Best-First-Suche taucht der Algorithmus direkt in den profitabelsten mathematischen Pfad ein und etabliert frühzeitig einen massiven `max_profit`, wodurch sofort alles andere abgeschnitten (pruned) wird.

## Ansatz

Alles aus `bb_01` findet Anwendung (die Knotenstruktur, der Zustand, die Bounding-Funktion des Fractional Knapsack). Der einzige Unterschied ist die Reihenfolge der Traversierung.

Da Pythons `heapq` ein Min-Heap ist und wir den Knoten mit der *höchsten* möglichen Profit-Schranke expandieren wollen, können wir die Knoten einfach mit ihren Schranken multipliziert mit `-1` in die Priority Queue einfügen!

1. Erstellen Sie eine Priority Queue.
2. Fügen Sie den Wurzelknoten in die PQ ein, priorisiert nach seiner oberen Schranke.
3. Solange die PQ nicht leer ist:
   - Entnehmen Sie den Knoten mit der **höchsten Schranke**.
   - **Entscheidende Prüfung:** Wenn die höchstmögliche Schranke des besten Knotens in der Queue IMMER NOCH schlechter ist als unser aktueller `max_profit`, können wir **den gesamten Algorithmus sofort beenden!** Da es sich um eine Priority Queue handelt, garantieren wir mathematisch, dass kein anderer verbleibender Knoten in der Queue den `max_profit` übertreffen kann.
   - Expandieren Sie den Knoten (Zweige für "Nehmen" und "Überspringen").
   - Wenn ein Zweig gültig ist, aktualisieren Sie `max_profit`.
   - Berechnen Sie die Schranken für die neuen Zweige. Wenn deren Schranken > max\_profit sind, fügen Sie sie in die PQ ein.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bb_03: 0/1 Knapsack (Least-Cost B&B).

Solve 0/1 knapsack via Least-Cost (LC) branch and
"""


def solve(values, weights, capacity, n):
    """0/1 Knapsack via Least-Cost Branch and Bound.

    Sort items by value/weight ratio descending. Build a
    priority queue (min-heap by lower bound) of live nodes.
    Each node has level, accumulated value, accumulated weight,
    and an upper bound (fractional knapsack from this level).
    Pop the node with the smallest lower bound; if it is at
    leaf level, update the best. Generate both children
    (exclude and include the next item), compute their bounds,
    and enqueue if they are still promising (UB <= best).
    """
    if n == 0 or capacity <= 0:
        return 0
    # Sort items by value/weight ratio descending.
    order = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    v_sorted = [values[i] for i in order]
    w_sorted = [weights[i] for i in order]
    # Precompute suffix sums for the fractional upper bound.
    import heapq
    INF = float("inf")
    best = 0

    def upper_bound(level, cur_value, cur_weight):
        """Fractional knapsack UB from `level` onwards."""
        if cur_weight > capacity:
            return -INF
        value = cur_value
        weight = cur_weight
        for i in range(level, n):
            if weight + w_sorted[i] <= capacity:
                weight += w_sorted[i]
                value += v_sorted[i]
            else:
                # Take a fraction of item i.
                frac = (capacity - weight) / w_sorted[i]
                value += v_sorted[i] * frac
                break
        return value

    def lower_bound(level, cur_value, cur_weight):
        """LB: same as UB but break instead of taking fraction."""
        if cur_weight > capacity:
            return -INF
        value = cur_value
        weight = cur_weight
        for i in range(level, n):
            if weight + w_sorted[i] <= capacity:
                weight += w_sorted[i]
                value += v_sorted[i]
            else:
                break
        return value

    # For MAXIMIZATION, the correct LC search is "best-first by
    # upper bound": pop the node with the highest UB. Early-exit
    # when the head's UB is no greater than the current best.
    # We use a max-heap by negating the UB.
    # Each queue entry: (neg_ub, counter, level, cur_value, cur_weight)
    counter = 0
    pq = []
    initial_ub = upper_bound(0, 0, 0)
    heapq.heappush(pq, (-initial_ub, 0, 0, 0, 0, 0))
    while pq:
        neg_ub, _, level, cur_value, cur_weight, _ = heapq.heappop(pq)
        ub = -neg_ub
        # Early-exit: if the highest UB in the queue is no
        # better than our best-known solution, no future node
        # can improve on `best`.
        if ub <= best:
            break
        if level == n:
            # Leaf.
            if cur_value > best:
                best = cur_value
            continue
        # Right child: exclude item at this level.
        right_value = cur_value
        right_weight = cur_weight
        right_ub = upper_bound(level + 1, right_value, right_weight)
        if right_ub > best:
            right_lb = lower_bound(level + 1, right_value, right_weight)
            if right_lb < INF:
                counter += 1
                heapq.heappush(pq, (-right_ub, counter, level + 1,
                                    int(right_value),
                                    int(right_weight), 0))
        # Left child: include item at this level (if it fits).
        if cur_weight + w_sorted[level] <= capacity:
            left_value = cur_value + v_sorted[level]
            left_weight = cur_weight + w_sorted[level]
            left_ub = upper_bound(level + 1, left_value, left_weight)
            if left_ub > best:
                left_lb = lower_bound(level + 1, left_value, left_weight)
                if left_lb < INF:
                    counter += 1
                    heapq.heappush(pq, (-left_ub, counter, level + 1,
                                        int(left_value),
                                        int(left_weight), 0))
    return best
```

</details>

## Durchlauf

*(Konzeptionell)*
`capacity = 10`
`Items: I0(40,4), I1(50,5), I2(20,5)`

1. **Wurzel:** `profit=0`. Schranke=94. `PQ = [Root(94)]`.
2. **Pop Wurzel (94):**
   - Nehme I0: `profit=40`. Schranke=94. `max_profit=40`.
   - Überspringe I0: `profit=0`. Schranke=70.
   - `PQ = [Take(94), Skip(70)]`.
3. **Pop Take (94):** *(Beachten Sie, dass der Skip-Zweig komplett ignoriert wird!)*
   - Nehme I1: `profit=90, w=9`. Schranke=94 (40+50 + 1/5*20). `max_profit=90`.
   - Überspringe I1: `profit=40, w=4`. Schranke=60 (40+20).
   - `PQ = [Take-Take(94), Skip(70), Take-Skip(60)]`.
4. **Pop Take-Take (94):**
   - Nehme I2: Über Kapazität! (w=14 > 10). Ungültig.
   - Überspringe I2: `profit=90`. Schranke=90.
   - `PQ = [Skip-I2(90), Skip(70), Take-Skip(60)]`.
5. **Pop Skip-I2 (90):**
   - Ende erreicht. `max_profit` ist bereits 90.
   - `PQ = [Skip(70), Take-Skip(60)]`.
6. **Pop Skip (70):**
   - Moment! `u.bound (70) <= max_profit (90)`. **SCHLEIFE ABBRECHEN!**

Der Algorithmus terminiert sofort! Er hat nicht einmal die Knoten unterhalb des `Skip(70)`-Zweigs generiert! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | Viel schneller als FIFO B&B | $O(Generierte Knoten)$ |
| **Schlechtester Fall** | $O(2^N)$ | $O(2^N)$ |

Die Best-First-Heuristik führt im Allgemeinen dazu, dass weit weniger Knoten generiert werden als beim FIFO-Ansatz, da sie die optimale Lösung (oder eine sehr nahe liegende) fast sofort findet, wodurch die Schranken aller anderen ausstehenden Knoten obsolet werden. Im mathematischen Schlechtesten Fall degradiert sie jedoch dazu, den gesamten $O(2^N)$-Raum zu untersuchen.
Die Platzkomplexität ist in durchschnittlichen Fällen stark verbessert, da weniger Knoten gleichzeitig in der Priority Queue liegen.

## Varianten & Optimierungen

- **A* Suche:** LC-Suche ist mathematisch identisch mit dem A*-Suchalgorithmus auf Graphen! Die Pfadkosten `g(x)` sind der bisher gesammelte Profit, und die Heuristik `h(x)` ist die obere Schranke des Fractional Knapsack für die verbleibenden Items. Da der Fractional Knapsack eine zulässige Heuristik ist (er unterschätzt den maximalen Profit nie), garantiert A* Optimalität!

## Anwendungen in der Praxis

- **KI-Planer:** Best-First-Suche ist das Fundament fast aller modernen KI-Aktionsplanungs- und Routing-Logiken.

## Verwandte Algorithmen in cOde(n)

- **[bb_01 - 0-1 Knapsack FIFO](bb_01_0-1-knapsack.md)** — Die Breitensuche-Variante desselben Algorithmus.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*