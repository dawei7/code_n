## General
A tempting forward dynamic program asks how much health the knight has upon reaching each cell. That state is insufficient: a path with a larger current total may already have dipped to zero earlier, and two paths with the same current health may require different initial health. The useful state runs in the opposite direction.

Let `need[r][c]` mean the minimum health the knight must have **immediately before entering** cell `(r, c)` to reach the princess while never falling below one. If the cheaper of the right and downward continuations requires `next_need`, then the current cell changes health by `dungeon[r][c]`, giving

`need[r][c] = max(1, next_need - dungeon[r][c])`.

The clamp to one handles beneficial rooms. If a room adds more health than the remainder of the path requires, the knight still cannot enter with zero or negative health.

At the destination, the same formula applies if the required health after leaving it is defined as one. An implementation can place a sentinel `1` immediately right of the destination (or immediately below it) and infinity at other out-of-grid positions. This avoids separate transition logic while ensuring no path exits through an invalid boundary.

Process cells from bottom-right toward top-left. A one-dimensional array is sufficient: before updating column `c`, `dp[c]` holds the requirement for the cell below, while `dp[c + 1]` already holds the newly computed requirement to the right. Use the smaller of those two continuations.

In the example grid, the destination value `-5` requires `6` health on entry. The beneficial `30` to its left requires only `1`, while the `1` above the destination requires `5`. Propagating these requirements backward eventually yields `7` at the entrance. The result is not the path with the greatest final health; it is the smallest starting reserve that survives every prefix of one complete path.

At the destination, `max(1, 1 - dungeon[r][c])` is exactly the least entry health that remains positive after the final room. Assume the requirements to the right and below a cell are correct. Any valid path must choose one of those neighbors, and choosing the smaller requirement cannot demand more starting health than choosing the larger one. Entering with `max(1, next_need - cell_value)` is sufficient because the room then leaves at least `next_need` health, and it is minimal because any smaller positive value either dies in the room or leaves too little for either continuation. Backward induction proves every state, including the top-left answer.

## Complexity detail
Each of the $m \cdot n$ cells is evaluated once, so time is $O(mn)$. Compressing the next row into a `dp` array uses $O(n)$ space when `n` is the column count. The uncompressed recurrence would use $O(mn)$ space.

## Alternatives and edge cases
- Greedily choosing the largest immediate health gain fails because a locally attractive route may contain a fatal later loss.
- A forward state containing only maximum current health loses the minimum-prefix information needed to decide survivability.
- A full two-dimensional backward table is correct and sometimes easier to visualize, but stores states that are no longer needed.
- A nonnegative single cell still requires one initial health; a cell `-x` requires $x + 1$.
- All-positive, all-negative, one-row, and one-column dungeons use the same recurrence without special path logic.
