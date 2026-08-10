## General

This is an unweighted shortest-path problem whose state must include both the snake’s position and orientation. Breadth-first search explores every legal state in increasing number of moves.

**Encode a state compactly**

Queue entries store flattened indices `a` and `b` for the snake’s two occupied cells. Index `r * n + c` represents coordinate `(r, c)`.

The first cell is always the left cell when horizontal or the top cell when vertical. Therefore, its flattened index `a` plus orientation uniquely determines the second cell: `a + 1` horizontally or `a + n` vertically.

The visited set uses `(a, status)`, where status zero means the two rows match and status one means vertical. It does not need `b` because `b` is implied. The start occupies `(0,0)` and `(0,1)`, encoded in the queue as `(0, 1)` and in visited as `(0, 0)`.

**Centralize state validation**

The helper `move` receives two target coordinates. It checks all four bounds, both grid cells are empty, and the compact state has not been visited. It then appends flattened endpoints and records anchor plus orientation.

Marking on enqueue prevents different parents from inserting the same state.

**Generate translations and rotations**

Moving right adds one column to both endpoints. Moving down adds one row to both. The helper verifies both destination cells.

For a horizontal snake, clockwise rotation keeps the left anchor and places the second cell below it. The entire two-by-two area below must be clear. The outer check verifies the lower-right cell, while `move` verifies the anchor and lower-left target.

For a vertical snake, counterclockwise rotation keeps the top anchor and places the second cell to its right. The outer check verifies the bottom-right swept cell, while `move` verifies the two final cells.

These extra corner checks prevent rotating through an obstacle even when the final pair alone is empty.

**BFS layers give the minimum**

`ans` is the move count for the current queue layer. The inner loop processes the captured layer size, while generated states wait for the next layer. The target flattened pair is the final row’s last two cells.

When that pair is dequeued, every state reachable in fewer moves has already been processed. The returned `ans` is therefore minimal. If the queue empties, every reachable legal state was explored and the target is impossible, so `-1` is correct.

There are only two orientations for each possible anchor, giving $O(n^2)$ states rather than an unbounded movement history.

**Why the rotation checks cover the complete two-by-two square**

Suppose the snake is horizontal at top-left anchor `(r, c)`, occupying `(r, c)` and `(r, c + 1)`. A clockwise rotation ends at `(r, c)` and `(r + 1, c)`. The lower-right cell `(r + 1, c + 1)` is not part of the final snake, but it lies in the square through which the rotation occurs and must be empty. The outer condition checks that lower-right cell; `move` checks the lower-left destination and the unchanged anchor.

The vertical case is symmetric. From `(r, c)` and `(r + 1, c)`, counterclockwise rotation ends horizontally at `(r, c)` and `(r, c + 1)`. The bottom-right cell must also be empty. Separating the swept-corner check from the generic final-state helper keeps `move` reusable for translations.

**Why endpoint order never becomes ambiguous**

Every generated translation adds the same offset to both endpoints, preserving their top-or-left ordering. Each rotation explicitly passes the unchanged anchor first and the new cell second. Consequently, the code never stores the same geometric snake once with endpoints reversed. Without this canonical order, the visited representation could treat equivalent states as different and double the search work.

It also makes the target pair comparable directly, without normalizing endpoint order at dequeue time.

## Complexity detail

There are at most $2n^2$ compact anchor-orientation states. Each is enqueued once and generates a constant number of moves. Time complexity is $O(n^2)$.

The queue and visited set can each hold $O(n^2)$ states. Auxiliary-space complexity is $O(n^2)$.

## Alternatives and edge cases

- **Three-dimensional distance array:** Store distance by row, column, and orientation instead of a set plus BFS layers. It has the same bounds.
- **A-star search:** A heuristic may explore fewer states but adds complexity without improving the worst-case state bound.
- **Blocked translation cell:** Both resulting occupied cells must be empty; the helper checks them uniformly.
- **Blocked rotation corner:** The extra cell swept through the two-by-two square must also be empty.
- **Start already at target:** For `n = 2`, the start pair equals the target and BFS returns zero.
- **Same anchor, different orientation:** They are distinct states and must have different visited keys.
- **Flattening:** Division and remainder recover row and column without storing coordinate tuples.
- **Unreachable target:** Exhausting the finite state graph returns `-1`.
- **Visited on enqueue:** This preserves shortest discovery and avoids duplicate work.
- **Target orientation:** The required final pair is horizontal; a vertical snake near the corner is not sufficient.
