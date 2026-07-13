# Find the Largest Area of Square Inside Two Rectangles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3047 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-largest-area-of-square-inside-two-rectangles](https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/).

### Goal
Given two arrays of rectangles, where each rectangle is defined by its bottom-left and top-right coordinates, determine the maximum area of a square that can be formed within the intersection of any two rectangles (one from the first set and one from the second). If no intersection exists, the area is zero.

### Function Contract
**Inputs**

- `bottomLeft`: A list of lists of integers, where each element `[x1, y1]` represents the bottom-left corner of a rectangle.
- `topRight`: A list of lists of integers, where each element `[x2, y2]` represents the top-right corner of a rectangle.

**Return value**

- `int`: The maximum area of a square that can fit inside the intersection of any two rectangles.

### Examples
**Example 1**

- Input: `bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]`
- Output: `1`

**Example 2**

- Input: `bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,3]]`
- Output: `1`

**Example 3**

- Input: `bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]`
- Output: `0`

---

## Solution
### Approach
The problem relies on **Geometric Intersection** logic. For any two rectangles defined by `(x1, y1)` to `(x2, y2)` and `(x3, y3)` to `(x4, y4)`, their intersection is a rectangle defined by `[max(x1, x3), max(y1, y3)]` to `[min(x2, x4), min(y2, y4)]`. If the resulting width and height are positive, the side length of the largest square that can fit inside is `min(width, height)`. We iterate through all pairs to find the global maximum.

### Complexity Analysis
- **Time Complexity**: `O(N * M)`, where `N` is the number of rectangles in the first set and `M` is the number of rectangles in the second set, as we compare every pair.
- **Space Complexity**: `O(1)`, as we only store the maximum area found so far.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
    max_side = 0
    n = len(bottomLeft)

    # Iterate through all pairs of rectangles
    for i in range(n):
        for j in range(i + 1, n):
            # Intersection coordinates
            x_left = max(bottomLeft[i][0], bottomLeft[j][0])
            y_bottom = max(bottomLeft[i][1], bottomLeft[j][1])
            x_right = min(topRight[i][0], topRight[j][0])
            y_top = min(topRight[i][1], topRight[j][1])

            # Calculate width and height of the intersection
            width = x_right - x_left
            height = y_top - y_bottom

            # If intersection exists, find the largest square side
            if width > 0 and height > 0:
                side = min(width, height)
                if side > max_side:
                    max_side = side

    return max_side * max_side
```
</details>
