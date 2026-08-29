## General

**Use the BST ordering to follow only one path**

Every node in the first output must have value at most `target`, and every node in the second must be greater.

At a BST node:

- If its value is at most the target, its entire left subtree also belongs to the smaller output. Only its right subtree may contain values on both sides.
- If its value is greater, its entire right subtree belongs to the greater output. Only its left subtree may be mixed.

Therefore recursion needs to split only one child at each level, following a root-to-leaf search path.

**Define the recursive result**

`dfs(root)` returns two roots:

`[smaller_or_equal, greater]`

containing exactly the nodes of the input subtree partitioned by the target.

For an empty subtree, both results are `None`.

**Case one: root belongs to the smaller tree**

When `root.val <= target`, the root and its complete left subtree belong in the first result.

Recursively split `root.right` into `l` and `r`. Here `l` contains right-subtree nodes still at most the target, and `r` contains the greater nodes.

The smaller part `l` was originally inside root’s right subtree and should remain there, so assign:

`root.right = l`.

The output is `[root, r]`.

**Case two: root belongs to the greater tree**

When `root.val > target`, the root and its complete right subtree belong in the second result.

Split `root.left` into `l` and `r`. The `l` portion belongs entirely to the first output. Portion `r` contains values greater than the target and remains root’s left child:

`root.left = r`.

Return `[l, root]`.

**Why the reassigned child preserves BST order**

In the first case, `l` came from the original right subtree, so every value remains greater than the root while also being at most the target. It is valid as the reconstructed right child.

In the second case, `r` came from the original left subtree, so every value remains less than the root while being greater than the target. It is valid as the reconstructed left child.

**Preserving original structure**

The algorithm changes only edges that cross the split path. Entire subtrees known to lie on one side are returned untouched.

When both a parent and child remain in the same output and their edge does not need to bridge around nodes sent to the other side, the original relationship is preserved. The recursive child reassignment reconnects exactly the portion that remains with the parent.

**Trace target two in a balanced tree**

At root four, four is greater, so split its left subtree rooted at two. Node two belongs to the smaller tree, so split its right subtree rooted at three. Three is greater, and its empty left split returns nothing smaller and three greater.

Node two’s right becomes empty and it roots the smaller output with child one. Node three remains in the greater side and becomes the left portion returned to four, so four’s left becomes three. All other greater subtrees remain unchanged.

**Target need not occur**

Every decision uses only `<=` or `>`. If target lies between existing values, recursion still partitions at that numeric boundary. No equality search is needed.

**Why recursion stops after height steps**

At each node, one entire child subtree is classified without visiting it, and recursion enters only the potentially mixed child. The path ends at `None`.


Induct on subtree height. The empty result is correct. If root is small, BST ordering classifies its left subtree, and induction correctly splits its right; reconnecting the small part yields exactly the smaller tree while the other returned root contains every greater node. The large-root case is symmetric.

Only valid BST subtrees are reattached in their original side positions, so both outputs remain BSTs and preserve all required internal relationships.

## Complexity detail

Let `h` be tree height. Recursion visits at most one node per level along the split path, so time is `O(h)`.

The call stack uses `O(h)` space. No new tree nodes are allocated; the original nodes and pointers are reused.

In a balanced tree `h = O(log n)`, while a skewed tree has `h = O(n)`.

## Alternatives and edge cases

- **Traverse every node and rebuild trees:** This costs `O(n)` and loses more original structure than necessary.

- **Iterative path rewiring:** Two dummy roots can assemble the sides in `O(h)` time without recursion, but pointer handling is less direct.

- **Root equals target:** It belongs to the smaller-or-equal output, and only its right subtree may need splitting.

- **All nodes at most target:** The first output is the original root and the second is `None`.

- **All nodes greater:** The first output is `None` and the second is the original root.

- **Absent target:** Comparisons still define the correct partition.

- **Input mutation:** Child pointers along the split path are intentionally changed.

- **Empty recursive subtree:** It returns two null roots and terminates path reconstruction.
