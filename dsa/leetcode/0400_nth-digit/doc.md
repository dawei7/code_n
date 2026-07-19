# Nth Digit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 400 |
| Difficulty | Medium |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/nth-digit/) |

## Problem Description
### Goal
Write the positive integers consecutively without separators to form the infinite decimal sequence `123456789101112...`. Given a positive one-based position `n`, locate the digit occupying that position.

Return the digit as an integer from `0` through `9`. Positions count individual decimal characters rather than whole numbers, so a multi-digit integer contributes several consecutive positions. Skip complete blocks of one-digit, two-digit, and longer numbers arithmetically instead of constructing the enormous prefix string. Once the containing number is found, select the correct digit within its ordinary left-to-right representation.

### Function Contract
**Inputs**

- `n`: the one-based digit position in the concatenated positive-integer sequence

**Return value**

- Return the decimal digit at position `n` as an integer from `0` through `9`.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `3`

**Example 2**

- Input: `n = 11`
- Output: `0`

**Example 3**

- Input: `n = 190`
- Output: `1`
