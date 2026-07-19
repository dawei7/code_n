# Ugly Number III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1201 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Binary Search, Combinatorics, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ugly-number-iii/) |

## Problem Description

### Goal

For this problem, an ugly number is any positive integer divisible by at least one of the three given integers `a`, `b`, or `c`. Divisibility by more than one of them still identifies a single number in the ordered sequence.

Given `n` and the three divisors, return the $n$th ugly number in increasing order. The result is guaranteed to exist between 1 and $2\times10^9$, inclusive.

### Function Contract

**Inputs**

- `n`: The 1-indexed position, where $1\le n\le10^9$.
- `a`, `b`, and `c`: Positive divisors, each at most $10^9$, with $1\le abc\le10^{18}$.
- Let $U=2\times10^9$, the guaranteed upper bound on the answer.

**Return value**

- The $n$th positive integer divisible by `a`, `b`, or `c`.

### Examples

**Example 1**

- Input: `n = 3`, `a = 2`, `b = 3`, `c = 5`
- Output: `4`

The sequence begins `2,3,4,5,6,8,...`.

**Example 2**

- Input: `n = 4`, `a = 2`, `b = 3`, `c = 4`
- Output: `6`

**Example 3**

- Input: `n = 5`, `a = 2`, `b = 11`, `c = 13`
- Output: `10`
