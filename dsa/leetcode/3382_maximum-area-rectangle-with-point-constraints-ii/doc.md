# Maximum Area Rectangle With Point Constraints II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3382 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Binary Indexed Tree, Segment Tree, Geometry, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/) |

## Problem Description

### Goal

There are $n$ distinct points on an infinite plane. Parallel arrays `xCoord` and `yCoord` describe them: point $i$ is located at `(xCoord[i], yCoord[i])`.

Choose four supplied points as the corners of an axis-aligned rectangle. Besides those four corners, the closed rectangle must contain no supplied point: an extra point strictly inside it or anywhere along one of its four borders invalidates the choice.

Return the greatest possible rectangle area. If no four points satisfy every condition, return `-1`.

### Function Contract

**Inputs**

- `xCoord`: The list of horizontal coordinates.
- `yCoord`: The list of vertical coordinates, where the value at each index belongs to the point with the corresponding `xCoord` value.

Let $n=\lvert\texttt{xCoord}\rvert=\lvert\texttt{yCoord}\rvert$. The constraints are $1\leq n\leq2\cdot10^5$ and $0\leq\texttt{xCoord[i]},\texttt{yCoord[i]}\leq8\cdot10^7$. All coordinate pairs are unique.

**Return value**

- The maximum area of a valid axis-aligned rectangle, or `-1` when none exists.

### Examples

**Example 1**

- Input: `xCoord = [1,1,3,3], yCoord = [1,3,1,3]`
- Output: `4`
- Explanation: The four points are the corners of a clear square of width and height two.

**Example 2**

- Input: `xCoord = [1,1,3,3,2], yCoord = [1,3,1,3,2]`
- Output: `-1`
- Explanation: The point `(2,2)` lies inside the only possible rectangle.

**Example 3**

- Input: `xCoord = [1,1,3,3,1,3], yCoord = [1,3,1,3,2,2]`
- Output: `2`
- Explanation: The extra points on the two vertical sides split the height-two square into valid height-one rectangles.
