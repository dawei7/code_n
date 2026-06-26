## Problem Description & Examples
### Goal
Given the head of a linked list represented as a list of integers `head`, insert a new node between every pair of adjacent nodes with a value equal to the greatest common divisor of them.

Return the modified list of integers.

### Function Contract
**Inputs**

- `head`: List[int]

**Return value**

List[int] - list with GCDs inserted

### Examples
**Example 1**

- Input: `head = [18, 6, 10, 3]`
- Output: `[18, 6, 6, 2, 10, 1, 3]`

**Example 2**

- Input: `head = [50, 28]`
- Output: `[50, 2, 28]`

**Example 3**

- Input: `head = [38]`
- Output: `[38]`

---

## Underlying Base Algorithm(s)
- [Euclidean GCD](math_01_gcd-euclidean.md)
- [Modular exponentiation](math_03_modular-exponentiation.md)
- [Convex hull](geometric_02_convex-hull-graham-scan.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
