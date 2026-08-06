## Description

You are given two positive integers `xCorner` and `yCorner`, and a 2D array `circles`, where `circles[i] = [x_i, y_i, r_i]` denotes a circle with center at `(x_i, y_i)` and radius `r_i`.

There is a rectangle in the coordinate plane with its bottom left corner at the origin and top right corner at the coordinate `(xCorner, yCorner)`. You need to check whether there is a path from the bottom left corner to the top right corner such that the **entire path** lies inside the rectangle, **does not** touch or lie inside **any** circle, and touches the rectangle **only** at the two corners.

Return `true` if such a path exists, and `false` otherwise.
