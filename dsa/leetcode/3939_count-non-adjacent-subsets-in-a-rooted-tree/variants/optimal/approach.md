## General

**Track both the root choice and the residue of each subtree.** For every node $u$ and residue $r$, maintain two counts:

- `not_selected[u][r]`: independent subsets of $u$'s subtree whose sum is congruent to $r$ modulo $K$ and that omit $u$;
- `selected[u][r]`: such subsets that include $u$.

Before processing children, omitting $u$ gives the empty local choice with residue zero, while selecting it gives residue `nums[u] % k`. Thus `not_selected[u][0] = 1` and `selected[u][nums[u] % k] = 1`.

**Merge a child by circular convolution.** Suppose child $v$ has already been completed. If $u$ is omitted, the child root may be omitted or selected, so each parent residue combines with `not_selected[v][s] + selected[v][s]`. If $u$ is selected, adjacency forbids selecting $v$, so it combines only with `not_selected[v][s]`. The merged residue is $(r+s)\bmod K$, and every pair of independent choices contributes the product of their counts. These are exactly the allowed combinations: different child subtrees have no edges between them, and the merge rule handles the only connecting edge $(u,v)$.

The input guarantee `parent[i] < i` places every descendant after its ancestors. Processing node labels from $N-1$ down to $1$ therefore ensures that a node's complete distribution is ready when it is merged into its parent; no recursive traversal is needed. Once every non-root node has been merged, the two root arrays count every independent subset by residue and by whether the root was selected.

Both root states with residue zero satisfy the divisibility condition. Their sum still includes the globally empty subset through the unselected state, so subtract one and apply the result modulus. Every valid nonempty subset has one unique sequence of child choices in these merges, while every counted sequence respects each parent-child edge, proving that the final count is exact.

## Complexity detail

Let $N$ be the node count and $K=k$. Merging one tree edge considers at most $K$ parent residues and $K$ child residues, taking $O(K^2)$ time. There are $N-1$ edges, so the total time is $O(NK^2)$. The two length-$K$ distributions stored for every node use $O(NK)$ space; temporary merge arrays use another $O(K)$ and do not change the bound.

The implementation records only nonzero residue states in each inner merge, which reduces work before a subtree reaches all residues but does not change the worst-case bound.

For scaling evidence, define

$$
S=NK^2.
$$

The three benchmark tiers use stars with $K=1$ and $N=4$, $8$, and $16$, so $S=4$, $8$, and $16$. With the modulus fixed, the required dynamic program is linear in $S$. A direct enumeration of all $2^N$ node subsets grows exponentially, yet the largest tier remains small enough to finish and receive an ordinary complexity verdict rather than hitting the safety cap.

## Alternatives and edge cases

- **Enumerate every node subset:** Testing adjacency and divisibility for all $2^N$ masks is a useful tiny-tree oracle, but it is exponential and cannot handle $N=1000$.
- **Ignore the selected/unselected distinction:** A residue-only subtree count cannot determine whether merging a child would select both endpoints of their connecting edge.
- **Merge a selected parent with every child state:** This incorrectly admits subsets containing both a node and its direct child; only the child's unselected distribution is legal in that branch.
- **Subtract the empty subset too early:** Each unselected node state needs its empty local choice so sibling combinations can be formed. Remove exactly one empty subset only after the root distribution is complete.
- **Modulus one:** Every sum has residue zero, but the adjacency restriction still matters; the DP becomes a count of all nonempty independent sets.
- **Single-node tree:** The only nonempty subset contains the root and is counted precisely when its value is divisible by $K$.
- **Deep chain:** Reverse label order avoids recursion-depth failure even when all 1000 nodes form one path.
- **Large node values:** Reduce each value modulo $K$ at initialization; the full values are never needed afterward.
