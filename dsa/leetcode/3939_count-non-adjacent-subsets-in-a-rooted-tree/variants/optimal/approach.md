## General

The two requirements interact in different ways:

- the no-adjacent-nodes rule is local to every parent-child edge;
- divisibility depends on the sum of all selected values.

Tree dynamic programming handles the local edge rule, while storing sums only by their remainder modulo `k` keeps the numeric state small.

**Two states for every subtree root**

For each node `u` and remainder $r$, the source maintains:

- `not_selected[u][r]`: the number of valid independent subsets inside `u`'s currently accumulated subtree whose selected values sum to remainder $r$ and do not include `u`;
- `selected[u][r]`: the corresponding number that do include `u`.

“Independent” here means that no selected parent-child pair appears within that subtree.

Only the remainder matters because adding two sums affects divisibility according to

$$
(a+b)\bmod k
=\bigl((a\bmod k)+(b\bmod k)\bigr)\bmod k.
$$

There is no need to retain full sums as large as $10^9N$.

**Initialize a node before its children**

Viewed alone, a node has two possible subsets:

1. Exclude it. This is the empty subset with sum remainder zero, so `not_selected[node][0] = 1`.
2. Include it. Its remainder is `value % k`, so `selected[node][value % k] = 1`.

Every other entry begins at zero.

The empty subset is intentionally present during merging because a child subtree may contribute no selected node. It is removed exactly once from the final answer.

**Why reverse node order is a postorder**

The parent encoding guarantees `parent[i] < i` for every non-root node. Every descendant therefore has a larger label than each ancestor on its path.

Processing nodes from `node_count - 1` down to 1 ensures that, when node `u` is about to merge into its parent, all children of `u` have already merged into `u`. Its two arrays describe its complete subtree.

The parent may already include other children with larger labels. Merging one complete child at a time gradually builds the parent's complete subtree. Node zero is never merged upward because it is the root.

**Allowed combinations across one edge**

Suppose `node` is being merged into `ancestor = parent[node]`.

If the ancestor is not selected, the child's root may be either excluded or selected. Both choices respect the connecting edge. For each child remainder, the source computes:

`count_any = child_not + child_yes`.

The transition is then:

$$
\text{merged\_not}[a+b]
\mathrel{+}=
\text{ancestor\_not}[a]\,
\bigl(\text{child\_not}[b]+\text{child\_yes}[b]\bigr).
$$

If the ancestor is selected, the child's root must be excluded; otherwise that edge would have both endpoints selected. The only allowed transition is:

$$
\text{merged\_yes}[a+b]
\mathrel{+}=
\text{ancestor\_yes}[a]\,
\text{child\_not}[b].
$$

There is deliberately no product of `ancestor_yes` and `child_yes`.

In both formulas, $a+b$ is reduced modulo $k$. Since each operand is already between zero and $k-1$, their sum is below $2k$, so one subtraction when it reaches `k` is sufficient.

**Why multiplication and addition count all choices**

For one left-side subset and one child-subtree subset, their node sets are disjoint. Choosing one from each creates exactly one combined subset. Therefore the number of combinations is the product of their counts.

Different remainder pairs or different constituent subsets produce separate combined choices, so their products are added. The tree has only one edge between the child subtree and the accumulated ancestor side, and the selected/excluded transition enforces that edge exactly. All other internal edges were already enforced within the two DP tables.

Every independent subset of the combined subtree decomposes uniquely into its restriction on the accumulated ancestor portion and its restriction on this child subtree. Thus the merge neither misses nor double-counts a subset.

**Sparse lists reduce unnecessary loop work**

The source builds `ancestor_states` only for remainders where at least one parent-root state has a nonzero count modulo $10^9+7$. It similarly builds `child_states` only when the excluded or combined count can contribute.

This can make practical work smaller when few remainders are reachable. It does not change the worst-case bound because all `k` remainders may be present on both sides.

Counts are always interpreted modulo `1_000_000_007`. The child sum is reduced immediately, and complete merged arrays are reduced after all products have been accumulated. Python integers can hold those intermediate products safely.

**Finish at the root and remove the empty subset**

After all nodes have merged upward, the two tables at node zero describe the whole tree. A sum divisible by `k` has remainder zero. Both root-excluded and root-selected subsets are allowed, so their counts are added:

`not_selected[0][0] + selected[0][0]`.

The empty subset is included exactly once in `not_selected[0][0]`. The problem requires a nonempty subset, so the source subtracts one and then applies the modulus. Python's modulo produces the correct nonnegative residue even if subtraction temporarily gives a negative value.

Every remaining counted subset has remainder zero and obeys every parent-child restriction, exactly matching both validity conditions.

## Complexity detail

Let $N$ be the number of nodes and $K=k$.

Each of the $N-1$ child-to-parent merges may combine up to $K$ ancestor remainder states with up to $K$ child remainder states. The worst-case time is therefore $O(NK^2)$. Building state lists and reducing arrays contributes only $O(NK)$ additional work.

The two main tables each contain $N$ arrays of length $K$, so they use $O(NK)$ space. Temporary merged arrays and sparse state lists use $O(K)$ space for one merge and do not change the peak bound.

The manifest's $O(NK^2)$ time and $O(NK)$ space bounds accurately describe the checked source.

## Alternatives and edge cases

- **Enumerate all node subsets:** There are $2^N$ subsets before adjacency and divisibility filtering, which is infeasible for $N=1000$.
- **Track exact sums:** Values can be as large as $10^9$, and divisibility needs only the remainder. Exact-sum states would be unnecessarily enormous.
- **Use one DP state per remainder:** Whether the subtree root is selected determines what its parent may do. Combining the two states would lose the edge constraint.
- **Merge a selected parent with a selected child:** This is precisely the forbidden adjacent pair; the source correctly omits that transition.
- **Process nodes in increasing label order:** A child table would not yet contain its descendants. The `parent[i] < i` guarantee makes reverse labels a valid bottom-up order.
- **Forget the empty subset during DP:** Empty child choices are necessary when combining independent subtrees. It should remain available until one final subtraction.
- **Forget the final subtraction:** The empty subset has sum zero and would otherwise be counted as valid.
- **Single-node tree:** The result is one exactly when that node's value is divisible by `k`; the empty subset is removed.
- **`k = 1`:** Every sum has remainder zero. The DP counts all nonempty independent node subsets modulo the required modulus.
- **Several children of one parent:** They are merged sequentially. When the parent is excluded, each child root is independently free; when it is selected, every child root is forced out.
- **Sibling nodes both selected:** Siblings are not adjacent, so this is valid. Their choices combine through separate child merges.
- **Counts congruent to zero modulo the modulus:** Treating such a state as absent is safe because all later arithmetic and the requested result are also modulo that modulus.
- **Large node values:** Applying `value % k` at initialization captures every fact about the value needed by later merges.
