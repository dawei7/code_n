## General

**Keep the route as the only state.** At each stop, future cost depends on the
current route but not on the earlier sequence of choices. Let `regular_cost`
and `express_cost` be the minimum totals for reaching the previous stop on the
corresponding routes. At stop 0 these are `0` and `expressCost`, because
starting on express requires the initial transfer.

**Advance both states together.** To reach the next stop on regular, arrive
from either previous route and pay the regular segment; returning from express
is free:

`next_regular = min(regular_cost, express_cost) + regular[i]`.

To arrive on express, either stay there or transfer from regular before taking
the express segment:

`next_express = min(express_cost, regular_cost + expressCost) + express[i]`.

Compute both values from the old states before replacing either one. Append
their minimum because the destination stop counts as reached from either
route.

These transitions enumerate every possible final move into each state and
extend only minimum-cost prefixes. By induction, both state costs are optimal
at every stop, so every appended destination cost is optimal as well.

## Complexity detail

The algorithm performs constant work for each of $n$ segments, taking $O(n)$
time. Only two rolling state costs are needed beyond the returned length-$n$
list, so total result storage is $O(n)$ and auxiliary workspace is $O(1)$.

## Alternatives and edge cases

- **Two full DP arrays:** Storing regular and express costs for every stop is
  equivalent but uses additional $O(n)$ workspace.
- **Shortest path graph:** Model `(stop, route)` pairs as vertices and run a
  general shortest-path algorithm; this is correct but obscures the acyclic
  left-to-right structure.
- **Recompute every destination:** Solving each prefix independently repeats
  work and takes $O(n^2)$ time.
- **Initial express use:** The express state at stop 0 must already include
  `expressCost`.
- **Free return:** A transition from express to regular adds no transfer fee.
- **Repeated entry:** Every later regular-to-express transition pays
  `expressCost` again.
