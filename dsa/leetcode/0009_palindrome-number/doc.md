# Palindrome Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 9 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-number/) |

## Problem Description
### Goal
Given a signed integer `x`, determine whether its usual decimal representation is a palindrome. The digits must read in the same order from left to right and from right to left; the representation contains no leading zeroes.

Negative values are not palindromes because the minus sign has no matching symbol at the opposite end. A positive value ending in zero is likewise invalid unless the entire number is zero. Return a boolean result, and solve the digit comparison numerically rather than converting the integer into a string.

### Function Contract
**Inputs**

- `x`: signed 32-bit `int`

**Return value**

`True` when the decimal representation is palindromic; otherwise `False`.

### Examples
**Example 1**

- Input: `x = 121`
- Output: `True`

**Example 2**

- Input: `x = -121`
- Output: `False`

**Example 3**

- Input: `x = 10`
- Output: `False`
