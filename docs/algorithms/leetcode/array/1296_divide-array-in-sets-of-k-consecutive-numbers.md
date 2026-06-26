# Divide Array in Sets of K Consecutive Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1296 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting |
| Official Link | [divide-array-in-sets-of-k-consecutive-numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/) |

## Problem Description & Examples
### Goal
Decide whether the array can be partitioned into groups of size `k`, where each group consists of consecutive integer values.

### Function Contract
**Inputs**

- `nums`: integer array.
- `k`: required group length.

**Return value**

`true` if such a partition exists, otherwise `false`.

### Examples
**Example 1**

- Input: `nums = [1,2,3,3,4,4,5,6]`, `k = 4`
- Output: `true`

**Example 2**

- Input: `nums = [3,3,2,2,1,1]`, `k = 3`
- Output: `true`

**Example 3**

- Input: `nums = [1,2,3,4]`, `k = 3`
- Output: `false`

---

## Underlying Base Algorithm(s)
Greedy counting over sorted values.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
