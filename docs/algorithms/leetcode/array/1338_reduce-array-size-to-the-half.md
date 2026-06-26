# Reduce Array Size to The Half

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1338 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [reduce-array-size-to-the-half](https://leetcode.com/problems/reduce-array-size-to-the-half/) |

## Problem Description & Examples
### Goal
Remove all occurrences of as few distinct integers as possible so that the remaining array length is at most half of the original length.

### Function Contract
**Inputs**

- `arr`: integer array.

**Return value**

The minimum number of distinct values to remove.

### Examples
**Example 1**

- Input: `arr = [3,3,3,3,5,5,5,2,2,7]`
- Output: `2`

**Example 2**

- Input: `arr = [7,7,7,7,7,7]`
- Output: `1`

**Example 3**

- Input: `arr = [1,2,3,4]`
- Output: `2`

---

## Underlying Base Algorithm(s)
Frequency counting and greedy selection.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
