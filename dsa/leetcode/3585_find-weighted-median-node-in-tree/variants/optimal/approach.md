## General

Root the tree at node 0 and record for every node its depth, direct parent, and weighted distance from the root. Build a binary-lifting table in which `up[b][x]` is the ancestor $2^b$ edges above `x`. The table supports both lowest common ancestor queries and power-of-two movement along an ancestor chain.

For a query directed from `u` to `v`, let `l` be their lowest common ancestor. Define the two path weights

$$
D_u=\operatorname{dist}(u)-\operatorname{dist}(l),\qquad
D_v=\operatorname{dist}(v)-\operatorname{dist}(l),
$$

so the total weight is $T=D_u+D_v$. Comparisons use doubled integer distances instead of floating-point halves.

If $2D_u\ge T$, the threshold is reached while climbing from `u` toward `l`. Starting at `u`, greedily take the largest ancestor jump that keeps the accumulated distance strictly below half, meaning `2 * climbed < T`. After all powers are considered, the direct parent of the current node is exactly the first node that reaches or crosses the threshold. The strict comparison preserves a node whose distance is exactly half.

Otherwise the crossing lies after `l` on the descending part toward `v`. A node `x` on that branch qualifies when

$$
2\bigl(\operatorname{dist}(x)-\operatorname{dist}(l)\bigr)\ge T-2D_u.
$$

Begin at `v` and lift upward as far as possible while the candidate remains on or below `l` and still satisfies this inequality. The final node is the highest qualifying descendant of `l`, which is precisely the first qualifying node encountered from `u`. A query from a node to itself has total weight zero and returns that node directly.

## Complexity detail

Let $n$ be the node count and $q$ the number of queries. Iterative traversal takes $O(n)$ time. Building $O(\log n)$ ancestor levels takes $O(n\log n)$ time and space. Each LCA and threshold search takes $O(\log n)$ time, so total time is $O((n+q)\log n)$ and auxiliary space is $O(n\log n)$.

The benchmark defines $S=n=q$ on a unit-weight chain and repeats a query spanning the complete tree. The accepted preprocessing and lifting use $O(S\log S)$ time. A calibrated slower alternative explicitly reconstructs the $\Theta(S)$-node path for every query, taking $O(S^2)$ time while producing identical answers.

## Alternatives and edge cases

- **Traverse every queried path:** Walking from one endpoint to the other directly is easy to reason about but can require $O(nq)$ time.
- **Binary search with repeated ancestor queries:** Searching a depth and recomputing path distances adds an avoidable logarithmic factor; weighted binary lifting locates the crossing in one descent through the levels.
- **Euler tour plus range minimum query:** It can answer LCA efficiently, but an additional ancestor-jump structure is still needed to locate the weighted threshold.
- **Query direction:** `[u, v]` and `[v, u]` can have different answers because the first qualifying node is measured from the first endpoint.
- **Exact half:** A node at exactly half qualifies, so upward jumps on the first half must preserve strict inequality before returning the next ancestor.
- **Same endpoint:** A zero-length path has total weight zero and its sole node is the answer.
- **Non-root LCA:** Both path-weight components must be measured relative to the actual lowest common ancestor, not always node 0.
- **Large weights:** Root distances can reach roughly $10^{14}$, requiring 64-bit arithmetic in fixed-width languages.
- **Deep chain:** Use iterative traversal to avoid recursion-depth failure when the tree contains $10^5$ nodes.
