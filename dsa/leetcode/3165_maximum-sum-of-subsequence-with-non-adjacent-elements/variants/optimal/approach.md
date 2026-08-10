## General

**Why ordinary DP is not enough after many updates**

For a fixed array, maximum nonadjacent-subsequence sum follows the familiar recurrence “skip current or take current plus the best two positions back.” Recomputing it after every point update would cost $O(nq)$.

A segment tree can update one position in $O(\log n)$, but each node must store enough boundary information to combine two adjacent segments without selecting both elements at their shared boundary.

**Meaning of the four node states**

For a segment, `sab` is its maximum valid nonadjacent-subsequence sum under endpoint permissions:

- first bit $a$ says whether the segment's leftmost element is allowed to be selected;
- second bit $b$ says whether its rightmost element is allowed to be selected.

A permission of 1 does not force selection; it merely permits it. A permission of 0 forbids that endpoint.

Thus:

- `s00` forbids both endpoints;
- `s01` forbids left and permits right;
- `s10` permits left and forbids right;
- `s11` permits both.

At a leaf, the only element can be selected only when both endpoint permissions are 1, because it is simultaneously the left and right endpoint. The code sets

`s11 = max(0, value)`

and leaves the other states zero. Taking zero represents the allowed empty subsequence and handles negative values.

**Combine two adjacent children**

The rightmost element of the left child and leftmost element of the right child are adjacent and cannot both be selected. To guarantee this, every combination forbids at least one of these inner endpoints.

For example, with both outer parent endpoints permitted:

`s11 = max(left.s10 + right.s11, left.s11 + right.s01)`.

The first choice forbids the left child's right endpoint; the second forbids the right child's left endpoint. Because permissions do not force selection, cases where neither inner endpoint is chosen are already included.

The other formulas apply the same rule while passing parent outer permissions down:

$$
\begin{aligned}
s_{00}&=\max(L_{00}+R_{10},L_{01}+R_{00}),\\
s_{01}&=\max(L_{00}+R_{11},L_{01}+R_{01}),\\
s_{10}&=\max(L_{10}+R_{10},L_{11}+R_{00}),\\
s_{11}&=\max(L_{10}+R_{11},L_{11}+R_{01}).
\end{aligned}
$$

Each state is therefore the optimum under its boundary permissions.

**Point updates**

`modify` descends to one leaf, replaces its `s11` with `max(0,v)`, and recomputes the four states on the path back to the root. Nodes outside that path represent unchanged array segments.

The full-array answer is the root's `s11` because both global endpoints may be selected. The helper call `query(1,1,n)` immediately returns that root state through its full-coverage branch.

After every update query, the solution adds this nonnegative maximum to `ans` modulo $10^9+7$.

The source does not write the update into `nums`, but the tree already contains the complete current state. Later updates operate on tree leaves, so mutating the original list is unnecessary.


At leaves, the four states exactly represent the best allowed choice. Assume both child nodes are correct. Any valid parent subsequence restricts to valid child subsequences and cannot select both shared-boundary elements, so it belongs to at least one of the two formula cases. Conversely, each formula case combines child solutions while forbidding one shared endpoint, making the union valid. Taking the maximum yields the exact parent optimum.

Induction establishes every node state after building and after each update. Root `s11` is therefore the maximum sum of any nonadjacent subsequence, including empty.

**Exact helper limitation**

`SegmentTree.query` only recurses when the requested range lies wholly in the left child or wholly in the right child. A partial range crossing a midpoint would leave `ans` at zero instead of combining both sides. This is a latent defect for general range queries.

The solution calls it only with `[1,n]`, which fully covers the root and returns immediately. Therefore, the defect does not affect any supported problem execution, but the helper should not be reused as a general range-query implementation.

## Complexity detail

Building the empty tree nodes costs $O(n)$. However, the exact source then initializes values by calling `modify` once for each of $n$ input elements. Each call costs $O(\log n)$, so exact initialization time is $O(n\log n)$, not $O(n)$.

Each of $q$ queries performs one point modification in $O(\log n)$ and a full-root query in $O(1)$. Total exact time is

$$
O((n+q)\log n).
$$

The manifest's $O(n+q\log n)$ would require building leaf values and pushing up all nodes in one linear recursive construction, which the source does not do.

The tree array holds $O(n)$ `Node` objects, each with four sums and interval boundaries. Recursion depth for build or update is $O(\log n)$. Auxiliary space is $O(n)$.

The output is one accumulated integer rather than a list. Modular reduction after each addition is algebraically valid.

## Alternatives and edge cases

- **Recompute linear DP after each update:** Simple but costs $O(nq)$ time.
- **Linear-value segment-tree build:** Initialize leaves directly during `build` and push up once, realizing the manifest's $O(n)$ construction time.
- **Matrix DP states:** Represent transitions as max-plus matrices; segment-tree multiplication gives another systematic formulation.
- **Store exact endpoint selection states:** Possible, but impossible states need negative infinity rather than zero. Permission states make the empty choice convenient.
- **All values negative:** Every leaf `s11` is zero, so the empty subsequence yields full answer zero.
- **Single element:** Root is a leaf and answer is `max(0,value)` after each update.
- **Adjacent positive values:** Merge formulas prevent both from being selected together.
- **Separated positive values:** They can contribute together when no selected indices are adjacent.
- **Repeated updates to one position:** Each replaces the leaf state; old values do not accumulate.
- **Modulo timing:** Each per-query maximum is computed exactly before being added modulo $10^9+7$.
- **Custom max function:** The module-level two-argument `max` shadows Python's built-in but every source call passes exactly two integers.
- **Partial query helper:** It is incorrect for ranges crossing a midpoint, but the only actual query is full coverage and bypasses that branch.
- **Input list not updated:** The segment tree, not `nums`, is the authoritative mutable representation after initialization.
