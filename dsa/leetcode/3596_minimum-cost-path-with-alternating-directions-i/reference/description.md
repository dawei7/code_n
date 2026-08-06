## Description

Consider an `m`-by-`n` grid whose rows and columns are zero-indexed. Entering cell `(i, j)` costs `(i + 1) * (j + 1)`. A path starts at `(0, 0)`, includes that cell's entrance cost, and aims to reach the bottom-right cell `(m - 1, n - 1)`.

Movement directions alternate. On the first, third, and every subsequent odd-numbered transition, move to an adjacent cell either right or down. On each even-numbered transition, move to an adjacent cell either left or up. Every move must remain inside the grid. Return the least possible sum of entrance costs along a valid path to the destination, or `-1` when the alternating rules make the destination unreachable.
