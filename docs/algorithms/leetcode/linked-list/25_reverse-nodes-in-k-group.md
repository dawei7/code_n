# Reverse Nodes in k-Group

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_87` |
| Frontend ID | 25 |
| Difficulty | Hard |
| Topics | Linked List, Recursion |
| Official Link | [reverse-nodes-in-k-group](https://leetcode.com/problems/reverse-nodes-in-k-group/) |

## Problem Description & Examples
### Goal
Given the roots of two binary trees (level-order arrays), check whether they are the same or not (same structure and node values).

### Function Contract
**Inputs**

- `p`: List - level-order tree 1
- `q`: List - level-order tree 2

**Return value**

bool - True if trees are identical

### Examples
**Example 1**

- Input: `p = [1, 2, 3], q = [1, 2, 3]`
- Output: `True`

**Example 2**

- Input: `p = [7], q = [7]`
- Output: `True`

**Example 3**

- Input: `p = [3, 10], q = [2, 5]`
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
