## General

Sort node indices by `nums[node]` and remember each original node's sorted position. In this order, the one-hop neighbors to the right of position `i` form a contiguous interval: every position through the last value at most `values[i] + maxDiff` is adjacent, and every later value is not. A two-pointer scan computes that last position as `farthest[i]` for all `i` in linear time after sorting.

For two sorted positions $l<r$, an optimal path can always take the farthest reachable position at every hop. Any alternative first hop ends no farther right. Because `farthest` is non-decreasing, replacing that hop with the farther one cannot reduce the next hop's reach; repeating the exchange never uses more edges. The shortest distance is therefore the number of repeated applications of `farthest` required to reach or pass $r$.

Build a binary-lifting table where `jumps[p][i]` is the position reached after $2^p$ greedy hops from `i`. For a query, inspect powers from largest to smallest and take each jump that advances but remains strictly before the target. One final one-hop check either reaches the target, yielding the accumulated minimum distance plus one, or proves the endpoints disconnected because greedy reach has stopped. Original query direction is irrelevant because the graph is undirected.

## Complexity detail

Let $Q$ be the number of queries. Sorting costs $O(n\log n)$, the two-pointer scan costs $O(n)$, and constructing the jump table costs $O(n\log n)$. Each query takes $O(\log n)$ time, giving $O((n+Q)\log n)$ total time. The inverse positions and reach arrays use $O(n)$ space, and the jump table uses $O(n\log n)$ space.

## Alternatives and edge cases

- **Materialize every graph edge:** A group of close values can form a clique with $\Theta(n^2)$ edges.
- **Breadth-first search per query:** Repeating graph search can take quadratic or worse total work across $10^5$ queries.
- **Apply greedy hops one at a time:** The farthest-hop strategy is correct, but a long chain may require $O(n)$ work per query; binary lifting reduces it to $O(\log n)$.
- **Only test connected components:** Component labels distinguish `-1` from reachable, but do not provide the minimum number of edges.
- **Unsorted node labels:** Queries use original indices, so every node needs an inverse mapping into sorted-value order.
- **Equal values with `maxDiff = 0`:** All equal-valued nodes share direct edges and distinct endpoints have distance one.
- **Self-query:** Its distance is zero without consulting the jump table.
- **Disconnected fixed point:** When `farthest[current] == current` before the target, no sequence of edges can cross the next value gap.
