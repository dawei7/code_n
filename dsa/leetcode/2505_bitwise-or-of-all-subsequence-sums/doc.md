# Bitwise OR of All Subsequence Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2505 |
| Difficulty | Medium |
| Topics | Array, Math, Bit Manipulation, Brainteaser, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/) |

## Problem Description
### Goal
You are given an integer array `nums`. A subsequence is obtained by deleting zero or more elements while preserving the relative order of the elements that remain. The empty subsequence is permitted and has sum $0$.

Consider the sum of every possible subsequence. Combine all of those sums with the bitwise OR operation and return the resulting integer. Different subsequences may have the same sum; duplicates do not change the OR.

### Function Contract
**Inputs**

- `nums`: A list of $n$ nonnegative integers, where $1\le n\le10^5$ and $0\le\texttt{nums[i]}\le10^9$.

**Return value**

An integer equal to the bitwise OR of every achievable subsequence sum.

### Examples
**Example 1**

- Input: `nums = [2,1,0,3]`
- Output: `7`
- Explanation: The achievable sums include every value from $0$ through $6$, whose bitwise OR is $7$.

**Example 2**

- Input: `nums = [0,0,0]`
- Output: `0`
- Explanation: Every subsequence has sum $0$.

**Example 3**

- Input: `nums = [4,4]`
- Output: `12`
- Explanation: The distinct sums are $0$, $4$, and $8$, and $4\mathbin{|}8=12$.
