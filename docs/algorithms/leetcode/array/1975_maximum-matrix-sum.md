# Maximum Matrix Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1975 |
| Difficulty | Medium |
| Topics | Array, Greedy, Matrix |
| Official Link | [maximum-matrix-sum](https://leetcode.com/problems/maximum-matrix-sum/) |

## Problem Description & Examples
### Goal
You may repeatedly choose adjacent cells and multiply both by `-1`. Maximize the sum of all matrix entries.

### Function Contract
**Inputs**

- `matrix`: an integer grid.

**Return value**

Return the largest achievable matrix sum.

### Examples
**Example 1**

- Input: `matrix = [[1,-1],[-1,1]]`
- Output: `4`

**Example 2**

- Input: `matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]`
- Output: `16`

**Example 3**

- Input: `matrix = [[-1,0],[-2,-3]]`
- Output: `6`

---

## Underlying Base Algorithm(s)
The operations allow signs to be rearranged while preserving the parity of the number of negative values unless a zero exists. Sum absolute values. If the negative count is odd and there is no zero, subtract twice the smallest absolute value.

---

## Complexity Analysis
- **Time Complexity**: `O(mn)`
- **Space Complexity**: `O(1)`
