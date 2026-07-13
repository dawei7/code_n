# Maximum Population Year

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1854 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Counting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-population-year](https://leetcode.com/problems/maximum-population-year/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-population-year/).

### Goal
Given birth and death years for several people, find the earliest year with the largest living population. A person is counted from birth year through the year before death.

### Function Contract
**Inputs**

- `logs`: a list of `[birth, death]` year pairs.

**Return value**

Return the earliest year with maximum population.

### Examples
**Example 1**

- Input: `logs = [[1993,1999],[2000,2010]]`
- Output: `1993`

**Example 2**

- Input: `logs = [[1950,1961],[1960,1971],[1970,1981]]`
- Output: `1960`

**Example 3**

- Input: `logs = [[2000,2001],[2001,2002]]`
- Output: `2000`

---

## Solution
### Approach
Use a difference array over years. Add `1` at each birth year and subtract `1` at each death year, then prefix-sum years in order. Update the best year only when the population is strictly larger, which preserves the earliest year for ties.

### Complexity Analysis
- **Time Complexity**: `O(n + Y)`, where `Y` is the year range
- **Space Complexity**: `O(Y)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
