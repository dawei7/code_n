# Maximum Number of Ways to Partition an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2025 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Counting, Enumeration, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/) |

## Problem Description

### Goal

For an integer array `nums`, a pivot is an index from `1` through
`len(nums) - 1`. It partitions the array immediately before that index and is
valid when the sum of all elements on its left equals the sum of all elements
on its right.

You may replace one array element with `k`, or leave the array unchanged.
Return the largest number of valid pivots obtainable after this optional
single replacement.

### Function Contract

Let $N$ be the length of `nums`.

**Inputs**

- `nums`: a list of $N$ integers, where $2 \le N \le 10^5$ and each value is
  between $-10^5$ and $10^5$, inclusive.
- `k`: the replacement value, where $-10^5 \le k \le 10^5$.

**Return value**

- The maximum number of equal-sum pivot indices after changing at most one
  element to `k`.

### Examples

**Example 1**

- Input: `nums = [2, -1, 2], k = 3`
- Output: `1`
- Explanation: Replacing the first value produces `[3, -1, 2]`, whose pivot
  at index `2` has equal sums.

**Example 2**

- Input: `nums = [0, 0, 0], k = 1`
- Output: `2`
- Explanation: Leaving the array unchanged keeps both pivots valid.

**Example 3**

- Input: `nums = [22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], k = -33`
- Output: `4`
