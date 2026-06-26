## Problem Description & Examples
### Goal
Design an algorithm to serialize a binary tree to a string and deserialize it back.

`solve(root)` takes a level-order array, serializes it, deserializes it, and returns the result (should equal input).

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

List - roundtrip result (serialize then deserialize)

### Examples
**Example 1**

- Input: `root = [1, 2, 3, None, None, 4, 5]`
- Output: `[1, 2, 3, None, None, 4, 5]`

**Example 2**

- Input: `root = [54]`
- Output: `[54]`

**Example 3**

- Input: `root = [9, 98]`
- Output: `[9, 98]`

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
