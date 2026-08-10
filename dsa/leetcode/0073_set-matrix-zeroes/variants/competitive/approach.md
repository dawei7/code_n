## General

**Reuse matrix boundary cells as dimension markers**

The straightforward marker method needs one external Boolean per row and column. This implementation observes that the matrix already has a reserved-looking cell for every dimension: `matrix[i][0]` can mark row `i`, and `matrix[0][j]` can mark column `j`. After original zeroes have been discovered, those first-column and first-row cells can store the same yes-or-no information without allocating dimension-sized arrays.

The shared corner `matrix[0][0]` cannot independently describe both the first row and first column. Moreover, interior discoveries will deliberately write marker zeroes into the boundary. The source therefore records the original status of both boundary dimensions in the scalar Booleans `first_col` and `first_row` before any marker writes occur.

**Preserve the original first-column and first-row facts**

The first `reduce` checks whether any `matrix[i][0]` is zero, producing `first_col`. The second checks the first row, producing `first_row`. Each accumulator starts as false and combines its current value with the next equality test using logical `or`, so the final Boolean records whether at least one original boundary cell was zero.

Once an accumulator becomes true, Python's short-circuit `or` may skip later equality checks, but the result remains correct because existence has already been proved. The matrix is guaranteed nonempty, so accesses to row zero and column zero are valid.

These snapshots must occur before interior scanning. For example, an original zero at `(2, 3)` will set `matrix[2][0]` and `matrix[0][3]` to zero as markers. Those new boundary zeroes must not be mistaken for evidence that the original first column or first row contained a zero.

**Mark effects of interior original zeroes**

The discovery loops start at row one and column one. They intentionally exclude the boundary cells whose original effects have already been saved. When an interior `matrix[i][j]` is zero, the tuple assignment writes zero to `matrix[i][0]` and `matrix[0][j]`. Those two cells now mean “clear row `i`” and “clear column `j`.”

No interior target cell is changed during this phase. Only marker locations are mutated. Consequently, scanning later interior cells still sees their original values. A marker written in the first row or first column is outside both loop ranges and cannot be rediscovered as though it were an original interior zero.

After discovery, for every interior row `i`, `matrix[i][0] == 0` exactly when that row was already marked by an original boundary zero or contains an original interior zero. Similarly, each first-row cell marks its column. The original boundary cases are finally governed by the separately saved flags.

**Clear the interior before clearing its markers**

The second nested loop again visits only the interior. It sets `matrix[i][j]` to zero when either `matrix[i][0]` or `matrix[0][j]` is zero. This is the union of all affected interior rows and columns.

The boundary must remain intact until this phase finishes because it is the marker storage. If the algorithm zeroed the entire first row too early, every column marker would become zero and every interior column would be cleared. If it zeroed the first column too early, the same false cascade would affect every row. Deferring boundary cleanup preserves the recorded evidence until its last use.

**Restore the required boundary results from saved flags**

After every interior cell is final, markers are no longer needed. If `first_col` is true, all cells in column zero are cleared. If `first_row` is true, all cells in row zero are cleared. The order of these last two loops is harmless because their decisions come from saved Booleans, not from current matrix contents. They overlap only at `(0, 0)`, and writing zero more than once has no effect.

Consider `[[0,1,2,0],[3,4,5,2],[1,3,1,5]]`. The snapshots make both `first_row` true and `first_col` true because the corner is zero. Interior scanning finds no additional original zero, but the first-row cell at column three was already zero and functions as that column's marker. Interior update clears column three. The final boundary loops clear the first column and first row, yielding exactly the required matrix.

**Why the transformation is exact**

Every original zero is either on the first row, on the first column, or in the interior. The two saved flags cover the first two categories, and interior scanning writes both relevant markers for the third. Thus every row and column that must be cleared is represented.

An interior cell is cleared exactly when one of its dimension markers is zero. A boundary cell is cleared according to its saved original-dimension flag or, for non-corner boundary marker cells, remains zero when an interior zero marked its dimension. Therefore every required cell becomes zero. Because markers are written only from original interior zeroes and saved flags reflect only original boundary zeroes, no unaffected dimension is invented. The method is correct and modifies the matrix in place.

## Complexity detail

The two reductions inspect $m+n$ boundary cells. The discovery and application phases each inspect at most $(m-1)(n-1)$ interior cells, and final cleanup visits at most $m+n$ cells. The combined time is $O(mn)$, matching the manifest.

Apart from loop variables, two Booleans, and short-lived reduction accumulator values, all marker information is stored inside the input matrix. Auxiliary space is $O(1)$, also matching the manifest. The returned result consumes no separate space because the method mutates the input and implicitly returns `None`.

## Alternatives and edge cases

- **External row and column arrays:** They simplify discovery and proof but use $O(m+n)$ auxiliary space.
- **Sets of affected dimensions:** They can store only marked indices, but worst-case space is still $O(m+n)$.
- **Copy then write:** Reading from a full copy prevents cascades but costs $O(mn)$ extra space.
- **Use one boundary flag plus the corner:** A common formulation lets `matrix[0][0]` represent the first row and stores only a separate first-column Boolean. The selected source uses two saved flags for symmetry and clarity.
- **One-row matrix:** The interior row loops are empty. `first_row` decides whether the complete row is cleared, while existing first-row zero markers correctly participate in that decision.
- **One-column matrix:** The interior column loops are empty, and `first_col` determines the complete result.
- **Zero at `(0, 0)`:** Both saved flags become true, so both boundary dimensions are cleared.
- **Interior zero:** It writes one row marker and one column marker without changing other interior cells during discovery.
- **No zeroes:** Both flags remain false, no markers are written, and every value is preserved.
- **All zeroes:** Every marker and both flags are zero/true, so the matrix remains all zeroes.
- **Cleanup order:** Boundary clearing must follow interior application; moving it earlier destroys marker meaning.
- **`reduce` readability:** Built-in `any` over each boundary would express the existence tests more directly, but both approaches use constant auxiliary state.
- **Nonzero values:** Their magnitude and sign are irrelevant; only exact equality with zero creates a marker.
- **Return contract:** The method intentionally has no explicit return value and changes the supplied nested lists.
