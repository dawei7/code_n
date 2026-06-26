## Problem Description & Examples
### Goal
Implement a basic calculator to evaluate a simple expression string. The expression may contain `+`, `-`, `(`, `)`, and non-negative integers.

### Function Contract
**Inputs**

- `s`: str - arithmetic expression

**Return value**

int - result of the expression

### Examples
**Example 1**

- Input: `s = "1 + 1"`
- Output: `2`

**Example 2**

- Input: `s = '33 - (38 - 14 - 49)'`
- Output: `58`

**Example 3**

- Input: `s = '49'`
- Output: `49`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
