# Sort Linked List Already Sorted Using Absolute Values

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2046 |
| Difficulty | Medium |
| Topics | Linked List, Two Pointers, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/) |

## Problem Description

### Goal

A nonempty singly linked list is already sorted in non-decreasing order by the
absolute values of its nodes. Thus, as the list is traversed, node magnitudes
never decrease, although their signed values may alternate between negative,
zero, and positive.

Rearrange the existing nodes so their actual signed values are in
non-decreasing order, and return the new head. The list may contain duplicate
values and equal absolute values. The follow-up requires a linear-time
solution, so comparison sorting is unnecessary.

### Function Contract

Let $N$ be the number of nodes.

**Inputs**

- `head`: the head of a singly linked list containing
  $1 \le N \le 10^5$ nodes.
- Every node value lies from $-5000$ through $5000$, and absolute values are
  non-decreasing along the input links.

**Return value**

- The head of the same nodes relinked in non-decreasing order by their signed
  values.

### Examples

**Example 1**

- Input: `head = [0, 2, -5, 5, 10, -10]`
- Output: `[-10, -5, 0, 2, 5, 10]`

**Example 2**

- Input: `head = [0, 1, 2]`
- Output: `[0, 1, 2]`
- Explanation: The actual values are already non-decreasing.

**Example 3**

- Input: `head = [1]`
- Output: `[1]`
