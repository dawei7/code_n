# All Divisions With the Highest Score of a Binary Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2155 |
| Difficulty | Medium |
| Topics | Array |
| Official Link | [all-divisions-with-the-highest-score-of-a-binary-array](https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/) |

## Problem Description & Examples
### Goal
Split a binary array at every boundary from `0` through `n`. A split's score is the number of zeros to its left plus the number of ones to its right. Return every boundary attaining the highest score.

### Function Contract
**Inputs**

- `nums`: a binary array.

**Return value**

All maximum-scoring split indices in increasing order.

### Examples
**Example 1**

- Input: `nums = [0, 0, 1, 0]`
- Output: `[2, 4]`

**Example 2**

- Input: `nums = [0, 0, 0]`
- Output: `[3]`

**Example 3**

- Input: `nums = [1, 1]`
- Output: `[0]`

---

## Underlying Base Algorithm(s)
Initialize the score at split zero as the total number of ones. Move the split one element at a time: crossing a zero increases the score by one, while crossing a one decreases it by one. Track the best score and replace or extend the answer list on each boundary.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the output in the worst case, with `O(1)` auxiliary state
