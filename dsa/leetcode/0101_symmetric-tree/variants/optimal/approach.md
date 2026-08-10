## General

A tree is symmetric when its left and right subtrees are mirror images across the vertical line through the root. Mirror equality differs from ordinary tree equality in one decisive way: corresponding child directions are crossed. The left child of one side must mirror the right child of the other, and the right child must mirror the left.

The selected helper `dfs(root1, root2)` tests exactly this relation between two subtree roots.

**The identity and empty-position cases**

The first condition is `root1 == root2`. Under the standard platform `TreeNode`, equality is object identity. The most important successful case is when both references are `None`: two corresponding mirror positions are both empty and therefore match.

The shortcut also succeeds if both references are literally the same node object. Such aliasing is uncommon between the root's left and right subtrees in a proper tree, but comparing one reference with itself is safe.

That identity case deserves care: a general tree is not necessarily symmetric with itself when compared in the same orientation. Here, however, reaching the exact same node from both mirror paths means the two references expose the same value and the same child objects. The shortcut treats the whole shared region as equal without recursively crossing its children. In the canonical tree model, the left and right subtrees do not share nodes, so this optimization normally matters only for the two-`None` base case. If arbitrary directed graphs with shared or cyclic nodes were allowed, a separate visited-pair design would be needed; those structures are outside the binary-tree contract.

If the equality shortcut fails and either reference is `None`, exactly one mirror position is occupied. The structures differ, so the helper returns false. If both nodes exist but their values differ, the reflected contents differ and the helper also returns false.

Python evaluates the combined `or` condition left to right. It never reads `.val` after finding an absent reference.

**Why the recursive child directions cross**

Once both current nodes exist and have equal values, the outer children must satisfy:

`dfs(root1.left, root2.right)`

and the inner children must satisfy:

`dfs(root1.right, root2.left)`.

Comparing left with left and right with right would test whether the two subtrees are identical in the same orientation, not reflected. A far-left node on one side must correspond to a far-right node on the other.

The two calls are joined with `and`. If the first comparison fails, the second is skipped because one mismatch already disproves symmetry. If it succeeds, the inner pair must still be checked.

**Trace of the asymmetric example**

For `[1,2,2,null,3,null,3]`, the initial helper pair contains the two nodes valued two, so their values match.

The first crossed call compares the left node's left child, which is `None`, with the right node's right child, which is node three. Exactly one exists, so it returns false. The tree is rejected even though its two children of the root have equal values. Equal values at one level cannot compensate for children placed on the wrong sides.

For `[1,2,2,3,4,4,3]`, the outer pair compares the two threes and the inner pair compares the two fours. Their corresponding missing children also match, so every recursive condition succeeds.

**Why the recursion is correct**

Two empty mirror positions agree. One empty position or unequal values cannot agree. For two equal-valued real nodes, their subtrees form mirror images exactly when the first node's left mirrors the second's right and the first's right mirrors the second's left.

The helper implements this recursive definition literally. Structural induction from empty child pairs proves that it returns true exactly for mirrored subtree pairs. Calling it on `root.left` and `root.right` therefore decides symmetry around the center.

The Reference guarantees a nonempty tree, so accessing `root.left` is safe. A reusable version for an unrestricted API should return true when `root is None` before accessing children.

The source only reads nodes and never modifies links or values.

## Complexity detail

Let $n$ be the number of nodes. In a symmetric tree, every node participates in a paired comparison, giving $O(n)$ time. An asymmetric tree may short-circuit earlier, but the worst case remains linear.

The recursion stack follows paired root-to-leaf paths. If $h$ is tree height, auxiliary space is $O(h)$, matching the manifest. Balanced trees use $O(\log n)$ depth; skewed structural paths can require $O(n)$.

No mirrored copy, traversal array, or other collection is allocated.

## Alternatives and edge cases

- **Iterative paired stack:** Push crossed child pairs for depth-first processing. It avoids recursion and uses $O(h)$ pending storage.
- **Paired breadth-first queue:** It is easy to visualize level by level but can require $O(n)$ space on a wide tree.
- **Create a mirrored copy:** Mirroring one side and comparing it works but wastes linear storage and risks unwanted mutation.
- **Single node:** Both root children are `None`, so the first helper call returns true.
- **Equal values are insufficient:** Missing children must occur at reflected positions.
- **Duplicate values:** Position-based comparisons handle repeated values without ambiguity.
- **Empty root outside the contract:** The exact public method would dereference it; add a guard for general reuse.
- **Direction matters:** Outer pairs are left/right, while inner pairs are right/left.
- **Short-circuiting:** The first proven mismatch safely ends the remaining work.
- **Root value:** The root lies on the mirror axis and needs no partner comparison; only its two subtrees must mirror. This is why the public call begins at the children.
- **Mirror relation is recursive:** Matching just one level cannot prove symmetry, because a deeper descendant may occupy the wrong reflected position.
