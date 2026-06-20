# 0-1 Rucksackproblem (Branch-and-Bound-Verfahren mit minimalen Kosten)

| | |
|---|---|
| **ID** | `bb_03` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(2^N)$ Worst Case |
| **Schwierigkeitsgrad** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Best-First-Suche](https://en.wikipedia.org/wiki/Best-first_search) |

## Problemstellung

Lösen Sie das 0-1-Rucksackproblem mit der **Least-Cost-Branch-and-Bound-Methode (Best-First)**.
In `bb_01` haben wir den Zustandsraumbaum mithilfe einer Standard-FIFO-Queue (Breitensuche) untersucht. Dabei werden zunächst alle Knoten auf Ebene 1, dann alle Knoten auf Ebene 2 usw. ausgewertet.
Bei „Least Cost B&B“ musst du eine Priority Queue verwenden, um stets den Knoten mit der vielversprechendsten mathematischen Schranke zu erweitern, unabhängig von seiner Tiefe im Baum.

**Eingabe:** Eine Liste von `(value, weight)`-Paaren und ein `capacity`.
**Ausgabe:** Der maximal mögliche Wert.

## Wann man es einsetzt

- Dies ist die standardmäßige, vollständig optimierte Version von „Branch and Bound“. Eine einfache FIFO-Queue wird in Produktions-Engines selten verwendet, da sie enorm viel Zeit damit verschwendet, mathematisch schlechte Verzweigungen zu untersuchen, nur weil diese im Baum flach liegen.
- Durch die Verwendung der Best-First-Suche taucht der Algorithmus direkt in den mathematisch profitabelsten Pfad ein und ermittelt frühzeitig einen massiven `max_profit`, wodurch alles andere sofort ausgemerzt wird.

## Vorgehensweise

Alles aus `bb_01` gilt (die Knotenstruktur, der Zustand, die Begrenzungsfunktion des Fractional Knapsack). Der einzige Unterschied besteht in der Durchlaufreihenfolge.

Da Pythons `heapq` ein Min-Heap ist und wir den Knoten mit der *höchstmöglichen* Gewinn-Obergrenze erweitern wollen, können wir Knoten einfach mit ihren durch `-1` multiplizierten Obergrenzen in die Priority Queue einfügen!

1. Erstelle eine Priority Queue.
2. Füge den Wurzelknoten in die Priority Queue ein, priorisiert nach seiner Obergrenze.
3. Solange die Priority Queue nicht leer ist:
   - Entnehme den Knoten mit der **höchsten Obergrenze**.
   - **Entscheidende Überprüfung:** Wenn die höchstmögliche Obergrenze des besten Knotens in der Queue NOCH IMMER schlechter ist als unser aktuelles `max_profit`, können wir **den gesamten Algorithmus sofort beenden!** Da es sich um eine Priority Queue handelt, ist mathematisch garantiert, dass auch kein anderer in der Queue verbleibender Knoten `max_profit` übertreffen kann.
   - Erweitere den Knoten (Zweige „Take“ und „Skip“).
   - Wenn ein Zweig gültig ist, aktualisiere `max_profit`.
   - Berechne die Grenzen für die neuen Zweige. Wenn ihre Grenzen > max\_profit sind, füge sie in die PQ ein.

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
`capacity = 10`
`Items: I0(40,4), I1(50,5), I2(20,5)`

1. **Wurzel:** `profit=0`. Grenze = 94. `PQ = [Root(94)]`.
2. **Pop Root (94):**
   - I0 nehmen: `profit=40`. Grenze=94. `max_profit=40`.
   - I0 überspringen: `profit=0`. Bound=70.
   - `PQ = [Take(94), Skip(70)]`.
3. **Take (94) vom Stack entfernen:** *(Beachten Sie, dass der „Skip“-Zweig vollständig ignoriert wird!)*
   - I1 ausführen: `profit=90, w=9`. Grenze = 94 (40 + 50 + 1/5 * 20). `max_profit=90`.
   - I1 überspringen: `profit=40, w=4`. Grenzwert=60 (40+20).
   - `PQ = [Take-Take(94), Skip(70), Take-Skip(60)]`.
4. **Pop Take-Take (94):**
   - Take I2: Überkapazität! (w=14 > 10). Ungültig.
   - I2 überspringen: `profit=90`. Grenzwert=90.
   - `PQ = [Skip-I2(90), Skip(70), Take-Skip(60)]`.
5. **Pop Skip-I2 (90):**
   - Das Ende ist erreicht. `max_profit` ist bereits 90.
   - `PQ = [Skip(70), Take-Skip(60)]`.
6. **Pop Skip (70):**
   - Moment! `u.bound (70) <= max_profit (90)`. **SCHLEIFE UNTERBRECHEN!**

Der Algorithmus bricht sofort ab! Er hat die Knoten unterhalb des Zweigs `Skip(70)` gar nicht erst generiert! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | Deutlich schneller als FIFO-B&B | $O(Nodes Generated)$ |
| **Schlimmster Fall** | $O(2^N)$ | $O(2^N)$ |

Die „Best-First“-Heuristik führt im Allgemeinen dazu, dass weitaus weniger Knoten generiert werden als beim FIFO-Ansatz, da sie fast sofort die optimale Lösung (oder eine sehr nahe liegende) findet, wodurch die Grenzen aller anderen ausstehenden Knoten hinfällig werden. Im mathematisch ungünstigsten Fall muss jedoch dennoch der gesamte $O(2^N)$ Raum durchsucht werden.
Die Platzkomplexität wird in durchschnittlichen Fällen erheblich verbessert, da sich weniger Knoten gleichzeitig in der Priority Queue befinden.

## Varianten & Optimierungen

- **A*-Suche:** Die LC-Suche ist mathematisch identisch mit dem A*-Suchalgorithmus auf Graphen! Die Pfadkosten `g(x)` entsprechen dem bisher erzielten Gewinn, und die Heuristik `h(x)` ist die fraktionale Obergrenze der verbleibenden Elemente. Da der fraktionale Rucksack eine zulässige Heuristik ist (sie unterschätzt niemals den maximalen Gewinn), garantiert A* die Optimalität!

## Praktische Anwendungen

- **KI-Planer:** Die Best-First-Suche bildet die Grundlage fast aller modernen KI-Aktionsplanungs- und Routing-Logiken.

## Verwandte Algorithmen in cOde(n)

- **[bb_01 – 0-1-Rucksack-FIFO](bb_01_0-1-knapsack.md)** — Die Breiten-Erste-Suche-Variante desselben Algorithmus.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
