# Numbers With Repeated Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1012 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/numbers-with-repeated-digits/) |

## Problem Description

### Goal

You are given a positive integer `n`. Consider every positive integer in the inclusive range `[1, n]` and its ordinary base-10 representation, without leading zeroes.

Return how many of those integers contain at least one repeated digit. A number qualifies when any decimal digit occurs in two or more positions; other digits may occur once or not at all. Count numbers, not the number of repeated positions within each number.

### Function Contract

**Inputs**

- `n`: the inclusive upper bound, where $1\le n\le10^9$.

Let $D$ be the number of decimal digits in `n`.

**Return value**

- The number of positive integers no greater than `n` that have at least one repeated decimal digit.

### Examples

**Example 1**

- Input: `n = 20`
- Output: `1`
- Explanation: Only `11` has a repeated digit.

**Example 2**

- Input: `n = 100`
- Output: `10`
- Explanation: The qualifying values are `11`, `22`, through `99`, plus `100`.

**Example 3**

- Input: `n = 1000`
- Output: `262`
