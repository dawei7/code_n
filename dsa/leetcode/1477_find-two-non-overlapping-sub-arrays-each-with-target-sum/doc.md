# Find Two Non-overlapping Sub-arrays Each With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1477 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/) |

## Problem Description
### Goal

Given a positive-integer array `arr` and a positive integer `target`, choose two contiguous subarrays whose sums are both exactly `target`. The chosen index intervals must be non-overlapping; adjacency is allowed, but no array position may belong to both.

Several valid pairs may exist. Minimize the sum of the two subarray lengths and return that minimum. Return `-1` if fewer than two mutually non-overlapping target-sum subarrays exist, even when the array contains several target-sum subarrays that overlap one another.

### Function Contract
**Inputs**

Let $N$ be the length of `arr`.

- `arr`: a positive-integer array with $1 \le N \le 10^5$.
- Every element satisfies $1 \le \texttt{arr[i]} \le 1000$.
- `target`: the required sum for each selected subarray, where $1 \le \texttt{target} \le 10^8$.

**Return value**

Return the minimum possible combined length of two non-overlapping contiguous subarrays whose sums each equal `target`. Return `-1` when no such pair exists.

### Examples
**Example 1**

- Input: `arr = [3,2,2,4,3], target = 3`
- Output: `2`
- Explanation: The two singleton subarrays containing `3` are disjoint and have total length two.

**Example 2**

- Input: `arr = [7,3,4,7], target = 7`
- Output: `2`
- Explanation: Target-sum subarrays `[7]`, `[3,4]`, and `[7]` exist. Choosing the two singleton endpoint subarrays gives the smallest combined length.

**Example 3**

- Input: `arr = [4,3,2,6,2,3,4], target = 6`
- Output: `-1`
- Explanation: Only the singleton `[6]` sums to the target, so no pair can be formed.
