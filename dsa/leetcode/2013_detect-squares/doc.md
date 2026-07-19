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
