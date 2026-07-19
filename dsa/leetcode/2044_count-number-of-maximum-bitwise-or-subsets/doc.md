# Count Number of Maximum Bitwise-OR Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2044 |
| Difficulty | Medium |
| Topics | Array, Backtracking, Bit Manipulation, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/) |

## Problem Description

### Goal

Choose any nonempty subset of the integer array `nums` and compute the bitwise
OR of its selected elements. A subset is determined by selected indices, so
equal values at different indices still create different subsets.

Find the greatest bitwise OR attainable by any subset, then return how many
different nonempty index subsets attain that value. Selected indices need not
be adjacent, and their original relative order is preserved within a subset.

### Function Contract

Let $N$ be the length of `nums`.

**Inputs**

- `nums`: an array of positive integers with $1 \le N \le 16$ and
  $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- The number of nonempty index subsets whose bitwise OR equals the maximum
  possible subset OR.

### Examples

**Example 1**

- Input: `nums = [3, 1]`
- Output: `2`
- Explanation: Subsets selecting `[3]` and `[3, 1]` both have OR `3`.

**Example 2**

- Input: `nums = [2, 2, 2]`
- Output: `7`
- Explanation: Every one of the $2^3-1$ nonempty index subsets has OR `2`.

**Example 3**

- Input: `nums = [3, 2, 1, 5]`
- Output: `6`
