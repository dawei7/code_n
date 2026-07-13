# Number of Days in a Month

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1118 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-days-in-a-month](https://leetcode.com/problems/number-of-days-in-a-month/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-days-in-a-month/).

### Goal
Given a year and a month number, return how many days that month has. February has `29` days in leap years and `28` otherwise.

### Function Contract
**Inputs**

- `year`: Gregorian calendar year.
- `month`: Month number from `1` through `12`.

**Return value**

Number of days in the given month.

### Examples
**Example 1**

- Input: `year = 1992, month = 7`
- Output: `31`

**Example 2**

- Input: `year = 2000, month = 2`
- Output: `29`

**Example 3**

- Input: `year = 1900, month = 2`
- Output: `28`

---

## Solution
### Approach
Use a fixed month-length table for all months except February. For February, apply the Gregorian leap-year rule: a year is leap if it is divisible by `400`, or if it is divisible by `4` but not by `100`.

### Complexity Analysis
- **Time Complexity**: `O(1)`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
