# Maximum Number of Distinct Elements After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3397 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. For each array element, you may perform the following operation at most once: add any integer from the inclusive range `[-k, k]` to that element. Choosing zero leaves the element unchanged.

Select the adjustments to maximize the number of distinct values in the resulting array. Different elements may receive different adjustments, and an adjusted value may lie outside the original input-value range.

Return the largest achievable distinct-element count.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1\le n\le10^5$ and $1\le\texttt{nums[i]}\le10^9$.
- `k`: The maximum absolute adjustment, where $0\le k\le10^9$.

**Return value**

- The maximum number of distinct values obtainable after adjusting each element at most once.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 2, 3, 3, 4], k = 2`
- **Output:** `6`

One valid result is `[-1, 0, 1, 2, 3, 4]`, in which all six values are distinct.

#### Example 2

- **Input:** `nums = [4, 4, 4, 4], k = 1`
- **Output:** `3`

The available integer targets are 3, 4, and 5, so at most three of the four elements can contribute distinct values.
