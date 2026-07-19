# Counting Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 338 |
| Difficulty | Easy |
| Topics | Dynamic Programming, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/counting-bits/) |

## Problem Description
### Goal
Given a nonnegative integer `n`, consider every integer from `0` through `n` in increasing order. For each value, count the positions containing `1` in its ordinary binary representation.

Return a list of length $n + 1$ whose entry at index `i` is the set-bit count for `i`. Thus the first entry is always zero, and each input value contributes exactly one output count. Compute the full list in linear time $O(n)$, possibly in a single pass, without using a built-in bit-count function. Reuse relationships among smaller binary values instead of independently inspecting every bit of every integer.

### Function Contract
**Inputs**

- `n`: a non-negative integer

**Return value**

- A list of $n + 1$ integers where result index `i` contains the number of `1` bits in `i`.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `[0, 1, 1]`
- Explanation: `0`, `1`, and `2` are `0`, `1`, and `10` in binary.

**Example 2**

- Input: `n = 5`
- Output: `[0, 1, 1, 2, 1, 2]`

**Example 3**

- Input: `n = 0`
- Output: `[0]`
