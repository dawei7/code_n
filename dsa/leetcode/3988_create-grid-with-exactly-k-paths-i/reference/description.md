## Description

You are given three integers `m`, `n`, and `k`. Build any grid with `m` rows and `n` columns whose cells contain only `.` or `#`. A dot is a free cell, while a hash is an obstacle that cannot belong to a path.

A valid path starts at the top-left cell `(0, 0)`, finishes at the bottom-right cell `(m - 1, n - 1)`, and visits only free cells. Each move must go either one cell right, from `(i, j)` to `(i, j + 1)`, or one cell down, from `(i, j)` to `(i + 1, j)`.

Return any grid having exactly `k` valid paths between those two corners. If no grid with that path count exists for the requested dimensions, return an empty array.
