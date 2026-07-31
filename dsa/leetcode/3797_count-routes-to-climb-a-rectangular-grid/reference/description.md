## Description

You are given a rectangular string array `grid` with `n` rows and `m` columns. A `'.'` marks an available cell, while `'#'` marks a blocked cell.

A climbing route begins at any available cell in the bottom row `n - 1` and finishes at an available cell in the top row `0`. Every move must go between two different available cells and satisfy all of these rules:

- Its Euclidean distance is at most `d`. Between `(r1, c1)` and `(r2, c2)`, that distance is $\sqrt{(r1-r2)^2+(c1-c2)^2}$.
- It either remains within the current row or moves exactly one row upward, from row `r` to row `r - 1`.
- Two consecutive moves may not both remain on the same row. After a same-row move, the next move must go upward unless the same-row move ends the route.

Return the number of different valid routes modulo $10^9+7$.
