## General
**Serialize only preorder values**

Visit each node before its left and right subtrees and write its value. A general binary tree would need null markers, but the BST ordering property determines where each preorder value can belong, so structural markers can be omitted.

**Reconstruct under allowable value bounds**

Read preorder values with one shared cursor. A recursive call receives an open interval `(lower, upper)`. If the next value is outside that interval, it belongs to a later subtree and the call returns `None` without consuming it. Otherwise consume it as the root, then build its left subtree under `(lower, value)` and right subtree under `(value, upper)`.

**Why bounds recover the original shape**

Preorder fixes each subtree root before its descendants. In a BST, all left-subtree values and only those values lie below the root within the inherited bounds; right-subtree values lie above it. The first value that violates a child's interval begins an ancestor's later subtree. Induction on the preorder segment therefore reconstructs every original edge uniquely.

**Keep codec calls independent**

The serialization buffer and deserialization cursor are local to each call. Reusing a codec instance cannot leak values or cursor state between trees.

## Complexity detail
Serialization and bounded reconstruction each visit every node once, giving $O(n)$ time. The token array, reconstructed output, and worst-case recursion depth use $O(n)$ space.

## Alternatives and edge cases
- **Postorder plus bounds:** consuming postorder from the end reconstructs the right subtree before the left with the same linear complexity.
- **General-tree null markers:** works for any binary tree but emits extra structural tokens unnecessary for a BST.
- **Insert preorder values one at a time:** is simple but takes $O(n^2)$ time on a skewed tree.
- **Empty tree:** encode an empty string and decode it as `None`.
- **Skewed BST:** recursion depth can reach `n`.
- **Multi-digit values:** delimit tokens rather than treating individual characters as nodes.
