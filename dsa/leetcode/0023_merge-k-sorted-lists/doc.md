# Merge k Sorted Lists

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 23 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) |

## Problem Description
### Goal
You are given an array containing `k` linked-list heads. Every linked list is sorted in ascending order, but different lists may contain equal values, have different lengths, or be empty. The array itself may also be empty.

Merge all linked lists into one list sorted in ascending order and return its head. Preserve every duplicate occurrence and omit no node. The app encodes lists as integer arrays for execution, while the native platform method reconnects the original linked-list nodes into the combined result.

### Function Contract
**Inputs**

- `lists`: `List[List[int]]`, with each inner list sorted in nondecreasing order

**Return value**

A sorted `List[int]` containing every input value with multiplicity preserved.

### Examples
**Example 1**

- Input: `lists = [[1, 4, 5], [1, 3, 4], [2, 6]]`
- Output: `[1, 1, 2, 3, 4, 4, 5, 6]`

**Example 2**

- Input: `lists = []`
- Output: `[]`

**Example 3**

- Input: `lists = [[]]`
- Output: `[]`
