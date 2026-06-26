# Duplicate Zeros

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1089 |
| Difficulty | Easy |
| Topics | Array, Two Pointers |
| Official Link | [duplicate-zeros](https://leetcode.com/problems/duplicate-zeros/) |

## Problem Description & Examples
### Goal
Modify the array in place as if every zero were duplicated and the array were then truncated back to its original length.

### Function Contract
**Inputs**

- `arr`: a mutable integer array.

**Return value**

No value is returned; `arr` is changed in place.

### Examples
**Example 1**

- Input: `arr = [1,0,2,3,0,4,5,0]`
- Output: `[1,0,0,2,3,0,0,4]`

**Example 2**

- Input: `arr = [1,2,3]`
- Output: `[1,2,3]`

**Example 3**

- Input: `arr = [0,0,1]`
- Output: `[0,0,0]`

---

## Underlying Base Algorithm(s)
Two pointers, in-place backward writing.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` extra space.
