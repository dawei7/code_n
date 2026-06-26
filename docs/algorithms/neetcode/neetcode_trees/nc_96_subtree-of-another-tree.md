## Problem Description & Examples
### Goal
A thief can rob houses arranged in a binary tree (level-order array). No two directly connected houses can be robbed. Find the maximum money that can be robbed.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

int - maximum amount robbed

### Examples
**Example 1**

- Input: `root = [3, 2, 3, None, 3, None, 1]`
- Output: `7`

**Example 2**

- Input: `root = [25]`
- Output: `25`

**Example 3**

- Input: `root = [9, 37]`
- Output: `37`

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
