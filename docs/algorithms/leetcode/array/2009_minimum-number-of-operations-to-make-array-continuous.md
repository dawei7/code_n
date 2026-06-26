# Minimum Number of Operations to Make Array Continuous

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2009 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Binary Search, Sliding Window |
| Official Link | [minimum-number-of-operations-to-make-array-continuous](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/) |

## Problem Description & Examples
### Goal
In one operation, replace any element with any integer. Minimize operations so the array has `n` distinct values spanning exactly `n - 1` between minimum and maximum.

### Function Contract
**Inputs**

- `nums`: an integer array of length `n`.

**Return value**

Return the minimum number of replacements needed to make the array continuous.

### Examples
**Example 1**

- Input: `nums = [4,2,5,3]`
- Output: `0`

**Example 2**

- Input: `nums = [1,2,3,5,6]`
- Output: `1`

**Example 3**

- Input: `nums = [1,10,100,1000]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Sort unique values. For each possible minimum value `x`, keep all unique values within `[x, x + n - 1]` using a sliding window. Values outside the largest such window, plus duplicates already removed from uniqueness, must be replaced.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
