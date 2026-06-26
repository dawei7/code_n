## Problem Description & Examples
### Goal
Given a sorted linked list (as an array), remove all duplicates such that each element appears only once.

### Function Contract
**Inputs**

- `head`: List[int] (sorted)

**Return value**

List[int] - sorted list without duplicates

### Examples
**Example 1**

- Input: `head = [1, 1, 2, 3, 3]`
- Output: `[1, 2, 3]`

**Example 2**

- Input: `head = [2, 2]`
- Output: `[2]`

**Example 3**

- Input: `head = [1, 3]`
- Output: `[1, 3]`

---

## Underlying Base Algorithm(s)
- [Reverse linked list](linked_list_01_reverse-linked-list.md)
- [Cycle detection](linked_list_02_detect-cycle-in-linked-list.md)
- [Merge sorted linked lists](linked_list_03_merge-two-sorted-linked-lists.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
