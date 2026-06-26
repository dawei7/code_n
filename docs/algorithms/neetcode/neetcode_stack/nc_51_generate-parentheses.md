## Problem Description & Examples
### Goal
Given a sorted array `nums` and a `target`, return the index of `target` in the array, or `-1` if not found.

### Function Contract
**Inputs**

- `nums`: List[int] (sorted)
- `target`: int

**Return value**

int - index of target, or -1

### Examples
**Example 1**

- Input: `nums = [-1, 0, 3, 5, 9, 12], target = 9`
- Output: `4`

**Example 2**

- Input: `nums = [-90, -2, 7, 94], target = 94`
- Output: `3`

**Example 3**

- Input: `nums = [-84, -66, 45, 95], target = 95`
- Output: `3`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
