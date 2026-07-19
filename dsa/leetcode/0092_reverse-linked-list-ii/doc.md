# Reverse Linked List II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 92 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-linked-list-ii/) |

## Problem Description
### Goal
You are given a singly linked list and two valid one-based positions `left` and `right`, with `left <= right`. Reverse the order of the nodes in that inclusive segment by changing their links.

Return the possibly changed head after reconnecting the reversed segment to the untouched prefix and suffix. Nodes outside the interval retain their original order, and node values must not be exchanged as a substitute for relinking. When both positions are equal, the list remains unchanged.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as `List[int]` in app cases
- `left`: first one-based position to reverse
- `right`: final one-based position to reverse

**Return value**

The resulting linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `head = [1,2,3,4,5], left = 2, right = 4`
- Output: `[1,4,3,2,5]`

**Example 2**

- Input: `head = [5], left = 1, right = 1`
- Output: `[5]`

**Example 3**

- Input: `head = [1,2,3], left = 1, right = 3`
- Output: `[3,2,1]`
