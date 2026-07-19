# Integer to English Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 273 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, String, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/integer-to-english-words/) |

## Problem Description
### Goal
Given a nonnegative 32-bit integer, write its value using conventional English number words. Compose groups for hundreds and the larger scales `Thousand`, `Million`, and `Billion`, omitting any group whose numerical value is zero.

Return a capitalized string with words separated by single spaces, no leading or trailing whitespace, no hyphens, and no inserted word `and`. The value zero is represented exactly as `"Zero"`. Within each nonzero three-digit group, use the standard forms from `One` through `Nineteen` and the tens through `Ninety`, preserving their numerical order without spelling individual digits.

### Function Contract
**Inputs**

- `num`: a nonnegative integer

**Return value**

Capitalized English number words separated by single spaces, without `and`; zero becomes `"Zero"`.

### Examples
**Example 1**

- Input: `num = 123`
- Output: `"One Hundred Twenty Three"`

**Example 2**

- Input: `num = 12345`
- Output: `"Twelve Thousand Three Hundred Forty Five"`

**Example 3**

- Input: `num = 1234567`
- Output: `"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"`
