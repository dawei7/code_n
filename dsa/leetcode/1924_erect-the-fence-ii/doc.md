# Erect the Fence II

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/erect-the-fence-ii/) |
| Frontend ID | 1924 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each pair in `trees` gives the Cartesian coordinates of a tree in a garden. Enclose every tree with one fence made from rope, and require the rope to form a perfect circle. A tree is enclosed when it lies either inside the circle or on its circumference.

Among all enclosing circles, find one with the smallest possible radius. Return its center coordinates and radius as `[x, y, r]`. Floating-point answers within $10^{-5}$ of the true values are accepted.

### Function Contract

**Inputs**

- `trees`: an array of $N$ points `[x, y]`.
- $1 \le N \le 3000$ and $0 \le x,y \le 3000$.

**Return value**

- Return `[x, y, r]` for the minimum enclosing circle.
- Every input point must be at distance at most $r$ from `(x, y)`.

### Examples

**Example 1**

- Input: `trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]`
- Output: `[2.0, 2.0, 2.0]`

**Example 2**

- Input: `trees = [[1,2],[2,2],[4,2]]`
- Output: `[2.5, 2.0, 1.5]`
