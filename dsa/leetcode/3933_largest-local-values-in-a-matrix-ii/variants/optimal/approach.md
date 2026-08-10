## General

A nonzero cell with value $x$ considers almost the entire rectangle whose row and column coordinates are at distance at most $x$ from the cell. The rectangle is clipped at the matrix boundaries. Up to four positions are then excluded: the positions whose row distance and column distance are both exactly $x$, which are the four geometric corners of the unclipped square when they exist.

The cell is a local maximum unless one of the remaining considered positions contains a value strictly greater than $x$. Equal values are allowed.

Checking this neighborhood separately for every cell would be expensive because $x$ can be as large as $200$, and a single neighborhood can contain most of the matrix. The source reverses the viewpoint: it processes candidate values from largest to smallest and maintains a binary grid marking exactly the cells whose values are greater than the current value. A two-dimensional prefix sum then counts those larger cells inside any candidate rectangle in constant time.

**Group candidate cells by their value**

The list `positions` has 201 buckets, one for each permitted matrix value from zero through 200. During the initial scan, every nonzero cell coordinate `(row, column)` is appended to the bucket indexed by its value.

Zero cells are deliberately absent. The definition says a local maximum must be nonzero, so zero never needs to be tested as a candidate. A zero also can never be greater than a positive candidate, so omitting it does not hide a disqualifying neighbor.

Grouping coordinates lets the main loop handle all cells of value $x$ together. This is important because equal-valued cells must not disqualify one another.

**Meaning of the `greater` grid**

The main loop visits `value` from 200 down to 1. Before processing bucket `positions[value]`, `greater[r][c]` is one exactly when

$$
\texttt{matrix[r][c]}>\texttt{value}.
$$

It is zero for equal values, smaller values, and original zeroes. The source preserves this meaning by waiting until every candidate of the current value has been checked before marking those current cells in `greater`.

This descending sweep transforms a value comparison into a count query. A candidate has some considered cell greater than itself exactly when the corresponding neighborhood contains at least one marked position.

**Build a two-dimensional prefix sum for the current threshold**

If at least one candidate has the current value, the source constructs `prefix` over the binary `greater` matrix. Its indexing has an extra zero row and zero column. The entry

`prefix[r + 1][c + 1]`

stores the number of marked cells in rows zero through `r` and columns zero through `c`.

For each matrix row, `running` accumulates marked cells from the left. `above` refers to the previous prefix row and `current` to the row being filled. The assignment

`current[column + 1] = above[column + 1] + running`

adds everything above the current row to everything seen so far within the row. This is equivalent to the usual two-dimensional prefix recurrence but avoids separately reading the upper-left entry.

Once built, the number of greater cells in an inclusive rectangle from `top` through `bottom` and `left` through `right` is obtained by inclusion-exclusion:

$$
P[bottom+1][right+1]
-P[top][right+1]
-P[bottom+1][left]
+P[top][left].
$$

The four terms respectively take the large origin rectangle, remove the portion above, remove the portion left of the target, and restore the overlap removed twice.

**Clip each candidate's square to the matrix**

For a cell `(row, column)` of value $x$, the source calculates

- `top = max(0, row - x)`,
- `bottom = min(rows - 1, row + x)`,
- `left = max(0, column - x)`,
- `right = min(columns - 1, column + x)`.

These are exactly the valid coordinates whose row and column distances are each at most $x$. The prefix query counts every greater value in that clipped rectangle.

The candidate cell itself is inside the rectangle, but it is not marked in `greater` because its value equals $x$, so including it is harmless.

**Remove the special corner positions**

The rectangular query includes positions whose row distance and column distance are both exactly $x$, but the statement excludes them. The source enumerates the two possible rows `row - value` and `row + value` and the two possible columns `column - value` and `column + value`. Their Cartesian product gives the four possible corners.

Each corner is checked for matrix bounds because clipping may have removed it from the rectangle. If an in-bounds corner contains a value greater than the candidate, it contributed one to the prefix count and `larger` is decremented.

Corners whose values are equal or smaller were not marked and contributed zero, so they require no subtraction. After these corrections, `larger` counts exactly the greater values among considered cells. A zero count means the candidate is a local maximum and increments `answer`.

**Advance the descending threshold**

Only after every cell in the current bucket has been decided does the source set its `greater` flag to one. On the next iteration, where the candidate value is smaller, these cells are correctly classified as greater.

This ordering proves the maintained threshold meaning by induction. It also explains why a group of equal cells can all be local maxima: none is marked while that group is evaluated, and the requirement rejects only a strictly greater value.

Every nonzero cell appears in exactly one bucket and is tested once. Its rectangle count plus explicit corner removal exactly matches the definition, so `answer` is the number requested.

## Complexity detail

Let $N$ be the number of rows, $M$ the number of columns, $A=NM$, and $V=201$ the fixed value-domain size.

The initial grouping and final marking of all cells take $O(A)$ total time. For every distinct positive value that appears, the source builds one $O(A)$ prefix matrix. There can be at most $V-1$ such values, so this contributes $O(VNM)$ time in the worst case. Rectangle and corner work is constant per nonzero candidate, totaling another $O(A)$.

Overall time is $O(VNM)$, matching the manifest. Since $V=201$ is fixed by the constraints, it can also be viewed as linear in the number of matrix cells with a relatively large constant.

The `greater` grid and one current `prefix` grid use $O(NM)$ space. The coordinate buckets collectively store at most $NM$ coordinate pairs plus $O(V)$ bucket objects. Peak additional space is therefore $O(NM+V)$.

## Alternatives and edge cases

- **Scan every neighborhood literally:** This is simple but a candidate of value $x$ may inspect $\Theta(x^2)$ cells. Across a $200$ by $200$ matrix, repeated large neighborhoods are much more expensive than shared prefix counts.
- **Use a prefix sum of raw values:** A sum cannot reveal whether any entry exceeds $x$. The binary `greater` grid encodes exactly the disqualifying predicate for the current threshold.
- **Mark equal-valued cells before checking their bucket:** Equal values are allowed and must not count as larger. Delaying the marks until after the whole bucket is essential.
- **Forget the four excluded corners:** A greater value at an exact-distance corner is explicitly ignored by the definition. The rectangle query must be corrected for those positions.
- **Subtract every in-bounds corner:** Only a marked, strictly greater corner contributed to `larger`. Subtracting an unmarked corner could make the count negative and incorrectly accept a candidate.
- **Candidate value zero:** Zero cells are never local maxima and are not placed in a bucket.
- **All values equal and nonzero:** No cell is marked as greater while that value is processed, so every cell is accepted.
- **Candidate near a boundary:** Clipped bounds exclude out-of-matrix positions, and corner checks independently verify bounds before reading.
- **Value larger than both matrix dimensions:** The clipped rectangle covers the whole matrix, while all four exact-distance corners are out of bounds. The candidate is compared with every matrix cell.
- **Several greater cells in the neighborhood:** The algorithm needs only whether the corrected count is zero; their exact positions are irrelevant except for excluded corners.
- **One-row or one-column matrix:** The prefix formula remains valid. For positive $x$, no position can usually satisfy both exact row and column distances in the missing dimension, so the corner loops simply find no in-bounds excluded corner.
- **Largest value 200:** Its bucket is processed while `greater` is entirely zero, so all cells of global maximum value are accepted, as no strictly greater matrix value exists.
