# Maximum Area Rectangle With Point Constraints I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3380 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Indexed Tree, Segment Tree, Geometry, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-area-rectangle-with-point-constraints-i](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/).

### Goal
Given a set of 2D points, identify the largest possible area of a rectangle whose sides are parallel to the coordinate axes, such that all four vertices of the rectangle are present in the input set, and no other points from the input set lie strictly inside or on the boundary of the rectangle.

### Function Contract
**Inputs**

- `points`: A list of lists, where each inner list `[x, y]` represents the coordinates of a point in a 2D plane.

**Return value**

- An integer representing the maximum area found. If no such rectangle exists, return -1.

### Examples
**Example 1**

- Input: `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`
- Output: `-1`
- Explanation: The rectangle formed by (1,1), (1,3), (3,1), (3,3) contains the point (2,2), so it is invalid.

**Example 2**

- Input: `points = [[1,1],[1,3],[3,1],[3,3]]`
- Output: `4`
- Explanation: The rectangle formed by these four points has area (3-1) * (3-1) = 4.

**Example 3**

- Input: `points = [[0,0],[1,1],[0,1],[1,0]]`
- Output: `1`

---

## Solution
### Approach
The algorithm uses a hash set for $O(1)$ point lookups. We iterate through all pairs of points that could serve as diagonal vertices of a rectangle. For each pair $(x1, y1)$ and $(x2, y2)$, we check if the other two required vertices $(x1, y2)$ and $(x2, y1)$ exist in the set. If they do, we verify the "empty" constraint by iterating through all input points to ensure no other point falls within the rectangle's bounds.

### Complexity Analysis
- **Time Complexity**: $O(N^3)$, where $N$ is the number of points. We iterate over $O(N^2)$ pairs of points, and for each valid rectangle, we perform an $O(N)$ check to ensure no points are inside.
- **Space Complexity**: $O(N)$ to store the points in a hash set for efficient lookup.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(points: list[list[int]]) -> int:
    point_set = set(tuple(p) for p in points)
    n = len(points)
    max_area = -1

    # Sort points to potentially optimize or just iterate
    # We iterate through all pairs of points as potential diagonals
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # A rectangle must have sides parallel to axes
            # So x1 != x2 and y1 != y2
            if x1 == x2 or y1 == y2:
                continue

            # Check if the other two corners exist
            p3 = (x1, y2)
            p4 = (x2, y1)

            if p3 in point_set and p4 in point_set:
                # Calculate area
                width = abs(x1 - x2)
                height = abs(y1 - y2)
                area = width * height

                # Check if any other point is inside or on the boundary
                min_x, max_x = min(x1, x2), max(x1, x2)
                min_y, max_y = min(y1, y2), max(y1, y2)

                is_valid = True
                for k in range(n):
                    px, py = points[k]
                    # Check if point is inside or on boundary
                    # We already know the 4 corners are in the set
                    if min_x <= px <= max_x and min_y <= py <= max_y:
                        if (px, py) not in {(x1, y1), (x2, y2), p3, p4}:
                            is_valid = False
                            break

                if is_valid:
                    max_area = max(max_area, area)

    return max_area
```
</details>
