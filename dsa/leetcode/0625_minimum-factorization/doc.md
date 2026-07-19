# Minimum Factorization

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 625 |
| Difficulty | Medium |
| Topics | Math, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-factorization/) |

## Problem Description
### Goal
Given a positive integer `a`, find the smallest positive integer whose decimal digits have a product equal to `a`. The order of the output digits affects the numerical value, so among all valid digit factorizations you must return the numerically smallest one.

For an input smaller than `10`, the one-digit value itself is the smallest result. Otherwise, construct the answer from digit factors `2` through `9`. Return `0` if no such digit factorization exists or if the smallest valid result is greater than the maximum signed 32-bit integer, $2^{31} - 1$.

### Function Contract
**Inputs**

- `a`: a positive 32-bit integer

**Return value**

- The smallest integer whose decimal digits multiply to `a`
- An input below 10 is already its own smallest one-digit result
- Return `0` when no factorization into digits 2 through 9 exists or the smallest result exceeds $2^{31} - 1$

### Examples
**Example 1**

- Input: `a = 48`
- Output: `68`

**Example 2**

- Input: `a = 15`
- Output: `35`

**Example 3**

- Input: `a = 13`
- Output: `0`
