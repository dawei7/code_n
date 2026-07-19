# Student Attendance Record I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 551 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/student-attendance-record-i/) |

## Problem Description
### Goal
Given a student's attendance string, each character is `A` for absent, `L` for late, or `P` for present. Award eligibility depends on the complete record rather than only a prefix or the final day.

Return `True` only when the record contains fewer than two `A` characters in total and never contains three or more consecutive `L` characters. Two absences anywhere cause failure, and a run `LLL` causes failure even when no absence occurs. Separated late days do not combine into one run, while present or absent days break a late streak.

### Function Contract
**Inputs**

- `s`: a string containing `P` for present, `A` for absent, and `L` for late

**Return value**

- `True` when both award conditions hold; otherwise `False`

### Examples
**Example 1**

- Input: `s = "PPALLP"`
- Output: `True`

**Example 2**

- Input: `s = "PPALLL"`
- Output: `False`

**Example 3**

- Input: `s = "AA"`
- Output: `False`
