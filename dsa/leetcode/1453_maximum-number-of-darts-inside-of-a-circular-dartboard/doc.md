# Maximum Number of Darts Inside of a Circular Dartboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1453 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-number-of-darts-inside-of-a-circular-dartboard](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/).

### Goal
Given dart coordinates and a dartboard radius, place the board center anywhere to cover as many darts as possible.

### Function Contract
**Inputs**

- `darts`: a list of `[x, y]` dart coordinates.
- `r`: the board radius.

**Return value**

The maximum number of darts that can lie inside or on one circle of radius `r`.

### Examples
**Example 1**

- Input: `darts = [[-2,0],[2,0],[0,2],[0,-2]], r = 2`
- Output: `4`

**Example 2**

- Input: `darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5`
- Output: `5`

**Example 3**

- Input: `darts = [[1,2],[3,5],[1,-1]], r = 2`
- Output: `2`

---

## Solution
### Approach
Computational geometry over circle centers. For every pair of darts within diameter `2r`, compute the possible circle centers through both points, then count darts within each candidate circle.

### Complexity Analysis
- **Time Complexity**: `O(n^3)` with pair-generated centers and full recounts.
- **Space Complexity**: `O(1)` besides temporary center data.

### Reference Implementations
<details>
<summary>python</summary>

```python
import math


def solve(darts, r):
    points = [tuple(point[:2]) for point in darts if isinstance(point, list) and len(point) >= 2]
    if not points:
        return 0
    radius = float(abs(r))
    eps = 1e-7

    def count(cx, cy):
        return sum((x - cx) ** 2 + (y - cy) ** 2 <= radius * radius + eps for x, y in points)

    best = 1
    for i, (x1, y1) in enumerate(points):
        best = max(best, count(x1, y1))
        for x2, y2 in points[i + 1:]:
            dx, dy = x2 - x1, y2 - y1
            dist_sq = dx * dx + dy * dy
            dist = math.sqrt(dist_sq)
            if dist > 2 * radius + eps or dist == 0:
                continue
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            height = math.sqrt(max(0.0, radius * radius - dist_sq / 4))
            ux, uy = -dy / dist, dx / dist
            best = max(best, count(mid_x + ux * height, mid_y + uy * height))
            best = max(best, count(mid_x - ux * height, mid_y - uy * height))
    return best
```
</details>
