# Merge k Sorted Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_86` |
| Frontend ID | 23 |
| Difficulty | Hard |
| Topics | Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort |
| Official Link | [merge-k-sorted-lists](https://leetcode.com/problems/merge-k-sorted-lists/) |

## Problem Description & Examples
### Goal
Given the root of a binary tree (level-order array), determine if it is height-balanced (depth of subtrees differs by at most 1 for every node).

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

bool - True if height-balanced

### Examples
**Example 1**

- Input: `root = [3, 9, 20, None, None, 15, 7]`
- Output: `True`

**Example 2**

- Input: `root = [50]`
- Output: `True`

**Example 3**

- Input: `root = [18, 73]`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Reverse linked list](linked_list_01_reverse-linked-list.md)
- [Cycle detection](linked_list_02_detect-cycle-in-linked-list.md)
- [Merge sorted linked lists](linked_list_03_merge-two-sorted-linked-lists.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
