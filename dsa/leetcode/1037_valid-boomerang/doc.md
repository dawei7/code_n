# Valid Boomerang

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1037 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/valid-boomerang/) |

## Problem Description

### Goal

You are given exactly three points on the x-y plane, with `points[i] = [xi, yi]`.

Return `true` when the three points form a boomerang. A boomerang requires all three points to be distinct and requires that they do not lie on one straight line. Thus any repeated coordinate makes the answer false, as does any placement where one common line contains every point, regardless of their input order.

### Function Contract

**Inputs**

- `points`: exactly three coordinate pairs.
- Every x- and y-coordinate is an integer between $0$ and $100$, inclusive.

**Return value**

- Whether the three points are distinct and non-collinear.

### Examples

**Example 1**

- Input: `points = [[1,1],[2,3],[3,2]]`
- Output: `true`

**Example 2**

- Input: `points = [[1,1],[2,2],[3,3]]`
- Output: `false`
- Explanation: All three points lie on the same diagonal line.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Form two direction vectors:** From the first point, use vectors ((x_2-x_1,y_2-y_1)) and ((x_3-x_1,y_3-y_1)).

**Test their two-dimensional cross product:** The signed doubled area of the triangle is
$$
(x_2-x_1)(y_3-y_1)-(y_2-y_1)(x_3-x_1).
$$
It is zero exactly when the vectors are linearly dependent and the three points are collinear. Return whether it is nonzero.

A duplicate point produces a zero direction vector, so the same test also rejects every failure of the distinctness requirement without a separate set check. A nonzero cross product simultaneously proves distinctness and non-collinearity, exactly matching the boomerang definition.

#### Complexity detail

The input always contains three points. A fixed number of integer subtractions and multiplications takes $O(1)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Compare slopes with division:** Equal slopes identify collinearity, but vertical lines require special handling and floating-point division can introduce precision concerns.
- **Enumerate lattice positions:** Choose the farthest point pair and walk through integer positions on its segment to see whether the third lies there. This can take time proportional to the coordinate span.
- **Duplicate points:** Any duplicate makes the cross product zero and the answer false.
- **Vertical or horizontal line:** The determinant handles both without special cases.
- **Third point outside the other two:** Collinearity still makes the answer false; the test concerns the entire line, not only one segment.
- **Boundary coordinates:** Values at zero and 100 remain safe for ordinary integer arithmetic.

</details>
