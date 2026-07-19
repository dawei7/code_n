# Reverse Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 206 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Linked List, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-linked-list/) |

## Problem Description
### Goal
Given the head of a singly linked list, reverse the direction of the chain so that nodes are encountered in the exact opposite order. The original final node becomes the new head, and each node's `next` pointer must lead to the node that previously preceded it.

Return the new head while reusing the existing nodes rather than constructing a separate list of copied values. The original head becomes the final node and must point to `null`, with every input node appearing exactly once in the reversed chain. An empty list returns `null`, and a one-node list returns the same node unchanged.

### Function Contract
**Inputs**

- `head`: the first node of a singly linked list

**Return value**

The new linked list head whose traversal yields the original values in reverse order.

### Examples
**Example 1**

- Input: `[1,2,3,4,5]`
- Output: `[5,4,3,2,1]`

**Example 2**

- Input: `[1,2]`
- Output: `[2,1]`

**Example 3**

- Input: `[]`
- Output: `[]`
