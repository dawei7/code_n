# Count Binary Palindromic Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3677 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-binary-palindromic-numbers/) |

## Problem Description
### Goal

A non-negative integer is binary-palindromic when its ordinary binary representation, written without leading zeros, reads identically from left to right and right to left. The number zero is included by definition and has representation `0`.

Given a non-negative upper bound `n`, count every integer $k$ in the inclusive range $0\le k\le n$ whose binary representation is a palindrome.

### Function Contract

**Inputs**

- `n`: a non-negative integer satisfying $0\le n\le10^{15}$.

**Return value**

Return the number of binary-palindromic integers in the inclusive interval from zero through `n`.

### Examples

**Example 1**

- Input: `n = 9`
- Output: `6`

The qualifying values are `0`, `1`, `3`, `5`, `7`, and `9`, whose binary forms are `0`, `1`, `11`, `101`, `111`, and `1001`.

**Example 2**

- Input: `n = 0`
- Output: `1`

Zero itself is explicitly considered binary-palindromic.

**Example 3**

- Input: `n = 8`
- Output: `5`

The next binary palindrome after `111` is `1001`, which represents 9 and lies above the bound.
