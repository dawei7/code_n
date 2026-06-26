# Find Peak Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 162 |
| Difficulty | Medium |
| Topics | Array, Binary Search |
| Official Link | [find-peak-element](https://leetcode.com/problems/find-peak-element/) |

## Problem Description & Examples
### Goal
Find any index whose value is greater than its immediate neighbors. The virtual
values outside the array are treated as negative infinity.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

An index of any peak element.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 1]`
- Output: `2`

**Example 2**

- Input: `nums = [1, 2, 1, 3, 5, 6, 4]`
- Output: `5`

**Example 3**

- Input: `nums = [1]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Use binary search on the slope. If `nums[mid] < nums[mid + 1]`, a peak must
exist to the right because the sequence is rising. Otherwise, a peak exists at
`mid` or to the left. Continue until the search collapses to one index.

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`.
- **Space Complexity**: `O(1)`.
