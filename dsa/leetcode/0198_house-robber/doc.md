# House Robber

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 198 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/house-robber/) |

## Problem Description
### Goal
Houses stand along one street, and `nums[i]` gives the nonnegative amount of money in house `i`. Robbing two directly adjacent houses on the same night triggers an alarm, so any chosen set of houses must leave at least one unrobbed position between consecutive choices.

Return the maximum total amount that can be collected without selecting adjacent indices. You may skip any house, including one with a smaller amount when doing so enables more valuable choices later. If every house contains zero, the result is zero. The function returns only the optimal sum, not the selected indices or a modified list of remaining amounts.

### Function Contract
**Inputs**

- `nums`: nonnegative amounts arranged along one street

**Return value**

The maximum sum of a subset containing no adjacent positions.

### Examples
**Example 1**

- Input: `[1,2,3,1]`
- Output: `4`

**Example 2**

- Input: `[2,7,9,3,1]`
- Output: `12`

**Example 3**

- Input: `[50]`
- Output: `50`
