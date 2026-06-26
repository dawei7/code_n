# LFU Cache

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_85` |
| Frontend ID | 460 |
| Difficulty | Hard |
| Topics | Hash Table, Linked List, Design, Doubly-Linked List |
| Official Link | [lfu-cache](https://leetcode.com/problems/lfu-cache/) |

## Problem Description & Examples
### Goal
Given the root of a binary tree (level-order array), return the length of the diameter of the tree (longest path between any two nodes, measured in number of edges).

### Function Contract
**Inputs**

- `root`: List - level-order binary tree

**Return value**

int - diameter (longest path in edges)

### Examples
**Example 1**

- Input: `root = [1, 2, 3, 4, 5]`
- Output: `3`

**Example 2**

- Input: `root = [50]`
- Output: `0`

**Example 3**

- Input: `root = [18, 73]`
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
