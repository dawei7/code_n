## Problem Description & Examples
### Goal
Given a non-negative integer `x`, return the integer square root of `x` (floor of the actual square root, without using built-in `sqrt` functions).

### Function Contract
**Inputs**

- `x`: int - non-negative

**Return value**

int - floor of sqrt(x)

### Examples
**Example 1**

- Input: `x = 8`
- Output: `2`

**Example 2**

- Input: `x = 49`
- Output: `7`

**Example 3**

- Input: `x = 34`
- Output: `5`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
