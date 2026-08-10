## General

**Record updates lazily instead of rewriting cells.** The constructor stores the supplied matrix as `self.g` and creates an empty operation log `self.ops`. An update does not visit any cell. It appends the rectangle boundaries and new value as one tuple.

This makes even a very large subrectangle update constant-time: its effect is represented symbolically. The original matrix remains unchanged and serves as the baseline before any recorded update covers a queried coordinate.

**A later update overrides an earlier one.** To answer `getValue(row, col)`, the code examines operations from newest to oldest through `self.ops[::-1]`. The first rectangle containing the coordinate is the most recent assignment affecting that cell, so its stored value is immediately returned.

Containment uses inclusive comparisons on both dimensions: `r1 <= row <= r2` and `c1 <= col <= c2`. This matches the upper-left and bottom-right contract and includes boundary cells.

If no update rectangle contains the coordinate, the cell has never been changed logically. The correct value is the original `self.g[row][col]`.

**Why older matching operations may be ignored.** Suppose an early update paints the whole matrix five and a later update paints the bottom row ten. A bottom-row query finds the ten update first and returns it. Although the earlier five also covers the cell, it was overwritten there. A top-row query skips the ten rectangle, reaches the earlier five, and returns five.

This is exactly last-write-wins semantics. Searching backward allows the method to stop once the answer is known instead of applying every update in chronological order.

**The representation invariant.** After any operation sequence, `g` contains the initial values and `ops` contains every update in chronological order. The logical value of a cell is the value in the last log entry covering it, or its baseline matrix value when no such entry exists.

Appending an update preserves this definition by making it the last write for its covered cells and irrelevant elsewhere. Backward search implements the definition directly, proving both methods correct.

**Aliasing matters.** The constructor assigns `self.g = rectangle` rather than copying the nested lists. The class itself never mutates `g`, but external mutation of the original matrix after construction would change baseline values for cells not covered by updates. The judged usage normally treats the supplied rectangle as owned input.

**Python's reverse slice is a real copy.** `self.ops[::-1]` creates a reversed list before iteration. It takes time and temporary memory proportional to the number of updates, even if the newest update matches immediately. Using `reversed(self.ops)` would traverse lazily and avoid that copy while preserving behavior.

**Be precise about complexity.** If `U` updates have been recorded, update is amortized `O(1)`, while getValue is `O(U)` worst-case. The object permanently stores `O(U)` tuples, and the reverse slice adds `O(U)` transient space per query.

Thus the manifest's `O(U + Q)` time and `O(1)` space do not describe the general exact source when many queries scan the update log. Across `Q` queries, worst-case time is `O(UQ)` after `O(U)` update work, although early matches can reduce actual scanning.

## Complexity detail

Construction stores references and initializes a list in `O(1)` auxiliary work, excluding the already supplied matrix. Each append is amortized `O(1)`.

With `u` current updates, a query copies `u` tuple references and may test all `u` rectangles, taking `O(u)` time and `O(u)` temporary space. The retained operation log is also `O(u)`.

For a complete sequence, time is the sum of current log lengths examined by queries. In the worst case of `U` updates followed by `Q` uncovered queries, this is `O(UQ)`. Stored space is `O(U)` beyond the input matrix.

The coordinate and tuple operations are constant time.

## Alternatives and edge cases

- **Use reversed directly:** `reversed(self.ops)` avoids the copied reverse slice and reduces each query's temporary space to `O(1)`, while keeping `O(U)` worst-case time.
- **Eagerly update every cell:** Queries become `O(1)`, but one update costs the rectangle's area.
- **Two-dimensional lazy structures:** Segment trees or other range-update structures can improve larger workloads but are much more complex.
- **No updates:** The query falls through to the original matrix value.
- **Newest update covers the cell:** It is logically found first, though the reverse slice still copies the entire log.
- **Overlapping updates:** The most recent covering rectangle wins.
- **Disjoint updates:** Each affects only its own coordinates.
- **Boundary coordinate:** Inclusive comparisons correctly include rectangle edges and corners.
- **Whole-matrix update:** One tuple represents it; no cell loop occurs.
- **Repeated same value:** It is still a valid later write and may be returned.
- **Original matrix ownership:** External baseline mutation can be observed for never-updated cells because no copy is made.
- **Operation-log growth:** Updates are never compacted, so retained space grows linearly with update calls.
- **Complexity reporting:** Use `O(1)` update, `O(U)` query, and `O(U)` retained space for this source.
