# Minimum Time Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 539 |
| Difficulty | Medium |
| Topics | Array, Math, String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-difference/) |

## Problem Description
### Goal
Given at least two time strings in 24-hour `HH:MM` format, interpret each as a minute position on a clock that repeats every day. The distance between two times is the smaller circular separation, so a pair near midnight may be closer across the day boundary than within the same linear ordering.

Return the minimum difference in minutes over every pair of time points. Duplicate times produce difference zero, and the comparison includes the wraparound gap between the latest and earliest sorted times. The function returns only the integer minute difference, not the selected pair or a duration string.

### Function Contract
**Inputs**

- `time_points`: at least two valid times formatted as `HH:MM`

**Return value**

- The minimum circular difference in minutes between any pair of times

### Examples
**Example 1**

- Input: `time_points = ["23:59", "00:00"]`
- Output: `1`

**Example 2**

- Input: `time_points = ["00:00", "23:59", "00:00"]`
- Output: `0`

**Example 3**

- Input: `time_points = ["01:01", "02:01"]`
- Output: `60`
