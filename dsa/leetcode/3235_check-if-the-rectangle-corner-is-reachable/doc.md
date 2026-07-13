# Check if the Rectangle Corner Is Reachable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3235 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Depth-First Search, Breadth-First Search, Union-Find, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [check-if-the-rectangle-corner-is-reachable](https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/).

### Goal
Determine if there exists a path from the bottom-left corner (0, 0) to the top-right corner (X, Y) of a rectangle without passing through any of the given circular obstacles. The path must stay within the bounds of the rectangle [0, X] x [0, Y].

### Function Contract
**Inputs**

- `X`: An integer representing the width of the rectangle.
- `Y`: An integer representing the height of the rectangle.
- `circles`: A list of lists, where each inner list `[xi, yi, ri]` represents a circle centered at `(xi, yi)` with radius `ri`.

**Return value**

- A boolean: `True` if a path exists from (0, 0) to (X, Y), `False` otherwise.

### Examples
**Example 1**

- Input: `X = 3, Y = 4, circles = [[2, 1, 1]]`
- Output: `True`

**Example 2**

- Input: `X = 3, Y = 3, circles = [[1, 1, 2]]`
- Output: `False`

**Example 3**

- Input: `X = 3, Y = 3, circles = [[2, 1, 1], [1, 2, 1]]`
- Output: `False`

---

## Solution
### Approach
The problem is equivalent to checking if the circular obstacles form a "chain" that blocks the path from the bottom-left to the top-right. A path is blocked if there is a sequence of overlapping circles that connects the left/top boundary of the rectangle to the right/bottom boundary. This can be solved using Disjoint Set Union (DSU) or Graph Traversal (DFS/BFS) to identify connected components of circles and their intersections with the rectangle boundaries.

### Complexity Analysis
- **Time Complexity**: O(N^2), where N is the number of circles, due to checking intersections between every pair of circles.
- **Space Complexity**: O(N) to store the DSU structure or the adjacency list for graph traversal.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(x: int, y: int, circles: list[list[int]]) -> bool:
    n = len(circles)
    parent = list(range(n + 2))

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    # n: left/top boundary (x=0 or y=y)
    # n+1: right/bottom boundary (x=x or y=0)
    for i in range(n):
        cx, cy, r = circles[i]

        # Check intersection with left (x=0) or top (y=Y)
        if cx <= r or abs(cy - y) <= r:
            union(i, n)

        # Check intersection with right (x=X) or bottom (y=0)
        if abs(cx - x) <= r or cy <= r:
            union(i, n + 1)

        # Check intersection between circles
        for j in range(i + 1, n):
            x2, y2, r2 = circles[j]
            dist_sq = (cx - x2)**2 + (cy - y2)**2
            if dist_sq <= (r + r2)**2:
                union(i, j)

    # If the two boundaries are connected, the path is blocked
    if find(n) == find(n + 1):
        return False

    # Check if the start or end points are inside any circle
    for cx, cy, r in circles:
        if cx**2 + cy**2 <= r**2:
            return False
        if (cx - x)**2 + (cy - y)**2 <= r**2:
            return False

    return True
```
</details>
