## Problem Description & Examples
### Goal
Given the head of a singly linked list (as an array), return the middle node's value. If there are two middles, return the second.

### Function Contract
**Inputs**

- `head`: List[int]

**Return value**

int - value of the middle node

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4, 5]`
- Output: `3`

**Example 2**

- Input: `head = [50]`
- Output: `50`

**Example 3**

- Input: `head = [18, 73]`
- Output: `73`

---

## Underlying Base Algorithm(s)
- [Reverse linked list](linked_list_01_reverse-linked-list.md)
- [Cycle detection](linked_list_02_detect-cycle-in-linked-list.md)
- [Merge sorted linked lists](linked_list_03_merge-two-sorted-linked-lists.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
