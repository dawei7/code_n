# Thousand Separator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1556 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/thousand-separator/) |

## Problem Description
### Goal

You are given a non-negative integer `n`. Write its ordinary base-ten representation, but use a dot (`.`) as the thousands separator.

Starting at the rightmost digit, place a dot between each adjacent group of three digits. The leftmost group may contain one, two, or three digits, and a value with at most three digits has no separator. Return the resulting representation as a string.

### Function Contract
**Inputs**

- `n`: An integer satisfying $0 \le n \le 2^{31} - 1$.
- Let $D$ be the number of decimal digits in `n`, counting `0` as one digit. The source bound guarantees $1 \le D \le 10$.

**Return value**

Return the decimal digits of `n` with a dot before every three-digit group measured from the right. Do not add leading zeros or a leading or trailing dot.

### Examples
**Example 1**

- Input: `n = 987`
- Output: `"987"`

**Example 2**

- Input: `n = 1234`
- Output: `"1.234"`

**Example 3**

- Input: `n = 123456789`
- Output: `"123.456.789"`
