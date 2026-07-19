# Day of the Year

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1154 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/day-of-the-year/) |

## Problem Description

### Goal

You are given a string `date` representing a Gregorian calendar date in `YYYY-MM-DD` format. Return that date's day number within its year, counting January 1 as day $1$ and continuing through the calendar months in order.

The string always represents a valid date from January 1, 1900 through December 31, 2019. The calculation must therefore respect the Gregorian leap-year rules: February has 29 days in a leap year and 28 otherwise. All other month lengths follow the ordinary Gregorian calendar.

### Function Contract

**Inputs**

- `date`: A valid Gregorian date string of length 10 in `YYYY-MM-DD` format. Positions `4` and `7` contain `"-"`, and every other character is a digit.

The represented date lies between January 1, 1900 and December 31, 2019, inclusive.

**Return value**

- The 1-indexed day number of `date` within its year.

### Examples

**Example 1**

- Input: `date = "2019-01-09"`
- Output: `9`

**Example 2**

- Input: `date = "2019-02-10"`
- Output: `41`

**Example 3**

- Input: `date = "2000-03-01"`
- Output: `61`
