## Problem Description & Examples
### Goal
Given a linked list (as an array), return `True` if it is a palindrome.

### Function Contract
**Inputs**

- `head`: List[int]

**Return value**

bool - True if list is a palindrome

### Examples
**Example 1**

- Input: `head = [1, 2, 2, 1]`
- Output: `True`

**Example 2**

- Input: `head = [4]`
- Output: `True`

**Example 3**

- Input: `head = [1, 3]`
- Output: `False`

---

## Underlying Base Algorithm(s)
- [Reverse linked list](linked_list_01_reverse-linked-list.md)
- [Cycle detection](linked_list_02_detect-cycle-in-linked-list.md)
- [Merge sorted linked lists](linked_list_03_merge-two-sorted-linked-lists.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
