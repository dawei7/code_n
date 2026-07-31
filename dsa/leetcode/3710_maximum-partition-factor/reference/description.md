## Description

You are given a two-dimensional integer array `points`, where `points[i] = [x_i, y_i]` is the position of point $i$ in the Cartesian plane.

For points $i$ and $j$, their **Manhattan distance** is

$$
\lvert x_i-x_j\rvert+\lvert y_i-y_j\rvert.
$$

Divide all $n$ points into exactly two non-empty groups. A split's **partition factor** is the minimum Manhattan distance over every unordered pair of points that belongs to the same group.

Return the greatest partition factor achievable by any valid split.
