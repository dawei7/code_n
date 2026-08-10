## General

**Compress a two-dimensional recurrence into one row**

For an open cell, paths arrive from above or from the left. A full DP table would store both predecessor counts explicitly. The selected solution reuses a one-dimensional list `ways`:

- before processing column `j` in the current row, `ways[j]` still holds the count from the cell above;
- after processing column `j`, `ways[j]` becomes the count for the current cell;
- `ways[j-1]` has already been updated and therefore holds the count from the left.

Adding those two values implements the same recurrence with only one row of storage.

**Seed the starting path**

`ways` starts as all zeros except `ways[0] = 1`. This represents one empty path located at the top-left before any cell is processed.

If the starting cell is open, processing `(0,0)` leaves this one intact because `j > 0` is false. If the start is blocked, the obstacle branch resets `ways[0]` to zero, correctly eliminating every possible path.

**Obstacles erase paths through their cell**

When `obstacleGrid[i][j] == 1`, the code assigns `ways[j] = 0`. The old value from above must not survive because paths cannot enter the obstacle, and zero ensures later cells in the row cannot receive paths through it from the left.

For an open cell with `j > 0`, `ways[j] += ways[j-1]` combines above and left. The two predecessor sets are disjoint by their final move direction.

**First-column behavior**

Before the inner loop, the source checks whether the first cell of the row is blocked and sets `ways[0]` to zero if so. The inner loop then checks that same obstacle again at `j = 0`, making the first assignment redundant but harmless.

For an open first-column cell, `j > 0` is false, so `ways[0]` retains its count from above. Once an obstacle sets it to zero, all lower first-column cells retain zero because there is no left predecessor that could restore a path.

**Row-scan invariant**

At the start of row `i`, `ways[j]` contains the path count for row `i-1`, column `j`, except `ways[0]` may already have been zeroed for the current row's first obstacle. During the inner scan, entries left of `j` hold current-row counts, while entries at and right of `j` still hold previous-row counts.

Obstacle zeroing or above-plus-left addition computes the exact current state at `j` and advances this boundary by one. At the end of the row, the whole array represents that row. Repeating through all rows leaves `ways[-1]` as the bottom-right path count.

**Trace through a blocked center**

For the three-by-three example, the first row evolves to `[1,1,1]`. In the second row, column 0 stays 1, the obstacle at column 1 becomes zero, and column 2 remains 1 from above. The final row becomes `[1,1,2]`, so two valid paths reach the destination.

**Why the result is exact**

The start seed, obstacle-zero rule, and open-cell sum are the correct base and recurrence for every coordinate. The row-major update order preserves the two needed predecessor values at each step. By induction over rows and columns, every `ways[j]` after update is exact, including the final returned entry.

The input grid is never changed, so obstacle facts remain stable throughout the traversal.

**Why old-row values do not leak into later rows**

Every array entry is overwritten conceptually when its cell is processed: an obstacle assigns zero, while an open cell keeps its above value and adds the already-current left value. By the end of a row, no entry still represents the earlier row. Reusing the same list is therefore a controlled rolling update, not an accidental mixture of two incomplete tables.

## Complexity detail

The nested loops inspect every one of the $mn$ cells once and do constant work, giving $O(mn)$ time.

`ways` has $n$ entries, and all other state is scalar. Auxiliary space is $O(n)$, matching the manifest. The source comment says $O(m+n)$, which is a valid looser upper bound but not tight for this implementation.

## Alternatives and edge cases

- **Orient storage to the shorter dimension:** Transpose the iteration conceptually so the rolling array has $\min(m,n)$ entries. The selected source always uses the column count.
- **Top-down memoization:** It visits reachable states naturally but can cache $O(mn)$ values and use recursion-stack space.
- **Full DP grid:** It is easiest to visualize but stores $mn$ counts when one previous row is enough.
- **Blocked start:** The initial one is immediately reset to zero, and all later counts remain unreachable from it.
- **Blocked destination:** Its final update sets `ways[-1]` to zero.
- **Obstacle after valid paths:** Resetting rather than adding prevents paths from passing through the blocked coordinate.
- **One row:** Counts propagate from left until an obstacle zeroes the path, after which all later cells remain zero.
- **One column:** `ways[0]` propagates downward until the first obstacle.
- **One open cell:** The starting one remains and is returned.
- **Redundant first-column check:** It writes the same zero again inside the inner loop but does not change correctness or complexity.
