# Array With Elements Not Equal to Average of Neighbors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1968 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [array-with-elements-not-equal-to-average-of-neighbors](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/) |

## Problem Description & Examples
### Goal
Rearrange the array so no interior element equals the average of its immediate neighbors.

### Function Contract
**Inputs**

- `nums`: an array of distinct integers.

**Return value**

Return any valid rearrangement.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5]`
- Output: `[1,3,2,5,4]`

**Example 2**

- Input: `nums = [6,2,0,9,7]`
- Output: `[0,6,2,9,7]`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `[1,3,2]`

---

## Underlying Base Algorithm(s)
Sort the values and then interleave small and large positions, or swap adjacent sorted pairs. This creates alternating local highs and lows, which prevents a middle value from sitting exactly between its neighbors.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` depending on whether the rearrangement is built in place.
