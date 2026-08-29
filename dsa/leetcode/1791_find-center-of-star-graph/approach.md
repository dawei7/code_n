## General

**Use the promise that the graph is already a valid star**

A star graph has one center connected to every other node. Each non-center node is a leaf connected only to that center. Therefore, the center is an endpoint of every edge, while a leaf appears in exactly one edge.

A degree-counting solution could inspect all $n-1$ edges and find the node with degree $n-1$. That is unnecessary because the input is guaranteed to be a valid star. Any two different star edges must share the center, and they cannot share a leaf.

The graph has at least three nodes, so it has at least two edges. The protected solution looks only at `edges[0]` and `edges[1]`.

**Test one endpoint of the first edge**

Write the first edge as `[a, b]`. Exactly one of `a` and `b` is the center; the other is the leaf attached by this edge.

The expression `edges[0][0] in edges[1]` asks whether `a` is one of the two endpoints of the second edge. Membership in this two-element list performs at most two equality checks.

- If `a` appears in the second edge, then `a` belongs to two distinct star edges. A leaf has degree one and cannot do that, so `a` must be the center.
- If `a` does not appear in the second edge, then `a` is the first edge's leaf. The other first-edge endpoint `b` must therefore be the center, so the solution returns `edges[0][1]`.

This conditional completely identifies the common endpoint without constructing sets, degree arrays, or an adjacency list.

**Why the first two edges must have exactly one common endpoint**

Every edge in a star has the form `[center, leaf]`, although the input may list those two endpoints in either order. The first two entries of `edges` represent two different connections in the valid $n-1$ edge star. Their leaf endpoints are different nodes because each leaf has exactly one connection and the star contains one edge per leaf. Both edges contain the center. They consequently intersect in exactly that one node.

This is why checking just one endpoint of the first edge is enough. If it is not the common node, the first edge has only one other endpoint, and that other endpoint must be common.

**Following both endpoint orders**

For `edges = [[1, 2], [2, 3], [4, 2]]`, the tested node is 1. It is not in `[2, 3]`, so 1 is a leaf and the function returns the other first-edge endpoint, 2. Node 2 is indeed present in every edge.

The same graph could list its first edge as `[2, 1]`. The tested node would then be 2, which is present in the second edge. The function would return 2 through the first branch. Thus arbitrary endpoint order does not affect the result.

For `[[1, 2], [5, 1], [1, 3], [1, 4]]`, node 1 occurs in both initial edges and is returned immediately. The remaining edges need not be inspected because validity guarantees that the same node is their center as well.

**Why ignoring the rest of the input is safe**

Normally, examining only two edges would not prove a fact about an entire graph. Here the source contract already proves that `edges` represents a valid star. The algorithm's job is only to identify which endpoint plays the promised center role.

Once the common node of two star edges is known, there cannot be another center candidate. Two different nodes cannot both be incident to every edge of a star with at least three nodes: an edge connecting the center to a third leaf would exclude the other candidate. The common endpoint is unique, and the remaining input can provide no contradictory valid-star information.

This illustrates an important algorithm-design principle: strong input guarantees can eliminate work. The constant-time method is correct because it uses the star invariant explicitly, not because two arbitrary graph edges usually reveal a global center.

**Why the returned node is correct**

If the tested first endpoint appears in the second edge, it is incident to at least two edges and therefore cannot be a degree-one leaf. The only non-leaf node in a star is the center, so returning it is correct.

If the tested endpoint does not appear in the second edge, the center still must lie on the first edge and also on the second edge. The first edge's other endpoint is the only remaining possibility, so returning that endpoint is correct. These cases are exhaustive and establish that the conditional always returns the unique center.

## Complexity detail

The solution accesses two fixed edges and tests membership in a list of exactly two integers. The number of comparisons is bounded by a constant independent of $n$ and the number of edges. Time complexity is therefore $O(1)$, matching the manifest.

Only existing list entries are referenced, and no growing data structure is allocated. Auxiliary space is $O(1)$.

Although the input itself contains $n-1$ edges and occupies $O(n)$ storage, input storage is not auxiliary memory created by the algorithm. The method deliberately does not scan or copy that input.

## Alternatives and edge cases

- **Degree counting:** Count both endpoints of every edge and return the node with degree $n-1$. This works for a valid star but costs $O(n)$ time and $O(n)$ space.
- **Adjacency list:** Building the full graph also reveals degrees, but it stores information that the star guarantee makes unnecessary.
- **Set intersection:** Intersecting the endpoint sets of the first two edges finds the center in constant time, though allocating sets is more machinery than the direct membership test.
- **Compare all four endpoint combinations:** It works, but testing one first-edge endpoint already determines which of the two is common.
- **Arbitrary endpoint order:** The center may appear first or second in either edge; list membership handles both orientations.
- **Minimum graph size:** With $n=3$, there are exactly two edges, so both required entries exist and their shared endpoint is the center.
- **Many-node star:** The method still reads only two edges; graph size does not affect its work.
- **First tested node is the center:** Membership succeeds and returns that node.
- **Second first-edge node is the center:** Membership for the first node fails, so the conditional returns the other endpoint.
- **Distinct leaves:** Two different valid star edges cannot share a leaf, which makes their intersection unique.
- **Duplicate edges:** They would undermine the "two distinct leaves" reasoning, but duplicate connections are not part of the promised valid star representation.
- **Self-loops:** The contract excludes them through `u_i != v_i` and the valid-star guarantee.
- **Invalid arbitrary graph:** The first two edges may share a non-global node or share nothing, so this constant-time rule must not be reused without the star guarantee.
- **No need to infer `n`:** The center is identified directly; computing `len(edges) + 1` adds no useful information.
- **Input preservation:** The expression only reads endpoints and never reorders or mutates `edges`.
