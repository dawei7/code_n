# Find Greatest Common Divisor of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1979 |
| Difficulty | Easy |
| Topics | Array, Math, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) |

## Problem Description
### Goal
Given an integer array `nums`, identify its smallest value and its largest
value. Return the greatest common divisor of those two endpoints.

The greatest common divisor is the largest positive integer that divides both
endpoint values without a remainder. Values between the minimum and maximum
do not otherwise affect the requested result. The array contains only positive
integers and may include repeated values at either endpoint.

### Function Contract
**Inputs**

- `nums`: a list of $N$ positive integers, where $2 \le N \le 1000$.
- Every value is in the inclusive range from `1` through `1000`.
- Let $M=\max(\texttt{nums})$.

**Return value**

- $\gcd(\min(\texttt{nums}),\max(\texttt{nums}))$.

### Examples
**Example 1**

- Input: `nums = [2, 5, 6, 9, 10]`
- Output: `2`

**Example 2**

- Input: `nums = [7, 5, 6, 8, 3]`
- Output: `1`

**Example 3**

- Input: `nums = [3, 3]`
- Output: `3`
