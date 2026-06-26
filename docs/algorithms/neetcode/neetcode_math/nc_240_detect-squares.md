## Problem Description & Examples
### Goal
You are given a stream of points on the 2D plane. Design an API that detects square structures.

`solve(operations)` processes operations of the form:
- `["add", x, y]` -> adds a point to the data structure
- `["count", x, y]` -> counts the number of ways to choose three points from the data structure such that they form an axis-aligned square with the query point `[x, y]`

Return a list of counts matching each `"count"` operation in order.

### Function Contract
**Inputs**

- `operations`: List[List] - add/count operations

**Return value**

List[int] - count values for each count operation

### Examples
**Example 1**

- Input: `operations = [["add", 3, 10], ["add", 11, 2], ["add", 3, 2], ["count", 11, 10]]`
- Output: `[1]`

**Example 2**

- Input: `operations = [['count', 4, 1], ['add', 5, 4], ['add', 3, 4], ['add', 2, 5]]`
- Output: `[0]`

**Example 3**

- Input: `operations = [['add', 1, 3], ['add', 4, 4], ['add', 2, 1], ['add', 4, 4]]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
