# Check If It Is a Straight Line

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1232 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-it-is-a-straight-line](https://leetcode.com/problems/check-if-it-is-a-straight-line/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-it-is-a-straight-line/).

### Goal
Determine whether all given points lie on one straight line.

### Function Contract
**Inputs**

- `coordinates`: list of `[x, y]` points.

**Return value**

`true` if all points are collinear, otherwise `false`.

### Examples
**Example 1**

- Input: `coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]`
- Output: `true`

**Example 2**

- Input: `coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]`
- Output: `false`

**Example 3**

- Input: `coordinates = [[0,0],[0,5],[0,-2]]`
- Output: `true`

---

## Solution
### Approach
Cross-product collinearity test.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(coordinates):
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    dx = x1 - x0
    dy = y1 - y0
    return all((x - x0) * dy == (y - y0) * dx for x, y in coordinates[2:])
```
</details>
