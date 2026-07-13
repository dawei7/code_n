# Cheapest Flights Within K Stops

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 787 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/) |

## Problem Description

### Goal

There are `n` cities numbered from `0` through $n - 1$, with directed flights `[from, to, price]`. Given source city `src`, destination `dst`, and integer `k`, consider routes having at most `k` intermediate stops, equivalently at most $k + 1$ flights.

Return the cheapest total price among all routes satisfying that stop limit. If no permitted route reaches `dst`, return `-1`. Flight direction must be respected, and a cheaper path using too many intermediate cities is not a valid answer.

### Function Contract

**Inputs**

- `n`: the number of cities, numbered from `0` through $n - 1$.
- `flights`: triples `[origin, destination, price]` describing directed flights.
- `src`: the departure city.
- `dst`: the destination city.
- `k`: the maximum number of intermediate cities, so at most $k + 1$ flights may be used.

**Return value**

- The minimum valid route price, or `-1` if the destination cannot be reached within the stop limit.

### Examples

**Example 1**

- Input: `n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1`
- Output: `200`
- Explanation: The route through city `1` uses one stop and is cheaper than the direct flight.

**Example 2**

- Input: `n = 3, flights = [[0,1,2],[1,2,2],[0,2,5]], src = 0, dst = 2, k = 0`
- Output: `5`
- Explanation: With no stops allowed, only the direct flight qualifies.

**Example 3**

- Input: `n = 3, flights = [[0,1,2]], src = 0, dst = 2, k = 1`
- Output: `-1`
- Explanation: No route reaches city `2`.

### Required Complexity

- **Time:** $O((k + 1) \cdot E)$
- **Space:** $O(V)$

<details>
<summary>Approach</summary>

#### General

**Define cost by the number of flights allowed**

Let `costs[city]` be the cheapest price using at most the number of flights processed so far. Initially only `src` costs zero. Perform $k + 1$ rounds because a route with `k` intermediate stops contains at most $k + 1$ flight edges.

**Relax every flight from the previous round**

At the start of a round, copy `costs` into `next_costs`. For each flight `u -> v`, use only `costs[u]` from the previous round to improve `next_costs[v]`. The copy retains routes that use fewer edges, while separating the arrays prevents two flights from chaining inside one round and silently exceeding the edge budget.

After round `r`, induction shows that each entry is the minimum cost among routes using at most `r` flights: retained entries cover shorter routes, and every route using exactly `r` flights is a valid previous-round route followed by one relaxed edge. Thus after $k + 1$ rounds, the destination entry considers exactly all permitted routes. An infinite entry means none exists.

#### Complexity detail

Each of the $k + 1$ rounds scans all `E` flights, taking $O((k + 1) \cdot E)$ time. The current and next cost arrays each contain `V` entries, for $O(V)$ auxiliary space.

#### Alternatives and edge cases

- **Heap over city and flights used:** Dijkstra-style states `(price, city, edges)` can stop at the first valid destination pop, but the edge count must remain part of the state.
- **Two-dimensional dynamic programming:** Store the best price for every city and exact edge count; this uses $O(kV)$ space instead of rolling arrays.
- **Depth-first route enumeration:** Exploring every route up to the stop limit is correct but can grow exponentially in dense graphs.
- **Unrestricted shortest path:** Keeping only one best cost per city without an edge dimension can discard a more expensive prefix that leaves enough stops for the optimal valid route.
- **No stops:** Only direct flights may be used.
- **Unreachable destination:** Return `-1`, not infinity.
- **Cycles:** Positive prices and the explicit edge budget keep the dynamic program finite.
- **Round isolation:** Relaxations must read the old array and write the copy to enforce one additional flight per round.

</details>
