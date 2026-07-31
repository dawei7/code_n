## General

Represent the tree with adjacency lists and maintain each vertex's current degree. The task becomes identifying which edges can never be necessary in an optimal closed walk.

**Discarding branches with no useful coin**

A leaf without a coin cannot help collect anything: entering its edge would force an immediate return without gaining access to a coin. Remove every such leaf. A neighbor may then become a coinless leaf, so continue with a queue until no removable branch remains. The surviving tree is the minimal connected subtree whose leaves all contain coins.

**Accounting for collection distance two**

A walk does not need to reach a coin vertex itself. Once the walk visits a vertex at distance at most $2$, that coin can be collected. Therefore remove all current leaves from the useful subtree, then remove the new leaves created by that first round. These two simultaneous layers represent edges that can be covered for free by the distance-two collection operation.

Every edge still present after both rounds separates useful coin regions that are more than two edges beyond its opposite side. Any valid route must cross such an edge to reach the required interior and, because the route must return to its starting vertex, must cross it again in the reverse direction. Conversely, a depth-first tour of the remaining subtree traverses every surviving edge exactly twice and brings every pruned coin within distance $2$. If $E$ edges survive, the answer is therefore $2E$.

Tracking `remaining_edges` while removing leaves avoids a final traversal. Degree zero marks a removed vertex, and each original edge is processed only when one of its endpoints is deleted.

## Complexity detail

Let $n$ be the number of vertices. Building the adjacency lists takes $O(n)$ time because a tree has $n-1$ edges. Every vertex enters a pruning queue at most once per relevant phase, and every adjacency entry is inspected only a constant number of times, so all pruning also takes $O(n)$ time.

The adjacency lists, degree array, and queues use $O(n)$ space.

## Alternatives and edge cases

- **Repeated full-tree leaf searches:** Recomputing all current leaves after every deletion is correct, but a path can make it take $O(n^2)$ time.
- **Rooted dynamic programming:** Tree DP can model travel and coin distance states, but it introduces more states and proof obligations than the equivalent leaf-pruning view.
- **No coins or a single vertex:** The useful subtree can be empty and no edge traversal is required.
- **Coins within two layers:** If the first and second leaf-removal rounds delete every useful edge, one starting vertex can collect all coins without moving.
- **Simultaneous rounds:** The two distance layers must be removed level by level. Newly exposed leaves belong to the next round, not the current one.
- **Closed-walk requirement:** Each surviving edge is counted twice specifically because the route must finish at its chosen starting vertex.
