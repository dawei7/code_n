## General

The competitive solution reconstructs each subtree from a half-open inorder interval and the matching preorder start. A dictionary maps every unique value to its inorder index, turning every root split into constant-time lookup.

The helper state is:

`buildTreeRecu(lookup, preorder, inorder, pre_start, in_start, in_end)`.

The relevant inorder values occupy `[in_start, in_end)`. The interval length is `in_end - in_start`. `pre_start` points to the first value of the corresponding preorder block.

The `inorder` parameter is passed through but never read inside the helper; all needed inorder information comes from interval indices and `lookup`. This redundancy is harmless.

**Half-open empty interval**

If `in_start == in_end`, the interval contains zero values, so the subtree is absent and the method returns `None`.

Half-open ranges make size arithmetic clean and permit an empty child at either boundary without using indices outside the array.

**Root selection**

For a nonempty subtree, preorder's first value is its root:

`preorder[pre_start]`.

The code creates a `TreeNode` and finds that value's absolute inorder position `i`. Values in `[in_start, i)` belong to the left subtree; values in `[i + 1, in_end)` belong to the right.

The left-subtree size is:

$$
L=i-\texttt{in\_start}.
$$

**Why the preorder starts differ**

The left child block follows immediately after the root, so its preorder start is `pre_start + 1`.

The right block follows the root plus all $L$ left-subtree nodes. Its start must therefore be:

$$
\texttt{pre\_start}+1+L
=\texttt{pre\_start}+1+i-\texttt{in\_start}.
$$

That is the source's longer right-call expression. Forgetting $L$ would incorrectly treat the left subtree's first value as the right root.

The left inorder interval ends at `i`; the right begins at `i + 1`. Both use the same exclusive original `in_end`.

**Detailed example**

With root three, `pre_start` is zero, current inorder interval is `[0, 5)`, and lookup places three at index one. The left size is one.

The left call begins preorder at one and inorder `[0, 1)`, producing nine. The right call begins preorder at `0 + 1 + 1 = 2` and inorder `[2, 5)`, so its root is twenty.

Within the right interval, twenty is at inorder index three and the left size is one. The child calls therefore select fifteen and seven in their correct positions.

**Why all values land in the correct subtree**

For any valid BST-independent binary tree reconstruction, inorder alone establishes membership relative to the root: everything before the root position is in its left subtree, and everything after is in its right subtree. Preorder establishes which value roots each resulting group.

Unique values make the split position singular. The two child intervals are disjoint, exclude the root, and together contain every remaining value. Their preorder blocks have matching sizes and order. Induction on interval length proves that the returned structure has both supplied traversals.

This reasoning does not use BST value ordering; the tree may be any binary tree.

**Checking the half-open arithmetic**

The current subtree size is `in_end - in_start`. Its left size is `i - in_start`, its right size is `in_end - i - 1`, and one node is the root. Adding them gives:

$$
(i-\texttt{in\_start})+(\texttt{in\_end}-i-1)+1
=\texttt{in\_end}-\texttt{in\_start}.
$$

Thus no node is lost or counted twice. The right preorder start advances by one root plus exactly the left size. Its remaining block therefore has exactly the right interval's size.

This calculation also explains why `i` must come from the global lookup yet be interpreted relative to `in_start`. Using `i` directly as the left size would work only for subtrees whose inorder interval starts at zero.

## Complexity detail

The lookup-building loop processes $n$ values. Each real node is constructed once and performs one expected $O(1)$ dictionary access, so time is $O(n)$.

The dictionary occupies $O(n)$ space. Recursive depth is tree height $h$, at most $n$. The new tree has $n$ nodes as required output. Auxiliary and total space are therefore $O(n)$ under the manifest.

Even for a balanced tree with $O(\log n)$ stack depth, the index dictionary still requires $O(n)$ auxiliary memory, so the overall auxiliary bound does not fall below linear in this implementation.

The method passes array references and integer bounds rather than copying slices, preserving linear behavior.

## Alternatives and edge cases

- **Size-based state:** Carry preorder start, inorder start, and subtree size instead of an exclusive endpoint. It is algebraically equivalent.
- **Iterator-based recursion:** Consume preorder values globally while recursive inorder bounds determine subtrees.
- **Iterative construction:** Use a stack and an inorder pointer to close completed left subtrees; it avoids recursion-depth limits.
- **Linear search per root:** Simpler but can become $O(n^2)$.
- **Single node:** Both half-open child ranges are empty.
- **All-left or all-right tree:** Recursion depth reaches $n$, risking Python `RecursionError` for the maximum constraint.
- **Unique values:** Required so `lookup[value]` identifies one position.
- **Not specifically a BST:** Values are partitioned by traversal positions, not numerical comparison.
- **Supporting `TreeNode`:** The top-level class supplies mutable child fields; construction assigns them after node creation.
- **Unused helper parameter:** The recursive function receives `inorder` but never reads it. Removing that parameter would not change behavior because `lookup` and bounds carry all needed information.
- **No slicing:** Passing indices rather than subarrays prevents repeated copying and keeps total time linear.
