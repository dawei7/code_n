## General

**Represent both constraints in one state.** Let `reachable[a][b]` mean that some assignment of the items processed so far places exactly weight `a` in bag 1 and exactly weight `b` in bag 2. Initially only `(0, 0)` is reachable.

For an item of weight `t`, every old state has three choices: leave the item out, reach `(a + t, b)` when it fits in bag 1, or reach `(a, b + t)` when it fits in bag 2. These are precisely the legal decisions, and taking their union preserves every feasible assignment without ever putting one item in both bags.

Iterate both capacity coordinates downward. Any state created for the current item then lies at a larger coordinate that has already been visited, so it cannot be extended again during the same iteration. After all items, scan the reachable states and maximize `a + b`.

## Complexity detail

Let $n$ be the number of items. Each item scans the $(w1+1)(w2+1)$ capacity grid, taking $O(n\cdot w1\cdot w2)$ time. The boolean grid uses $O(w1\cdot w2)$ auxiliary space.

The benchmark sets size $N=n$ and also uses `w1 = w2 = N`, with tiers 2, 5, and 10 spanning 5x. The accepted dynamic program has $O(N^3)$ work under that scaling. A direct exact search explores all three decisions for every item in $O(3^N)$ time; the selected tiers let it finish all outputs while still exposing its principal exponential growth.

## Alternatives and edge cases

- **Top-down memoization:** Caching `(item index, remaining w1, remaining w2)` has the same asymptotic bounds and can skip unreachable states, at the cost of recursion and dictionary overhead.
- **Enumerate all assignments:** Trying skip, bag 1, and bag 2 independently for every item is exact but takes exponential time.
- **No fitting item:** The initial `(0, 0)` state remains reachable, so the answer is `0`.
- **One item:** It contributes once if it fits either capacity; it must never be counted in both bags.
- **Equal capacities:** The bags remain distinct state dimensions even when their numerical limits match.
- **Unused capacity:** Maximizing packed weight does not require either bag to be filled exactly.
