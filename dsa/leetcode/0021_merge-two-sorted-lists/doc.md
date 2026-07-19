# Merge Two Sorted Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 21 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Linked List, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/) |

## Problem Description
### Goal
You are given the heads of two linked lists whose node values are sorted in ascending order. Either list may be empty, and equal values may occur within one list or across both lists.

Merge the two lists into one list sorted in ascending order and return its head. Every input node must appear exactly once in the result, with duplicate values preserved. Form the merged list by splicing together the nodes of the two input lists rather than replacing their values or allocating a new node for every element.

### Function Contract
**Inputs**

- `list1`: `ListNode` linked list head, encoded as `List[int]` in app cases
- `list2`: `ListNode` linked list head, encoded as `List[int]` in app cases

**Return value**

The merged linked list head, normalized to `List[int]` by the app.

### Examples
**Example 1**

- Input: `list1 = [1, 2, 4], list2 = [1, 3, 4]`
- Output: `[1, 1, 2, 3, 4, 4]`

**Example 2**

- Input: `list1 = [], list2 = []`
- Output: `[]`

**Example 3**

- Input: `list1 = [], list2 = [0]`
- Output: `[0]`
