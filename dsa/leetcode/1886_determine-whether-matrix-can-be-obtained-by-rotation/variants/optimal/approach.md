## General

**There are only four possible orientations.** Rotating a square matrix by 90 degrees four times returns to the original arrangement. Therefore, every allowed result is one of the 0-degree, 90-degree, 180-degree, or 270-degree orientations. The source checks all four possibilities simultaneously while scanning the target rather than physically rotating `mat` four times.

**Store surviving orientations as bits.** Variable `ok` starts as binary `0b1111`. Each of its four low bits means that one orientation is still compatible with every cell examined so far. When a comparison for an orientation fails, the code clears only that orientation's bit with `ok &= ~bit`. A cleared bit can never become viable later because one mismatching cell is enough to disprove whole-matrix equality.

Although Python's `~` produces a negative integer with conceptually unbounded leading one bits, AND with the current four-bit `ok` clears the intended low bit and leaves the other candidate bits unchanged. For example, `ok &= ~0b0010` removes the second orientation but preserves the first, third, and fourth.

**Compare each target cell with four source coordinates.** For every target position `(i, j)`, the code reads:

- `mat[i][j]` for the original orientation;
- `mat[j][n - 1 - i]` for one quarter-turn orientation;
- `mat[n - 1 - i][n - 1 - j]` for the half-turn orientation;
- `mat[n - 1 - j][i]` for the other quarter-turn orientation.

These are exactly the source positions that land at target coordinate `(i, j)` under the four rotations. The two quarter-turn formulas correspond to opposite rotation directions, but both belong to the same allowed cycle of 90-degree increments. Each value is compared with `target[i][j]`. A mismatch clears the associated bit.

**Derive the coordinate transformations.** Under a clockwise quarter-turn, original coordinate `(r, c)` moves to `(c, n - 1 - r)`. Solving for the source of target `(i, j)` gives `(n - 1 - j, i)`, the fourth lookup. Under a counterclockwise quarter-turn, the source is `(j, n - 1 - i)`, the second lookup. Applying either quarter-turn twice gives `(n - 1 - i, n - 1 - j)`, the third lookup. Zero turns leave `(i, j)` unchanged.

**Eliminate candidates monotonically.** Suppose the identity bit remains set after some prefix of cells. That means every identity comparison seen so far matched. If a later identity cell differs, its bit is cleared. The same statement holds independently for every rotation. Thus after processing a cell, `ok` represents exactly the orientations matching all cells up through that point. No candidate needs a mismatch counter or a separate matrix.

**Return early only when no recovery is possible.** After the four comparisons for a cell, the code checks `if ok == 0: return False`. Once all bits are zero, every orientation already has at least one witnessed mismatch. Future cells cannot erase those mismatches or restore a bit, so false is certain and scanning can stop. If the loops finish, `ok != 0` means at least one orientation matched every one of the $n^2$ target cells, so true is returned.

**Trace a two-by-two orientation.** For `mat = [[0, 1], [1, 0]]` and `target = [[1, 0], [0, 1]]`, identity fails at target position `(0, 0)` because `mat[0][0] = 0`. A quarter-turn lookup reads a source corner containing one and remains viable. As remaining cells are scanned, that same orientation continues matching all target values, while incompatible bits are cleared. At least one bit survives, so the method returns true.

**Why simultaneous checking is correct.** Every legal rotation has one of the four coordinate maps listed above. For any one map, its bit survives exactly when every source value selected by that map equals the corresponding target value. Equality at all $n^2$ positions is precisely matrix equality. Therefore a nonzero final mask exists exactly when at least one allowed rotation produces `target`. The bitmask changes only how four Boolean candidates are stored; it does not approximate the comparison.

**Inputs remain unchanged.** Unlike in-place rotation simulation, the source only reads from `mat` and `target`. This avoids mutation, avoids restoring the matrix after failed orientations, and keeps the auxiliary state to one integer plus loop indices.

## Complexity detail

The nested loops visit all $n^2$ cells in the worst case. At each cell, four comparisons, four possible bit clears, and one mask test take constant time. Four is a fixed number of orientations, so total time is $O(n^2)$. Early exit can reduce work on incompatible matrices but does not change the worst-case bound.

The algorithm allocates no rotated matrix and no structure depending on $n$. `ok`, `n`, and loop indices use $O(1)$ auxiliary space. The input matrices are read-only. This matches the manifest.

The coordinate expressions always remain between zero and `n - 1` because both `i` and `j` lie in that range. The method works identically for binary values and would in fact compare arbitrary cell values; the binary constraint is not needed by the rotation logic.

## Alternatives and edge cases

- **Rotate in place up to four times:** Compare after each rotation and mutate layers of `mat`. This also uses $O(1)$ extra space and $O(n^2)$ time, but changes the input and has more error-prone swap logic.
- **Build a new rotated matrix:** A comprehension such as transposed reversed rows makes each orientation easy to see, but allocates $O(n^2)$ additional space for every rotation.
- **Compare only counts of zeros and ones:** Equal counts are necessary but not sufficient because rotation must preserve exact relative positions. Coordinate comparisons are required.
- **One-by-one matrix:** All four coordinate formulas refer to the sole cell. The result is simply whether the two cells are equal.
- **Rotational symmetry:** More than one bit may survive when `mat` is symmetric. The result only needs existence, so retaining multiple candidates is harmless.
- **Target equal without rotation:** The identity bit remains set and true is returned even if all rotated orientations fail.
- **No orientation works:** Bits may fail at different cells. Early false occurs as soon as the last remaining orientation receives its first mismatch.
- **Direction terminology:** The source checks both quarter-turn directions plus 180 degrees and identity. Since repeated 90-degree rotations generate all four, the result does not depend on naming one direction as the primary rotation.
- **Bitwise complement in Python:** `~bit` is negative, but AND with the nonnegative four-bit candidate mask has the intended low-bit clearing behavior. Using `ok ^= bit` would be unsafe because it could turn an already-cleared candidate back on.
