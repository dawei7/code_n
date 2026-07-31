## General

**Turn marking delays into directed path costs**

If propagation crosses an edge from a marked node into node $v$, the added delay depends only on $v$: it is $1$ when $v$ is odd and $2$ when $v$ is even. Therefore, for a fixed start $s$, the time at which a node $v$ is marked is the sum of these destination costs along the unique tree path from $s$ to $v$. The requested value for $s$ is the maximum such weighted distance.

Running a traversal from every possible start would repeat almost all path work. Instead, root the tree temporarily at node $0$ and calculate every eccentricity with two linear passes.

**First pass: best path into each subtree**

Let `downward[u]` be the largest additional marking time from $u$ to any node in the rooted subtree of $u$. For a child $v$, entering $v$ costs $1$ or $2$ according to the parity of $v$, after which the best continuation costs `downward[v]`. Thus `downward[u]` is the maximum of zero and these child contributions.

Process nodes in reverse traversal order so every child value is ready before its parent. Iterative traversal avoids depending on recursion depth for a tree that may contain $10^5$ nodes.

**Second pass: reroot without recomputing paths**

Let `upward[u]` be the best weighted distance from $u$ to a node outside $u$'s rooted subtree. Then the answer at $u$ is the larger of `downward[u]` and `upward[u]`.

When moving the conceptual root from $u$ to a child $v$, any path leaving $v$ first enters $u$, paying the parity-dependent cost of $u$. It may then stop at $u$, continue along `upward[u]`, or enter one of $v$'s sibling subtrees. Keep the largest and second-largest child contributions at $u$; if $v$ supplied the largest, use the second-largest, otherwise use the largest. This exclusion prevents a path from immediately returning into $v$'s own subtree and lets every edge be processed only a constant number of times.

The two states account for every possible endpoint: it lies either inside the current rooted subtree or outside it. Their maximum is therefore exactly the time at which the last node is marked for that start.

## Complexity detail

Building the adjacency lists and both tree passes take $O(n)$ time. The graph, parent order, and dynamic-programming arrays use $O(n)$ space.

## Alternatives and edge cases

- **Traverse from every start:** A weighted DFS or BFS computes correct answers but takes $O(n^2)$ time on the full set of starts.
- **Unweighted tree diameter:** Ordinary edge counts are insufficient because entering an odd node costs one while entering an even node costs two; the distance is also direction-dependent at its first endpoint.
- **Recursive rerooting:** It expresses the same recurrence compactly but can overflow the call stack on a path with $10^5$ nodes.
- A two-node tree has different answers in its two directions when one endpoint is even and the other odd.
- The initially marked node contributes no cost, regardless of its parity.
- A leaf's best route may go through its parent and across a sibling subtree.
- When a child owns its parent's largest downward contribution, its rerooted state must use the second-largest contribution.
- Tied largest child contributions are safe: excluding either child still leaves an equal contribution from the other.
- A path-shaped tree exercises the maximum traversal depth, while a star exercises the top-two exclusion logic.
- Node parity, not traversal depth, determines each destination cost.
