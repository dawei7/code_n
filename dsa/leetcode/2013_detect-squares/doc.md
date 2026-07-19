# Detect Squares

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2013 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Design, Counting, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/detect-squares/) |

## Problem Description

### Goal

Maintain a multiset of points from a stream on the $x$-$y$ plane. Adding the
same coordinate more than once creates distinct stored points.

For a query point, count the ways to choose three stored points so that those
points together with the query form an axis-aligned square of positive area.
Its four sides must be parallel or perpendicular to the coordinate axes and
have equal nonzero length. Duplicate coordinate occurrences multiply the
number of choices.

### Function Contract

Let $P$ be the number of stored point occurrences and $H$ the number of
distinct stored $x$-coordinates on the query point's horizontal row.

**Operations**

- `DetectSquares()` initializes an empty structure.
- `add([x, y])` stores one occurrence of the coordinate.
- `count([x, y])` returns the number of qualifying square choices using the
  supplied coordinate as one corner.
- Coordinates satisfy $0\le x,y\le1000$, and at most $3000$ calls to `add` and
  `count` occur.

**Return value**

For the app-local operation stream, return one output per operation: `null` for
construction and additions, and the integer result for each count.

### Examples

**Example 1**

- Input: add `[3, 10]`, `[11, 2]`, and `[3, 2]`; then count `[11, 10]`
- Output: `1`
- Explanation: The three stored points complete one square of side length
  eight.

**Example 2**

- Input: the preceding points followed by count `[14, 8]`
- Output: `0`
- Explanation: No stored horizontal partner can complete an axis-aligned
  square for that query.

**Example 3**

- Input: add a second occurrence of `[11, 2]`; then count `[11, 10]` again
- Output: `2`
- Explanation: Either occurrence at `[11, 2]` can be chosen, so the same
  coordinate square contributes twice.

### Required Complexity

- **Time:** $O(H)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Store multiplicities globally and by horizontal row.** A counter keyed by
`(x, y)` records how many occurrences exist at every coordinate. A second map
from each `y` to its counter of `x` values lets a query inspect only possible
horizontal partners. Each addition increments both counters.

**Use each horizontal partner to determine both possible squares.** For query
`(x, y)` and stored partner `(other_x, y)`, let
`side = other_x - x`. Ignore `side == 0`, which would produce zero area. The
other two corners are either `(x, y + side)` and
`(other_x, y + side)`, or the corresponding coordinates at `y - side`.
For each orientation, multiply the occurrence counts at all three stored
corners and add the product.

Every positive-area axis-aligned square containing the query has exactly one
other corner on the query's horizontal row. That corner fixes its signed side
length and the two remaining coordinates, so the scan reaches the square
exactly once. Conversely, every nonzero product represents independent choices
of the three required stored occurrences, including duplicates. The sum
therefore equals the number of valid ways.

#### Complexity detail

An addition takes average $O(1)$ time. A count visits the $H$ distinct
horizontal coordinates on the query row and performs constant-time counter
lookups for each, taking $O(H)$ time. Storing counters for $P$ occurrences uses
$O(P)$ space in the worst case.

#### Alternatives and edge cases

- **Scan every stored coordinate:** Testing each point as a possible diagonal
  or horizontal corner takes $O(P)$ per count even when the query row is
  sparse.
- **Enumerate triples:** Choosing every three stored points is conceptually
  direct but requires cubic work before geometry checks.
- Repeated additions at one coordinate are distinct choices and multiply the
  result rather than being deduplicated.
- A stored point sharing both query coordinates cannot define a positive side
  length and must be ignored as a horizontal partner.
- Squares may extend above or below the query row, including coordinates at
  the legal boundaries $0$ and $1000$.

</details>
