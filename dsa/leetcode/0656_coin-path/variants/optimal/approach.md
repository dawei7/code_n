## General
**Define the cheapest suffix from every position**

Let `cost[i]` be the minimum total cost of a valid path that starts at index `i` and reaches the final index. The destination has cost `coins[-1]`. A blocked position is unreachable, while every other position considers each reachable next index `j` from $i + 1$ through `i + maxJump` and minimizes `coins[i] + cost[j]`.

Process indices from right to left so every candidate suffix has already been solved. Alongside each finite cost, store the chosen next index; this is enough to reconstruct the path without copying complete suffix paths into every DP state.

**Resolve equal costs lexicographically**

Examine candidate next indices in increasing order and replace a state's choice only when a strictly lower cost is found. If two candidates have equal cost, the smaller next index produces the lexicographically smaller full path because both paths share $i + 1$ as their first element and differ next at those candidate indices. Each chosen suffix is already lexicographically smallest by the same right-to-left argument.

This rule also handles zero-cost positions correctly: an extra early index may make a path lexicographically smaller even though it does not change the total cost.

**Why reconstruction returns exactly the required path**

The destination state is optimal by definition. Assuming all states to the right of `i` store their minimum-cost, lexicographically smallest suffixes, the transition checks every legal first jump and therefore finds the minimum possible cost from `i`; the increasing scan selects the smallest first jump among ties. Induction proves the property for index zero. Following the saved next indices reaches the destination when its cost is finite, and an infinite start cost proves no valid path exists.

## Complexity detail
Each of the `N` positions examines at most `B = maxJump` next positions, giving $O(N \cdot B)$ time. The cost and next-index arrays use $O(N)$ space, and the returned path contains at most `N` indices.

## Alternatives and edge cases
- **Store a complete best path at every state:** simplifies tie comparison, but repeated path copying can raise time and memory use to quadratic in long-path cases.
- **Forward dynamic programming:** can compute minimum costs, but lexicographic tie propagation is less direct because competing prefixes may reach the same position.
- **Shortest-path search:** models positions as a directed acyclic graph, but a heap adds overhead that the fixed right-to-left topological order avoids.
- A blocked start or destination makes the result empty.
- A single unblocked position returns `[1]` because the start is already the destination.
- Zero-cost ties must still prefer the lexicographically smallest sequence, not the path with fewer jumps.
- Unreachable intermediate positions remain excluded even when their numeric neighbors are reachable.
