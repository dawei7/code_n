## General

Represent the branches that remain open by an $N$-bit mask. Enumerating all
$2^N$ masks also covers closing no branches and closing every branch. For one
mask, initialize an all-pairs distance matrix only for active branches. Insert
an undirected road only when both endpoints are active, keeping the shortest
weight when parallel roads exist.

Run Floyd-Warshall with active branches as endpoints and intermediates. This
restriction is essential: a route through a closed branch is unavailable even
when both of its endpoints remain open. After the relaxation, accept the mask
exactly when every ordered pair of active branches has distance at most
`maxDistance`. Masks with zero or one active branch satisfy this condition
vacuously.

For each mask, the matrix initially contains exactly its usable direct roads.
Floyd-Warshall then considers every sequence of active intermediate branches,
so each final entry is the true shortest permitted distance. The final test is
therefore equivalent to the requirement for that remaining set. Since every
remaining set corresponds to exactly one closing set, counting accepted masks
gives the requested answer.

## Complexity detail

Let $N$ be the number of branches and $R=\lvert\texttt{roads}\rvert$. There
are $2^N$ masks. Initializing and relaxing one mask costs
$O(N^3+R)$ time, giving $O(2^N(N^3+R))$ total time. The distance matrix and
active-branch list use $O(N^2)$ space; matrices are reused between masks.

## Alternatives and edge cases

- **Shortest paths in the original graph:** Precomputing once is incorrect because a shortest route may pass through a branch that the current set closes.
- **Dijkstra from every active branch:** Rebuilding the retained graph and running repeated Dijkstra searches is correct, but Floyd-Warshall is simpler for $N\le10$ and dense or parallel roads.
- **Repeated Bellman-Ford:** Relaxing every retained road up to $N-1$ times from every active source is correct but adds avoidable source and edge factors.
- **Enumerate simple paths:** Testing all permitted simple routes can recover shortest distances but adds another exponential factor.
- **Parallel roads:** Keep the minimum direct weight between two retained endpoints before relaxation.
- **No or one active branch:** There is no distinct pair that violates the limit, so these sets are valid.
- **Closed intermediate branch:** Its incident roads disappear and it cannot connect two branches that remain open.
- **Disconnected retained set:** Its infinite pair distance exceeds every finite `maxDistance`, making the set invalid.
