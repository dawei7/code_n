## General

**Represent both directions explicitly.** For a listed conversion $A \to B$ with multiplier $r$, add an edge from $A$ to $B$ weighted by $r$ and an edge from $B$ to $A$ weighted by $1/r$. A path product is then exactly the amount of its destination currency obtained from one unit of its source currency.

Traverse the day-1 graph from `initialCurrency`, multiplying edge rates along the way. This records how much of each reachable currency can be held after day 1. Perform the same traversal from `initialCurrency` in the day-2 graph. If this second traversal records a multiplier $q$ from the initial currency to currency $C$, the valid rates guarantee that converting $C$ back to the initial currency on day 2 multiplies by $1/q$.

For every currency $C$ reached by both traversals, the complete two-day result obtained by holding $C$ overnight is therefore

$$
\frac{\text{day1}[C]}{\text{day2}[C]}.
$$

The initial currency itself appears in both maps with multiplier 1, so making no conversions remains an available result.

Within one day's valid graph, every path between the same two currencies has the same product; otherwise the rates would contradict one another or form a profitable cycle. Consequently, visiting each currency once loses no better same-day alternative. Every legal two-day strategy has some overnight currency $C$, and the two traversals compute exactly its day-1 forward and day-2 return multipliers. Taking the maximum over their intersection therefore considers and optimizes every possible strategy.

## Complexity detail

Let $n$ and $m$ be the numbers of listed pairs on days 1 and 2. Each pair creates two adjacency entries. The two graph constructions, traversals, and final map intersection take $O(n+m)$ time and $O(n+m)$ space.

The benchmark defines `size` as the number of pairs on each day and uses the complete legal span of 2, 5, and 10 pairs. The reference traverses each day once. A correct slower baseline traverses day 2 separately from every currency reached on day 1, taking $O((n+m)^2)$ time when both graphs have comparable size.

## Alternatives and edge cases

- **Run a day-2 traversal for every intermediate currency:** This is correct, but repeats the same graph work and becomes quadratic instead of deriving all return rates from one traversal.
- **Bellman-Ford or Dijkstra:** Neither repeated relaxation nor shortest-path priority ordering is needed because valid same-day rates give one consistent product between connected currencies.
- **Use only listed edge directions:** Every conversion is reversible at the reciprocal rate, so omitting reverse edges can miss the optimum or incorrectly report a currency as unreachable.
- **Multiply the two forward maps:** `day2[C]` describes conversion from the initial currency to $C$; returning from $C$ requires its reciprocal, so the correct combination is division.
- **Disconnected currencies:** A currency usable on only one day cannot serve as an overnight bridge and is excluded from the intersection.
- **Zero conversions:** Holding the initial currency across one or both days is valid, which guarantees an answer of at least 1.
- **Floating-point results:** Products and reciprocals use ordinary floating-point arithmetic; comparisons should retain the full computed values rather than rounding intermediate amounts.
