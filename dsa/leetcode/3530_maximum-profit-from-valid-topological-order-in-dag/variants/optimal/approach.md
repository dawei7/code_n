## General

A topological prefix is completely characterized by the set of nodes it already contains. Encode that set as a bitmask. For each node, also encode all of its direct predecessors in `prerequisites[node]`. The node can be appended exactly when it is absent from the current mask and every prerequisite bit is already present.

Let `dp[mask]` be the greatest profit of any valid topological prefix whose nodes are precisely `mask`. All such prefixes have the same length, so the next node always receives position `mask.bit_count() + 1`. Starting with `dp[0] = 0`, append each currently available node and maximize the value for the resulting mask.

The implementation processes masks in layers by prefix length and stores only reachable masks in each layer. This avoids repeatedly scanning masks that cannot represent a topological prefix. To see why the recurrence is complete, consider any valid prefix ending in node `v`: removing `v` leaves a valid shorter prefix, and every predecessor of `v` is in that shorter mask, so the transition adds it. Conversely, every transition checks all prerequisites before appending its node, so it preserves topological validity. Induction on the prefix length therefore shows that `dp[mask]` is optimal for every reachable mask; the full mask gives the requested optimum.

## Complexity detail

There are at most $2^n$ masks. Each reachable mask tests at most $n$ possible next nodes, and each prerequisite test is one constant-time bit operation, so the time complexity is $O(n \cdot 2^n)$. The DP array, reachable-mask layers, and prerequisite masks use $O(2^n)$ space.

## Alternatives and edge cases

- **Greedy by current score:** Choosing the smallest or largest available score can be suboptimal because a node's placement may unlock successors with very different scores.
- **Enumerate topological orders:** A graph without edges has $n!$ valid orders, which is too large for $n=22$.
- **Memoized recursion:** The same subset recurrence works top-down, but the iterative layers avoid recursion overhead and make the position explicit.
- **No edges:** Every subset is reachable; the optimum places scores in ascending order so larger scores receive larger positions.
- **A single chain:** Only one mask is reachable at each layer, and the forced ordering is evaluated directly.
- **Direct predecessor masks:** It is unnecessary to compute transitive closure; satisfying every direct edge already guarantees a valid topological order.
