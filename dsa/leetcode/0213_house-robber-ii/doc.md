# House Robber II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 213 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/house-robber-ii/) |

## Problem Description
### Goal
Houses are arranged in a circle, and `nums[i]` gives the nonnegative amount available at each house. Robbing two neighboring houses triggers an alarm; because the street is circular, the first and last positions are neighbors in addition to every adjacent pair inside the array.

Return the maximum total obtainable from a set containing no neighboring houses. You may skip any house, and a one-house street allows that house to be chosen because it is not two distinct adjacent selections. The function returns only the best sum, not the selected indices. A plan valid for a straight street may be invalid here if it includes both endpoints.

### Function Contract
**Inputs**

- `nums`: nonnegative house values in circular order

**Return value**

The maximum valid total.

### Examples
**Example 1**

- Input: `[2,3,2]`
- Output: `3`

**Example 2**

- Input: `[1,2,3,1]`
- Output: `4`

**Example 3**

- Input: `[50]`
- Output: `50`
