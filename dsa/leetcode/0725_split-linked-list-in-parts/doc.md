# Split Linked List in Parts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 725 |
| Difficulty | Medium |
| Topics | Linked List |
| Official Link | [LeetCode](https://leetcode.com/problems/split-linked-list-in-parts/) |

## Problem Description
### Goal
Given the head of a singly linked list and an integer `k`, split the list into exactly `k` consecutive linked-list parts while keeping nodes in their original order.

Make the part sizes as equal as possible, so no two sizes differ by more than one and every earlier part has size greater than or equal to every later part. Return an array containing the `k` part heads. When `k` exceeds the number of nodes, the remaining final parts are null.

### Function Contract
**Inputs**

- `head`: the first node of a singly linked list, or `None` for an empty list
- `k`: the positive number of parts to produce

**Return value**

- A list of `k` linked-list heads in original order; empty parts are represented by `None`

### Examples
**Example 1**

- Input: `head = [1,2,3], k = 5`
- Output: `[[1],[2],[3],[],[]]`

**Example 2**

- Input: `head = [1,2,3,4,5,6,7,8,9,10], k = 3`
- Output: `[[1,2,3,4],[5,6,7],[8,9,10]]`

**Example 3**

- Input: `head = [], k = 3`
- Output: `[[],[],[]]`
