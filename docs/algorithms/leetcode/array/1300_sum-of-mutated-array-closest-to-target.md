# Sum of Mutated Array Closest to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1300 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sorting |
| Official Link | [sum-of-mutated-array-closest-to-target](https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/) |

## Problem Description & Examples
### Goal
Choose an integer value. Replace every array element greater than that value with the value, then make the resulting sum as close as possible to `target`. Return the smallest value in a tie.

### Function Contract
**Inputs**

- `arr`: positive integer array.
- `target`: desired sum.

**Return value**

The integer cap value that gives the closest mutated sum.

### Examples
**Example 1**

- Input: `arr = [4,9,3]`, `target = 10`
- Output: `3`

**Example 2**

- Input: `arr = [2,3,5]`, `target = 10`
- Output: `5`

**Example 3**

- Input: `arr = [60864,25176,27249,21296,20204]`, `target = 56803`
- Output: `11361`

---

## Underlying Base Algorithm(s)
Binary search on the cap value.

---

## Complexity Analysis
- **Time Complexity**: `O(n log max(arr))`
- **Space Complexity**: `O(1)`
