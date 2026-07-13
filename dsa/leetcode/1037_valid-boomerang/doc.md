# Valid Boomerang

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1037 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [valid-boomerang](https://leetcode.com/problems/valid-boomerang/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/valid-boomerang/).

### Goal
Given three 2D points, determine whether they form a non-degenerate boomerang: the points must be distinct and not lie on one straight line.

### Function Contract
**Inputs**

- `points`: List[List[int]] containing exactly three `[x, y]` coordinates

**Return value**

bool - `True` if the three points are non-collinear

### Examples
**Example 1**

- Input: `points = [[1, 1], [2, 3], [3, 2]]`
- Output: `True`

**Example 2**

- Input: `points = [[1, 1], [2, 2], [3, 3]]`
- Output: `False`

**Example 3**

- Input: `points = [[0, 0], [0, 0], [1, 1]]`
- Output: `False`

---

## Solution
### Approach
2D cross product collinearity test.

### Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
"""Optimal solution for LeetCode 1037: Valid Boomerang."""


def solve(points: list[list[int]]) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = points
    return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)
```
</details>
