## General

The required order is a concatenation of four non-overlapping pieces:

1. the root;
2. non-leaf nodes on the left boundary from top to bottom;
3. all leaves from left to right;
4. non-leaf nodes on the right boundary from bottom to top.

The solution builds the root directly and uses one DFS helper in three modes for the other pieces.

Mode `i == 0` collects the left boundary, mode `i == 1` collects leaves, and mode `i == 2` collects the right boundary.

**How the code recognizes a leaf.** In a proper binary tree, a leaf has both child references equal to `None`, so `root.left == root.right` is true. A non-leaf has at least one child; its child references are therefore not both `None`, and `root.left != root.right` is true.

This is a compact structural test. It does not compare node values.

**Collect the left boundary without its leaf.** Starting from `root.left`, mode zero processes a node only if it is non-leaf. It appends the value immediately, giving top-to-bottom order.

It then follows:

- the left child when one exists;
- otherwise the right child.

That matches the definition of the left boundary. When the path reaches a leaf, the non-leaf condition fails and nothing is appended, preventing duplication with the separate leaf phase.

If the root has no left child, the call receives `None` and the left boundary remains empty, even if the tree has a right subtree. This matches the source definition.

**Collect all leaves from left to right.** Mode one begins at the root. If the current node is a leaf, it appends the value. Otherwise it recursively visits the left subtree and then the right subtree.

This left-before-right DFS encounters leaves in their horizontal left-to-right order. Non-leaf values are not appended in this mode.

Beginning at the root ensures leaves in both subtrees are included. The root itself is handled specially before this call.

**Collect the right boundary in forward order, then reverse it.** Starting from `root.right`, mode two appends each non-leaf value top to bottom. It follows:

- the right child when one exists;
- otherwise the left child.

This mirrors the right-boundary definition. Leaves are excluded by the same non-leaf test.

The collected list `right` is top down, but the required output wants bottom up. The expression `right[::-1]` reverses it during final concatenation.

**Handle the root exactly once.** The answer starts as `[root.val]`. If `root.left == root.right`, the root is a leaf and the method returns immediately.

This special case is necessary because the problem says the root is not considered part of the leaf portion. Without the early return, leaf-mode DFS would append the root again.

For a non-leaf root, leaf mode cannot append it, so starting from the root is safe.

For tree `[1, null, 2, 3, 4]`, the left-boundary call is empty. Leaf DFS outputs three and four. Right-boundary mode starts at two, appends two, then reaches leaf four and stops. Reversing the one-element right list leaves two, producing `[1,3,4,2]`.

In the larger example, left mode appends two but excludes leaf four. Leaf mode outputs four, seven, eight, nine, and ten. Right mode appends three and six but excludes ten; reversing gives six then three. Concatenation matches the requested boundary.

**Why no physical node is duplicated.** The root is handled separately. Boundary modes explicitly exclude leaves. Leaf mode includes only leaves. Left and right boundary paths begin in disjoint root subtrees, so their non-leaf nodes cannot overlap. These categories are therefore disjoint.

**Why every required node appears.** Mode zero follows exactly the fallback rule defining each next left-boundary node. Mode two follows the mirrored right rule. Mode one visits every node and records exactly all leaves in left-to-right order. Together with the root, all four specified portions are complete.

Equal node values do not cause deduplication because lists store each visited node's value at its structural position. Two different boundary nodes with the same value correctly produce repeated output entries.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. Leaf DFS visits every node once. The two boundary walks visit at most $O(h)$ additional nodes. Total time is $O(n)$.

Recursive depth is $O(h)$. The manifest's $O(h)$ space bound treats the returned boundary values as output storage. The exact code also builds temporary `left`, `leaves`, `right` lists and a reversed right copy before joining them into `ans`; those fragments collectively hold $O(n)$ values in the worst case. Thus auxiliary storage is $O(h)$ only under the conventional exclusion of output-fragment storage, while literal peak allocated list storage can be $O(n)$.

## Alternatives and edge cases

- **One preorder traversal with boundary flags:** Track whether each node lies on a left or right boundary and append into ordered sections. It can combine classification but requires careful flag propagation.
- **Iterative boundary walks plus leaf DFS:** This expresses the three pieces separately and avoids recursion for the two narrow boundary paths.
- **Include boundary leaves:** That duplicates the leftmost and rightmost leaves when the leaf list is added.
- **Single-node tree:** The root-only early return produces one value.
- **No left child:** The left boundary is empty by definition, not taken from the right subtree.
- **No right child:** The right boundary is empty; leaves and left boundary still work.
- **Boundary node missing preferred child:** Left mode falls back right, while right mode falls back left.
- **Skewed tree:** Non-leaf nodes belong to one boundary, the terminal leaf appears once in the leaf section.
- **Root with two leaf children:** Boundaries exclude both leaves, and leaf mode appends them left to right.
- **Duplicate values:** Structural nodes remain separate output entries.
- **Right-order reversal:** Appending the right path directly would produce top-to-bottom order, opposite the contract.
