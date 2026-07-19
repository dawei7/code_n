# Reverse Nodes in k-Group

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 25 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Linked List, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/) |

## Problem Description
### Goal
You are given a singly linked list and a positive group size `k`. Starting at the head, partition the node sequence into consecutive groups of up to `k` nodes and reverse the links inside every group that contains exactly `k` nodes.

Return the resulting head after reconnecting the reversed groups. A final group shorter than `k` must retain its original order. The operation changes node links rather than swapping stored values, uses each original node once, and preserves the group order along the list.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases
- `k`: positive `int` no larger than the list length

**Return value**

The grouped linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4, 5], k = 2`
- Output: `[2, 1, 4, 3, 5]`

**Example 2**

- Input: `head = [1, 2, 3, 4, 5], k = 3`
- Output: `[3, 2, 1, 4, 5]`

**Example 3**

- Input: `head = [1], k = 1`
- Output: `[1]`
