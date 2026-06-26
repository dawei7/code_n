## Problem Description & Examples
### Goal
Design a time-based key-value store. Each key can store multiple values at different timestamps. `set(key, value, timestamp)` stores the value. `get(key, timestamp)` returns the value set for that key with the largest timestamp <= the given timestamp.

`solve(operations)` processes `["set", key, value, timestamp]` and `["get", key, timestamp]`.

### Function Contract
**Inputs**

- `operations`: List[List] - set/get time operations

**Return value**

List[str] - results of get operations

### Examples
**Example 1**

- Input: `[["set", "foo", "bar", 1], ["get", "foo", 1]]`
- Output: `["bar"]`

**Example 2**

- Input: `operations = [['get', 'bar', 2], ['set', 'foo', 'd', 1], ['get', 'bar', 3], ['get', 'baz', 2]]`
- Output: `['', '', '']`

**Example 3**

- Input: `operations = [['get', 'foo', 1], ['set', 'bar', 'd', 1], ['set', 'baz', 'b', 5], ['set', 'bar', 'd', 6]]`
- Output: `['']`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(log n)`
- **Space Complexity**: `O(1)` auxiliary space, excluding the output object unless the output itself is the constructed result.
