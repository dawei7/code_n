# Maximum Vacation Days

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 568 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-vacation-days/) |

## Problem Description
### Goal
You begin in city `0` on Monday of week `0` and have a fixed number of weeks available for travel. At the start of each week, you may remain in your current city or take one directed flight that exists in `flights`; taking that flight consumes no vacation days. You then receive the vacation allowance recorded for the city where you spend that week.

Choose the weekly sequence of stays and flights that maximizes the total vacation days collected from `days`. A city that cannot be reached from your current location at that week's start is not a valid choice, and future connectivity may make a smaller immediate allowance part of the optimal schedule.

### Function Contract
**Inputs**

- `flights`: a square matrix where `flights[i][j] = 1` permits travel from city `i` to city `j`
- `days`: a matrix where `days[i][w]` is the vacation allowance in city `i` during week `w`

**Return value**

- The maximum total vacation days achievable

### Examples
**Example 1**

- Input: `flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]`
- Output: `12`

**Example 2**

- Input: no flights and weekly allowances `[[1,1,1],[7,7,7],[7,7,7]]`
- Output: `3`

**Example 3**

- Input: all intercity flights and allowances `[[7,0,0],[0,7,0],[0,0,7]]`
- Output: `21`
