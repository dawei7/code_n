## General
**Bounded walks make exhaustive search practical**

Build an adjacency list for the undirected graph. A depth-first search state contains the current node, elapsed time, current quality, and visit counts. From that state, try every incident edge whose travel time keeps the route within `maxTime`. The degree limit gives at most four choices per step, while the minimum edge time bounds the depth by $L \le 10$.

**Count a node only on entry to the visited set**

Before following an edge, increment the destination's visit count. Add its value to the running quality only when that count changes from zero to one. After the recursive call, decrement the count to restore the previous path state. Whenever the current node is $0$, the explored prefix is itself a valid return route, so use its quality to update the answer; exploration may continue if time remains.

The search enumerates every edge sequence whose total time fits the budget because it branches over every legal next edge. Visit counts make the maintained quality equal to the sum of exactly the distinct nodes on that sequence. Every valid path is therefore considered at its return to node $0$, and taking the greatest recorded quality produces the optimum.

## Complexity detail
Building the graph takes $O(n+e)$ time and space. With branching factor at most four and at most $L$ traversals, DFS visits $O(4^L)$ states, giving $O(n+e+4^L)$ total time. The adjacency list, visit-count array, and recursion stack use $O(n+e+L)$ space. The contract fixes $L \le 10$, but retaining $L$ shows the bounded exponential search explicitly.

## Alternatives and edge cases
- **Recompute quality from the whole path:** This remains correct, but scanning all node visit counts at return states adds an avoidable factor of $n$.
- **Bitmask dynamic programming:** A mask can represent distinct visits only when the relevant node count is small; the graph may contain up to $1000$ nodes.
- **Shortest-return pruning:** Precomputing each node's shortest distance to node $0$ can prune states that cannot return in time, improving constants without changing the worst-case bound.
- The zero-length route at node $0$ is always valid and includes `values[0]`.
- A high-value node is useless when the remaining time cannot cover both reaching it and returning.
- Revisiting a node or edge is allowed and may be necessary to return, but a node's value is added only once.
- Disconnected nodes never affect the result.
- A route using exactly `maxTime` seconds is valid.
