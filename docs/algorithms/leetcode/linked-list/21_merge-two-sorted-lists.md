# Merge Two Sorted Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_75` |
| Frontend ID | 21 |
| Difficulty | Easy |
| Topics | Linked List, Recursion |
| Official Link | [merge-two-sorted-lists](https://leetcode.com/problems/merge-two-sorted-lists/) |

## Problem Description & Examples
### Goal
Two numbers are given as linked lists in **reverse** order. Add the two numbers and return the sum as a reversed linked list.

Inputs are `l1` and `l2` (arrays of digits in reverse order).

### Function Contract
**Inputs**

- `l1`: List[int] - digits in reverse order
- `l2`: List[int] - digits in reverse order

**Return value**

List[int] - sum in reverse order

### Examples
**Example 1**

- Input: `l1 = [2, 4, 3], l2 = [5, 6, 4]`
- Output: `[7, 0, 8]`

**Example 2**

- Input: `l1 = [6], l2 = [6]`
- Output: `[2, 1]`

**Example 3**

- Input: `l1 = [2], l2 = [9]`
- Output: `[1, 1]`

---

## Underlying Base Algorithm(s)
- [Reverse linked list](linked_list_01_reverse-linked-list.md)
- [Cycle detection](linked_list_02_detect-cycle-in-linked-list.md)
- [Merge sorted linked lists](linked_list_03_merge-two-sorted-linked-lists.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
