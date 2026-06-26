# Online Stock Span

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_54` |
| Frontend ID | 901 |
| Difficulty | Medium |
| Topics | Stack, Design, Monotonic Stack, Data Stream |
| Official Link | [online-stock-span](https://leetcode.com/problems/online-stock-span/) |

## Problem Description & Examples
### Goal
Suppose an ascending sorted array is rotated between 1 and n times. Find the minimum element. Assume all values are unique.

### Function Contract
**Inputs**

- `nums`: List[int] - rotated sorted array with unique elements

**Return value**

int - minimum element

### Examples
**Example 1**

- Input: `nums = [3, 4, 5, 1, 2]`
- Output: `1`

**Example 2**

- Input: `nums = [4, 5, 6, 7, 0, 1, 2]`
- Output: `0`

**Example 3**

- Input: `nums = [11, 13, 15, 17]`
- Output: `11`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
