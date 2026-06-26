# Can Make Arithmetic Progression From Sequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1502 |
| Difficulty | Easy |
| Topics | Array, Sorting |
| Official Link | [can-make-arithmetic-progression-from-sequence](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/) |

## Problem Description & Examples
### Goal
Determine whether the array can be reordered into an arithmetic progression.

### Function Contract
**Inputs**

- `arr`: an integer array.

**Return value**

`true` if some ordering has a constant adjacent difference; otherwise `false`.

### Examples
**Example 1**

- Input: `arr = [3, 5, 1]`
- Output: `true`

**Example 2**

- Input: `arr = [1, 2, 4]`
- Output: `false`

**Example 3**

- Input: `arr = [7, 7, 7]`
- Output: `true`

---

## Underlying Base Algorithm(s)
Sort the values, compute the first adjacent difference, and verify every later
adjacent pair has the same difference.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(1)` extra space if sorting in place.
