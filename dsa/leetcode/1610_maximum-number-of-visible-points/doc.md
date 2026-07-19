# Maximum Number of Visible Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1610 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry, Sliding Window, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-visible-points/) |

## Problem Description
### Goal
You remain at the integral coordinate `location` on the plane and may rotate to face any direction. A field of view with width `angle` degrees includes both angular boundaries. After rotating counterclockwise by $d$ degrees from east, it covers every direction from $d-\texttt{angle}/2$ through $d+\texttt{angle}/2$.

Each entry in `points` is an integral coordinate. Coordinates may repeat, points do not block one another, and every point exactly at `location` is visible regardless of rotation. Choose the viewing direction that maximizes the number of visible points and return that maximum.

### Function Contract
**Inputs**

- `points`: an array of $n$ coordinate pairs, where $1 \le n \le 10^5$ and each coordinate is between 0 and 100. Duplicate points are allowed.
- `angle`: the inclusive field-of-view width in degrees, with $0 \le \texttt{angle} < 360$.
- `location`: the fixed observer coordinate, whose two components are also between 0 and 100.

**Return value**

Return the greatest number of points simultaneously visible for some rotation of the field of view.

### Examples
**Example 1**

- Input: `points = [[2, 1], [2, 2], [3, 3]]`, `angle = 90`, `location = [1, 1]`
- Output: `3`
- Explanation: All three directions fit within an inclusive 90-degree sector; collinear points do not obstruct one another.

**Example 2**

- Input: `points = [[2, 1], [2, 2], [3, 4], [1, 1]]`, `angle = 90`, `location = [1, 1]`
- Output: `4`
- Explanation: The point at the observer is always visible in addition to the three directional points.

**Example 3**

- Input: `points = [[1, 0], [2, 1]]`, `angle = 13`, `location = [1, 1]`
- Output: `1`
