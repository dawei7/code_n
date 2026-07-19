## General
For every possible top-left corner, inspect the nine cells in its 3 by 3 window. The center of any normal 3 by 3 magic square is `5`, so that constant-time check can reject many candidates immediately. Then collect the nine values and require their set to be exactly `{1, 2, ..., 9}`; this simultaneously enforces the allowed range and distinctness.

Those nine distinct numbers have total $45$, so if all three row sums are equal, their common value must be $15$. Check each row, each column, and both diagonals against $15$. A candidate is counted only if every condition succeeds.

Every contiguous 3 by 3 subgrid has exactly one enumerated top-left corner. The value-set test enforces the membership part of the definition, and the eight sum tests enforce all required lines. Therefore a window is counted if and only if it is a magic square, and summing the accepted windows returns the requested total.

## Complexity detail
There are at most $(r-2)(c-2)$ candidate windows. Each performs work on exactly nine values and eight fixed lines, so the total time is $O(rc)$. The temporary set contains at most nine integers, which is constant-sized, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Lo Shu perimeter pattern:** Every normal 3 by 3 magic square is a rotation or reflection of one pattern, so its perimeter can be matched against valid cyclic orders; this is fast but less direct and easier to index incorrectly.
- **Rescan the full grid per window:** Filtering all grid cells to extract each 3 by 3 candidate is correct but costs $O(r^2c^2)$ time instead of examining only nine cells.
- **Grid smaller than 3 by 3:** No candidate top-left position exists, so the result is zero.
- **Duplicate in-range value:** Correct line sums alone are insufficient; the values must also be distinct and cover `1` through `9`.
- **Value outside 1 through 9:** Even if some sums happen to be `15`, the window is not a magic square.
- **Overlapping windows:** Each valid top-left position contributes independently.
