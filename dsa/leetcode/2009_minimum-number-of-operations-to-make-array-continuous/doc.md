# Minimum Number of Operations to Make Array Continuous

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2009 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Binary Search, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/) |

## Problem Description

### Goal

In one operation, choose any position in the integer array `nums` and replace
its value with any integer.

An array of length $N$ is continuous only when all its elements are unique and
the difference between its maximum and minimum equals $N-1$. These conditions
mean its values form every integer in one interval of length $N$, although
their array order is irrelevant. Determine the minimum number of replacements
needed to make `nums` continuous.

### Function Contract

**Inputs**

- `nums`: a list of $N$ integers, where $1\le N\le10^5$ and
  $1\le\texttt{nums[i]}\le10^9$.

**Return value**

Return the smallest number of array positions whose values must be replaced.

### Examples

**Example 1**

- Input: `nums = [4, 2, 5, 3]`
- Output: `0`
- Explanation: The four unique values already span from $2$ through $5$.

**Example 2**

- Input: `nums = [1, 2, 3, 5, 6]`
- Output: `1`
- Explanation: Replacing `6` with `4` produces one continuous interval.

**Example 3**

- Input: `nums = [1, 10, 100, 1000]`
- Output: `3`
- Explanation: Keep `1` and replace the other positions with `2`, `3`, and
  `4`.
