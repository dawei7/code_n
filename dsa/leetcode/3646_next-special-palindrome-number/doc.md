# Next Special Palindrome Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3646 |
| Difficulty | Hard |
| Topics | Backtracking, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/next-special-palindrome-number/) |

## Problem Description

### Goal

A positive integer is special when its decimal representation is a palindrome and every digit that occurs satisfies a frequency rule: digit $k$ must appear exactly $k$ times. For example, `22` is special because it is palindromic and contains two copies of digit 2. Digit 0 cannot occur because an occurring digit cannot appear zero times.

Given a non-negative integer `n`, find the numerically smallest special palindrome that is strictly greater than `n`. Equality is not sufficient when `n` is already special.

### Function Contract

**Inputs**

- `n`: An integer satisfying $0\le n\le 10^{15}$.

**Return value**

Return the smallest special palindrome strictly greater than `n`.

### Examples

#### Example 1

- **Input:** `n = 2`
- **Output:** `22`
- **Explanation:** `22` is the first larger palindrome whose digit 2 occurs exactly twice.

#### Example 2

- **Input:** `n = 33`
- **Output:** `212`
- **Explanation:** `212` is palindromic, digit 1 occurs once, and digit 2 occurs twice.
