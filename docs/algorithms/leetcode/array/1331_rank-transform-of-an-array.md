# Rank Transform of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1331 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting |
| Official Link | [rank-transform-of-an-array](https://leetcode.com/problems/rank-transform-of-an-array/) |

## Problem Description & Examples
### Goal
Replace each array value by its rank among the distinct values, where the smallest value has rank `1` and equal values share the same rank.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

The rank-transformed array.

### Examples
**Example 1**

- Input: `arr = [40,10,20,30]`
- Output: `[4,1,2,3]`

**Example 2**

- Input: `arr = [100,100,100]`
- Output: `[1,1,1]`

**Example 3**

- Input: `arr = [37,12,28,9,100,56,80,5,12]`
- Output: `[5,3,4,2,8,6,7,1,3]`

---

## Underlying Base Algorithm(s)
Sorting distinct values and hash lookup.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
