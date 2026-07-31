## General

For a fixed repair threshold, retain only edges whose cost is at most that threshold. Because every usable edge contributes one step, breadth-first search from node `0` finds the minimum number of edges needed to reach every node. Stop expanding a node once its distance equals `k`; the threshold is feasible exactly when node `n - 1` is discovered within the limit.

Feasibility is monotone in `money`. Raising the threshold can only add usable edges, so a feasible threshold stays feasible at every larger value. The minimum answer, when it exists, equals the cost of some edge: between consecutive distinct edge costs, the usable graph does not change.

Build the undirected adjacency list and sort the distinct repair costs. First test the largest cost. If the destination still cannot be reached within `k` edges, even repairing every edge is insufficient, so return `-1`.

Otherwise, binary-search the sorted costs. When the middle cost is feasible, keep it as a possible answer and search the lower half. When it is infeasible, discard it and every lower cost. The search finishes at the first threshold whose repaired graph contains an allowed route, which is exactly the minimum required money.

## Complexity detail

Let $N$ be the number of nodes and $M$ the number of edges. Building the adjacency list takes $O(N+M)$ space and time, while sorting the distinct costs takes $O(M\log M)$ time. Each of $O(\log M)$ feasibility checks performs $O(N+M)$ breadth-first work. The combined bound is $O((N+M)\log M)$ time and $O(N+M)$ auxiliary space.

## Alternatives and edge cases

- **Scan thresholds in ascending order:** Running a fresh breadth-first search after adding each distinct cost is correct but can take $O(M(N+M))$ time.
- **Minimax path without a hop state:** A standard minimum-bottleneck path ignores the `k`-edge limit and may choose a cheaper route that is too long.
- **Dynamic programming by hop count:** Tracking the smallest bottleneck cost for every node after each of `k` steps is correct but can require $O(kM)$ time.
- **Disconnected destination:** If the largest threshold fails, no smaller threshold can help and the result is `-1`.
- **Connected but too many edges:** A path may exist in the fully repaired graph yet still be invalid because its shortest edge count exceeds `k`.
- **Direct expensive edge:** A costly one-edge route can be optimal when cheaper alternatives require more than `k` edges.
- **Threshold semantics:** Choosing `money` repairs every edge at or below it; there is no additional sum of individual repair costs.
