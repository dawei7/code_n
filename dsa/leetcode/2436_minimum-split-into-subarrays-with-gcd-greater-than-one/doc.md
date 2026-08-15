# Minimum Split Into Subarrays With GCD Greater Than One

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2436 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Greedy, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Minimum Split Into Subarrays With GCD Greater Than One](https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. Divide it into one or more disjoint subarrays so that every input element belongs to exactly one part. Each part must be contiguous, and the greatest common divisor of all values in that part must be strictly greater than 1.

Among every partition satisfying those requirements, return the smallest possible number of subarrays. The greatest common divisor is the largest positive integer that divides every value in the selected subarray without a remainder.

### Function Contract

**Inputs**

- `nums`: A nonempty array whose values are all at least 2.

Its length $n$ satisfies $1 \le n \le 2000$, and every value is at most $10^9$. Let $V=\max(\texttt{nums})$.

**Return value**

- The minimum number of contiguous parts whose individual GCDs are greater than 1.

### Examples

#### Example 1

- **Input:** `nums = [12, 6, 3, 14, 8]`
- **Output:** `2`

The parts `[12, 6, 3]` and `[14, 8]` have GCDs 3 and 2.

#### Example 2

- **Input:** `nums = [4, 12, 6, 14]`
- **Output:** `1`

The GCD of the complete array is 2, so no split is necessary.

#### Example 3

- **Input:** `nums = [2, 3, 5, 7]`
- **Output:** `4`

Every adjacent extension would reduce the current GCD to 1, so every value forms its own part.
