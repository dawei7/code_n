# Palindrome Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 234 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Linked List, Two Pointers, Stack, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-linked-list/) |

## Problem Description
### Goal
Given the head of a singly linked list, consider the sequence of values encountered by following its `next` pointers. Determine whether that sequence is identical when read from the first node to the last and from the last node back to the first.

Return `True` for a palindromic value sequence and `False` otherwise. Node identity does not need to mirror—only corresponding stored values must match. A one-node list is a palindrome. Meet the follow-up target of $O(n)$ time and $O(1)$ space rather than copying all node values into another data structure. The function returns only the boolean classification, not a reversed list or the matching node pairs.

### Function Contract
**Inputs**

- `head`: the head of a singly linked list

**Return value**

`True` when the sequence of node values is a palindrome; otherwise `False`.

### Examples
**Example 1**

- Input: `head = [1, 2, 2, 1]`
- Output: `True`

**Example 2**

- Input: `head = [1, 2]`
- Output: `False`

**Example 3**

- Input: `head = [7]`
- Output: `True`
