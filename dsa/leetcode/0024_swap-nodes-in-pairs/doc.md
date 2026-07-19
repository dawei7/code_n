# Swap Nodes in Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 24 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/) |

## Problem Description
### Goal
Given the head of a singly linked list, divide its nodes from the front into consecutive pairs. Reverse the order inside every complete pair: the first node should follow the second, the third should follow the fourth, and so on.

Return the head after all pair swaps. The links between actual nodes must change; exchanging only their stored values is not allowed. If the list length is odd, the final node has no partner and remains after all swapped pairs. Empty and one-node lists are unchanged.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases

**Return value**

The swapped linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4]`
- Output: `[2, 1, 4, 3]`

**Example 2**

- Input: `head = []`
- Output: `[]`

**Example 3**

- Input: `head = [1, 2, 3]`
- Output: `[2, 1, 3]`
