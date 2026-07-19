## General
**Reuse boundary cells as row and column marker arrays**

The first cell of each row can mark whether that row must be zeroed, and the first cell of each column can do the same for its column. Their intersection, `matrix[0][0]`, cannot independently represent both the first row and first column, so save two separate booleans describing whether each boundary originally contains a zero.

Then scan only the interior. For every original zero at `(row, col)`, set `matrix[row][0] = 0` and `matrix[0][col] = 0`. These writes store metadata in cells whose final values are allowed to become zero when the corresponding unit is cleared.

**Clear the interior before the marker boundaries**

In a separate pass, zero an interior cell when either its row marker or column marker is zero. Only after every interior cell has consumed the markers should the first row and first column be cleared according to their saved flags.

Clearing a boundary early would destroy marker information: writing all zeros into the first row before the interior pass would falsely indicate that every column originally required clearing.

**Marker zeroes represent original causes, not cascading effects**

After the marking pass, for each nonboundary row and column, its marker is zero exactly when that row or column contained an original zero in the scanned interior. The saved flags independently preserve the original zero status of the shared marker row and column.

**Trace an interior zero without a boundary zero**

For a center zero in `[[1,1,1],[1,0,1],[1,1,1]]`, mark `matrix[1][0]` and `matrix[0][1]`. The application pass clears row 1 and column 1; neither saved boundary flag is set, so other first-row and first-column cells remain unchanged.

**Boundary markers encode exactly the zeroed row and column sets**

Every original interior zero writes one marker in its row's first cell and one in its column's first cell. The later pass clears a cell exactly when at least one of those markers is present, which is precisely when an original interior zero shares its row or column.

Separate flags preserve whether the original first row or first column contained zero before those cells were reused as markers. Applying them last distinguishes original boundary requirements from marker side effects. The final zeros are therefore exactly the union of rows and columns containing an original zero.

## Complexity detail
The matrix is scanned and updated a constant number of times, for $O(mn)$ time. Two booleans and loop indices use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Store zero-row and zero-column sets:** is straightforward but uses $O(m+n)$ extra space.
- **Set cells to zero immediately during discovery:** incorrectly treats newly created zeros as original ones and can erase the whole matrix.
- **Copy the matrix:** simplifies separating discovery from updates but violates the constant-space requirement.
- A zero at `(0,0)` sets both saved boundary flags. One-row and one-column matrices rely primarily on those flags and still work.
- Marker cells written during discovery must not cause additional rows or columns beyond the ones they represent; restricting discovery to the interior prevents that feedback.
