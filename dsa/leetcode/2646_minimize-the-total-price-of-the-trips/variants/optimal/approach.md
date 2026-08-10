## General

**Separate route usage from the halving decision**

In a tree, there is exactly one simple path between any two nodes. The phrase “any path” therefore gives no routing choice: each trip uses its unique tree path.

The total contribution of node $i$ before halving is:

$$
\texttt{usage[i]}\times\texttt{price[i]},
$$

where `usage[i]` is the number of trip paths containing that node.

Once these usage counts are known, the individual trips no longer need to be considered. The remaining problem is:

> Choose a set of non-adjacent tree nodes to halve, minimizing the sum of their usage-weighted prices.

The exact solution implements these two stages with one DFS per trip followed by a two-state tree DP.

**Build the undirected tree**

Adjacency list `g` contains both directions of every edge. Although the input tree is unrooted, recursive calls carry a parent `fa` to avoid traversing the edge back upward.

The final DP arbitrarily roots the tree at node zero. Root choice does not change adjacency or the valid non-adjacent sets; it only defines parent-child directions for the recurrence.

**Count one trip's path with reversible DFS**

For trip from `start` to `end`, helper `dfs(i, fa, k)` searches for target $k$.

On entering node $i$, it increments `cnt[i]`. If $i=k$, it returns true, preserving that increment.

Otherwise, it recursively searches neighbors other than the parent. `any(...)` stops at the first child subtree that reaches the target.

If no child finds the target, node $i$ is not on the successful path. The code undoes its tentative increment with `cnt[i] -= 1` and returns false.

Thus failed branches leave no trace, while nodes from start through target retain one added count.

**Why the path search works**

Because the graph is a tree, removing the parent edge prevents cycles and every descendant subtree is disjoint. Exactly one route from the current node can contain the target.

The DFS initially marks the currently explored route. Backtracking removes marks from every route that dead-ends. When the unique target route succeeds, true propagates upward through exactly its ancestors.

After the call, precisely the unique start-to-end path has been incremented once. Repeating for every trip makes `cnt[i]` the total usage frequency.

**Turn usage into two costs per node**

For node $i$, define its full weighted contribution:

$$
C_i=\texttt{cnt[i]}\times\texttt{price[i]}.
$$

Halving its price makes the contribution $C_i/2$. Prices are guaranteed even, so integer division `a // 2` is exact.

Helper `dfs2(i, fa)` returns pair $(a,b)$:

- $a$: minimum subtree cost when node $i$ is not halved;
- $b$: minimum subtree cost when node $i$ is halved.

It initializes:

$$
a=C_i,\qquad b=C_i/2.
$$

**Combine child states**

For child $j$, recursive result $(x,y)$ means:

- $x$: child not halved;
- $y$: child halved.

If current node is not halved, the child may be either state, so add:

$$
\min(x,y)
$$

to $a$.

If current node is halved, adjacency forbids halving the child. Only child state $x$ is legal, so add $x$ to $b$.

Children are independent once the current state is fixed because a tree has no edges between separate child subtrees.

**Why two states are sufficient**

The only interaction across an edge is whether both endpoints are halved. A parent does not need to know which deeper descendants were selected, only whether the child itself is selected.

Each returned state already includes the optimal legal choices inside that child's entire subtree under its root condition. This compresses exponentially many subsets into two numbers per node.

**Finish at the root**

Node zero has no parent, so it may be halved or not. The answer is:

`min(dfs2(0, -1))`.

Every tree node belongs to the root's subtree, so this minimum is the complete cost.

**Trace the role of usage**

In the first example, a node such as node one appears in all three trip paths, while node zero appears only in one. Halving a frequently used node can save more, but adjacency may prevent halving its children.

The DP compares these actual weighted savings rather than greedily choosing the highest raw price. A lower-priced node used many times can matter more than a high-priced node used once.


The path DFS proves that `cnt[i]` counts exactly how many trip sums include node $i$. By linearity of summation, total cost for any fixed halved set is the sum of the corresponding full or half weighted node contributions.

For `dfs2`, induct on subtree size. Leaf initialization gives the only two possible states. For an internal node, fixing whether it is halved makes child subproblems independent; the recurrence enumerates every legal child-root choice and chooses the cheapest. Therefore, both returned values are optimal under their stated conditions.

Taking the cheaper root state covers every legal non-adjacent set, proving the final minimum.

**Why halving is decided once**

Prices are chosen before all trips, so a node is either halved for every use or never halved. Multiplying usage by full or half price exactly represents this persistent decision.

## Complexity detail

Let $t=\texttt{len(trips)}$. Each trip DFS can visit $O(n)$ nodes, so usage aggregation costs $O(nt)$. The tree DP visits each node once in $O(n)$ time. Total time is $O(nt)$.

The adjacency list, usage counter, and recursion states use $O(n)$ space. Recursive depth can reach $O(n)$ for a path-shaped tree.

## Alternatives and edge cases

- **LCA difference accumulation:** With preprocessing, aggregate many paths more efficiently, but $n\le50$ makes one DFS per trip simpler.
- **Enumerate all halved subsets:** Exponential and unnecessary; the non-adjacency constraint is a tree independent-set DP.
- **Greedy by price or usage:** Can choose adjacent nodes or miss a better combination of descendants.
- **Trip with same start and end:** Only that one node receives a usage increment.
- **Unused node:** Its weighted cost is zero in both states, though selecting it may still block a child and is never beneficial.
- **Single-node tree:** The only node can be halved, and the DP returns its half weighted cost.
- **Even prices:** They make `a // 2` exact.
- **Root choice:** Any node can root the DP without changing the optimum.
- **Failed path branch:** Its tentative usage increments must be rolled back.
- **Deep tree:** Recursive implementations may need stack considerations outside the small $n$ constraint.
