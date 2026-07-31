# Find the K-Beauty of a Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2269 |
| Difficulty | Easy |
| Topics | Math, String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-k-beauty-of-a-number/) |

## Problem Description

### Goal

Read the positive integer `num` as its decimal string. Its $k$-beauty is the
number of contiguous substrings of exactly $k$ digits whose numeric value is a
divisor of `num`.

Leading zeroes inside a substring are allowed when interpreting its value, so
`"04"` represents $4$ and `"00"` represents $0$. Zero never counts because it
is not a divisor of any value. Count occurrences by position: two identical
qualifying substrings at different positions both contribute.

Given `num` and `k`, return the $k$-beauty of `num`.

### Function Contract

**Inputs**

- `num`: An integer satisfying $1\le\texttt{num}\le10^9$.
- `k`: A window length satisfying $1\le k\le d$, where $d$ is the number of decimal digits in `num`.

**Return value**

Return the number of length-$k$ decimal substrings whose nonzero numeric value
divides `num` without a remainder.

### Examples

**Example 1**

- Input: `num = 240, k = 2`
- Output: `2`

Both `"24"` and `"40"` divide $240$.

**Example 2**

- Input: `num = 430043, k = 2`
- Output: `2`

The two occurrences of `"43"` qualify. `"30"` and `"04"` do not divide the
number, while `"00"` represents zero and is excluded.
