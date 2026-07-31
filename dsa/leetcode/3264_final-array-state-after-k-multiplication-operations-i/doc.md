# Final Array State After K Multiplication Operations I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3264 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/) |

## Problem Description

### Goal

Given an integer array `nums`, perform exactly `k` updates. For each update, find the array's current minimum value. If that minimum occurs at several positions, choose its first occurrence, meaning the smallest index.

Multiply the selected value by `multiplier` and store the product back at the same index. The next operation observes this modified array, so both the minimum value and the winning index may change. Return the array state after all `k` operations.

### Function Contract

**Inputs**

- `nums`: An integer list of length $n$, where $1 \le n \le 100$ and every value is between 1 and 100 inclusive.
- `k`: The number of operations, where $1 \le k \le 10$.
- `multiplier`: The positive factor used by every operation, where $1 \le \texttt{multiplier} \le 5$.

**Return value**

- The length-$n$ final array after exactly `k` minimum-selection and multiplication operations.

### Examples

**Example 1**

- Input: `nums = [2,1,3,5,6], k = 5, multiplier = 2`
- Output: `[8,4,6,5,6]`

The selected indices are 1, 0, 1, 2, and 0 as the minimum changes.

**Example 2**

- Input: `nums = [1,2], k = 3, multiplier = 4`
- Output: `[16,8]`

**Example 3**

- Input: `nums = [3,3,5], k = 2, multiplier = 1`
- Output: `[3,3,5]`

The first `3` is selected both times because multiplication by one leaves the tied minimum unchanged.
