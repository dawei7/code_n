# Maximum Score from Performing Multiplication Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1770 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [maximum-score-from-performing-multiplication-operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/) |

## Problem Description & Examples
### Goal
For each multiplier in order, choose one number from either the left or right end of `nums`, multiply it by the current multiplier, and add it to the score. Maximize the total score after all multipliers are used.

### Function Contract
**Inputs**

- `nums`: a list of integers.
- `multipliers`: the multipliers used in order.

**Return value**

Return the maximum score.

### Examples
**Example 1**

- Input: `nums = [1,2,3], multipliers = [3,2,1]`
- Output: `14`

**Example 2**

- Input: `nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]`
- Output: `102`

**Example 3**

- Input: `nums = [5,1,4], multipliers = [2,3]`
- Output: `23`

---

## Underlying Base Algorithm(s)
Use DP over how many operations have been done and how many picks came from the left. If `op` operations are complete and `left` were taken from the left side, the right index is determined. Transition by taking the next number from the left or right and adding the corresponding multiplier product.

---

## Complexity Analysis
- **Time Complexity**: `O(m^2)`, where `m = len(multipliers)`
- **Space Complexity**: `O(m)` with rolling DP
