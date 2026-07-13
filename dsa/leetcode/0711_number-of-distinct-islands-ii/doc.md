# Number of Distinct Islands II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 711 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Sorting, Matrix, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-distinct-islands-ii/) |

## Problem Description
### Goal
Given a binary grid, an island is a maximal group of `1` cells connected horizontally or vertically. Count how many distinct island shapes occur.

Two islands have the same shape when one can be translated, rotated by a multiple of 90 degrees, or reflected so that all occupied cells coincide. Absolute location and any of those transformations do not create a new shape, while diagonal contact does not join islands. Return the number of equivalence classes under all allowed transformations.

### Function Contract
**Inputs**

- `grid`: a rectangular matrix whose `1` cells are land and whose `0` cells are water

**Return value**

- The number of island equivalence classes under translation, quarter-turn rotations, and reflection

### Examples
**Example 1**

- Input: `grid = [[1,1,0,1],[0,0,0,1]]`
- Output: `1`
- Explanation: the horizontal and vertical dominoes differ only by rotation.

**Example 2**

- Input: `grid = [[1,0,0,1,1],[1,1,0,0,1]]`
- Output: `1`
- Explanation: the two three-cell corners are congruent after reflection and rotation.

**Example 3**

- Input: `grid = [[1,1,1,0,1,0],[0,0,0,0,1,1]]`
- Output: `2`
- Explanation: a three-cell line cannot become a three-cell corner.

### Required Complexity

- **Time:** $O(RC)$
- **Space:** $O(RC)$

<details>
<summary>Approach</summary>

#### General

**Collect each connected component once**

Scan the grid with a global visited set. At every unvisited land cell, run a four-directional traversal and collect all of that island's coordinates relative to the traversal origin.

**Generate all eight rigid orientations**

For each relative point `(x, y)`, the combinations
`(±x, ±y)` and `(±y, ±x)` describe the four rotations and their reflected forms. Build the transformed point set for each of these eight coordinate rules.

**Remove translation after every transform**

A rotation can move coordinates into negative ranges. Normalize each transformed set by subtracting its minimum x-coordinate and minimum y-coordinate from every point. The resulting `frozenset` depends only on that oriented shape, not its position.

**Use the complete transform family as the identity**

Wrap the eight normalized sets in another `frozenset`. Rotating or reflecting an island merely permutes this family, so congruent islands produce exactly the same nested set without needing to choose an arbitrary orientation. Insert each family into the global shape set.

**Why distinct families mean noncongruent islands**

If two islands are congruent, applying the inverse rigid transform makes one normalized orientation equal to the other, and their full transform families coincide. Conversely, a shared normalized orientation directly supplies a rotation or reflection plus translation that makes the occupied cells coincide. Thus family equality is exactly the required equivalence.

#### Complexity detail

Every cell is scanned and each land cell is traversed once. Constructing eight transforms performs constant work per land cell, so total time is $O(RC)$. Visited coordinates, traversal storage, transformed shapes, and distinct canonical families together use $O(RC)$ space.

#### Alternatives and edge cases

- **Lexicographically minimum transform:** sort every normalized orientation and choose the smallest tuple; it is conventional but introduces $O(a \log a)$ work for an island of area `a`.
- **Pairwise shape matching:** try all transforms whenever a new island is compared with earlier representatives; repeated comparisons can become quadratic in the number of islands.
- **Reflood from every land cell:** normalization still deduplicates results, but repeatedly traversing one component can take quadratic time in its area.
- An all-water grid returns `0`.
- All isolated cells belong to one shape class.
- Shapes with equal area are not necessarily congruent.
- Symmetric shapes may produce fewer than eight distinct normalized orientations; the outer set naturally removes duplicates.

</details>
