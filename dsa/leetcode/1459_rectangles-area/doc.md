# Rectangles Area

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1459 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/rectangles-area/) |

## Problem Description
### Goal

The `Points` table stores identified points in a two-dimensional coordinate
plane. Any two points can serve as opposite corners of an axis-aligned
rectangle: the horizontal side length is the absolute difference between their
$x$-coordinates, and the vertical side length is the absolute difference
between their $y$-coordinates.

Report every unordered pair of points that determines a rectangle with
non-zero area. A pair sharing an $x$-coordinate has zero width, and a pair
sharing a $y$-coordinate has zero height, so neither belongs in the result.
Represent each pair once, with the smaller point ID in `p1` and the larger ID
in `p2`.

For every valid pair, return `p1`, `p2`, and its `area`. Order rows by
`area` from largest to smallest. Break equal-area ties by `p1` ascending,
then by `p2` ascending.

### Function Contract
**Inputs**

- `Points(id, x_value, y_value)`:
  - `id` uniquely identifies a row.
  - `x_value` and `y_value` are the point's integer coordinates.

Let $P$ be the number of rows in `Points`, and let $R$ be the number of
reported non-degenerate point pairs.

**Return value**

Return a table with columns `p1`, `p2`, and `area`. Each row represents
one pair with `p1 < p2`,
`Points[p1].x_value != Points[p2].x_value`, and
`Points[p1].y_value != Points[p2].y_value`. Its area is

$$
\lvert x_1-x_2\rvert\,\lvert y_1-y_2\rvert.
$$

Sort by `area DESC, p1 ASC, p2 ASC`.

### Examples
**Example 1**

- Input: `Points = [(1,2,7), (2,4,8), (3,2,10)]`
- Output: `[(2,3,4), (1,2,2)]`
- Explanation: IDs 1 and 3 share $x=2$, so their rectangle has zero area and
  is excluded.

**Example 2**

- Input: `Points = [(1,0,0), (2,0,5), (3,4,5)]`
- Output: `[(1,3,20)]`
- Explanation: The other two pairs have either zero width or zero height.

**Example 3**

- Input: `Points = [(9,-2,-3)]`
- Output: `[]`
- Explanation: A single point cannot form a pair.
