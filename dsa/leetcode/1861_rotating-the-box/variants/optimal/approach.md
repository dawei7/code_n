## General

**Separate rotation from gravity.** The method first constructs the box’s exact 90-degree clockwise orientation, including stones, obstacles, and empty cells. It then lets stones fall downward within each output column. Keeping these phases separate makes both coordinate mapping and obstacle behavior explicit.

If the input has `m` rows and `n` columns, the rotated result has `n` rows and `m` columns. `ans = [[None] * m for _ in range(n)]` allocates that shape.

**Map every input cell to its rotated coordinate.** Input cell `(i, j)` moves to output row `j` and output column `m - i - 1`. The assignment

`ans[j][m - i - 1] = boxGrid[i][j]`

implements that mapping for every cell. The reversal of the row index into the new column is what makes the rotation clockwise rather than counterclockwise.

After the nested loops, no `None` placeholder remains. Obstacles have rotated with the box, but they will stay fixed during the gravity phase.

**Process gravity one output column at a time.** Falling is vertical in the rotated box, so columns are independent. For each output column `j`, the method scans row indices from `n - 1` at the bottom upward to zero.

A deque `q` stores empty row positions available below the current scan point. Because rows are encountered bottom to top, they enter the deque from lower positions to higher positions. The front is therefore the lowest available empty destination.

**Empty cell handling.** When `ans[i][j] == "."`, row `i` is appended to `q`. A stone encountered later above it may fall into this position.

**Stone handling.** If the current cell contains a stone and `q` is nonempty, `q.popleft()` selects the lowest empty cell below within the same obstacle-separated segment. The destination becomes `"#"` and the stone’s old position becomes `"."`.

The old position is then appended to `q` because moving the stone created a new empty cell. It lies above all previously seen empty rows, so appending preserves the deque’s bottom-to-top order.

If `q` is empty, there is no reachable empty space below, so the stone stays.

**Obstacle handling.** When the scan reaches `"*"`, `q.clear()` discards every empty position below that obstacle. A stone above cannot pass through the obstacle, so those cells are not valid destinations. New empty cells found above it begin a fresh segment.

**Why choosing the lowest empty cell is correct.** Gravity makes a stone fall until the bottom, an obstacle, or another stone stops it. Among currently known reachable empties below, the lowest one is the farthest it can fall. Processing bottom-up ensures stones already placed below act as occupied support for later stones.

**Trace one column conceptually.** Suppose a rotated column from top to bottom is stone, empty, empty. Scanning upward starts with both empty rows in `q`, ordered bottom then middle. The stone moves to the bottom row, and its former top row becomes an available empty. The result is empty, empty, stone.

If an obstacle lies between the stone and those empties, clearing the deque at the obstacle prevents the illegal crossing.
Rotation visits every cell exactly once and applies the standard clockwise coordinate transform. During gravity, the deque invariant says it contains exactly the reachable empty rows below the scan position in the current obstacle segment, ordered lowest first. Empty, obstacle, and stone updates preserve that invariant. Therefore each stone is placed at its unique lowest reachable position. Processing every column yields the complete rotated box after gravity.

## Complexity detail

Let `N = m * n` be the number of cells. Rotation visits all `N` cells, and the gravity scan visits all `N` cells. Each row index enters and leaves a deque at most a constant number of times, so total time is `O(N)`.

The returned matrix uses `O(N)` space. A per-column deque can hold at most `n` row indices and is recreated for each column, so additional working space is `O(n)` at a time. Total space including output is `O(N)`.

## Alternatives and edge cases

- **Apply gravity before rotating:** In the original orientation, post-rotation downward corresponds to moving stones right. This can work but requires careful equivalence reasoning.
- **Write directly into the final matrix:** Rotation and falling can be combined segment by segment, reducing phases but increasing index complexity.
- **No stones:** Rotation copies obstacles and empties, and gravity makes no changes.
- **No empty cells:** Every deque remains empty and all stones stay after rotation.
- **Obstacle-separated regions:** Clearing the deque prevents stones from crossing boundaries.
- **Several stones above empties:** Bottom-up processing packs them at the bottom with no gaps.
- **Single row input:** It becomes one output column, and stones fall to its bottom.
- **Single column input:** Rotation produces one output row, so there is no vertical space for additional falling.
- **Input preservation:** All changes occur in `ans`; `boxGrid` is only read.
- **Output placeholders:** Every `None` is overwritten during complete rotation before gravity begins.
- **Deque order:** `popleft` selects the lowest reachable empty, while appending a moved stone’s origin preserves ordering.
- **Guaranteed initial rest:** The algorithm does not rely critically on it; the gravity phase still settles any represented stones correctly after rotation.
