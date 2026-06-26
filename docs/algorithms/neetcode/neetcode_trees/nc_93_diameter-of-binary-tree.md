## Problem Description & Examples
### Goal
Given a binary tree (level-order array), determine if it is a valid BST.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

bool - True if valid BST

### Examples
**Example 1**

- Input: `root = [2, 1, 3]`
- Output: `True`

**Example 2**

- Input: `root = [50]`
- Output: `True`

**Example 3**

- Input: `root = [18, 73]`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Tree preorder traversal](tree_01_preorder-traversal.md)
- [Tree inorder traversal](tree_02_inorder-traversal.md)
- [Level-order traversal](tree_05_level-order-traversal.md)
- [Lowest common ancestor](tree_17_lowest-common-ancestor.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
