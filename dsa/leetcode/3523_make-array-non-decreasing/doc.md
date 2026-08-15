# Make Array Non-decreasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3523 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Greedy, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-array-non-decreasing/) |

## Problem Description

### Goal

You are given an integer array `nums`. In one operation, choose any contiguous subarray and replace the entire chosen subarray with a single element whose value is the maximum value in that subarray. This shortens the array unless the chosen subarray has length one.

You may perform the operation any number of times, including zero. Among all arrays obtainable this way that are non-decreasing, return the maximum possible number of elements. Equal adjacent values are permitted in a non-decreasing result.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$.

The constraints are $1 \le n \le 2 \cdot 10^5$ and $1 \le \texttt{nums[i]} \le 2 \cdot 10^5$.

**Return value**

- The greatest achievable length of a non-decreasing array after zero or more allowed operations.

### Examples

#### Example 1

- **Input:** `nums = [4, 2, 5, 3, 5]`
- **Output:** `3`
- **Explanation:** Replace `[2, 5]` by `5`, producing `[4, 5, 3, 5]`; then replace `[3, 5]` by `5`, producing the non-decreasing array `[4, 5, 5]`.

#### Example 2

- **Input:** `nums = [1, 2, 3]`
- **Output:** `3`
- **Explanation:** The original array is already non-decreasing, so no operation is needed.
