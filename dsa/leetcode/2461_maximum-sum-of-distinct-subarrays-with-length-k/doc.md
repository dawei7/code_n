# Maximum Sum of Distinct Subarrays With Length K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2461 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. Consider every subarray whose length is exactly $k$. A subarray is a contiguous, non-empty sequence of elements from the array.

A candidate subarray is valid only when all of its elements are distinct. Return the maximum sum among all valid length-$k$ subarrays. If no candidate contains $k$ distinct values, return `0`.

### Function Contract

**Inputs**

- `nums`: A list of positive integers.
- `k`: The required subarray length.

The constraints are $1\le k\le\lvert\texttt{nums}\rvert\le10^5$ and $1\le\texttt{nums[i]}\le10^5$.

**Return value**

- The greatest sum of a length-$k$ subarray with pairwise distinct elements, or `0` if none exists.

### Examples

#### Example 1

- **Input:** `nums = [1, 5, 4, 2, 9, 9, 9], k = 3`
- **Output:** `15`
- **Explanation:** The valid windows have sums `10`, `11`, and `15`; later windows repeat `9`.

#### Example 2

- **Input:** `nums = [4, 4, 4], k = 3`
- **Output:** `0`
- **Explanation:** The only length-three subarray repeats the value `4`.
