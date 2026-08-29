# Number of Ways to Build Sturdy Brick Wall

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2184 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/) |

## Problem Description

### Goal

Build a wall with `height` rows, each exactly `width` units long. Every
available brick is one unit high and has a width listed in the unique array
`bricks`. Each brick type has an unlimited supply, but bricks cannot be
rotated.

Within a row, adjacent bricks create vertical joints at their meeting
positions. The wall is sturdy only when two adjacent rows have no joint at the
same interior position; their shared boundaries at the two ends are allowed.
Count all sturdy walls and return the result modulo $10^9+7$.

### Function Contract

**Inputs**

- `height`: the number of rows, with $1\le\texttt{height}\le100$.
- `width`: the required length of each row, with
  $1\le\texttt{width}\le10$.
- `bricks`: between one and ten distinct permitted brick widths, each in
  `[1,10]`.

Let $R$ be the number of distinct row layouts that exactly fill `width`, and
let $E$ be the number of ordered pairs of layouts with disjoint interior
joints.

**Return value**

Return the number of sturdy walls modulo $10^9+7$. Return zero if no row can
be filled exactly.

### Examples

#### Example 1

- **Input:** `height = 2`, `width = 3`, `bricks = [1,2]`
- **Output:** `2`

#### Example 2

- **Input:** `height = 1`, `width = 1`, `bricks = [5]`
- **Output:** `0`

#### Example 3

- **Input:** `height = 10`, `width = 5`, `bricks = [5]`
- **Output:** `1`
