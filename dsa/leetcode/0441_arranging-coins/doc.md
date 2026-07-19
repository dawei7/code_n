# Arranging Coins

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 441 |
| Difficulty | Easy |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/arranging-coins/) |

## Problem Description
### Goal
Given a positive number of coins `n`, build a staircase whose first row uses one coin, second row uses two, and row `r` uses exactly `r` coins. Rows must be completed in order from the first onward.

Return the greatest number of complete rows that can be built. Any remaining coins insufficient for the next full row are ignored, and no earlier row may be shortened to complete a later one. Equivalently, find the largest integer `k` whose triangular total $k \cdot (k + 1) / 2$ does not exceed `n`, using arithmetic that avoids overflow.

### Function Contract
**Inputs**

- `n`: the positive number of available coins

**Return value**

- Return the greatest integer `k` such that the first `k` rows require no more than `n` coins.

### Examples
**Example 1**

- Input: `n = 5`
- Output: `2`

**Example 2**

- Input: `n = 8`
- Output: `3`

**Example 3**

- Input: `n = 1`
- Output: `1`
