# Removing Minimum and Maximum From Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2091 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [removing-minimum-and-maximum-from-array](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/) |

## Problem Description & Examples
### Goal
Remove elements only from the front or back until both the minimum and maximum array values have been removed. Minimize deletions.

### Function Contract
**Inputs**

- `nums`: an array of distinct integers.

**Return value**

Return the minimum number of deletions.

### Examples
**Example 1**

- Input: `nums = [2,10,7,5,4,1,8,6]`
- Output: `5`

**Example 2**

- Input: `nums = [0,-4,19,1,8,-2,-3,5]`
- Output: `3`

**Example 3**

- Input: `nums = [101]`
- Output: `1`

---

## Underlying Base Algorithm(s)
Find the indices of the minimum and maximum. The optimal plan is one of three cases: remove both from the front, both from the back, or one from each side. Compute all three and take the minimum.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
