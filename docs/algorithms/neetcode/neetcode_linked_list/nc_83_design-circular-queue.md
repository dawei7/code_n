## Problem Description & Examples
### Goal
Given the root of a binary tree (as level-order array, `None` for empty nodes), invert the tree (mirror it) and return the level-order representation.

### Function Contract
**Inputs**

- `root`: List - level-order binary tree (None for missing nodes)

**Return value**

List - level-order inverted tree

### Examples
**Example 1**

- Input: `root = [4, 2, 7, 1, 3, 6, 9]`
- Output: `[4, 7, 2, 9, 6, 3, 1]`

**Example 2**

- Input: `root = [54]`
- Output: `[54]`

**Example 3**

- Input: `root = [9, 98]`
- Output: `[9, 98]`

---

## Underlying Base Algorithm(s)
- [Reverse linked list](linked_list_01_reverse-linked-list.md)
- [Cycle detection](linked_list_02_detect-cycle-in-linked-list.md)
- [Merge sorted linked lists](linked_list_03_merge-two-sorted-linked-lists.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
