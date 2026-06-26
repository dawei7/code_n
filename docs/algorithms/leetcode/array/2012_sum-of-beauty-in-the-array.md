# Sum of Beauty in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2012 |
| Difficulty | Medium |
| Topics | Array |
| Official Link | [sum-of-beauty-in-the-array](https://leetcode.com/problems/sum-of-beauty-in-the-array/) |

## Problem Description & Examples
### Goal
For each interior element, assign beauty `2` if it is greater than all elements to its left and less than all elements to its right; otherwise assign beauty `1` if it lies strictly between its immediate neighbors.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

Return the sum of beauty values for indices `1` through `n - 2`.

### Examples
**Example 1**

- Input: `nums = [1,2,3]`
- Output: `2`

**Example 2**

- Input: `nums = [2,4,6,4]`
- Output: `1`

**Example 3**

- Input: `nums = [3,2,1]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Precompute prefix maximums and suffix minimums. For each interior index, test the global condition first for beauty `2`; if it fails, test the local neighbor condition for beauty `1`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
