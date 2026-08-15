# Largest 3-Same-Digit Number in String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2264 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-3-same-digit-number-in-string/) |

## Problem Description

### Goal

The string `num` contains the decimal digits of a potentially large integer. A
good integer is any contiguous substring of exactly three characters whose
three digits are all identical.

Find the numerically largest good integer that occurs in `num` and return its
three-character representation. Leading zeroes are meaningful, so `"000"` is
a valid result and must remain three characters long. If no length-three
substring contains only one unique digit, return the empty string. Multiple or
overlapping occurrences of the same good integer do not change its value.

### Function Contract

**Inputs**

- `num`: A string of $n$ decimal digits, where $3\le n\le1000$.

**Return value**

Return the largest substring `ddd` for which three consecutive characters are
the same digit `d`, preserving `"000"` when zero is the best digit. Return `""`
when no such substring exists.

### Examples

#### Example 1

- **Input:** `num = "6777133339"`
- **Output:** `"777"`

#### Example 2

- **Input:** `num = "2300019"`
- **Output:** `"000"`

#### Example 3

- **Input:** `num = "42352338"`
- **Output:** `""`
