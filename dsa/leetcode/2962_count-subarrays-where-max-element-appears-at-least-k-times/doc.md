# Count Subarrays Where Max Element Appears at Least K Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2962 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/) |

## Problem Description
### Goal
You are given an integer array `nums` and a positive integer `k`. Identify the
maximum value of the complete array.

Count the subarrays in which that global maximum occurs at least `k` times. A
subarray is a contiguous, non-empty sequence of `nums`; it cannot skip or
reorder elements. Different start or end indices define different subarrays,
even when their value sequences happen to match.

### Function Contract
**Inputs**

- `nums`: the integer array whose contiguous subarrays are counted
- `k`: the minimum required frequency of the complete array's maximum value

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$1\le N\le10^5$, $1\le\texttt{nums[i]}\le10^6$, and $1\le k\le10^5$.

**Return value**

The number of contiguous subarrays containing the global maximum of `nums` at
least `k` times.

### Examples
**Example 1**

- Input: `nums = [1,3,2,3,3], k = 2`
- Output: `6`
- Explanation: Six ranges contain the global maximum `3` at least twice, including `[1,3,2,3]`, `[3,2,3]`, and `[3,3]`.

**Example 2**

- Input: `nums = [1,4,2,1], k = 3`
- Output: `0`
- Explanation: The global maximum `4` occurs only once in the entire array, so no subarray can contain it three times.
