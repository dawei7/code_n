# Find the Number of Ways to Place People I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3025 |
| Difficulty | Medium |
| Topics | Array, Math, Geometry, Sorting, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/) |

## Problem Description

### Goal

You are given $N$ distinct points with integer coordinates in a two-dimensional plane. Count ordered pairs $(A,B)$ for which $A$ lies on the upper-left side of $B$: $x_A\le x_B$ and $y_A\ge y_B$. Equality is allowed in either coordinate, so the two chosen points may define a horizontal or vertical line instead of a rectangle with positive area.

The closed axis-aligned rectangle or line segment having $A$ and $B$ as opposite corners must contain no other supplied point. Its border counts as part of the forbidden region; only $A$ and $B$ themselves may lie anywhere inside or on that boundary. Return the number of ordered pairs satisfying both conditions.

### Function Contract

**Inputs**

- `points`: A list of $N$ distinct coordinate pairs `[x, y]`, where $2\le N\le50$ and $0\le x,y\le50$.

**Return value**

The number of ordered pairs $(A,B)$ whose closed upper-left-to-lower-right rectangle or line contains no other point.

### Examples

#### Example 1

- **Input:** `points = [[1, 1], [2, 2], [3, 3]]`
- **Output:** `0`

Every point farther right is also higher, so no point can serve as the required lower-right endpoint.

#### Example 2

- **Input:** `points = [[6, 2], [4, 4], [2, 6]]`
- **Output:** `2`

The two adjacent pairs along the descending diagonal are empty; the outer pair is blocked by `[4, 4]`.

#### Example 3

- **Input:** `points = [[3, 1], [1, 3], [1, 1]]`
- **Output:** `2`

Horizontal or vertical lines are allowed, but a third point on the border blocks the larger rectangle.
