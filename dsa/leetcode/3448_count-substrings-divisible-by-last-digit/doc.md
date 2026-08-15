# Count Substrings Divisible By Last Digit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3448 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-substrings-divisible-by-last-digit/) |

## Problem Description

### Goal

Given a decimal digit string `s`, consider every non-empty contiguous substring. Interpret each substring as a decimal integer and inspect its final digit. Count the substring when that final digit is non-zero and the represented integer is divisible by it.

Leading zeros are permitted and do not invalidate a substring; they have their ordinary effect on its numeric value. A substring ending in `0` is never counted because division by its last digit would be undefined. Return the total across all start and end positions.

### Function Contract

**Inputs**

- `s`: A string of $n$ decimal digits, where $1\le n\le10^5$.

**Return value**

Return the number of non-empty substrings whose last digit is non-zero and divides the substring's decimal value exactly.

### Examples

#### Example 1

- **Input:** `s = "12936"`
- **Output:** `11`

Four of the fifteen substrings fail the divisibility rule, leaving eleven valid substrings.

#### Example 2

- **Input:** `s = "5701283"`
- **Output:** `18`

The count includes substrings with leading zeroes as well as each valid one-digit non-zero substring.

#### Example 3

- **Input:** `s = "1010101010"`
- **Output:** `25`

Only substrings ending at one of the five `1` digits qualify; their possible starting positions total twenty-five.
