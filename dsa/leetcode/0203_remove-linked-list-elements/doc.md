# Remove Linked List Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 203 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Linked List, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-linked-list-elements/) |

## Problem Description
### Goal
Given the head of a singly linked list and an integer `val`, remove every node whose stored value equals `val`. Matching nodes may occur at the beginning, middle, or end of the chain, and several matching occurrences may be consecutive.

Return the head of the filtered list after reconnecting the retained nodes in their original relative order. Reuse the existing nonmatching nodes rather than returning only their values, and ensure the final retained node points to `null`. If the original head is removed, the head must advance appropriately; if every node matches or the input is empty, return `null`.

### Function Contract
**Inputs**

- `head`: the first node of a singly linked list
- `val`: the value to remove

**Return value**

The head of the filtered linked list, preserving the relative order of retained nodes.

### Examples
**Example 1**

- Input: `head = [1,2,6,3,4,5,6], val = 6`
- Output: `[1,2,3,4,5]`

**Example 2**

- Input: `head = [], val = 1`
- Output: `[]`

**Example 3**

- Input: `head = [7,7,7], val = 7`
- Output: `[]`
