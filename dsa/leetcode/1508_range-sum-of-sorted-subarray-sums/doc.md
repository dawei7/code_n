# Range Sum of Sorted Subarray Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1508 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sorting, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/) |

## Problem Description
### Goal

Given an array `nums` of $n$ positive integers, form the sum of every non-empty continuous subarray. There are $n(n+1)/2$ such sums. Sort this multiset in non-decreasing order, preserving duplicate values as separate entries.

Return the sum of the entries at 1-indexed positions `left` through `right`, inclusive. Because the result may be large, return it modulo $10^9+7$.

### Function Contract
**Inputs**

Let $S = \sum \texttt{nums[i]}$.

- `nums`: A non-empty array of positive integers.
- `n`: The length of `nums`.
- `left`, `right`: Inclusive 1-indexed positions satisfying $1 \leq \texttt{left} \leq \texttt{right} \leq n(n+1)/2$.

**Return value**

Return the sum of sorted subarray-sum ranks `left` through `right`, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4], n = 4, left = 1, right = 5`
- Output: `13`
- Explanation: The sorted sums begin `[1, 2, 3, 3, 4]`, whose total is 13.

**Example 2**

- Input: `nums = [1, 2, 3, 4], n = 4, left = 3, right = 4`
- Output: `6`

**Example 3**

- Input: `nums = [1, 2, 3, 4], n = 4, left = 1, right = 10`
- Output: `50`
