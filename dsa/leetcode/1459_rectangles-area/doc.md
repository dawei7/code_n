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

### Required Complexity
- **Time:** $O(P^2 \log P)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Generate every unordered pair exactly once**

Self-join `Points` as `first_point` and `second_point`. The condition
`first_point.id < second_point.id` chooses one orientation of every pair:
for two distinct unique IDs exactly one ordering satisfies it. This both avoids
duplicate rows and directly establishes the required `p1 < p2` convention.

An inner join is appropriate because every result requires two existing rows.
No grouping or `DISTINCT` is necessary: uniqueness of `id` and the strict
ID inequality already make each pair unique.

**Reject degenerate rectangles before reporting them**

Require different $x$-coordinates and different $y$-coordinates in the join
predicate. These conditions are equivalent to positive width and positive
height, respectively. Because both absolute differences are then nonzero,
their product is a positive area.

Project the smaller ID as `p1`, the larger ID as `p2`, and calculate
`ABS(first_point.x_value - second_point.x_value) *
ABS(first_point.y_value - second_point.y_value)` as `area`. Coordinate
signs and relative positions do not matter because the absolute differences
are geometric side lengths.

**Apply the complete deterministic ordering**

Sort first by the computed `area` alias descending. For equal areas, sort by
`p1` and then `p2`, both ascending. All three keys are necessary: relying
on physical row order or on only the area does not satisfy the required
tie-breaking contract.

Every emitted row comes from two distinct IDs, passes both non-degeneracy
tests, and has the exact area formula, so every output row is valid. Conversely,
any valid rectangle has two distinct IDs; exactly its smaller-ID/larger-ID
orientation satisfies the self-join inequality, and its unequal coordinates
pass the filters. Therefore every valid rectangle appears exactly once.

#### Complexity detail

The self-join considers $O(P^2)$ unordered pairs and emits $R\le
P(P-1)/2$ rows. Computing each area is constant work. Sorting the result costs
$O(R\log R)$, which is $O(P^2\log P)$ in the worst case. The database may
materialize $O(R)$ rows for the required sort; indexes and a particular query
planner can change constants but not the worst-case output size.

#### Alternatives and edge cases

- **Cross join plus `DISTINCT`:** Generating both orientations and removing
  duplicates does extra work and complicates canonical `p1`/`p2` values;
  the strict ID inequality prevents duplicates directly.
- **Correlated lookup per pair:** Repeatedly rescanning `Points` while
  calculating each pair remains correct but can grow to $O(P^3)$ and is
  unnecessary because both joined rows already contain all coordinates.
- **Same $x$-coordinate:** Width is zero, so exclude the pair even when its
  $y$-coordinates differ.
- **Same $y$-coordinate:** Height is zero, so exclude the pair even when its
  $x$-coordinates differ.
- **Duplicate coordinates under different IDs:** Both differences are zero;
  the pair is excluded, while each point may still form valid rectangles with
  other coordinates.
- **Negative coordinates:** `ABS` converts signed differences to positive
  side lengths.
- **Nonconsecutive IDs:** Pair orientation depends on numeric ID comparison,
  not input order or coordinate order.
- **Tied areas:** Include every valid pair and apply both ascending ID
  tie-breakers.
- **Fewer than two points:** Return an empty result with the required columns.

</details>
