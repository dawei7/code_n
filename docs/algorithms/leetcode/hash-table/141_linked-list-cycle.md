# Linked List Cycle

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_76` |
| Frontend ID | 141 |
| Difficulty | Easy |
| Topics | Hash Table, Linked List, Two Pointers |
| Official Link | [linked-list-cycle](https://leetcode.com/problems/linked-list-cycle/) |

## Problem Description & Examples
### Goal
Given a linked list (as an array), sort it in ascending order.

### Function Contract
**Inputs**

- `head`: List[int]

**Return value**

List[int] - sorted list

### Examples
**Example 1**

- Input: `head = [4, 2, 1, 3]`
- Output: `[1, 2, 3, 4]`

**Example 2**

- Input: `head = [-2]`
- Output: `[-2]`

**Example 3**

- Input: `head = [-66, 45]`
- Output: `[-66, 45]`

---

## Underlying Base Algorithm(s)
- [Reverse linked list](linked_list_01_reverse-linked-list.md)
- [Cycle detection](linked_list_02_detect-cycle-in-linked-list.md)
- [Merge sorted linked lists](linked_list_03_merge-two-sorted-linked-lists.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
