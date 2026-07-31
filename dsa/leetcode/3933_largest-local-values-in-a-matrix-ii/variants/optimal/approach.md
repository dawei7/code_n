## General

**Separate candidates by their value.** Place every nonzero coordinate into a bucket indexed by its cell value. Process those buckets from `200` down to `1`. A binary grid named `greater` records which matrix positions have already been processed.

Before the bucket for value `x` is examined, `greater[row][column]` is `1` exactly when the original value at that position is strictly greater than `x`. Positions equal to `x` have not been inserted yet, which is crucial because ties do not disqualify a local maximum. Zero positions never become candidates, although they remain part of every queried neighborhood.

**Turn each neighborhood into one rectangle query.** If the current bucket is nonempty, build a two-dimensional prefix sum over `greater`. For a cell `(row, column)` of value `x`, clamp the opposite corners of its square to the matrix boundaries and query the number of strictly greater positions in that entire rectangle in constant time.

The rectangular prefix query initially includes the four special corners `(row ± x, column ± x)`. Inspect those four coordinates directly and subtract an in-bounds corner whenever its matrix value is greater than `x`. The remaining count therefore covers exactly the neighborhood defined by the problem. A count of zero means the current cell is a local maximum.

After every coordinate in the bucket has been queried, mark those coordinates in `greater`. This delayed update establishes the same strict-greater property for the next smaller value. Consequently, each query counts all and only disqualifying cells: every larger considered value contributes one, equal values contribute none, excluded corners are removed, and out-of-bounds positions never enter the rectangle. Counting precisely the queries that return zero yields the requested answer.

## Complexity detail

Let $A=nm$, let $V=201$ be the source-bounded value-domain size, and let $D\le V-1$ be the number of distinct positive values that occur. Grouping the coordinates takes $O(A)$ time. One $O(A)$ prefix grid is built for each present positive value, while all candidate queries together take $O(A)$ time. The total is $O(DA+A)$, which is $O(VNM)$ in the manifest notation.

The coordinate buckets collectively store at most $A$ entries. The `greater` grid and the largest prefix grid also use $O(A)$ cells, and the bucket array uses $O(V)$ space, for $O(NM+V)$ auxiliary space.

The benchmark fixes every entry to one positive value and defines its size as the number of matrix cells $A$. On those tiers, the accepted method builds one prefix grid and takes $O(A)$ time. Directly scanning a candidate's entire neighborhood takes $O(A)$ work for each of the $A$ candidates and therefore exposes a genuine $O(A^2)$ slower class.

## Alternatives and edge cases

- **Prefix grid for every threshold:** Build 201 separate two-dimensional prefix sums, each indicating values greater than one threshold. This also gives constant-time neighborhood queries, but it retains $O(VNM)$ cells instead of reusing one prefix grid.
- **Scan every neighborhood directly:** This is straightforward and correct, including after skipping the four corners, but an all-equal matrix can require $O((NM)^2)$ inspections.
- **Zero-valued cells:** They may be inspected as neighbors, but they can never be counted as local maxima because candidates must be nonzero.
- **Equal-valued cells:** A tie is not strictly greater. Query an entire value bucket before adding that bucket to the `greater` grid.
- **Excluded corners:** Remove a corner only when both its row distance and column distance equal the candidate value. Other boundary positions of the square remain part of the neighborhood.
- **Clipped neighborhoods:** A radius can exceed one or both matrix dimensions. Clamp the rectangular bounds and test only corner coordinates that actually lie inside the matrix.
