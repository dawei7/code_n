# Find the Key of the Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3270 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-key-of-the-numbers/) |

## Problem Description

### Goal

Given three positive integers, represent each one with exactly four decimal digits by adding leading zeros when necessary. Construct a four-digit key position by position: at each position, choose the smallest of the three digits appearing there.

Return the key as an integer. Converting the four generated digits to an integer removes any leading zeros; if all four selected digits are zero, the result is `0`.

### Function Contract

**Inputs**

- `num1`: A positive integer from 1 through 9999.
- `num2`: A positive integer from 1 through 9999.
- `num3`: A positive integer from 1 through 9999.

**Return value**

- The integer represented by the four coordinate-wise minimum digits after all three inputs are padded to width four.

### Examples

**Example 1**

- Input: `num1 = 1, num2 = 10, num3 = 1000`
- Output: `0`

The padded strings `0001`, `0010`, and `1000` have minimum digit zero in every position.

**Example 2**

- Input: `num1 = 987, num2 = 879, num3 = 798`
- Output: `777`

**Example 3**

- Input: `num1 = 1, num2 = 2, num3 = 3`
- Output: `1`
