# Next Day

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2758 |
| Difficulty | Easy |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| LeetCode | [Next Day](https://leetcode.com/problems/next-day/) |

## Problem Description

### Goal

Extend every JavaScript `Date` object with a `nextDay()` method. Calling the method on a valid date must produce the following calendar day as a string in `YYYY-MM-DD` format.

The calculation must handle calendar boundaries correctly. In particular, advancing a day may cross the end of a month or year, and February must follow the leap-year rules already implemented by `Date`.

### Function Contract

**Inputs**

The native submission adds no standalone function parameters. The method is invoked on a valid `Date` instance through `date.nextDay()`.

For the app-local adapter:

- `date`: A date string for which `new Date(date)` creates a valid `Date` object.

**Return value**

Return the next calendar day as a `YYYY-MM-DD` string. The receiver itself does not need to be modified.

### Examples

#### Example 1

- **Input:** `date = "2014-06-20"`
- **Output:** `"2014-06-21"`
- **Explanation:** June 21 is the calendar day immediately after June 20.

#### Example 2

- **Input:** `date = "2017-10-31"`
- **Output:** `"2017-11-01"`
- **Explanation:** Advancing one day crosses from October into November.

#### Example 3

- **Input:** `date = "2020-02-28"`
- **Output:** `"2020-02-29"`
- **Explanation:** The year 2020 is a leap year, so February contains a 29th day.
