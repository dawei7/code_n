# Intersection of Two Linked Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 160 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Linked List, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/intersection-of-two-linked-lists/) |

## Problem Description
### Goal
Given the heads of two singly linked lists that contain no cycles, determine whether their pointer chains merge at a shared node. Intersection is based on object identity: equal values stored in separate nodes do not count. Once the two lists share one node, all following nodes form the same common tail.

Return the first shared node object, or `null` when the lists remain separate. Do not change either list's structure while searching. The two prefixes may have different lengths, either head may itself be the intersection, and the lists may be empty. App cases construct one shared tail and display the returned node through its suffix values, preserving the same identity-based contract.

### Function Contract
**Inputs**

- `head_a`: first `ListNode` head, encoded as `{"prefix": [...], "shared": [...]}` in app cases
- `head_b`: second `ListNode` head with its own prefix and the same shared-tail values; the runner constructs one shared tail object for both heads

**Return value**

The shared `ListNode`, displayed by the app as its suffix values, or a null result displayed as `[]` when the lists do not intersect.

### Examples
**Example 1**

- Input: prefixes `[4,1]` and `[5,6,1]`, shared tail `[8,4,5]`
- Output: `[8,4,5]`

**Example 2**

- Input: prefixes `[1,9,1]` and `[3]`, shared tail `[2,4]`
- Output: `[2,4]`

**Example 3**

- Input: prefixes `[2,6,4]` and `[1,5]`, shared tail `[]`
- Output: `[]`
