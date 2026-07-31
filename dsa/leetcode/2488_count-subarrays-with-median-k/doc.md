# Count Subarrays With Median K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2488 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-subarrays-with-median-k/) |

## Problem Description

### Goal

Given an array `nums` of length $n$ containing distinct integers from $1$ through $n$, and a positive integer `k` that occurs in the array, count the nonempty contiguous subarrays whose median is exactly `k`.

To obtain a median, sort the selected subarray in ascending order. For an odd length, use its single middle element; for an even length, use the left of the two middle elements, which is the smaller one. Only contiguous ranges count as subarrays, and a qualifying range must contain `k` because all values are distinct.

### Function Contract

**Inputs**

- `nums`: A permutation of the integers from $1$ through $n$.
- `k`: A value in `nums` whose median occurrences must be counted.

The constraints satisfy $1 \le n \le 10^5$ and $1 \le \texttt{k} \le n$.

**Return value**

Return the number of nonempty contiguous subarrays of `nums` whose median, under the left-middle rule for even lengths, equals `k`.

### Examples

**Example 1**

- Input: `nums = [3, 2, 1, 4, 5], k = 4`
- Output: `3`
- Explanation: The qualifying ranges are `[4]`, `[4, 5]`, and `[1, 4, 5]`.

**Example 2**

- Input: `nums = [2, 3, 1], k = 3`
- Output: `1`
- Explanation: Only the one-element subarray `[3]` has median `3`.
