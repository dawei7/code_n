## Problem Description & Examples
### Goal
Given the root of a binary tree (level-order array) and an integer `target`, delete all leaf nodes with value equal to target. Repeat until no such leaves remain.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree
- `target`: int

**Return value**

List - tree after deleting all target leaves

### Examples
**Example 1**

- Input: `root = [1, 2, 3, 2, None, 2, 4], target = 2`
- Output: `[1, None, 3, None, 4]`

**Example 2**

- Input: `root = [4], target = 4`
- Output: `[]`

**Example 3**

- Input: `root = [5, 1], target = 2`
- Output: `[5, 1]`

---

## Underlying Base Algorithm(s)
- [Tree preorder traversal](tree_01_preorder-traversal.md)
- [Tree inorder traversal](tree_02_inorder-traversal.md)
- [Level-order traversal](tree_05_level-order-traversal.md)
- [Lowest common ancestor](tree_17_lowest-common-ancestor.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
