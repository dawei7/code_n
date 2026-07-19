# Base 7

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 504 |
| Difficulty | Easy |
| Topics | Math, String |
| Official Link | [LeetCode](https://leetcode.com/problems/base-7/) |

## Problem Description
### Goal
Given a signed decimal integer `num`, convert its magnitude to positional base 7, whose digits range from `0` through `6`. Preserve the numeric value rather than treating the decimal text as a sequence of characters to translate independently.

Return the base-7 representation as a string. Prefix a negative result with `-`, return exactly `"0"` when the input is zero, and omit leading zeroes for every nonzero value. The sign is not a base-7 digit, and the function returns text rather than a list of remainders or a decimal integer that resembles the converted digits.

### Function Contract
**Inputs**

- `num`: an integer in the supported range from $-10^{7}$ through $10^{7}$

**Return value**

- The conventional base-7 representation of `num`, with a leading `-` exactly when `num` is negative

### Examples
**Example 1**

- Input: `num = 100`
- Output: `"202"`

**Example 2**

- Input: `num = -7`
- Output: `"-10"`

**Example 3**

- Input: `num = 0`
- Output: `"0"`
