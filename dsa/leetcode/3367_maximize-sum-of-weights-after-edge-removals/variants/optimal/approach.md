## General

**Root the tree to make edge choices local.** Root the undirected tree at node zero. Every non-root node has one parent edge and zero or more child edges. The degree limit at a node depends on whether its parent edge is retained, so each subtree needs two values.

For `dfs(u, fa)`, the returned pair has these meanings:

- first value: best subtree weight when edge from `u` to its parent is not retained, leaving room for up to `k` child edges;
- second value: best subtree weight when the parent edge is retained, leaving room for only `k-1` child edges.

The parent edge's own weight is not included inside these returned values. Its parent adds that weight if it chooses the edge.

**Begin with every child edge removed.** For child `v`, recursive result `a` is the best value when `(u,v)` is not kept. Adding all such `a` values forms baseline `s`. This baseline is feasible because no child edge consumes degree at `u`.

**Measure the gain from retaining one child edge.** If `(u,v)` with weight `w` is kept, the child's state must switch from `a` to `b` because `v` now uses one degree slot for its parent. The total change relative to baseline is

$$
\texttt{gain}=w+b-a.
$$

This gain includes the edge weight and any loss caused by reducing the child's available child-edge capacity.

Even though `w` is positive, the net gain can be nonpositive if forcing the parent connection displaces more valuable edges below `v`. Since removing edges is allowed, the source stores only positive gains.

**Choose the best degree-limited gains.** Gains from different child subtrees are otherwise independent. When the parent edge of `u` is absent, `u` may retain up to `k` child edges, so the best choice is the largest `k` positive gains. When the parent edge is present, it may retain only the largest `k-1`.

Sorting `t` in descending order makes these sums `sum(t[:k])` and `sum(t[:k-1])`. Taking any smaller positive gain while rejecting a larger one would only reduce the objective and use the same one degree slot.

The returned pair is therefore

`(s + sum(t[:k]), s + sum(t[:k-1]))`.

**Why subtree choices combine safely.** Once the decision about edge `(u,v)` is fixed, all remaining choices inside child `v` belong exclusively to that subtree. Different child subtrees share no nodes or edges. Their optimum values can be added, and the only coupling is the number of retained child edges incident to `u`, handled by the top-gain limit.

**Handle the root.** Node zero has no parent edge, so its first returned value is the relevant answer. The source returns `max(x,y)`. Because `x` may choose up to `k` positive gains while `y` may choose only `k-1`, `x >= y`; the maximum is effectively `x` and remains correct.

**Trace a child gain.** Suppose excluding a child edge lets its subtree earn 20, while retaining the parent edge restricts that subtree to 14, and the connecting edge weighs 9. The gain is $9+14-20=3$, so keeping it improves the total by three. If the edge weighed five, the gain would be negative one and should be rejected despite its positive raw weight.

**Why the two returned states are exact.** Assume recursively that every child pair is optimal under its parent-edge condition. Baseline `s` is the best outcome with no child connections. Any feasible set of child connections changes it by the corresponding gains and may contain at most the available number. Selecting the largest positive allowed gains maximizes that sum. Induction from leaves to the root proves both states.

**Build the adjacency list once.** Every input edge is inserted in both directions. The parent parameter `fa` prevents DFS from traversing back up and is sufficient because the input is guaranteed to be a tree.

**A practical recursion defect at the maximum constraint.** A path-shaped tree can create recursion depth $\Theta(n)$. With $n=10^5$, standard Python's default recursion limit is far smaller. The exact source neither raises that limit nor uses an iterative traversal, so it can raise `RecursionError` on a valid deep tree even though the DP recurrence is mathematically correct.

## Complexity detail

Every edge is traversed a constant number of times. At a node with $d$ children, sorting gains costs $O(d\log d)$. Summed across the tree, this is at most $O(n\log n)$ time.

The adjacency list stores $O(n)$ entries, recursion can reach $O(n)$ depth, and gain lists collectively require $O(n)$ live/storage scale, giving $O(n)$ auxiliary space.

The stated asymptotic bounds match the manifest, but the unguarded recursive call stack is not operationally safe for every $n=10^5$ tree in normal Python.

## Alternatives and edge cases

- **Iterative postorder traversal:** It computes the same two states without recursion-depth failure and is safer at the maximum constraint.
- **Heap-select top gains:** Keeping only the largest `k` can reduce sorting cost for high-degree nodes, though full sorting is simple.
- **Greedy by raw edge weight:** It ignores the child-subtree opportunity cost `a-b` and can be wrong.
- **Leaf node:** Baseline is zero, gain list is empty, and both returned states are zero.
- **`k = 1`:** A node whose parent edge is kept may retain zero child edges; slice `t[:0]` is correctly empty.
- **Large `k`:** If the limit exceeds the number of positive child gains, all beneficial edges are retained.
- **Nonpositive net gain:** Rejecting it is valid because edge removal is optional.
- **Positive raw weights:** They do not guarantee positive DP gains.
- **Root state:** The parent-present value is unnecessary, and `max(x,y)` equals the parent-absent optimum.
- **Path tree:** DP choices are simple, but recursion depth can still crash the exact implementation.
- **Star tree:** The root chooses the largest `k` edge gains.
- **Tree guarantee:** The parent check is enough; a general graph would need a visited set.
- **Degree accounting:** Retaining a parent edge consumes exactly one of the node's `k` slots.
- **Tuple annotation:** `Tuple` and `List` must be available.
- **Input preservation:** The source builds `g` without changing `edges`.
- **Recursion limit:** No protective configuration is present in the exact file.
