# Find Target Indices After Sorting Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2089 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-target-indices-after-sorting-array/) |

## Problem Description

### Goal

You are given a zero-indexed integer array `nums` and an integer `target`. Imagine sorting `nums` in non-decreasing order. An index is a target index when the value at that position in the sorted array equals `target`.

Return every target index in increasing order. Repeated target values produce one index for each occurrence, while a target absent from the array produces an empty list. The original positions of the values do not affect the answer.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 100$.
- `target`: the value to locate after sorting.
- Every element of `nums` and `target` is between $1$ and $100$.

Let $k$ be the number of occurrences of `target` in `nums`.

**Return value**

Return the $k$ indices occupied by `target` after non-decreasing sorting, listed in increasing order.

### Examples

**Example 1**

- Input: `nums = [1, 2, 5, 2, 3]`, `target = 2`
- Output: `[1, 2]`
- Explanation: The sorted array is `[1, 2, 2, 3, 5]`.

**Example 2**

- Input: `nums = [1, 2, 5, 2, 3]`, `target = 3`
- Output: `[3]`

**Example 3**

- Input: `nums = [1, 2, 5, 2, 3]`, `target = 5`
- Output: `[4]`
