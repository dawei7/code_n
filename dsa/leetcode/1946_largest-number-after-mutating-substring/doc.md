# Largest Number After Mutating Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1946 |
| Difficulty | Medium |
| Topics | Array, String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-number-after-mutating-substring/) |

## Problem Description
### Goal
The string `num` represents a nonnegative integer using decimal digits. A
length-10 array `change` defines a replacement for every digit: digit `d` maps
to `change[d]`.

You may choose at most one substring, meaning one contiguous sequence of
positions, and replace every digit in that substring according to the mapping.
You may also leave `num` unchanged. Return the string representing the largest
integer obtainable under those rules.

### Function Contract
**Inputs**

- `num`: a string of $N$ decimal digits, where
  $1 \le N \le 10^5$.
- `change`: an array of exactly 10 integers; `change[d]` is between 0 and 9
  for each original digit `d`.

**Return value**

- The numerically largest length-$N$ digit string obtainable by mutating zero
  or one contiguous substring of `num`.

### Examples
**Example 1**

- Input: `num = "132", change = [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]`
- Output: `"832"`

**Example 2**

- Input: `num = "021", change = [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]`
- Output: `"934"`

**Example 3**

- Input: `num = "5", change = [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]`
- Output: `"5"`
