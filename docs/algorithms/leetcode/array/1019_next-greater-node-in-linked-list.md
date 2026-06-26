# Next Greater Node In Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1019 |
| Difficulty | Medium |
| Topics | Array, Linked List, Stack, Monotonic Stack |
| Official Link | [next-greater-node-in-linked-list](https://leetcode.com/problems/next-greater-node-in-linked-list/) |

## Problem Description & Examples
### Goal
For each node in a singly linked list, find the value of the next node to its right with a strictly larger value. Use `0` when no greater value exists.

### Function Contract
**Inputs**

- `head`: ListNode

**Return value**

List[int] - next greater value for each node position

### Examples
**Example 1**

- Input: `head = [2, 1, 5]`
- Output: `[5, 5, 0]`

**Example 2**

- Input: `head = [2, 7, 4, 3, 5]`
- Output: `[7, 0, 5, 5, 0]`

**Example 3**

- Input: `head = [1, 7, 5, 1, 9, 2, 5, 1]`
- Output: `[7, 9, 9, 9, 0, 5, 0, 0]`

---

## Underlying Base Algorithm(s)
Monotonic decreasing stack over list positions.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
