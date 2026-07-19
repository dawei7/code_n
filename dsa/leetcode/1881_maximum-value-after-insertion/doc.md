# Maximum Value after Insertion

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-value-after-insertion/) |
| Frontend ID | 1881 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A possibly negative integer `n` is supplied as a decimal string because it may contain as many as $10^5$ characters. Its digits, and a separate digit `x`, are all from `1` through `9`.

Insert exactly one copy of `x` somewhere among the decimal digits so that the represented integer is as large as possible. For a negative number, insertion may occur after the leading `'-'` but never before it. Preserve every original digit in its original relative order and return the maximizing representation as a string.

### Function Contract

**Inputs**

- `n`: a valid positive or negative integer string with at most $10^5$ characters; every decimal digit is from `1` through `9`.
- `x`: an integer digit satisfying $1 \le x \le 9$.

**Return value**

- Return the decimal string obtained by inserting `x` exactly once at the position that maximizes the represented integer.

### Examples

**Example 1**

- Input: `n = "99", x = 9`
- Output: `"999"`

All insertion positions produce the same representation.

**Example 2**

- Input: `n = "-13", x = 2`
- Output: `"-123"`

Among `"-213"`, `"-123"`, and `"-132"`, the middle value is greatest.

**Example 3**

- Input: `n = "73", x = 6`
- Output: `"763"`

Placing `6` before the first smaller digit `3` gives the largest result.
