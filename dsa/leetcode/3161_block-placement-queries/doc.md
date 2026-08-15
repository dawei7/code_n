# Block Placement Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3161 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Binary Indexed Tree, Segment Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/block-placement-queries/) |

## Problem Description

### Goal

Consider an infinite number line that begins at the origin and extends along the positive $x$-axis. Process a sequence of two kinds of queries in order.

A query `[1, x]` builds an obstacle at coordinate `x`. The input guarantees that no obstacle is already present there. A query `[2, x, sz]` asks whether a block of length `sz` can be positioned anywhere inside the closed interval $[0, x]$. The entire block must remain within that interval and may not intersect an obstacle, although either endpoint of the block may touch one. This query is only a check: it does not place the block, and therefore does not affect later queries.

Return one boolean for every type-2 query, in their original order, indicating whether such a placement exists.

### Function Contract

**Inputs**

- `queries`: A sequence of queries, each either `[1, x]` or `[2, x, sz]`.

Let $q$ be the number of queries and let $C$ be one more than the largest coordinate appearing in them. The constraints satisfy $1 \le q \le 150000$ and $1 \le x, sz \le \min(50000, 3q)$. Every type-1 coordinate is new when inserted, and at least one type-2 query is present.

**Return value**

- A list of booleans containing one answer for each type-2 query.

### Examples

#### Example 1

- **Input:** `queries = [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]`
- **Output:** `[false, true, true]`

An obstacle at coordinate `2` leaves no obstacle-free interval of length `3` inside $[0,3]$. Length `1` fits, and a length-`2` block can exactly touch the obstacle at its right endpoint.

#### Example 2

- **Input:** `queries = [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]`
- **Output:** `[true, true, false]`

Before the second obstacle is added, the interval from `0` to `7` can hold the length-`6` block. Adding an obstacle at `2` splits that space; the largest remaining gap has length `5`, so the last two checks differ.
