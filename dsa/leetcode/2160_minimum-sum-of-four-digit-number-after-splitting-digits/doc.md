# Minimum Sum of Four Digit Number After Splitting Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2160 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/) |

## Problem Description

### Goal

You are given a positive integer `num` containing exactly four decimal digits.
Use every occurrence of those four digits to form two new integers. Their digit
orders and the division of digits between the two integers may be chosen
freely; repeated digits remain separate occurrences.

Leading zeros are allowed in either new integer, so they do not contribute to
its numeric value. Return the smallest sum obtainable from any valid pair of
new integers.

### Function Contract

**Inputs**

- `num`: an integer with exactly four digits, where
  $1000 \le \texttt{num} \le 9999$.

**Return value**

The minimum possible sum of two integers formed using all four input digits.

### Examples

**Example 1**

- Input: `num = 2932`
- Output: `52`
- Explanation: The digits can form `29` and `23`, whose sum is `52`.

**Example 2**

- Input: `num = 4009`
- Output: `13`
- Explanation: Leading zeros allow the effective values `4` and `9`.
