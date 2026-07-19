# Remove Nth Node From End of List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 19 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) |

## Problem Description
### Goal
You are given the head of a nonempty singly linked list and a positive integer `n` that does not exceed its length. Count positions backward from the tail, where the final node is position one, and remove the node at position `n`.

Reconnect its predecessor directly to its successor and return the resulting list head. Removing the original head must therefore return the next node, while removing the tail leaves its predecessor as the new final node. The operation removes exactly one node and preserves the relative order of every survivor.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases
- `n`: `int` in `[1, length(head)]`

**Return value**

The resulting linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4, 5], n = 2`
- Output: `[1, 2, 3, 5]`

**Example 2**

- Input: `head = [1], n = 1`
- Output: `[]`

**Example 3**

- Input: `head = [1, 2], n = 1`
- Output: `[1]`
