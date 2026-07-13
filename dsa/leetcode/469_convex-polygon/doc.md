# Convex Polygon

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 469 |
| Difficulty | Medium |
| Topics | Array, Math, Geometry |
| Official Link | [LeetCode](https://leetcode.com/problems/convex-polygon/) |

## Problem Description
### Goal
Given polygon vertices in clockwise or counterclockwise boundary order, determine whether the polygon is convex. A convex polygon never changes turn direction as its boundary is traversed, including the closing edges back to the first vertices.

Return `True` when all nonzero cross products have the same sign. Collinear consecutive boundary points may be tolerated without creating an opposite turn, but any genuine left turn combined with a genuine right turn reveals a concavity and returns `False`. Vertex order is already the boundary order; do not reorder points or test only local angles without including wraparound triples.

### Function Contract
**Inputs**

- `points`: polygon vertices `[x, y]` listed in clockwise or counterclockwise boundary order

**Return value**

- `True` when the polygon never makes both left and right turns; otherwise `False`

### Examples
**Example 1**

- Input: `points = [[0, 0], [0, 1], [1, 1], [1, 0]]`
- Output: `True`

**Example 2**

- Input: `points = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]`
- Output: `False`

**Example 3**

- Input: `points = [[0, 0], [2, 0], [1, 2]]`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Measure each consecutive turn with a cross product**

For three consecutive vertices `a`, `b`, and `c`, compute the 2D cross product of vectors $b - a$ and $c - b$. A positive value is a left turn, a negative value a right turn, and zero means the boundary continues collinearly.

**Require one nonzero orientation around the cycle**

Remember the sign of the first nonzero cross product. Every later nonzero turn must have that same sign. Include wraparound triples by indexing modulo `n`, so turns at the final two vertices and back to the first are checked as well.

**Why a sign reversal identifies nonconvexity**

A convex polygon traversed in boundary order consistently turns toward its interior, regardless of whether traversal is clockwise or counterclockwise. A nonzero turn in the opposite direction creates an inward reflex angle and therefore a concavity. Collinear boundary points create zero cross products but no reflex angle, so they may be ignored when comparing orientation.

#### Complexity detail

The algorithm computes one constant-time cross product at each of `n` vertices, giving $O(n)$ time. It stores only the remembered sign and a few coordinates, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Compare every pair of turn signs:** is correct but repeats comparisons and takes $O(n^2)$ time.
- **Construct a convex hull:** can compare hull membership with the polygon but costs $O(n \log n)$ and discards the useful boundary order already provided.
- **Angle calculations:** using trigonometry introduces floating-point error where integer cross products are exact.
- **Clockwise order:** all nonzero signs are negative and remain valid.
- **Collinear consecutive vertices:** zero turns do not determine or contradict orientation.
- **Wraparound corners:** use modulo indices so the closing edge participates in two turn tests.
- **Large coordinates:** fixed-width languages should use a wide enough type for cross-product multiplication.

</details>
