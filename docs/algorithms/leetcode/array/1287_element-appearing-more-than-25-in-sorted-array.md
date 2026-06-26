# Element Appearing More Than 25% In Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1287 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [element-appearing-more-than-25-in-sorted-array](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/) |

## Problem Description & Examples
### Goal
Given a nondecreasing array with one value guaranteed to appear more than one quarter of the time, return that value.

### Function Contract
**Inputs**

- `arr`: sorted integer array.

**Return value**

The integer whose frequency is greater than `len(arr) / 4`.

### Examples
**Example 1**

- Input: `arr = [1,2,2,6,6,6,6,7,10]`
- Output: `6`

**Example 2**

- Input: `arr = [1,1]`
- Output: `1`

**Example 3**

- Input: `arr = [1,2,3,3,3,4]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Sorted-array frequency observation.

---

## Complexity Analysis
- **Time Complexity**: `O(n)` for the simple scan.
- **Space Complexity**: `O(1)`
