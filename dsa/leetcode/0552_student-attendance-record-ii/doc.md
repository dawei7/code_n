# Student Attendance Record II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 552 |
| Difficulty | Hard |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/student-attendance-record-ii/) |

## Problem Description
### Goal
An attendance record of length `n` is a string over `A` (absent), `L` (late), and `P` (present). It is eligible when it contains at most one `A` in total and contains no run of three or more consecutive `L` characters.

Return the number of eligible records of exactly length `n`, modulo `1,000,000,007`. Different character sequences count separately, and every position must receive one of the three statuses. A present day breaks a late streak, an absence also breaks that streak while consuming the single absence allowance, and invalid prefixes cannot become eligible after extension.

### Function Contract
**Inputs**

- `n`: the number of days in the attendance record

**Return value**

- The number of award-eligible records of length `n`, reduced modulo `1,000,000,007`

### Examples
**Example 1**

- Input: `n = 1`
- Output: `3`

**Example 2**

- Input: `n = 2`
- Output: `8`

**Example 3**

- Input: `n = 3`
- Output: `19`
