# Count Numbers with Unique Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 357 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/count-numbers-with-unique-digits/) |

## Problem Description
### Goal
Given an integer `n` from `0` through `8`, consider every integer `x` in the half-open range $0 \le x < 10^{n}$. An integer has unique digits when no decimal digit repeats in its usual representation.

Return the number of integers in the range that have unique digits. Leading zeroes are not written and therefore are not extra repeated digits, while the integer `0` itself counts as a valid one-digit value. For $n = 0$, the range contains only the conventionally counted zero case and returns `1`. Count numerical values rather than fixed-width strings padded to `n` positions.

### Function Contract
**Inputs**

- `n`: the number of available decimal positions, with $0 \le n \le 8$

**Return value**

- The number of integers below $10^{n}$ with pairwise distinct decimal digits.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `91`

**Example 2**

- Input: `n = 0`
- Output: `1`

**Example 3**

- Input: `n = 1`
- Output: `10`
