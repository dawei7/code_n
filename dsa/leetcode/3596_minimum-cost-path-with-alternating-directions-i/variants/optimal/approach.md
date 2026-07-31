## General
**Analyze the first two transitions:** From `(0, 0)`, the first transition can only reach `(0, 1)` or `(1, 0)`, when that cell exists. The following transition must go left or up. From `(0, 1)`, moving up would leave the grid, so left is the only legal choice and returns to `(0, 0)`. Symmetrically, `(1, 0)` can only move up to the origin.

The same argument repeats after every return to the origin. Consequently, no path can ever visit a cell other than `(0, 0)`, `(0, 1)`, or `(1, 0)`. The destination is reachable only when the grid is `1` by `1`, `1` by `2`, or `2` by `1`.

For a single-cell grid, the total is just the entrance cost of `(0, 0)`, which is `1`. In either one-step grid, the destination has entrance cost `2`, so the total is `1 + 2 = 3`. Every other dimension pair must return `-1`. These cases are exhaustive because the two-transition cycle prevents any additional progress.

## Complexity detail
The algorithm performs a fixed number of integer comparisons and one addition, independent of the values of `m` and `n`. Time is $O(1)$ and space is $O(1)$.

## Alternatives and edge cases
- **Graph search with move parity:** Breadth-first search over `(row, column, parity)` states can establish reachability, but it wastes up to $O(mn)$ time and space on a structure whose boundary behavior gives a constant-time proof.
- **Dynamic programming:** Recording the cheapest cost at every cell and parity is similarly unnecessary because the reachable component contains at most three cells.
- **Single cell:** No transition is needed; the starting entrance cost is still paid, so the answer is `1`.
- **One legal transition:** Both `1` by `2` and `2` by `1` cost `3` and are the only nontrivial reachable grids.
- **Long single row or column:** A second forward step is impossible because every even transition must undo the first one.
- **Two positive dimensions:** When both dimensions exceed `1`, the diagonal destination cannot be either one-step neighbor of the origin.
