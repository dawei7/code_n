# Find the Largest Area of Square Inside Two Rectangles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3047 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/) |

## Problem Description

### Goal

You are given `n` axis-aligned rectangles. Rectangle `i` has bottom-left corner `bottomLeft[i] = [a_i, b_i]` and top-right corner `topRight[i] = [c_i, d_i]`, so its horizontal and vertical sides are parallel to the coordinate axes.

Find the greatest possible area of a square that lies entirely inside a region shared by at least two of the rectangles. The square may be placed anywhere within that common region; it does not need to share a corner with either rectangle. A region covered by three or more rectangles is also eligible because it is covered by at least one pair.

If no two rectangles overlap with both positive width and positive height, return `0`.

### Function Contract

**Inputs**

- `bottomLeft`: the `n` bottom-left corners, where `bottomLeft[i] = [a_i, b_i]`.
- `topRight`: the corresponding `n` top-right corners, where `topRight[i] = [c_i, d_i]`.

The arrays have equal length, $2 \le n \le 1000$. Every coordinate is between $1$ and $10^7$, and each rectangle is proper: $a_i < c_i$ and $b_i < d_i$.

**Return value**

- An integer equal to the maximum square area available inside the intersection of at least two rectangles, or `0` when no such square has positive area.

### Examples

**Example 1**

- Input: `bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]`
- Output: `1`
- Explanation: Rectangles `0` and `1` overlap in a unit square, so the best side length is `1`.

**Example 2**

- Input: `bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]`
- Output: `4`
- Explanation: A side-`2` square fits in the overlap of the first two rectangles, giving area `4`.

**Example 3**

- Input: `bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]`
- Output: `1`
- Explanation: The widest square supported by any shared region has side length `1`.

**Example 4**

- Input: `bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]`
- Output: `0`
- Explanation: No pair overlaps with positive width and positive height.
