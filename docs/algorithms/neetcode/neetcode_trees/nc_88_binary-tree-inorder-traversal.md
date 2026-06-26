## Problem Description & Examples
### Goal
Given the roots of two binary trees `root` and `sub_root` (level-order arrays), return `True` if `sub_root` is a subtree of `root`.

### Function Contract
**Inputs**

- `root`: List - main tree (level-order)
- `sub_root`: List - pattern tree

**Return value**

bool - True if sub_root is a subtree of root

### Examples
**Example 1**

- Input: `root = [3, 4, 5, 1, 2], sub_root = [4, 1, 2]`
- Output: `True`

**Example 2**

- Input: `root = [7, 7, 1], sub_root = [1]`
- Output: `True`

**Example 3**

- Input: `root = [3, 10, 2], sub_root = [3]`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Tree preorder traversal](tree_01_preorder-traversal.md)
- [Tree inorder traversal](tree_02_inorder-traversal.md)
- [Level-order traversal](tree_05_level-order-traversal.md)
- [Lowest common ancestor](tree_17_lowest-common-ancestor.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
