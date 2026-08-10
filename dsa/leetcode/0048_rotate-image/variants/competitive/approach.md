## General

**Decompose clockwise rotation into two mirrors**

A value at original coordinate $(r,c)$ belongs at $(c,n-1-r)$ after a clockwise quarter-turn. The competitive source achieves that mapping in two stages: reflect across the anti-diagonal, then exchange top and bottom rows.

The anti-diagonal runs from the top-right corner to the bottom-left corner and satisfies $r+c=n-1$. Reflecting a coordinate across it maps

$$
(r,c) \longmapsto (n-1-c,n-1-r).
$$

The following top/bottom mirror maps `(a,b)` to `(n-1-a,b)`. Applying it to the reflected coordinate produces `(c,n-1-r)`, exactly the clockwise destination.

**How the anti-diagonal loop covers each pair once**

For row `i`, the inner loop uses `j` from 0 through `n - i - 1`. These coordinates satisfy `i + j <= n - 1`, so they lie on or on one side of the anti-diagonal. Each is swapped with `matrix[n-1-j][n-1-i]`, its reflected partner.

Cells exactly on the anti-diagonal map to themselves. The inclusive boundary causes harmless self-swaps for those cells. Cells on the opposite side are not used as starting coordinates, preventing a second swap that would undo the reflection.

After this phase, every original coordinate has undergone the anti-diagonal map. The loop's triangular shape is therefore deliberate, not a partial traversal bug.

**Flip the reflected matrix vertically**

The second phase pairs row `i` with row `n - 1 - i` and swaps every column. Only the top half of the rows should be used; otherwise every pair would be swapped twice. Under the older Python semantics intended by the source, `n / 2` is integer division, so `range(n / 2)` visits exactly those top rows.

For odd $n$, the middle row maps to itself and is omitted. For even $n$, all rows belong to one pair. After this phase, the composition of the two reflections is a $90^\circ$ clockwise rotation.

**Coordinate proof of correctness**

Take any original element at `(r,c)`. The first phase places it at `(n-1-c,n-1-r)`. The vertical mirror changes only the row coordinate, producing

$$
(n-1-(n-1-c),n-1-r)=(c,n-1-r).
$$

That is precisely its required final position. Both phases consist only of pairwise swaps and are bijections, so every value appears once and no temporary matrix is needed.

**A Python 3 compatibility defect**

The exact source writes `range(n / 2)`. In Python 2, division of two integers produces the intended integer half. In Python 3, `/` produces a float, and `range` rejects a float with `TypeError`. The anti-diagonal phase will run, but execution fails before the vertical mirror, leaving the input only partially transformed.

The intended Python 3 expression is `range(n // 2)`. This documentation does not modify the protected source, so it must state clearly that the selected implementation is not executable unchanged under Python 3. The mathematical algorithm remains valid under its intended integer-division semantics.

**Return-contract mismatch**

The task asks for in-place modification with a `None` return. This source mutates the input correctly under Python 2 semantics but then executes `return matrix`. Many online judges ignore the return value for in-place tasks, so the visible matrix is still correct. Under a strict API contract, however, returning the matrix rather than `None` is a behavioral mismatch.

**Which class is selected**

`Solution2` constructs a rotated matrix with `zip` and reversed rows, using $O(n^2)$ output storage. The canonical entry is the first class named `Solution`; `Solution2` does not override it and is not part of the in-place algorithm explained here.

## Complexity detail

The anti-diagonal traversal covers about half of the $n^2$ cells, and the row flip performs `floor(n/2) * n` swaps. Each swap is constant time, so the intended algorithm runs in $O(n^2)$ time.

It stores only `n`, loop indices, and temporary swap references. Under working integer-division semantics, auxiliary space is $O(1)$, matching the manifest. The Python 3 `TypeError` prevents completion but does not change the complexity of the intended algorithm.

## Alternatives and edge cases

- **Reverse row order then transpose:** Flip top and bottom rows, then swap across the main diagonal. This is another two-reflection decomposition with the same bounds.
- **Transpose then reverse each row:** A common formulation whose composition is also clockwise rotation. The phase order matters; reversing it can yield a counterclockwise turn.
- **Four-way cycles:** Rotate each layer directly in groups of four coordinates. It avoids two whole-matrix phases but makes boundary and offset arithmetic more error-prone.
- **New output matrix:** Directly assign `out[c][n-1-r] = matrix[r][c]`. It is simple but violates the required constant-extra-space, in-place operation.
- **Python 3 division:** `n / 2` is a float and cannot be passed to `range`. Replacing it with `n // 2` is necessary for the intended second phase.
- **Strict return semantics:** The source returns the matrix object rather than `None`. Its mutation is correct in the intended runtime, but its return does not match the documented contract.
- **Anti-diagonal self-swaps:** Coordinates satisfying `i+j=n-1` map to themselves. Including them is harmless and keeps the triangular bounds simple.
- **One-by-one matrix:** The anti-diagonal phase self-swaps the only cell and the row-flip loop is empty under integer division.
- **Odd dimension:** The middle row needs no top/bottom partner, while the anti-diagonal mirror still moves its off-diagonal cells as required.
- **Selected-class distinction:** `Solution2` allocates a new matrix and is not used when the harness instantiates `Solution`.
