## General
**Represent the four possible orientations**

Keep four Boolean possibilities, conveniently as four bits. For target coordinate `(row, column)`, the corresponding source values under rotations of $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$ are respectively:

- `mat[row][column]`
- `mat[N - 1 - column][row]`
- `mat[N - 1 - row][N - 1 - column]`
- `mat[column][N - 1 - row]`

**Eliminate impossible rotations**

Visit every target cell once. Compare it with each of those four source coordinates and clear an orientation's bit when its value differs. A cleared orientation can never recover, because full matrix equality requires every coordinate to match. If all four bits are cleared, return `False` immediately.

**Why a remaining bit is sufficient**

Each orientation bit survives exactly when every visited target coordinate matches the source coordinate mapped to it by that rotation. After all $N^2$ coordinates have been visited, any surviving bit therefore certifies equality of the complete matrices under its rotation. Conversely, every invalid rotation has at least one mismatching coordinate and is cleared there.

## Complexity detail
There are $N^2$ cells and four constant-time comparisons per cell, giving $O(N^2)$ time. The four-bit mask and loop indices occupy $O(1)$ auxiliary space; no rotated matrix is constructed.

## Alternatives and edge cases
- **Build each rotated matrix:** Transposing and reversing rows is straightforward and still takes $O(N^2)$ time, but materializing a rotation uses $O(N^2)$ extra space.
- **Rotate in place:** Layer-by-layer swaps use $O(1)$ extra space but mutate `mat`, which is unnecessary for a Boolean comparison.
- **Zero rotations:** An already equal matrix must return `True`.
- **One-cell matrix:** Rotation changes nothing, so the two values alone determine the result.
- **Symmetric matrices:** Multiple orientation bits may survive; only one is required.
- **Different cell counts:** Rotation preserves the number of zeros and ones, so unequal counts guarantee `False`, though a separate count pass is not needed.
