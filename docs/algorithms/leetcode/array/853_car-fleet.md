# Car Fleet

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_55` |
| Frontend ID | 853 |
| Difficulty | Medium |
| Topics | Array, Stack, Sorting, Monotonic Stack |
| Official Link | [car-fleet](https://leetcode.com/problems/car-fleet/) |

## Problem Description & Examples
### Goal
Given a rotated sorted array `nums` (all unique) and a `target`, return the index of `target` or `-1` if not found.

### Function Contract
**Inputs**

- `nums`: List[int] - rotated sorted (unique)
- `target`: int

**Return value**

int - index of target, or -1

### Examples
**Example 1**

- Input: `nums = [4, 5, 6, 7, 0, 1, 2], target = 0`
- Output: `4`

**Example 2**

- Input: `nums = [4, 5, 6, 7, 0, 1, 2], target = 3`
- Output: `-1`

**Example 3**

- Input: `nums = [1], target = 0`
- Output: `-1`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
