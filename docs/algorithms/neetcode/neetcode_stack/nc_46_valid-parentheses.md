## Problem Description & Examples
### Goal
Given a string `s`, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the **smallest in lexicographical order** among all possible results.

### Function Contract
**Inputs**

- `s`: str - lowercase letters

**Return value**

str - lexicographically smallest string without duplicate letters

### Examples
**Example 1**

- Input: `s = "bcabc"`
- Output: `"abc"`

**Example 2**

- Input: `s = 'ccba'`
- Output: `'cba'`

**Example 3**

- Input: `s = 'acca'`
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
