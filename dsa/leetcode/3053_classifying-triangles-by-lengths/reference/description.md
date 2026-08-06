## Description

Each row of `Triangles` provides three proposed side lengths, `A`, `B`, and
`C`. First determine whether those lengths can form a non-degenerate triangle:
the sum of every pair of sides must be strictly greater than the remaining
side. Equality is not sufficient because it produces a flat figure.

Classify every valid triangle by equality among its sides. Three equal lengths
produce `Equilateral`; exactly two equal lengths produce `Isosceles`; and
three different lengths produce `Scalene`. Return `Not A Triangle` whenever
the triangle inequalities fail. The result may be returned in any order.
