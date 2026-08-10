## General

**Three kinds of longest path can remain after the merge.** Adding one edge does not change distances between two nodes that were already in the first tree, so its original diameter $d_1$ remains a lower bound. The second tree's diameter $d_2$ also remains. A new longest path may instead start in the first tree, cross the new edge, and end in the second.

If the edge connects node $u$ in the first tree to node $v$ in the second, the longest cross-tree path has length

$$
\operatorname{ecc}_1(u)+1+\operatorname{ecc}_2(v),
$$

where a node's eccentricity is its greatest distance to any node of the same tree. To minimize this cross term, choose a center of each tree: a node with minimum eccentricity. A tree with diameter $d$ has radius

$$
\left\lceil\frac d2\right\rceil,
$$

which the source computes as `(d + 1) // 2`.

Connecting centers makes the cross-tree maximum equal to

$$
\left\lceil\frac{d_1}{2}\right\rceil
+1+
\left\lceil\frac{d_2}{2}\right\rceil.
$$

The merged diameter is therefore

$$
\max\left(
d_1,\,
d_2,\,
\left\lceil\frac{d_1}{2}\right\rceil+
\left\lceil\frac{d_2}{2}\right\rceil+1
\right).
$$

The main method computes exactly these three candidates.

**Why a center has radius ceiling-half the diameter.** Let the endpoints of a diameter path be $p$ and $q$. A middle node on that path is at distance at most $\lceil d/2\rceil$ from either endpoint. No branch outside the path can be farther from the middle, because combining such a branch with the farther diameter endpoint would create a path longer than $d$. Conversely, for any chosen connection node, at least one of $p$ and $q$ is at distance at least $\lceil d/2\rceil$; otherwise their path through that node would be too short. Hence no node has smaller eccentricity, and a middle node achieves the radius.

**Find a tree diameter with two depth-first traversals.** `treeDiameter` builds an undirected adjacency list. Its nested `dfs(i, fa, t)` visits the tree from node `i`, skips the parent `fa`, and tracks distance `t` from the traversal start. Whenever it sees a distance larger than `ans`, it saves that distance and node in the nonlocal variables `ans` and `a`.

The first traversal starts from node zero. In a tree, a farthest node from any starting node is an endpoint of some diameter. After that traversal, `a` holds such an endpoint.

The second traversal begins at `a`. The farthest distance from a diameter endpoint is the tree's diameter, so the final `ans` is returned.

The source does not reset `ans` between the traversals. This remains correct. The first traversal's maximum distance is at most the diameter found by the second traversal. If the second maximum is larger, `ans` is updated; if it is equal, retaining the old numeric value is harmless. The identity of `a` after the second traversal is not used.

**Why farthest-from-farthest works in a tree.** Unique simple paths are the key. Starting from any node and moving to a farthest node reaches an extremity: if that node lay internally on every longest relevant path, an adjacent branch direction would continue farther. From a diameter endpoint, the greatest possible distance is exactly to an opposite endpoint. Cycles could invalidate this simple argument, but the inputs are guaranteed trees.

**Handle one-node trees naturally.** An empty edge list represents a tree with one node numbered zero. Accessing `g[0]` on the `defaultdict` gives an empty neighbor list. Both DFS calls remain at distance zero, and the returned diameter is zero. Connecting two singleton trees then produces `max(0,0,0+0+1)=1`.

**Why the final maximum is both necessary and achievable.** Every merged tree contains both original trees unchanged, so it cannot have diameter below $d_1$ or $d_2$. Any connection nodes have eccentricities at least their tree radii, so the longest cross path cannot be shorter than the radius sum plus one. These three quantities form a lower bound. Connecting actual centers attains the radius cross term while leaving internal diameters unchanged, so the maximum of the three is achieved. The formula is exact.

## Complexity detail

Let $N$ and $M$ be the node counts of the two trees. Building both adjacency lists costs $O(N+M)$ time and space because each tree edge is inserted in both directions. Each DFS visits every node and edge once. Two traversals per tree are still $O(N+M)$ total time.

Adjacency lists use $O(N+M)$ memory. The recursive call stacks can be $O(N+M)$ in total bound, with a single tree traversal reaching depth equal to that tree's height. Thus auxiliary space is $O(N+M)$.

The manifest's asymptotic bounds are correct if its $N$ denotes total input size, but its summary says “two breadth-first searches each.” The exact source performs recursive depth-first searches. This distinction matters operationally: a path-shaped tree may have $10^5$ nodes, far beyond Python's ordinary recursion limit. The algorithmic bound is linear, but `solution.py` can raise `RecursionError` on a valid deep tree. Iterative BFS or DFS is required for robust full-constraint execution.

## Alternatives and edge cases

- **Two breadth-first searches:** Use a queue to find a farthest endpoint and then its farthest distance. It has the same linear bounds and avoids recursion-depth failure; it is what the manifest summary describes.
- **Iterative depth-first search:** An explicit stack also preserves the farthest-of-farthest method without relying on Python recursion.
- **One postorder diameter traversal:** Track the two greatest child depths at every node and update a global diameter. This needs only one traversal per tree but has the same asymptotic cost and the same recursion concern if written recursively.
- **Leaf trimming:** Repeatedly remove leaves to find one or two centers and infer the diameter/radius. It is linear but uses degree and queue bookkeeping.
- **Connect arbitrary nodes:** The internal diameters remain fixed, but a non-center can have larger eccentricity and increase the cross-tree path.
- **Even diameter:** There is one center and radius $d/2$.
- **Odd diameter:** There are two adjacent centers; either has radius $(d+1)/2$.
- **One singleton tree:** Its diameter and radius are zero, so the cross candidate is the other radius plus one.
- **Both singleton trees:** One new edge creates a two-node tree of diameter one.
- **Path-shaped tree:** Two-sweep diameter logic is ideal algorithmically, but recursive implementation depth is worst possible.
- **Star-shaped tree:** Diameter is two for at least two leaves; the hub is the center with radius one.
- **Old `ans` before second DFS:** It need not be reset because it cannot exceed the actual diameter discovered from the endpoint.
- **Node numbering:** Valid tree labels run from zero through node count minus one, so starting at zero is always legal even for an empty edge list.
- **Input preservation:** The edge lists are read to build new adjacency structures and are not mutated.
- **Manifest traversal mismatch:** Complexity remains linear, but documentation and operational expectations must call the source DFS, not BFS.
