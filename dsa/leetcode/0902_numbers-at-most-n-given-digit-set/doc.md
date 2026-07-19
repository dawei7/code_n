# Numbers At Most N Given Digit Set

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 902 |
| Difficulty | Hard |
| Topics | Array, Math, String, Binary Search, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) |

## Problem Description
### Goal
You are given an array `digits` of distinct one-character digits sorted in non-decreasing order. Every entry is between `"1"` and `"9"`, so no generated positive integer has a leading-zero issue.

Form positive integers by choosing characters from `digits`, with each available digit usable as many times as desired. The number of chosen positions is not fixed.

Given the positive integer `n`, return how many constructible positive integers are less than or equal to `n`.

### Function Contract
Let $k=\lvert\texttt{digits}\rvert$ and let $d$ be the number of decimal digits in `n`.

**Inputs**

- `digits`: $k$ unique digit strings, sorted in non-decreasing order, where $1 \leq k \leq 9$.
- `n`: an integer with $1 \leq n \leq 10^9$.

**Return value**

Return the count of positive integers no greater than `n` whose every decimal digit belongs to `digits`.

### Examples
**Example 1**

- Input: `digits = ["1","3","5","7"], n = 100`
- Output: `20`

All one- and two-digit choices are valid, giving $4+4^2=20$ numbers.

**Example 2**

- Input: `digits = ["1","4","9"], n = 1000000000`
- Output: `29523`

**Example 3**

- Input: `digits = ["7"], n = 8`
- Output: `1`
