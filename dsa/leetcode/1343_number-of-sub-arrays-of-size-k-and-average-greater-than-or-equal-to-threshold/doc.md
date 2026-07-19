# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1343 |
| Difficulty | Medium |
| Topics | Array, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) |

## Problem Description
### Goal
Given an integer array `arr`, examine every contiguous subarray containing exactly `k` elements. A window qualifies when the arithmetic average of its elements is greater than or equal to `threshold`.

Return the number of qualifying windows. Overlapping subarrays are counted separately, the comparison is inclusive, and a non-integer average must be compared at its actual value rather than after rounding or integer division.

### Function Contract
**Inputs**

- `arr`: a positive-integer array of length $n$, where $1\le n\le10^5$ and $1\le\texttt{arr[i]}\le10^4$.
- `k`: the exact window length, where $1\le k\le n$.
- `threshold`: the minimum permitted average, where $0\le\texttt{threshold}\le10^4$.

**Return value**

The number of length-`k` contiguous subarrays whose average is at least `threshold`.

### Examples
**Example 1**

- Input: `arr = [2,2,2,2,5,5,5,8]`, `k = 3`, `threshold = 4`
- Output: `3`

**Example 2**

- Input: `arr = [11,13,17,23,29,31,7,5,2,3]`, `k = 3`, `threshold = 5`
- Output: `6`
- Explanation: Averages need not be integers.

**Example 3**

- Input: `arr = [1,1,1,1]`, `k = 2`, `threshold = 2`
- Output: `0`
