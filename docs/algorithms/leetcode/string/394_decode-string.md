# Decode String

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_57` |
| Frontend ID | 394 |
| Difficulty | Medium |
| Topics | String, Stack, Recursion |
| Official Link | [decode-string](https://leetcode.com/problems/decode-string/) |

## Problem Description & Examples
### Goal
A peak element is an element that is strictly greater than its neighbors. Given an integer array `nums`, find a peak element and return its index. If multiple peaks exist, return any. Assume `nums[-1] = nums[n] = -`.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

int - index of a peak element

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 1]`
- Output: `2`

**Example 2**

- Input: `nums = [50, 98, 54]`
- Output: `1`

**Example 3**

- Input: `nums = [18, 73, 98]`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
