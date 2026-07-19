# Number of Substrings With Only 1s

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1513 |
| Difficulty | Medium |
| Topics | Math, String |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-substrings-with-only-1s/) |

## Problem Description
### Goal

Given a binary string `s`, count its non-empty substrings whose every character is `1`. Substrings are contiguous ranges of positions, and equal text occurring at different ranges counts separately.

A `0` cannot belong to a qualifying substring and therefore separates independent runs of `1` characters. Return the total number of qualifying ranges modulo $10^9+7$, because a long run can produce a count larger than the required output range.

### Function Contract
**Inputs**

Let $n$ be the length of `s`.

- `s`: A non-empty string of length $1 \leq n \leq 10^5$.
- Every character is either `0` or `1`.
- A substring is identified by its contiguous start and end positions; occurrences at different positions are distinct even when their contents match.

**Return value**

Return the number of non-empty all-`1` substrings, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `s = "0110111"`
- Output: `9`
- Explanation: The runs have lengths 2 and 3, contributing 3 and 6 substrings.

**Example 2**

- Input: `s = "101"`
- Output: `2`
- Explanation: Each isolated `1` contributes one substring.

**Example 3**

- Input: `s = "111111"`
- Output: `21`
