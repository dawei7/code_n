# Find Target Indices After Sorting Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2089 |
| Difficulty | Easy |
| Topics | Array, Binary Search, Sorting |
| Official Link | [find-target-indices-after-sorting-array](https://leetcode.com/problems/find-target-indices-after-sorting-array/) |

## Problem Description & Examples
### Goal
After sorting the array, list every index where `target` appears.

### Function Contract
**Inputs**

- `nums`: an integer array.
- `target`: value to locate after sorting.

**Return value**

Return the sorted-array indices containing `target`.

### Examples
**Example 1**

- Input: `nums = [1,2,5,2,3], target = 2`
- Output: `[1,2]`

**Example 2**

- Input: `nums = [1,2,5,2,3], target = 3`
- Output: `[3]`

**Example 3**

- Input: `nums = [1,2,5,2,3], target = 4`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Count how many values are smaller than `target` and how many equal `target`. The answer is the consecutive range starting at the smaller-count with length equal-count.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` excluding output.
