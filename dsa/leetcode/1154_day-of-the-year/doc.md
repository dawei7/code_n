# Day of the Year

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1154 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [day-of-the-year](https://leetcode.com/problems/day-of-the-year/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/day-of-the-year/).

### Goal
Given a date string in `YYYY-MM-DD` format, return its 1-indexed day number within that year.

### Function Contract
**Inputs**

- `date`: Valid calendar date formatted as `YYYY-MM-DD`.

**Return value**

The ordinal day of the year.

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

---

## Solution
### Approach
Parse the year, month, and day. Sum the lengths of all months before the given month, add the day, and include February 29 when the date is after February in a leap year.

A year is leap if it is divisible by `400`, or divisible by `4` but not by `100`.

### Complexity Analysis
- **Time Complexity**: `O(1)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
