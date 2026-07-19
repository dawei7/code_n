# Non-negative Integers without Consecutive Ones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 600 |
| Difficulty | Hard |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/) |

## Problem Description
### Goal
Given a positive integer `n`, consider every non-negative integer in the inclusive range `[0, n]`. Inspect each integer's ordinary binary representation and determine whether it avoids consecutive ones—that is, whether no two adjacent bit positions are both `1`.

Return the number of integers in the range that satisfy this condition. The value `0` is included and is valid, while an integer such as binary `11` is invalid as soon as one adjacent pair of ones occurs. Count integer values, not distinct binary substrings or bit positions.

### Function Contract
**Inputs**

- `n: int`: a nonnegative upper bound

**Return value**

- The number of integers `x` with $0 \le x \le n$ and $x \mathbin{\&} (x \gg 1) = 0$

### Examples
**Example 1**

- Input: `n = 5`
- Output: `5`

**Example 2**

- Input: `n = 1`
- Output: `2`

**Example 3**

- Input: `n = 2`
- Output: `3`
