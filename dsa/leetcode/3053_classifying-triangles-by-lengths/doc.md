# Classifying Triangles by Lengths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3053 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/classifying-triangles-by-lengths/) |

## Problem Description

### Goal

Each row of `Triangles` provides three proposed side lengths, `A`, `B`, and
`C`. First determine whether those lengths can form a non-degenerate triangle:
the sum of every pair of sides must be strictly greater than the remaining
side. Equality is not sufficient because it produces a flat figure.

Classify every valid triangle by equality among its sides. Three equal lengths
produce `Equilateral`; exactly two equal lengths produce `Isosceles`; and
three different lengths produce `Scalene`. Return `Not A Triangle` whenever
the triangle inequalities fail. The result may be returned in any order.

### Function Contract

**Inputs**

- `Triangles(A, B, C)`: Each row contains three integer side lengths, and the
  tuple `(A, B, C)` is the primary key.

Let $n$ be the number of rows.

**Return value**

- A one-column table named `triangle_type`, with one classification for every
  input row. Row order is unrestricted.

### Examples

**Example 1**

Sides `(20, 20, 23)` form an `Isosceles` triangle because exactly two sides
are equal and all triangle inequalities hold.

**Example 2**

Sides `(20, 20, 20)` are `Equilateral`, while `(20, 21, 22)` are `Scalene`.

**Example 3**

Sides `(13, 14, 30)` yield `Not A Triangle` because $13+14 \le 30$.
