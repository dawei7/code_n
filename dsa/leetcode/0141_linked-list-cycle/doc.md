# Linked List Cycle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 141 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/linked-list-cycle/) |

## Problem Description
### Goal
Given the head of a singly linked list, determine whether its pointer structure contains a cycle. A cycle exists when repeatedly following `next` links eventually reaches a node that has already been visited, rather than terminating at `null`.

Return `True` if any node participates in such a loop and `False` for an acyclic list. Nodes are identified by object identity, not by their stored values, so equal values at different positions do not create a cycle. Do not modify the linked list, and meet the constant-extra-memory follow-up. The app input encodes a possible tail link with `pos`, where `-1` means no cycle.

### Function Contract
**Inputs**

- `head`: linked list head, encoded in app cases as `{"values": [...], "pos": index}` where `pos = - 1` means no cycle and otherwise the tail links to that index

**Return value**

`True` when the list contains a cycle; otherwise `False`.

### Examples
**Example 1**

- Input: `values = [3,2,0,-4], pos = 1`
- Output: `True`

**Example 2**

- Input: `values = [1,2], pos = 0`
- Output: `True`

**Example 3**

- Input: `values = [1], pos = -1`
- Output: `False`
