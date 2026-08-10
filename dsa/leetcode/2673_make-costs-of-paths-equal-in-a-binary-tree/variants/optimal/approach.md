## General

**Use the perfect-tree indexing**

The tree is perfect: every internal node has exactly two children and all leaves have the same depth. Nodes are numbered from 1, while Python list `cost` is indexed from 0.

For a node numbered $i$:

- its left child is numbered $2i$;
- its right child is numbered $2i+1$;
- its own stored cost is `cost[i - 1]`;
- its children's stored values are `cost[2 * i - 1]` and `cost[2 * i]`.

There are $\lfloor n/2 \rfloor$ internal nodes. The loop starts at `n >> 1`, which is integer division by two, and ends at node 1.

**Summarize each completed subtree with one number**

At first, every `cost[j]` is merely the original cost of one node. During the bottom-up loop, the solution repurposes entries of internal nodes.

After node $i$ has been processed, `cost[i - 1]` means:

> the equal cost of every path that starts at node $i$ and ends at any leaf in its subtree, after the minimum balancing already performed below and at $i$.

Leaves already satisfy this meaning without work because there is only one path from a leaf to a leaf, whose total is that leaf's own cost.

This summary is enough for the parent. The parent does not need to know how costs are distributed deeper in a child subtree. It only needs the common path total offered by the left child and the one offered by the right child.

**Why nodes are processed in descending order**

Every child number is larger than its parent number. Iterating internal node numbers downward guarantees that when node $i$ is reached, both child subtrees have already been balanced.

Consequently, the two child entries are comparable summaries:

- every path through the left child currently has total `cost[l - 1]` from that child to a leaf;
- every path through the right child currently has total `cost[r - 1]` from that child to a leaf.

A top-down traversal would not yet know how much balancing each child subtree requires, so it could not make the optimal local decision.

**The smaller child side must catch up**

Let the two balanced child-to-leaf totals be $L$ and $R$. All paths leaving node $i$ through the left side have the same continuation total $L$, and all paths through the right side have continuation total $R$.

Because operations may only increase costs, the smaller side cannot make the larger side decrease. At least $\lvert L-R\rvert$ total increments must be added somewhere on the smaller side before the two groups of paths can become equal.

That lower bound is achievable. Increasing the smaller child's root cost by exactly $\lvert L-R\rvert$ raises every path in that child subtree by the same amount. The two sides then both have continuation total $\max(L,R)$.

Therefore the exact minimum contribution at node $i$ is:

$$
\lvert L-R\rvert.
$$

The solution adds this difference to `ans`.

**Why one increment at a child root represents the whole adjustment**

The code does not need to reconstruct which physical node receives every increment. It computes only the minimum number of increments.

If the left side is short by $d$, adding $d$ to the left child itself affects every root-to-leaf path that enters that subtree. This simultaneously fixes all those paths. Spreading increments among lower nodes cannot use fewer than $d$, because any one left path still needs its total raised by $d$ to meet the right total.

The perfect subtree has already been internally equalized, so changing its root preserves equality among all paths inside it.

**Build the summary for the parent**

After balancing the two child sides, their common child-to-leaf total is $\max(L,R)$. A path beginning at node $i$ also includes the original cost stored at node $i$.

The assignment

`cost[i - 1] += max(cost[l - 1], cost[r - 1])`

changes the parent's entry into:

$$
\text{cost at node }i+\max(L,R).
$$

That is exactly the common total from node $i$ to any leaf below it. It establishes the subtree-summary invariant for the next higher level.

**Trace a small tree**

Consider a three-node tree with costs `[1, 2, 3]`. Node 1 is the only internal node. Its left and right summaries are 2 and 3.

The left path is short by one, so `ans` increases by one. After that conceptual increment, both child sides total three. The root summary becomes `1 + 3 = 4`.

The two root-to-leaf path totals can indeed both be four: the left path becomes $1+3$, while the right path was already $1+3$. No zero-increment solution exists because their original totals differed by one.

**Why local optimal choices form a global optimum**

At each node, paths in its left and right subtrees must eventually be equal to each other in any valid global answer. Since those subtrees are disjoint, the unavoidable difference $\lvert L-R\rvert$ at this node cannot be repaired by an increment outside the two sides: an increment at the parent would raise both sides equally and leave their difference unchanged.

The algorithm pays exactly this unavoidable amount, never more, and produces a single equal summary for the parent. Repeating the argument from the leaves to the root proves that all final root-to-leaf paths are equal and that the sum in `ans` is minimum.

**Mutation is deliberate**

The input `cost` is modified in place to store subtree summaries. Original child costs are no longer needed after their subtree has been summarized and consumed by the parent.

This reuse removes the need for a separate dynamic-programming array. Callers that need the original costs afterward would have to pass a copy, but the challenge solution is allowed to mutate its local input.

## Complexity detail

The loop processes each of the $\lfloor n/2 \rfloor$ internal nodes exactly once. Every iteration performs constant-time indexing, arithmetic, comparison, and assignment. Total time is $O(n)$.

Apart from the input array reused for summaries, the algorithm stores only `ans` and a few indices and temporary values. Auxiliary space is $O(1)$. This excludes the input array itself and does not use recursion.

## Alternatives and edge cases

- **Recursive postorder traversal:** It can return each subtree's equal path total and accumulate differences, also in $O(n)$ time, but uses $O(\log n)$ call-stack space in this perfect tree.
- **Separate dynamic-programming array:** It avoids mutating `cost` but requires $O(n)$ extra space.
- **Enumerate every root-to-leaf path repeatedly:** This duplicates shared-prefix work and is less efficient.
- **Increase both sides to more than the larger total:** Valid but never minimal because the extra common increase is unnecessary.
- **Try to repair a child difference at the parent:** Impossible; increasing the parent raises both child-path groups equally and does not change their difference.
- **Single-node tree:** There are no internal nodes and no unequal paths, so the answer is zero.
- **Equal child summaries:** Their difference is zero; no increments are needed at that node.
- **Very unequal subtrees:** The absolute difference is both a lower bound and an achievable adjustment.
- **Index conversion:** Tree node $i$ maps to array index $i-1$; confusing the two causes off-by-one errors.
- **Input mutation:** `cost` ends with subtree totals at internal positions rather than its original contents.
- **Large totals:** The running answer and summarized costs must use an integer type capable of holding accumulated values; Python integers grow as needed.
