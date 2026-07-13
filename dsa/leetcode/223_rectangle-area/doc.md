# Rectangle Area

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 223 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rectangle-area/) |

## Problem Description
### Goal
Two axis-aligned rectangles are described by their lower-left and upper-right corner coordinates. Each rectangle has positive width and height, and the rectangles may be separate, touch along a boundary, overlap partially, or place one entirely inside the other.

Return the total plane area covered by at least one rectangle. Areas covered by both rectangles must be counted only once, while touching edges or corners contribute zero overlap. Coordinates may be negative, but width and height come from coordinate differences. The function returns only the union area, not the intersection rectangle or a set of boundary points.

### Function Contract
**Inputs**

- `ax1, ay1, ax2, ay2`: lower-left and upper-right corners of rectangle A
- `bx1, by1, bx2, by2`: corresponding corners of rectangle B

**Return value**

The total plane area covered by at least one rectangle.

### Examples
**Example 1**

- Input: `A=(-3,0)-(3,4), B=(0,-1)-(9,2)`
- Output: `45`

**Example 2**

- Identical two-by-two rectangles
- Output: `4`

**Example 3**

- Disjoint rectangles
- Output: the sum of their areas

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Add the two individual rectangle areas, then apply inclusion–exclusion by subtracting their intersection once. The separate sum counts points covered by only one rectangle once and points in both rectangles twice.

The intersection of axis-aligned rectangles is the product of their one-dimensional overlaps:

`overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))`

`overlap_height = max(0, min(ay2, by2) - max(ay1, by1))`.

The smaller right edge and larger left edge delimit the common x-interval; the y formula is analogous. Clamping at zero is not merely defensive: disjoint intervals give a negative raw difference, while rectangles touching at one edge or point have zero-area intersection.

For $A=(-3,0)-(3,4)$ and $B=(0,-1)-(9,2)$, the individual areas are `24` and `27`. Their overlap is width `3` and height `2`, area `6`, so the union is $24 + 27 - 6 = 45$.

This formula is exact because the intersection of two axis-aligned rectangles is itself an axis-aligned rectangle (or empty). Subtracting its area changes the twice-counted common region to one count without affecting any other covered point.

#### Complexity detail

The calculation uses a fixed number of comparisons, subtractions, and multiplications, so time and auxiliary space are both $O(1)$.

#### Alternatives and edge cases

- A coordinate sweep or plane subdivision is useful for many rectangles but unnecessary for two.
- Omitting the zero clamp can produce a positive-looking or negative overlap contribution for disjoint rectangles.
- Adding the individual areas without subtraction double-counts the intersection.
- Identical and nested rectangles reduce to the larger rectangle's area.
- Edge- and point-touching rectangles have zero overlap area; fixed-width implementations may need a wider type for coordinate products.

</details>
