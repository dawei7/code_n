# Confusing Number II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1088 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/confusing-number-ii/) |

## Problem Description

### Goal

A number is valid under a 180-degree rotation only when every decimal digit is one of `0`, `1`, `6`, `8`, or `9`. Rotation reverses the digit order and maps `0` to `0`, `1` to `1`, `6` to `9`, `8` to `8`, and `9` to `6`.

A positive integer is confusing when its rotated representation is valid and denotes a different number from the original. Given the positive upper bound `n`, count the confusing integers from 1 through `n`, inclusive. Numbers containing any other digit are not confusing because their rotation is invalid.

### Function Contract

**Inputs**

- `n`: a positive integer upper bound.

Let $D$ be the number of decimal digits in `n`, and let $C$ be the number of positive integers at most `n` composed only of valid rotation digits.

**Return value**

- The number of confusing integers in the inclusive interval from 1 through `n`.

### Examples

**Example 1**

- Input: `n = 20`
- Output: `6`

The confusing values are 6, 9, 10, 16, 18, and 19.

**Example 2**

- Input: `n = 100`
- Output: `19`
