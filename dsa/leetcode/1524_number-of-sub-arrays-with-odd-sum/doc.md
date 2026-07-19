# Number of Sub-arrays With Odd Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1524 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/) |

## Problem Description
### Goal

Given an integer array, count its nonempty contiguous subarrays whose element sum is odd. Subarrays are distinguished by their start and end indices, so equal values occurring in different positions still form different choices.

Because an array of length up to $10^5$ can contain quadratically many subarrays, the raw count may be large. Return the count modulo $10^9+7$ without enumerating every interval.

### Function Contract
**Inputs**

- `arr`: A list of $n$ integers with $1 \leq n \leq 10^5$.
- Every array value lies between 1 and 100, inclusive.

**Return value**

Return the number of nonempty contiguous subarrays whose sum is odd, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `arr = [1, 3, 5]`
- Output: `4`
- Explanation: The odd-sum intervals are the three singletons and the whole array.

**Example 2**

- Input: `arr = [2, 4, 6]`
- Output: `0`
- Explanation: Every possible sum is even.

**Example 3**

- Input: `arr = [1, 2, 3, 4, 5, 6, 7]`
- Output: `16`
