# Minimum Area Rectangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 939 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Geometry, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-area-rectangle/) |

## Problem Description

### Goal

Given distinct points `points` in the X-Y plane, find the minimum area of a rectangle whose four vertices all occur in the input and whose sides are parallel to the X and Y axes.

An axis-aligned rectangle requires two different x-coordinates and two different y-coordinates, with all four coordinate combinations present. Return its smallest positive area. If the supplied points cannot form any such rectangle, return `0`.

### Function Contract

**Inputs**

- `points`: a list of $N$ distinct pairs `[x, y]`, where $1 \le N \le 500$ and $0 \le x,y \le 4 \cdot 10^4$.

**Return value**

Return the minimum area of an axis-aligned rectangle using four input points, or `0` if none exists.

### Examples

**Example 1**

- Input: `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`
- Output: `4`

**Example 2**

- Input: `points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]`
- Output: `2`

### Required Complexity

- **Time:** $O(N^2)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Store every point for constant-time lookup.** Convert each coordinate pair into a tuple and insert it into a hash set. This makes it inexpensive to ask whether a potential missing corner exists.

**Treat each point pair as a possible diagonal.** For every unordered pair `(x1, y1)` and `(x2, y2)`, skip it when `x1 == x2` or `y1 == y2`, because such points cannot be opposite corners of a positive-area axis-aligned rectangle. Otherwise, the other two corners are `(x1, y2)` and `(x2, y1)`.

**Validate both corners and minimize area.** When both cross-corners occur in the set, the four points form exactly one axis-aligned rectangle with area $\lvert x_1-x_2\rvert\lvert y_1-y_2\rvert$. Update the smallest area. Every valid rectangle has two diagonals, so at least one examined pair discovers it; duplicate discovery does not affect the minimum. Return zero when no diagonal succeeds.

#### Complexity detail

There are $O(N^2)$ point pairs and each performs constant expected-time set lookups, giving $O(N^2)$ expected time. The coordinate set stores $N$ points and uses $O(N)$ space.

#### Alternatives and edge cases

- **List membership for cross-corners:** The same diagonal method remains correct, but each membership test costs $O(N)$ and raises total time to $O(N^3)$.
- **Group points by x-coordinate:** Compare pairs of y-values seen in each column and remember their most recent x-coordinate. This can also achieve quadratic worst-case time.
- **Only one shared coordinate:** Two points on the same row or column cannot serve as a diagonal and must be skipped.
- **No rectangle:** Return `0`, not an infinite sentinel.
- **Several rectangles sharing corners:** Evaluate each diagonal; only the smallest positive area matters.

</details>
