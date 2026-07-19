# Day of the Week

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1185 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/day-of-the-week/) |

## Problem Description

### Goal

You are given a valid calendar date as three integers: `day`, `month`, and `year`, in that order. Determine which day of the week corresponds to that date under the Gregorian calendar.

Return exactly one of `"Sunday"`, `"Monday"`, `"Tuesday"`, `"Wednesday"`, `"Thursday"`, `"Friday"`, or `"Saturday"`. Every input year is from `1971` through `2100`, inclusive. The known reference date January 1, 1971 was a Friday.

### Function Contract

**Inputs**

- `day`: The valid one-based day within the given month.
- `month`: The month number from `1` for January through `12` for December.
- `year`: A Gregorian year satisfying $1971\le\texttt{year}\le2100$.
- The three integers always describe a valid date, including the Gregorian leap-year rules for February.

**Return value**

- The full English weekday name corresponding to the input date, with the capitalization shown above.

### Examples

**Example 1**

- Input: `day = 31`, `month = 8`, `year = 2019`
- Output: `"Saturday"`

**Example 2**

- Input: `day = 18`, `month = 7`, `year = 1999`
- Output: `"Sunday"`

**Example 3**

- Input: `day = 15`, `month = 8`, `year = 1993`
- Output: `"Sunday"`
