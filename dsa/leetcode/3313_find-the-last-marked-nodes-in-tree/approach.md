## General

**Marking time is exactly tree distance.** Starting with node $i$ marked at time zero, after one second all nodes at distance one are marked, after two seconds all nodes at distance two are marked, and so on. Because a tree has one simple path between any two nodes, a node $v$ is marked at time $\operatorname{dist}(i,v)$. The last marked node is therefore any node farthest from $i$.

Computing a full traversal from every possible start would cost $O(n^2)$. The source uses a central tree fact: if $a$ and $b$ are endpoints of a tree diameter, then for every node $v$, at least one farthest node from $v$ is $a$ or $b$. Thus comparing distances to those two endpoints answers all starts.

**Find one diameter endpoint from an arbitrary start.** The source builds undirected adjacency `g`. It initializes `dist1[0] = 0` and runs `dfs(0, -1, dist1)`. The parent argument prevents immediately walking back across the edge just used. Since the input is a tree, that is enough to visit every node once without a separate visited set.

After traversal, `dist1[v]` is the number of edges from node zero to $v$. Selecting an index with maximum distance gives `a`. A standard tree property says a farthest node from any start is an endpoint of some diameter.

**Find the opposite endpoint and distances from `a`.** A second traversal starts at `a` and fills `dist2`. Its farthest node `b` is the other endpoint of a diameter. The path from `a` to `b` has maximum possible length among all tree paths. If several endpoints tie, `list.index(max(...))` chooses the first numeric index with the maximum stored distance; any resulting diameter is sufficient.

A third traversal from `b` fills `dist3`. Now `dist2[v]` is $\operatorname{dist}(a,v)$ and `dist3[v]` is $\operatorname{dist}(b,v)$ for every start $v$.

**Why a diameter endpoint is farthest from every node.** Consider a fixed node $v$ and the diameter path from $a$ to $b$. The unique path from $v$ meets that diameter at some attachment point $p$. Moving from $p$ toward whichever endpoint is farther produces a path from $v$ at least as long as moving to any interior point of the diameter.

Could a node $z$ off the diameter be farther from $v$ than both endpoints? Its branch attaches to the diameter at some point $q$. If that branch were long enough to beat both $a$ and $b$ from $v$, combining it with the farther side of the diameter would create a path longer than the supposed diameter. The maximality of $a$-$b$ rules this out. Therefore

$$
\operatorname{ecc}(v)
=
\max(\operatorname{dist}(v,a),\operatorname{dist}(v,b)).
$$

An endpoint achieving this maximum is a valid last marked node.

**Choose the more distant endpoint.** The return comprehension compares paired entries `x` and `y` from `dist2` and `dist3`. If `x > y`, endpoint `a` is farther and is returned. Otherwise it returns `b`. On a tie, both endpoints are marked at the same last time, and the statement permits either answer, so consistently choosing `b` is valid.

For a star centered at zero, any two leaves can be diameter endpoints. From the center, both are distance one and either may be returned. From a different leaf, the opposite selected endpoint is distance two and is correctly last.

**Recursive depth is a practical issue.** A tree may be a path of $10^5$ nodes. Each DFS then recurses once per node, which exceeds CPython's normal recursion limit. The abstract algorithm is linear and correct, but the exact source can raise `RecursionError` on a legal deep tree unless the harness raises the limit. Iterative DFS or BFS is the robust implementation choice.

## Complexity detail

The tree has $n$ nodes and $n-1$ edges. Each of the three traversals visits every node and examines both adjacency entries for every edge, costing $O(n)$ time. Finding maxima, locating their indices, and building the result are also $O(n)$. Total time is $O(n)$.

Adjacency lists use $O(n)$ space, the three distance arrays use $O(n)$ each, and the output has length $n$. The recursion stack can grow to $O(n)$. Total auxiliary space is $O(n)$, matching the manifest, with a constant factor from three arrays.

## Alternatives and edge cases

- **Traversal from every start:** It directly finds each eccentricity but costs $O(n^2)$ time on a tree and is unnecessary.
- **Two BFS traversals plus one extra BFS:** BFS computes the same unweighted distances iteratively and avoids recursion-depth failures while retaining $O(n)$ time.
- **Rerooting dynamic programming:** Compute the largest downward and upward distances for every node. It also runs in $O(n)$ but is more complex than diameter endpoints for this output.
- **Two-node tree:** The endpoints are the two nodes, and each start returns the other.
- **Star tree:** Any two leaves form a diameter. For the center, the tie can be resolved to either selected leaf.
- **Path tree:** Its endpoints are the diameter endpoints, and each node chooses the farther end.
- **Multiple diameters:** Any endpoint pair found by the farthest-node method supports the eccentricity formula; outputs need not match another valid implementation exactly.
- **Equal distances to both endpoints:** Both are last marked, and the source's `else b` tie choice follows the any-answer permission.
- **Initial node:** It is marked at time zero and can be last only in a one-node tree, but constraints require at least two nodes.
- **Parent-only traversal guard:** It is safe because the graph is a tree. In a general undirected graph with cycles, a full visited set would be necessary.
- **Deep recursion:** The exact source may fail at maximum path depth in standard Python; iterative traversal fixes the engineering defect.
- **Distance initialization:** Setting each root distance to zero and every child to parent plus one makes values exact edge counts, which correspond to seconds.
- **Output ordering:** Entry $i$ is constructed from distance-array position $i$, so it corresponds to starting node $i$ without extra mapping.
