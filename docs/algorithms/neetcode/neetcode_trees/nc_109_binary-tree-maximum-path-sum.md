## Problem Description & Examples
### Goal
Find the maximum path sum in a binary tree. The path does not need to pass through the root and can include negative values.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree with possibly negative values

**Return value**

int - maximum path sum

### Examples
**Example 1**

- Input: `root = [1, 2, 3]`
- Output: `6`

**Example 2**

- Input: `root = [29]`
- Output: `29`

**Example 3**

- Input: `root = [-3, -12]`
- Output: `-3`

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
