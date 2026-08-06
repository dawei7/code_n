## Description

You are given an array `points` where `points[i] = [x_i, y_i]` is the coordinates of the `i^th` point on a 2D plane. Multiple points can have the **same** coordinates.

You are also given an array `queries` where `queries[j] = [x_j, y_j, r_j]` describes a circle centered at `(x_j, y_j)` with a radius of `r_j`.

For each query `queries[j]`, compute the number of points **inside** the `j^th` circle. Points **on the border** of the circle are considered **inside**.

Return *an array *`answer`*, where *`answer[j]`* is the answer to the *`j^th`* query*.
