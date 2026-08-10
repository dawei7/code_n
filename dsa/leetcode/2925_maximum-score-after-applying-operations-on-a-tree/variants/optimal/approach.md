## General

All node values are positive. After operations, a root-to-leaf path has nonzero sum exactly when at least one node on that path was not taken and set to zero. We want maximize collected value while leaving such a witness on every path.

The recursive function returns two quantities for each subtree:

- the first component is the total original value of all nodes in the subtree;
- the second is the maximum score collectible from the subtree while keeping every path from its root to one of its leaves healthy, assuming no retained ancestor above is being used to satisfy those paths.

Call a child's returned pair $(a_c,b_c)$. The loop adds all child totals into `a` and all child healthy scores into `b`.

**Base case at a leaf**

A leaf subtree has only one root-to-leaf path containing that leaf. To keep its path sum nonzero without help from above in this state, the leaf must retain its positive value. It cannot be collected.

Therefore a leaf returns `(values[i], 0)`: its total value is `values[i]`, while the maximum healthy score inside the subtree is zero.

**Two choices at an internal node**

After aggregating children, the complete subtree total is

`values[i] + a`.

For the best healthy score, consider whether node $i$ is collected.

If we collect $i$, we gain `values[i]` but set it to zero. It cannot protect any root-to-leaf path, so every child subtree must independently remain healthy. The score is

`values[i] + b`.

If we do not collect $i$, its positive value remains on every path passing from $i$ to a leaf. Consequently, the health condition is already satisfied for all such paths, and every descendant may be collected. The obtainable score is the sum `a` of all child subtree values.

The best healthy score is therefore

`max(values[i] + b, a)`.

The function returns

`(values[i] + a, max(values[i] + b, a))`.

**Why the two cases are exhaustive and optimal**

Any valid strategy either collects $i$ or leaves it. If it collects $i$, each path must obtain a retained positive node below, which is exactly the independent healthy-subtree requirement represented by each child's second component. If it leaves $i$, every path already contains that retained positive value, so taking every descendant is optimal because all values are positive.

No third case is needed. The best score under each first decision is calculated exactly, and their maximum is the subtree optimum. Induction from leaves proves the second component returned at root $0$ is the global maximum.

**Why positivity is important**

Health is defined by path sum being nonzero, not explicitly by retaining a node. Because all original values are at least one and operations only replace values by zero, a path sum is nonzero if and only if some positive value remains. There is no cancellation by negative values.

Positivity also justifies collecting every descendant once a retained internal node protects the paths. Leaving an additional positive descendant would only reduce score without being necessary.

**Traversal mechanics**

The undirected tree is stored with both directions in `g`. Parameter `fa` records the parent. Neighbors equal to `fa` are skipped, preventing recursion from immediately returning along the same edge.

Variable `leaf` begins true and becomes false when any child is visited. This distinguishes a rooted leaf from an internal node even though a non-root leaf still has one adjacency entry for its parent.

## Complexity detail

Each node is visited once, and each undirected edge is examined from both endpoints. All work outside child recursion is constant, so time complexity is $O(n)$.

The adjacency list stores $2(n-1)$ neighbor entries and uses $O(n)$ space. Recursion can reach $O(n)$ depth on a path-shaped tree, so total auxiliary space is $O(n)$.

With the legal bound $n\le 20000$, a very deep path may exceed Python's default recursion limit. The recurrence is correct, but the exact recursive source has this robustness risk unless its environment raises the limit or the traversal is rewritten iteratively.

## Alternatives and edge cases

- **Minimize retained value:** An equivalent view is total tree value minus the minimum-value set hitting every root-to-leaf path. The returned pair computes the maximum-score form directly.
- **Greedily keep the cheapest node on each path:** Paths overlap, so a single retained ancestor may protect many leaves. Independent path choices can conflict or duplicate cost.
- **Iterative postorder:** A parent array and reversed traversal can compute the same pairs without recursion-depth failure.
- **Leaf root is not possible under $n\ge2$:** Still, the base case is general and would return score zero for a one-node tree.
- **Star tree:** Keeping the root permits collecting every leaf; collecting the root requires keeping every leaf. The recurrence compares these choices.
- **Path tree:** The condition reduces to retaining at least one node on the single root-to-leaf path, so the best score is total minus the smallest value.
- **Equal values:** Ties between collecting and retaining patterns do not matter because only the score is requested.
- **Parent skipping:** Checking `j != fa` is essential in the bidirectional adjacency list.
- **Recursive depth:** A chain can trigger `RecursionError` in standard Python despite the $O(n)$ algorithmic bound.
