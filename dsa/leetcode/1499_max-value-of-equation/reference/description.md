## Description

You are given an array `points` containing the coordinates of points on a 2D plane, sorted by the x-values, where `points[i] = [x_i, y_i]` such that `x_i < x_j` for all `1 <= i < j <= points.length`. You are also given an integer `k`.

Return *the maximum value of the equation *`y_i + y_j + |x_i - x_j|` where `|x_i - x_j| <= k` and `1 <= i < j <= points.length`.

It is guaranteed that there exists at least one pair of points that satisfy the constraint `|x_i - x_j| <= k`.
