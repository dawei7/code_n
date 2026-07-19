# Queries on Number of Points Inside a Circle

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/) |
| Frontend ID | 1828 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a list of points on the two-dimensional plane. Each point is represented as `[x, y]`, and several points may occupy the same coordinates; every occurrence is still a separate point.

Each query is `[xCenter, yCenter, radius]` and describes a circle. For every query, count the input points that lie inside the circle or exactly on its circumference. Return the counts in the same order as the queries.

### Function Contract

**Inputs**

- `points`: a list of $p$ integer coordinate pairs `[x, y]`, where $1 \le p \le 500$ and $0 \le x, y \le 500$.
- `queries`: a list of $q$ triples `[xCenter, yCenter, radius]`, where $1 \le q \le 500$, $0 \le \texttt{xCenter}, \texttt{yCenter} \le 500$, and $1 \le \texttt{radius} \le 500$.

**Return value**

- Return a list of $q$ integers. Entry $j$ is the number of occurrences in `points` whose coordinates are inside or on the circle described by `queries[j]`.

### Examples

**Example 1**

- Input: `points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]`
- Output: `[3,2,2]`

For the first query, `[1,3]` and `[3,3]` are on the boundary, while `[2,2]` is inside.

**Example 2**

- Input: `points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]`
- Output: `[2,3,2,4]`

**Example 3**

- Input: `points = [[0,0],[0,0],[3,4],[6,0]], queries = [[0,0,5]]`
- Output: `[3]`

Both copies of `[0,0]` count, and `[3,4]` lies exactly on the circumference.

### Required Complexity

- **Time:** $O(pq)$
- **Space:** $O(q)$

<details>
<summary>Approach</summary>

#### General

**Translate circle membership into a distance comparison**

For a query centered at $(c_x,c_y)$ with radius $r$, a point $(x,y)$ belongs to the circle precisely when

$$
(x-c_x)^2 + (y-c_y)^2 \le r^2.
$$

The non-strict inequality includes the circumference. Compare the squared quantities directly: square roots are unnecessary, and integer arithmetic avoids any floating-point rounding near the boundary.

**Evaluate every required point-query pair**

Process the queries in their original order. For one query, scan all points, compute the two coordinate differences, and increment that query's count whenever the squared-distance test succeeds. Append the completed count before moving to the next circle.

Each list entry is examined independently. Consequently, repeated coordinates contribute once per occurrence, as required; no coordinate deduplication is appropriate.

**Why the resulting counts are exact**

For a fixed query, the squared-distance inequality is equivalent to the geometric definition of being inside or on its circle because both distance and radius are nonnegative. The scan increments the count if and only if that predicate holds for each input occurrence. Therefore its final count contains every qualifying point exactly once and no nonqualifying point, and repeating this argument for every query gives the returned list.

#### Complexity detail

There are $q$ queries, and each scans all $p$ points with constant work per pair, for $O(pq)$ time. The returned list contains $q$ counts and uses $O(q)$ space. Excluding the required output, only the current radius, differences, and count are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Square-root distance:** Computing Euclidean distance with a square root is mathematically equivalent, but it is slower and introduces avoidable floating-point boundary concerns.
- **Enumerate integer coordinates in each circle:** A set of all lattice locations inside a query can answer membership checks, but constructing it costs work proportional to the circle's area and is wasteful when only the supplied points matter.
- **Spatial indexing:** A range tree, quadtree, or offline geometric method may improve repeated-query performance for much larger inputs, but its implementation and preprocessing overhead are unnecessary under the bounds here.
- **Circumference points:** Equality in the squared-distance test must count as inside.
- **Duplicate coordinates:** Count every occurrence in `points`; do not convert the input to a set.
- **No matches:** Append zero while preserving the query's position in the output.
- **Point at the center:** Its squared distance is zero, so it belongs to every valid query centered there.
- **Coordinate extremes:** Centers and points may lie at 0 or 500; subtract before squaring, and do not assume the full circle remains within the coordinate range.

</details>
