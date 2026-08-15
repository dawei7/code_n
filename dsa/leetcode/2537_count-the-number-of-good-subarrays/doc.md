# Count the Number of Good Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2537 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-the-number-of-good-subarrays](https://leetcode.com/problems/count-the-number-of-good-subarrays/) |

## Problem Description

### Goal

Given an integer array `nums` and a positive integer `k`, count its good subarrays. Within a candidate subarray `arr`, an index pair `(i, j)` contributes when $i < j$ and `arr[i] == arr[j]`; different pairs of positions count separately even when they contain the same value.

A subarray is good when it contains at least `k` such equal-value pairs. Because a subarray must be a non-empty contiguous sequence from `nums`, return the total number of choices of its left and right boundaries that meet this threshold.

### Function Contract

**Inputs**

- `nums`: A nonempty list of positive integers.
- `k`: The positive minimum number of equal-value index pairs required.

Let $n = \lvert\texttt{nums}\rvert$. The public constraints permit $n \leq 10^5$ and values of both `nums[i]` and `k` up to $10^9$.

**Return value**

Return the number of contiguous subarrays containing at least `k` pairs of equal values.

### Examples

#### Example 1

- **Input:** `nums = [1,1,1,1,1], k = 10`
- **Output:** `1`
- **Explanation:** Five equal elements create $\binom{5}{2}=10$ pairs, and only the full array reaches the threshold.

#### Example 2

- **Input:** `nums = [3,1,4,3,2,2,4], k = 2`
- **Output:** `4`
- **Explanation:** Four contiguous ranges contain at least two equal-value pairs.
