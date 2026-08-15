# Smallest Value of the Rearranged Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2165 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-value-of-the-rearranged-number/) |

## Problem Description

### Goal

Rearrange all decimal digits of an integer `num` to produce the smallest
possible numeric value. Every digit occurrence must be used exactly once, and
the rearranged representation may not begin with zero unless the number itself
is zero.

The sign is fixed: a positive input must remain positive, a negative input must
remain negative, and zero remains zero. For a negative number, making the
signed result smaller therefore means maximizing the magnitude formed by its
digits.

### Function Contract

**Inputs**

- `num`: an integer satisfying $-10^{15}\le\texttt{num}\le 10^{15}$.

The minus sign is not a digit and cannot be moved or changed.

**Return value**

Return the smallest signed integer obtainable by permuting every decimal digit
of `num` without a leading zero.

### Examples

#### Example 1

- **Input:** `num = 310`
- **Output:** `103`

Ascending digits would begin with zero, so the smallest nonzero digit is placed
first and the zero follows it.

#### Example 2

- **Input:** `num = -7605`
- **Output:** `-7650`

Descending magnitude digits form `7650`; applying the preserved negative sign
makes this the smallest value.

#### Example 3

- **Input:** `num = 0`
- **Output:** `0`

Zero has one digit and its only rearrangement is itself.
