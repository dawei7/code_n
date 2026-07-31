# Minimum Right Shifts to Sort the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2855 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` containing distinct positive integers. A right shift moves every element formerly at index $i$ to index $(i + 1) \bmod n$, so the last element wraps around to index $0$.

Find the minimum number of right shifts that makes `nums` sorted in increasing order. Return `-1` when no cyclic shift of the array can produce that order. An array that is already sorted requires zero shifts.

### Function Contract

**Inputs**

- `nums`: An array of distinct positive integers.

Let $n = \lvert\texttt{nums}\rvert$. The constraints guarantee $1 \le n \le 100$ and $1 \le \texttt{nums[i]} \le 100$.

**Return value**

The minimum number of cyclic right shifts needed to sort `nums`, or `-1` if no such shift exists.

### Examples

**Example 1**

- Input: `nums = [3, 4, 5, 1, 2]`
- Output: `2`

Two right shifts produce `[1, 2, 3, 4, 5]`.

**Example 2**

- Input: `nums = [1, 3, 5]`
- Output: `0`

The input is already sorted.

**Example 3**

- Input: `nums = [2, 1, 4]`
- Output: `-1`

None of its cyclic rotations is sorted.
