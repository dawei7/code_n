# Minimum Area Rectangle II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 963 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-area-rectangle-ii](https://leetcode.com/problems/minimum-area-rectangle-ii/) |

## Problem Description

### Goal

You are given distinct points in the Cartesian plane, with each point represented as `[x, y]`. Select four of them that are the vertices of a rectangle. The rectangle may be rotated by any angle; its sides are not required to be parallel to the coordinate axes.

Among every rectangle that can be formed entirely from the supplied points, return the smallest area. If no four points form a rectangle, return `0`. A floating-point answer is accepted when it differs from the exact area by at most $10^{-5}$.

### Function Contract

**Inputs**

- `points`: a list of $P$ distinct coordinate pairs, where $1 \le P \le 50$.
- Each coordinate is an integer between $0$ and $4\times10^4$, inclusive.

**Return value**

Return the minimum area of a rectangle whose four vertices belong to `points`, or `0` if none exists.

### Examples

**Example 1**

- Input: `points = [[1,2],[2,1],[1,0],[0,1]]`
- Output: `2.00000`

**Example 2**

- Input: `points = [[0,1],[2,1],[1,1],[1,0],[2,0]]`
- Output: `1.00000`

**Example 3**

- Input: `points = [[0,3],[1,2],[3,1],[1,3],[2,1]]`
- Output: `0`

### Required Complexity

- **Time:** $O(P^3)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Choose one corner and its two neighbors.** For each point `a`, enumerate distinct points `b` and `c`. The vectors from `a` to these candidates are adjacent rectangle sides exactly when their dot product is zero. Reject a zero-area choice and every non-perpendicular pair.

**Derive the fourth vertex.** A parallelogram with adjacent vertices `b` and `c` around `a` has opposite vertex `d = b + c - a`. Store every input coordinate in a set and test whether this derived point exists. Perpendicular adjacent sides plus the parallelogram relation prove that `a`, `b`, `c`, and `d` form a rectangle; no assumption about axis alignment is needed.

**Measure and minimize.** For a valid pair of perpendicular side vectors, the rectangle area is the product of their Euclidean lengths. Compute the squared length of each vector, take the square root of their product, and retain the smallest positive area. Every rectangle is considered from each of its corners, so the minimum cannot be missed. If no candidate succeeds, return `0`.

#### Complexity detail

There are $O(P^3)$ choices of one corner and two possible neighbors. The dot product, derived-coordinate lookup, and area calculation take constant average time, so total time is $O(P^3)$. The coordinate set uses $O(P)$ auxiliary space.

#### Alternatives and edge cases

- **Group equal diagonals:** Opposite rectangle vertices have the same midpoint and diagonal length. Group all point pairs by those two properties, then combine diagonals within a group; this is elegant but requires careful worst-case accounting and area reconstruction.
- **Enumerate four vertices:** Test every four-point subset and all possible side arrangements. This is correct but raises the running time to $O(P^4)$.
- **Axis-aligned-only search:** Looking only for equal x- and y-coordinates misses rotated rectangles and does not satisfy this problem.
- **No rectangle:** Fewer than four points, collinear points, or incompatible configurations must return `0`.
- **Multiple rectangles:** The result is the smallest positive area, regardless of orientation.
- **Floating-point output:** Integer dot products and coordinate lookup remain exact; floating point is needed only for the final square root.

</details>
