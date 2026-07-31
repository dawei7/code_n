## General

Treat each fixed-width non-prime integer as a graph vertex. Two vertices share an edge when exactly one decimal digit changes by one and the result keeps the original digit count. Entering a neighbor contributes that neighbor's value to the transformation cost; initialize the source distance to `n` so the original value is counted too.

All edge weights are nonnegative, but they are not equal. A route with fewer digit changes can cost more than a longer route through smaller integers, so breadth-first search is insufficient. Dijkstra's algorithm always removes the unsettled state with the smallest known accumulated cost. When `m` is removed from the heap, no later route can improve it because every remaining extension adds a nonnegative value.

Before the search, use the Sieve of Eratosthenes over $[0,U)$ to classify every possible state, where $U=10^d$ and $d$ is the common digit count. Reject immediately when either endpoint is prime. For each settled value, inspect every decimal place, create its possible increment and decrement neighbors, discard primes and values below the smallest $d$-digit integer, and relax the remaining edges.

Every permitted operation appears among these generated edges, and every generated edge changes exactly one digit as required. Thus legal transformations and graph walks correspond exactly, with identical costs. Dijkstra's minimum path therefore equals the requested minimum transformation cost; an unreachable destination correctly yields `-1`.

## Complexity detail

The sieve costs $O(U\log\log U)$. There are at most $U$ candidate states and at most $2dU$ directed digit-change edges. Binary-heap Dijkstra therefore takes $O(dU\log U)$ time, which dominates the sieve, and the primality table, distance table, and heap require $O(U)$ space.

The benchmark defines `size` as $U=10^d$ and uses legal two-, three-, and four-digit inputs. The reference removes the next state from a binary heap. A correct slower Dijkstra implementation scans the complete unvisited state set for the minimum distance at every iteration, increasing the selection work from logarithmic to linear in $U$; it must fail scaling while still producing every expected minimum.

## Alternatives and edge cases

- **Breadth-first search:** It minimizes the number of operations, not the sum of visited integer values, because edge weights differ.
- **Bellman-Ford:** It is correct for the graph but needlessly revisits all edges and is much slower than Dijkstra with nonnegative weights.
- **Linear-selection Dijkstra:** Scanning every unvisited state to find the next minimum preserves correctness but raises the worst-case search cost to $O(U^2+dU)$.
- **Trial division on every edge:** It avoids the sieve array but repeats primality work for the same states and is another avoidable slowdown.
- **Prime endpoint:** The starting and destination values are both occupied, so either being prime makes the answer `-1` immediately.
- **Identity transformation:** When `n == m` and the value is non-prime, no operation is needed and the cost is exactly `n`.
- **One is non-prime:** The sieve must mark both `0` and `1` as non-prime; otherwise valid boundary states are rejected.
- **Leading zero:** Decreasing the most significant digit of a value such as `1000` cannot produce `0000`, because all intermediate values retain $d$ digits.
- **No carry or borrow:** Each operation changes one chosen digit only; incrementing `9` and decrementing `0` are forbidden rather than propagated to another place.
- **Unreachable graph component:** Prime states can disconnect the legal graph, in which case exhausting the heap returns `-1`.
