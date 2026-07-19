# Sort List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 148 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-list/) |

## Problem Description
### Goal
Given the head of a linked list, sort it in ascending order. The result must contain the same nodes exactly once, including duplicates and negative values, and its final node must point to `null`.

Return the new head of the sorted chain, or `null` when the input list is empty. Meet the required $O(n \log n)$ running time and constant space target, which rules out quadratic comparison sorting and copying all values into a separate array. Sorting may change which original node becomes the head but must not replace the list with newly allocated value copies.

### Function Contract
**Inputs**

- `head`: linked list head, encoded as a list of integer values in app cases

**Return value**

The head node of the same linked-list nodes rearranged into sorted order.

### Examples
**Example 1**

- Input: `head = [4,2,1,3]`
- Output: `[1,2,3,4]`

**Example 2**

- Input: `head = [-1,5,3,4,0]`
- Output: `[-1,0,3,4,5]`

**Example 3**

- Input: `head = []`
- Output: `[]`
