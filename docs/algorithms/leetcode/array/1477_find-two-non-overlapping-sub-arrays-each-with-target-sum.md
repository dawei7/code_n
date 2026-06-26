# Find Two Non-overlapping Sub-arrays Each With Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1477 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming, Sliding Window |
| Official Link | [find-two-non-overlapping-sub-arrays-each-with-target-sum](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/) |

## Problem Description & Examples
### Goal
Find two non-overlapping contiguous subarrays whose sums both equal `target`, minimizing the total of their lengths.

### Function Contract
**Inputs**

- `arr`: a list of positive integers.
- `target`: the required subarray sum.

**Return value**

The minimum combined length, or `-1` if two such non-overlapping subarrays do not exist.

### Examples
**Example 1**

- Input: `arr = [3,2,2,4,3], target = 3`
- Output: `2`

**Example 2**

- Input: `arr = [7,3,4,7], target = 7`
- Output: `2`

**Example 3**

- Input: `arr = [4,3,2,6,2,3,4], target = 6`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Sliding window plus best-prefix DP. As each target-sum window ends, combine its length with the shortest valid window ending before it, then update the best length seen so far.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for prefix best lengths.
