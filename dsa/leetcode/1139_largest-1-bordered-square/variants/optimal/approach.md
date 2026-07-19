## General
**Precompute directional evidence.** For every cell, record `right[row][column]`, the number of consecutive `1`s beginning there and extending right, and `down[row][column]`, the analogous downward run. Fill both tables from bottom-right toward top-left so the neighboring run needed by each recurrence is already known.

**Test a border with four table lookups.** Consider a square with upper-left corner `(row, column)` and side `side`. Its top and left edges are complete exactly when `right[row][column] >= side` and `down[row][column] >= side`. Its bottom edge begins at `(row + side - 1, column)`, and its right edge begins at `(row, column + side - 1)`. The corresponding two run-length comparisons certify those edges. Interior entries never participate in these checks.

**Search areas from largest to smallest.** Enumerate `side` from $q$ down to `1`, and try every upper-left corner for which the square fits. The first certified border has the largest possible side because all larger side lengths were exhausted first; return `side * side` immediately. If no side-one square is found, every cell is zero and the answer is `0`.

The four comparisons are both necessary and sufficient: each covers one complete edge, including the corners, and together they cover the entire border. Descending enumeration therefore cannot return an invalid square or overlook a larger valid one.

## Complexity detail
The run-length tables take $O(mn)$ time to build. There are at most $q$ side lengths and at most $mn$ candidate upper-left corners per length, with $O(1)$ work per candidate, giving $O(mnq)$ time. The two $m \times n$ tables use $O(mn)$ auxiliary space.

## Alternatives and edge cases
- **Rescan every candidate border:** Directly inspect up to $O(q)$ cells for each of $O(mnq)$ candidates, increasing the worst-case time to $O(mnq^2)$.
- **Row and column prefix sums:** Four range-sum queries can also certify a border in constant time after $O(mn)$ preprocessing, with the same overall enumeration bound.
- **Filled-square dynamic programming:** The recurrence for a square containing only `1`s is too strict because zeros are allowed inside this problem's border.
- **Interior zeros:** They do not disqualify a square; only its four edges matter.
- **Single row or column:** The maximum side is one, so the result is `1` if any cell is `1`, otherwise `0`.
- **Broken corner:** A zero at any corner breaks two edges and invalidates that candidate.
