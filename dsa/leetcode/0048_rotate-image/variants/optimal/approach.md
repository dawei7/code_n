## General

**Start from the coordinate rule for a clockwise rotation**

In an $n \times n$ matrix, an element originally at row $r$ and column $c$ must end at row $c$ and column $n - 1 - r$ after a $90^\circ$ clockwise rotation:

$$
(r,c) \longmapsto (c,n-1-r).
$$

Moving every element directly to its destination would overwrite values that have not yet moved unless four-cell cycles are handled carefully. The selected solution instead decomposes the coordinate rule into two familiar in-place reflections: reverse the order of the rows, then transpose across the main diagonal.

**First transformation: flip top and bottom**

The first nested loop swaps row `i` with row `n - i - 1`, one column at a time. Only `n >> 1`, which equals integer floor division by two for nonnegative `n`, top rows are processed. This prevents swapping each pair twice.

After this vertical or horizontal-axis mirror, an original coordinate `(r, c)` has moved to `(n - 1 - r, c)`. For a three-by-three matrix,

`[[1,2,3],[4,5,6],[7,8,9]]`

becomes

`[[7,8,9],[4,5,6],[1,2,3]]`.

When $n$ is odd, the middle row is not swapped, which is correct because it mirrors to itself. Every element in paired rows is exchanged using Python's simultaneous assignment, so neither value is lost.

**Second transformation: transpose the main diagonal**

Transposition maps coordinate `(a, b)` to `(b, a)`. The source loops over each row `i` and only columns `j < i`, which is the strict lower triangle. It swaps `matrix[i][j]` with `matrix[j][i]`, the corresponding position in the strict upper triangle.

The main diagonal is omitted because `(i, i)` maps to itself. Processing only one triangle is essential: if both `(i, j)` and `(j, i)` were visited as starting cells, the second swap would undo the first.

Applied to the row-reversed example, transposition produces `[[7,4,1],[8,5,2],[9,6,3]]`, the required clockwise rotation.

**Why the composition has the exact destination mapping**

Track an original value at `(r, c)`. The row reversal sends it to `(n - 1 - r, c)`. Transposition exchanges the two coordinates, sending it to `(c, n - 1 - r)`. This is exactly the clockwise rule derived at the beginning.

Because both component transformations are bijections, every input cell moves to one distinct output cell. No value is duplicated or dropped. Since all swaps occur within `matrix`, the input object itself becomes the rotated image.

**Loop invariants for safe in-place mutation**

During the first phase, before row pair `i` is processed, every earlier top row and its mirrored bottom row have been exchanged exactly once, while unprocessed pairs retain their original relative positions. Finishing all `floor(n/2)` pairs completes the row reversal.

During the transpose phase, when handling `(i, j)` with `j < i`, its mirrored coordinate `(j, i)` has not been used as a lower-triangle starting position. Swapping the pair establishes both final transposed values at once. Previously handled unordered coordinate pairs are disjoint and remain correct.

Together, these invariants show the implementation does not rely on a temporary matrix or lose values through overwriting.

**Why square shape matters**

A transpose of a rectangular matrix changes its dimensions. In-place rotation inside the same nested-list shape is straightforward here because the contract guarantees exactly $n$ rows and $n$ columns. Every reflected or transposed coordinate remains within the same square index range.

The method returns no explicit value, so Python returns `None`, matching the contract. Its observable result is the changed `matrix` object.

## Complexity detail

The row-reversal phase swaps approximately $n^2/2$ element pairs: `floor(n/2)` row pairs times $n$ columns. The transpose phase swaps $n(n-1)/2$ off-diagonal pairs. Their sum is proportional to $n^2$, so time is $O(n^2)$. This is optimal up to constants because a rotation must place all $n^2$ matrix entries.

Only loop indices, `n`, and the temporary references created by tuple assignment are used. No second matrix or size-dependent helper structure is allocated, so auxiliary space is $O(1)$. The nested input rows are mutated in place.

## Alternatives and edge cases

- **Transpose first, then reverse each row:** Main-diagonal transposition followed by a left-to-right reversal also maps `(r,c)` to `(c,n-1-r)`. It is the most common equivalent decomposition.
- **Four-cell cyclic swaps:** Process one quadrant and rotate top, left, bottom, and right values in groups of four. It performs one direct rotation pass but has more intricate index formulas.
- **Allocate a new matrix:** Write each original value directly to `out[c][n-1-r]`. This is very easy to verify but violates the in-place requirement and uses $O(n^2)$ extra space.
- **Anti-diagonal reflection plus top/bottom flip:** This is another valid composition. Its reflection coordinates differ, so mixing formulas between decompositions would rotate or reflect incorrectly.
- **One-by-one matrix:** Both loops perform no swaps, leaving the sole value unchanged, which is the correct rotation.
- **Odd dimension:** The middle row is unchanged by the first flip, and diagonal cells are unchanged by transposition; off-axis cells still move normally.
- **Even dimension:** Every row participates in exactly one first-phase pair, with no special center.
- **Negative or repeated values:** Rotation depends only on positions, so value magnitude and equality have no effect.
- **Calling the method twice:** Two clockwise rotations produce a $180^\circ$ rotation; each call is an independent in-place coordinate transformation.
- **Return behavior:** The absence of `return` is intentional. Callers inspect the same matrix object after the method completes.
