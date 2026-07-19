## General
**Build a padded two-dimensional prefix table**

Create `prefix` with $m+1$ rows and $n+1$ columns of zeros. Define `prefix[r + 1][c + 1]` as the sum of the rectangle from `mat[0][0]` through `mat[r][c]`. Inclusion-exclusion gives the update from the cell value, the prefix above, and the prefix to the left, subtracting the overlap counted twice.

**Answer each clipped rectangle with four lookups**

For output position `(i, j)`, convert the clipped inclusive bounds to half-open bounds `[top, bottom)` and `[left, right)`. Its block sum is

`prefix[bottom][right] - prefix[top][right] - prefix[bottom][left] + prefix[top][left]`.

The full prefix at `bottom, right` contains the desired rectangle plus cells above and left. Subtracting those two outside strips removes them, while their shared corner was removed twice and must be added back. This leaves exactly the valid cells within $k$ rows and columns of the center. Applying the formula independently to every cell produces the required matrix.

## Complexity detail
Constructing the prefix table visits all $mn$ cells. Each of the $mn$ answers uses constant-time bound calculations and four prefix lookups, so total time is $O(mn)$. The prefix and answer matrices each occupy $O(mn)$ space.

## Alternatives and edge cases
- **Direct neighborhood enumeration:** Iterating through every cell in every clipped block is correct but can take $O(mn(2k+1)^2)$ time.
- **Two one-dimensional sliding passes:** Horizontal window sums followed by vertical window sums also achieve $O(mn)$ time, but require careful changing boundary widths.
- **Radius covers the matrix:** Every answer equals the complete matrix sum when the clipped block includes all rows and columns.
- **Corner cells:** Both row and column ranges clip on one side, which the half-open bounds handle uniformly.
- **Rectangular matrices:** Row and column limits are calculated separately; no square-shape assumption is valid.
- **Single cell:** Any legal positive radius still returns that one value.
