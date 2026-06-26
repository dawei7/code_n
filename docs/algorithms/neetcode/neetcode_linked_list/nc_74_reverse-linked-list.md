## Problem Description & Examples
### Goal
Given an array of integers `nums` containing `n+1` integers where each integer is in the range `[1, n]` inclusive, there is exactly one repeated number. Find and return it without modifying the array and using only constant extra space.

### Function Contract
**Inputs**

- `nums`: List[int] - values in [1, n], one duplicate

**Return value**

int - the duplicate number

### Examples
**Example 1**

- Input: `nums = [1, 3, 4, 2, 2]`
- Output: `2`

**Example 2**

- Input: `nums = [3, 2, 1, 2]`
- Output: `2`

**Example 3**

- Input: `nums = [3, 1, 2, 1]`
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
