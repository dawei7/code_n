# Number of Days Between Two Dates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1360 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-days-between-two-dates/) |

## Problem Description

### Goal

Given two valid Gregorian calendar dates, determine the absolute number of whole days separating them. Each input uses the fixed `YYYY-MM-DD` representation, with a four-digit year followed by a two-digit month and day.

The dates may arrive in either chronological order and may be identical. Calendar conversion must account for different month lengths and leap years, including the century rule that a year divisible by $100$ is not a leap year unless it is also divisible by $400$. Return the nonnegative difference.

### Function Contract

**Inputs**

- `date1` and `date2`: valid dates formatted as `YYYY-MM-DD`, within the supported Gregorian range.

**Return value**

- The absolute number of days between the two dates.

### Examples

**Example 1**

- Input: `date1 = "2019-06-29", date2 = "2019-06-30"`
- Output: `1`

**Example 2**

- Input: `date1 = "2020-01-15", date2 = "2019-12-31"`
- Output: `15`

**Example 3**

- Input: `date1 = "2020-02-28", date2 = "2020-03-01"`
- Output: `2`
- Explanation: February 29 contributes an additional day in leap year 2020.
