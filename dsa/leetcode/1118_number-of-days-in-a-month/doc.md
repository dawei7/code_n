# Number of Days in a Month

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1118 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-days-in-a-month/) |

## Problem Description

### Goal

You are given a Gregorian calendar `year` and a numeric `month`. Return the number of days in that month. April, June, September, and November have 30 days; the other non-February months have 31.

February normally has 28 days and has 29 in a leap year. A year divisible by 400 is a leap year. Otherwise, it is a leap year exactly when it is divisible by 4 but not by 100. Apply those century exceptions rather than using divisibility by 4 alone.

### Function Contract

**Inputs**

- `year`: a Gregorian calendar year with `1583 <= year <= 2100`.
- `month`: an integer from `1` for January through `12` for December.

**Return value**

- The integer number of days in the specified month of the specified year.

### Examples

**Example 1**

- Input: `year = 1992`, `month = 7`
- Output: `31`

**Example 2**

- Input: `year = 2000`, `month = 2`
- Output: `29`

**Example 3**

- Input: `year = 1900`, `month = 2`
- Output: `28`

Although 1900 is divisible by 4, it is a century year not divisible by 400.
