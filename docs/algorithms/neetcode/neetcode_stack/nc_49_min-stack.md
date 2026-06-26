## Problem Description & Examples
### Goal
Given a string `s`, repeatedly remove all adjacent duplicate pairs until no more can be removed. Return the final result.

### Function Contract
**Inputs**

- `s`: str - lowercase letters

**Return value**

str - string after removing all adjacent duplicate pairs

### Examples
**Example 1**

- Input: `s = "abbaca"`
- Output: `"ca"`

**Example 2**

- Input: `s = 'cc'`
- Output: `''`

**Example 3**

- Input: `s = 'ac'`
- Output: `'ac'`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
