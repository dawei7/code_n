## Problem Description & Examples
### Goal
Rob houses in a binary tree: no two directly linked nodes. Return max money.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

int - maximum amount

### Examples
**Example 1**

- Input: `root = [3, 4, 5, 1, 3, None, 1]`
- Output: `9`

**Example 2**

- Input: `root = [13]`
- Output: `13`

**Example 3**

- Input: `root = [5, 19]`
- Output: `19`

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
