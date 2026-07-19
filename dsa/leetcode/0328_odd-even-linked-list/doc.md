# Odd Even Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 328 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/odd-even-linked-list/) |

## Problem Description
### Goal
Given the head of a singly linked list, group nodes by their one-based positions in the original chain. Place all nodes from odd positions first, followed by all nodes from even positions.

Preserve the original relative order within both groups, so positions `1, 3, 5, ...` remain ordered and positions `2, 4, 6, ...` remain ordered. This grouping concerns position parity, not whether node values are odd or even. Rewire and reuse the existing nodes in $O(n)$ time and $O(1)$ extra space, return the resulting head, and ensure the final node points to `null`.

### Function Contract
**Inputs**

- `head`: the first node of the linked list, represented by a value list in app cases

**Return value**

The head of the reordered list containing the original odd-position nodes followed by the original even-position nodes.

### Examples
**Example 1**

- Input: `head = [1,2,3,4,5]`
- Output: `[1,3,5,2,4]`

**Example 2**

- Input: `head = [2,1,3,5,6,4,7]`
- Output: `[2,3,6,7,1,5,4]`

**Example 3**

- Input: `head = []`
- Output: `[]`
