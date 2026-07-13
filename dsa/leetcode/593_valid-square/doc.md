# Valid Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 593 |
| Difficulty | Medium |
| Topics | Math, Geometry |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-square/) |

## Problem Description
### Goal
Given the coordinates of four points `p1`, `p2`, `p3`, and `p4` in two-dimensional space, determine whether those points construct a valid square. The points are not supplied in any geometric order, and the square may be rotated relative to the coordinate axes.

Return `True` only when the four sides have equal positive length and the four interior angles are all 90 degrees; otherwise return `False`. Coincident points cannot form a square because its side length must be positive, and a rhombus without right angles is not sufficient.

### Function Contract
**Inputs**

- `p1, p2, p3, p4: list[int]`: four points represented as `[x, y]`

**Return value**

- `True` when the points form a nondegenerate square; otherwise `False`

### Examples
**Example 1**

- Input: `[0,0], [1,1], [1,0], [0,1]`
- Output: `True`

**Example 2**

- Input: `[0,0], [2,0], [2,1], [0,1]`
- Output: `False`

**Example 3**

- Input: `[0,0], [0,0], [1,0], [0,1]`
- Output: `False`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Ignore input order by examining every pair**

Four points determine exactly six pairwise distances. Compute squared Euclidean distances so all arithmetic remains integral and no square roots or floating-point comparisons are needed.

**Recognize the square distance pattern**

A nondegenerate square has four equal positive side lengths and two equal diagonals. By the Pythagorean theorem, each squared diagonal equals twice a squared side. Sort the six values and test that the first four are one positive value, the last two are equal, and the diagonal value is twice the side value.

**Why this pattern is sufficient**

The four equal shortest distances give every vertex degree two in the side graph; a triangle among three vertices would force the remaining pair distances to violate the two-equal-diagonals pattern. The four equal edges therefore form a cycle. Equal diagonals whose squared length is twice the edge length make adjacent side vectors perpendicular, so that cycle is a square. A positive shortest distance also rules out coincident points.

#### Complexity detail

There are always exactly four points and six distances. Computing and sorting this fixed-size collection takes $O(1)$ time and $O(1)$ space under the standard fixed-width integer model.

#### Alternatives and edge cases

- **Choose one vertex and compare vectors:** identify its two nearest points, verify equal lengths and zero dot product, then repeat or confirm the opposite vertex; this is also constant time.
- **Test all point permutations:** checking the side and diagonal pattern for 24 orders is constant but more error-prone.
- **Compute squares by repeated addition:** remains correct for integer coordinates but takes time proportional to coordinate differences instead of constant arithmetic operations.
- **Use square roots:** introduces unnecessary floating-point precision concerns.
- **Coincident points:** create a zero distance and must be rejected.
- **Rectangle that is not a square:** has unequal side lengths.
- **Rhombus that is not a square:** has unequal diagonals.
- **Rotated square:** has the same squared-distance multiset and qualifies.
- **Arbitrary input order:** does not affect the sorted distances.
- **Negative coordinates:** squared differences work unchanged.

</details>
