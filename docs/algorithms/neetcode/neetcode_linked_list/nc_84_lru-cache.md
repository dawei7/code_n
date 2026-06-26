## Problem Description & Examples
### Goal
Given the root of a binary tree (level-order array), return its maximum depth (number of nodes along the longest root-to-leaf path).

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

int - maximum depth

### Examples
**Example 1**

- Input: `root = [3, 9, 20, None, None, 15, 7]`
- Output: `3`

**Example 2**

- Input: `root = [98]`
- Output: `1`

**Example 3**

- Input: `root = [73]`
- Output: `1`

---

## Underlying Base Algorithm(s)
- [Reverse linked list](linked_list_01_reverse-linked-list.md)
- [Cycle detection](linked_list_02_detect-cycle-in-linked-list.md)
- [Merge sorted linked lists](linked_list_03_merge-two-sorted-linked-lists.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
