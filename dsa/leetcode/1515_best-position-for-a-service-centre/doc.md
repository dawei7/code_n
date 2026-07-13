# Best Position for a Service Centre

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1515 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Geometry, Randomized |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [best-position-for-a-service-centre](https://leetcode.com/problems/best-position-for-a-service-centre/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/best-position-for-a-service-centre/).

### Goal
Choose a point for a service centre so that the sum of Euclidean distances from
that point to all given customer positions is as small as possible.

### Function Contract
**Inputs**

- `positions`: a list of `[x, y]` coordinates.

**Return value**

The minimum possible total distance, accepted within a small floating-point
tolerance.

### Examples
**Example 1**

- Input: `positions = [[0, 1], [1, 0], [1, 2], [2, 1]]`
- Output: `4.0`

**Example 2**

- Input: `positions = [[1, 1], [3, 3]]`
- Output: `2.82843`

**Example 3**

- Input: `positions = [[1, 1]]`
- Output: `0.0`

---

## Solution
### Approach
The objective is convex over the plane. A common approach is nested ternary
search: for a fixed `x`, ternary-search the best `y`, then ternary-search `x`
using that inner optimum. Gradient descent with a shrinking step size is another
practical method for the same convex surface.

### Complexity Analysis
- **Time Complexity**: `O(n * I^2)` for nested ternary search with `I` iterations per dimension.
- **Space Complexity**: `O(1)` extra space.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math


def solve(positions):
    points = []
    for index, point in enumerate(positions):
        if isinstance(point, list) and len(point) >= 2:
            points.append((float(point[0]), float(point[1])))
        else:
            points.append((float(index), float(point)))
    if not points:
        return 0.0

    def total(cx, cy):
        return sum(math.hypot(px - cx, py - cy) for px, py in points)

    min_x = min(px for px, _ in points)
    max_x = max(px for px, _ in points)
    min_y = min(py for _, py in points)
    max_y = max(py for _, py in points)

    def best_for_x(cx):
        lo, hi = min_y, max_y
        for _ in range(80):
            third = (hi - lo) / 3.0
            y1 = lo + third
            y2 = hi - third
            if total(cx, y1) < total(cx, y2):
                hi = y2
            else:
                lo = y1
        cy = (lo + hi) / 2.0
        return total(cx, cy)

    lo, hi = min_x, max_x
    for _ in range(80):
        third = (hi - lo) / 3.0
        x1 = lo + third
        x2 = hi - third
        if best_for_x(x1) < best_for_x(x2):
            hi = x2
        else:
            lo = x1
    return best_for_x((lo + hi) / 2.0)
```
</details>
