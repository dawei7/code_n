# Check if the Rectangle Corner Is Reachable

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3235 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Depth-First Search, Breadth-First Search, Union-Find, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/) |

## Problem Description

### Goal

A rectangle has bottom-left corner $(0,0)$ and top-right corner $(\texttt{xCorner},\texttt{yCorner})$. Each entry `[x_i, y_i, r_i]` describes a closed circular obstacle centered at $(x_i,y_i)$ with radius $r_i$; circle centers and portions may lie outside the rectangle.

Determine whether a continuous path exists from the bottom-left corner to the top-right corner. The entire path must remain inside the rectangle, may touch the rectangle boundary only at its two endpoint corners, and may neither touch nor enter any circle. Tangency to an obstacle is forbidden.

### Function Contract

**Inputs**

- `xCorner`: The rectangle width, with $3\leq\texttt{xCorner}\leq10^9$.
- `yCorner`: The rectangle height, with $3\leq\texttt{yCorner}\leq10^9$.
- `circles`: Between $1$ and $1000$ triples `[x_i, y_i, r_i]`, whose positive coordinates and radii are at most $10^9$.

Let $n=\lvert\texttt{circles}\rvert$.

**Return value**

Return `True` exactly when an obstacle-free path satisfying all boundary restrictions exists.

### Examples

#### Example 1

- **Input:** `xCorner = 3, yCorner = 4, circles = [[2, 1, 1]]`
- **Output:** `True`
- **Explanation:** The single circle does not separate the two corners.

#### Example 2

- **Input:** `xCorner = 3, yCorner = 3, circles = [[1, 1, 2]]`
- **Output:** `False`
- **Explanation:** The circle blocks the starting corner and connects opposing boundary groups.

#### Example 3

- **Input:** `xCorner = 3, yCorner = 3, circles = [[2, 1, 1], [1, 2, 1]]`
- **Output:** `False`
- **Explanation:** The tangent circles form a barrier between the two required corners.

#### Example 4

- **Input:** `xCorner = 4, yCorner = 4, circles = [[5, 5, 1]]`
- **Output:** `True`
- **Explanation:** The circle lies outside the rectangle and does not reach even its top-right corner.
