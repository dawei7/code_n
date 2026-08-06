## Description

There is a regular convex polygon with `n` vertices. The vertices are labeled from `0` to `n - 1` in a clockwise direction, and each vertex has **exactly one monkey**. The following figure shows a convex polygon of `6` vertices.

<img alt="" src="https://assets.leetcode.com/uploads/2023/01/22/hexagon.jpg" style="width: 300px; height: 293px;" />
Simultaneously, each monkey moves to a neighboring vertex. A **collision** happens if at least two monkeys reside on the same vertex after the movement or intersect on an edge.

Return the number of ways the monkeys can move so that at least **one collision** happens. Since the answer may be very large, return it modulo `10^9 + 7`.
