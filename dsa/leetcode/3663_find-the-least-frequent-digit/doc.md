# Find The Least Frequent Digit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3663 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Math, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-least-frequent-digit/) |

## Problem Description
### Goal

Given a positive integer `n`, inspect the digits that occur in its ordinary decimal representation. For each present digit, its frequency is the number of positions in that representation containing the digit.

Choose a present digit whose frequency is smallest. Digits absent from `n` are not candidates, even though their occurrence count would be zero.

When several present digits share the minimum frequency, choose the numerically smallest one. Return the selected digit as an integer.

### Function Contract

**Inputs**

- `n`: an integer satisfying $1\le n\le2^{31}-1$.

Let $d$ denote the number of decimal digits in `n`; the legal domain has $1\le d\le10$.

**Return value**

Return the smallest digit among those appearing the minimum positive number of times in the decimal representation of `n`.

### Examples

**Example 1**

- Input: `n = 1553322`
- Output: `1`
- Digit `1` occurs once, while `2`, `3`, and `5` each occur twice.

**Example 2**

- Input: `n = 723344511`
- Output: `2`
- Digits `2`, `5`, and `7` each occur once, so the smallest tied digit is `2`.

**Example 3**

- Input: `n = 1012`
- Output: `0`
- Digits `0` and `2` each occur once; the smaller tied digit is `0`.
