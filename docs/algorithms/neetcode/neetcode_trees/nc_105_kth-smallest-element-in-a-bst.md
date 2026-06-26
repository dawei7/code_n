## Problem Description & Examples
### Goal
Given a BST root (level-order) and integer `k`, find the k-th smallest element using in-order traversal.

### Function Contract
**Inputs**

- `root`: List - BST level-order
- `k`: int

**Return value**

int - k-th smallest value

### Examples
**Example 1**

- Input: `root = [5, 3, 6, 2, 4], k = 3`
- Output: `3`

**Example 2**

- Input: `root = [3, 1, 4, None, 2], k = 1`
- Output: `1`

**Example 3**

- Input: `root = [5, 3, 6, 2, 4, None, None, 1], k = 3`
- Output: `3`

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
