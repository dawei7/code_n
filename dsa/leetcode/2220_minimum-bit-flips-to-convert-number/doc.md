# Minimum Bit Flips to Convert Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2220 |
| Difficulty | Easy |
| Topics | Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/) |

## Problem Description
### Goal

A bit flip chooses one position in an integer's binary representation and changes that bit from `0` to `1` or from `1` to `0`. Positions in the leading-zero region may also be chosen, even though those zeros are not normally displayed.

Given nonnegative integers `start` and `goal`, determine the minimum number of individual bit flips needed to transform `start` into `goal`.

### Function Contract
**Inputs**

- `start`: The nonnegative integer to transform.
- `goal`: The desired nonnegative integer.

Both values are at most $10^9$ and therefore use at most 30 relevant binary positions.

**Return value**

Return the minimum number of bit positions whose values must be changed.

### Examples
**Example 1**

- Input: `start = 10, goal = 7`
- Output: `3`

**Example 2**

- Input: `start = 3, goal = 4`
- Output: `3`

**Example 3**

- Input: `start = 42, goal = 21`
- Output: `6`
