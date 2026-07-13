# Day of the Week

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1185 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [day-of-the-week](https://leetcode.com/problems/day-of-the-week/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/day-of-the-week/).

### Goal
Given a valid date, return the English weekday name for that date.

### Function Contract
**Inputs**

- `day`: Day of month.
- `month`: Month number.
- `year`: Year.

**Return value**

Weekday name, such as `"Monday"` or `"Saturday"`.

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

---

## Solution
### Approach
Count days from a known reference date and take the result modulo `7`. For example, `1971-01-01` was a Friday, and the problem's date range can be measured forward from there.

Leap years add an extra day after February when the year is divisible by `400`, or divisible by `4` but not by `100`.

### Complexity Analysis
- **Time Complexity**: `O(1)` for the bounded year range.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
