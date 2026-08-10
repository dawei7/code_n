## General

**Store how many extra levels each fertile apex can support**

A single fertile cell has height 1, but it is not counted because a valid plot must contain more than one cell. For each position, the dynamic program stores the number of valid height extensions beyond that single apex.

The meaning of `f[i][j]` in the first pass is:

- `-1` if the cell is barren;
- `0` if the cell is fertile but supports no downward pyramid of height 2;
- `t > 0` if the largest downward pyramid with apex `(i, j)` has height `t + 1`.

This offset makes counting convenient. If the largest height is `t + 1`, then the valid pyramid heights are 2, 3, ..., `t + 1`, exactly `t` different plots with this apex. The code can therefore add `f[i][j]` directly to `ans`.

**Build ordinary pyramids from bottom to top**

An ordinary pyramid points downward: its apex is above its wider rows. To know how far an apex can extend, the cells in the row below must already be solved. The first loop consequently processes `i` from `m - 1` down to 0.

For a fertile interior cell, the recurrence is

`min(f[i + 1][j - 1], f[i + 1][j], f[i + 1][j + 1]) + 1`.

Why are all three lower cells needed? Extending a pyramid by one row requires fertile support down-left, directly down, and down-right. For more levels, those three positions must themselves support the corresponding smaller triangular regions. The shortest of the three available extensions is the limiting side, so the recurrence takes their minimum.

If any required lower cell is barren, its value is `-1`. The minimum becomes `-1` and adding one yields 0, correctly saying the current fertile cell supports only height 1 and contributes no counted pyramid.

Bottom-row cells and left or right boundary cells cannot be apexes of height 2 in the downward direction because some required cell would lie outside the grid. Their initially allocated value remains 0. Outside-grid cells are considered barren, and leaving these boundary values at zero produces the same non-counting result without indexing outside the matrix.

**Why one apex can contribute several plots**

Suppose `f[i][j] = 3`. The maximum pyramid height is 4. The same apex defines three different valid plots:

- use only the first two rows for height 2;
- use the first three rows for height 3;
- use all four rows for height 4.

Every smaller prefix of a fully fertile pyramid is also fully fertile. Therefore, adding 3 counts all possible heights for that apex, not just the largest one.

This is why the algorithm does not merely increment `ans` once when the recurrence is positive.

**Reuse the matrix for inverse pyramids**

An inverse pyramid points upward, so its apex is the bottommost cell and its supporting rows lie above it. The second pass scans from top to bottom, ensuring row `i - 1` already contains inverse-direction DP values.

Before applying the recurrence, it resets the meanings that cannot carry over from the downward pass:

- barren cells become `-1`;
- fertile cells on the top row or either side boundary become 0;
- other fertile cells use the minimum of the three cells above, plus one.

The inverse recurrence is

`min(f[i - 1][j - 1], f[i - 1][j], f[i - 1][j + 1]) + 1`.

Its interpretation mirrors the first pass. The new `f[i][j]` counts the number of inverse-pyramid heights of at least 2 whose bottom apex is `(i, j)`. Adding it to the same `ans` combines ordinary and inverse plots.

Reusing `f` is safe because the second pass reads only the immediately previous row in its current upward-oriented meaning. By the time row `i` is processed, old downward values in that row are overwritten before later rows depend on them.

**Why the recurrence captures the full triangular area**

For height 2, the apex and the three adjacent cells in the next row must be fertile. Values 0 at all three supports make the recurrence 1, counting that height.

Assume the values correctly describe all pyramids up to some height. A pyramid of height $h>2$ below `(i,j)` consists of the apex plus overlapping downward pyramidal regions rooted at the three neighboring cells in row `i+1`. All three must extend at least $h-1$ rows in their local representation. The minimum support length is therefore exactly the maximum common extension.

This inductive structure covers every cell across each required width, not merely the two slanted borders. The center support is necessary to guarantee the interior remains fertile.

The inverse pass has the identical argument with row direction reversed.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns.

Each pass visits all $mn$ cells and performs constant work per cell. Two full passes are still $O(mn)$ time.

The exact source allocates `f = [[0] * n for _ in range(m)]`, an $m$ by $n$ matrix. Its executable auxiliary space is therefore $O(mn)$, not the $O(n)$ stated in the branch manifest.

An $O(n)$ implementation is possible because each recurrence needs only the adjacent previously processed row. It could keep a rolling row for each directional pass. That optimization is not present in this solution file, so the documentation must distinguish the possible bound from the actual allocation.

The scalar answer and loop variables use constant additional storage beyond `f`.

## Alternatives and edge cases

- **Enumerate every apex and height:** Explicitly checking every triangular area repeats cell work and can become far slower than linear in the grid size. DP summarizes the maximum common extension once per cell.
- **Check only diagonal borders:** A triangle may have fertile edges but barren interior cells. The three-child recurrence includes center support and therefore covers the full area.
- **Rolling-row DP:** Retaining only the next row for downward pyramids and the previous row for inverse pyramids reduces auxiliary space to $O(n)$. The exact source instead keeps and reuses a full matrix.
- **Rotate the grid:** One could count ordinary pyramids, reverse row order, and repeat. Reversing or copying the grid is unnecessary because changing traversal direction gives the inverse recurrence directly.
- **Barren apex:** Its value is `-1` so a parent depending on it cannot extend through that position.
- **Fertile cell with barren support:** The recurrence yields zero, meaning height 1 only, which is correctly not counted.
- **Single row or single column:** No plot can have height at least 2. Every fertile cell remains at extension zero, so the answer is zero.
- **Boundary apex:** A height-2 plot would extend outside the grid, which is considered barren. Boundary values remain zero.
- **All fertile grid:** Many nested heights share each apex. Adding the extension value counts each allowable height separately.
- **Ordinary and inverse overlap:** The same cells may participate in plots of both orientations. They are distinct plots and are intentionally counted in separate passes.
- **Matrix reuse:** Boundary and barren values must be reset in the inverse pass. Leaving downward values there would contaminate the new direction.
- **Manifest-space discrepancy:** The claimed $O(n)$ bound describes a rolling optimization, while `f` in the exact code visibly contains $mn$ entries.
