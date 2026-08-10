## General

**Translate the four directions into row and column inequalities**

For building `(x,y)`:

- a left building has the same `x` and a smaller `y`;
- a right building has the same `x` and a larger `y`;
- an above building has the same `y` and a smaller `x`;
- a below building has the same `y` and a larger `x`.

The other building does not need to be immediately adjacent. Any coordinate farther in the required direction is sufficient.

Therefore, only the minimum and maximum occupied coordinates on the same row and column matter. A building is covered exactly when its `y` lies strictly inside its row's occupied range and its `x` lies strictly inside its column's occupied range.

**Group coordinates by row and by column**

The source creates two dictionaries:

- `g1[x]` contains every `y` coordinate of a building on row `x`;
- `g2[y]` contains every `x` coordinate of a building in column `y`.

For every input building, it appends once to each grouping. Unique coordinates ensure the same point is not duplicated, although different buildings naturally share rows or columns.

The grid size `n` is not used for array allocation. Dictionaries store only occupied rows and columns, which avoids `O(n)` storage when few buildings exist.

**Sort each occupied line**

The source sorts every list in `g1` and `g2`. After sorting:

- `g1[x][0]` is the leftmost occupied `y` on row `x`;
- `g1[x][-1]` is the rightmost;
- `g2[y][0]` is the topmost occupied `x` in column `y`;
- `g2[y][-1]` is the bottommost.

Intermediate sorted positions are not used. Sorting is one way to obtain the two extremes, though it is more work than necessary.

**Test a building against all four extremes**

For current `(x,y)`, the source assigns:

`l1 = g1[x]` and `l2 = g2[y]`.

The condition:

`l2[0] < x < l2[-1]`

means there is at least one smaller `x` and one larger `x` in the same column: an above and a below building.

The condition:

`l1[0] < y < l1[-1]`

means there is at least one smaller `y` and one larger `y` in the same row: a left and a right building.

Both conditions are joined with `and`, so all four directions must exist. Strict inequalities prevent the current building itself, or an extreme building with only one-sided neighbors, from satisfying a direction.

**Why looking only at extremes is enough**

If `y > min_row_y`, the building realizing that minimum is to the left. If `y < max_row_y`, the maximum witness is to the right. Conversely, if a left witness exists, the row minimum is necessarily smaller; if a right witness exists, the row maximum is larger.

Thus “strictly between row extremes” is equivalent to “has both a left and a right building.” The same proof applies vertically. No binary search for a nearest neighbor is needed.

**A cross-shaped example**

For buildings `(1,2), (2,2), (3,2), (2,1), (2,3)`:

- row two has sorted `y` values `[1,2,3]`;
- column two has sorted `x` values `[1,2,3]`.

Building `(2,2)` is strictly between both pairs of extremes, so it is counted. Building `(1,2)` is the minimum `x` in column two and fails the vertical condition. The other arms similarly fail at least one strict boundary.

**Why every counted building is covered**

If the source increments `ans`, the row list contains a coordinate below `y` and one above `y`, providing left and right witnesses at the same `x`. The column list contains an `x` below and above the current `x`, providing above and below witnesses at the same `y`. Hence all four required buildings exist.

Conversely, if a building is covered, its direction witnesses force it to be strictly inside both its row's and column's extrema. The source's condition succeeds. The test is therefore exact.

**Important complexity mismatch**

The manifest claims `O(B)` time for `B = len(buildings)`, but the protected source sorts complete coordinate lists. In the worst case, all buildings can share one row, causing a list of length `B` to be sorted in `O(B log B)` time; the column groups do not cancel that cost.

The logic remains correct, but the actual protected implementation is `O(B log B)` worst-case. Tracking only minima and maxima during the first pass would achieve the manifest's linear bound.

## Complexity detail

Let row group sizes be `r_1,r_2,...` and column group sizes be `c_1,c_2,...`, each family summing to `B`.

Building both dictionaries takes `O(B)` expected time. Sorting costs:

`sum r_i log r_i + sum c_j log c_j`,

which is at most `O(B log B)` for each family and `O(B log B)` overall. The final pass performs constant-time dictionary lookups and boundary comparisons per building, adding `O(B)`.

Thus actual worst-case time is `O(B log B)`, not the manifest's `O(B)`.

Each coordinate is stored once in a row list and once in a column list, so the dictionaries use `O(B)` auxiliary space. Sorting Python lists is in place but may use implementation-dependent temporary memory; the overall bound remains `O(B)`.

## Alternatives and edge cases

- **Track only four extremes:** Maintain min/max `y` per row and min/max `x` per column. This gives the same tests in `O(B)` expected time and is the direct way to achieve the manifest bound.
- **Use sets and search every direction:** Scanning coordinate-by-coordinate toward grid boundaries can cost `O(nB)` and ignores the fact that only extremes matter.
- **Sort all buildings globally:** A row-major and column-major sort can also derive neighbors, but two grouped extremes are simpler.
- **Require immediate adjacent cells:** The statement asks for a building somewhere in each direction, not necessarily at distance one.
- **Use non-strict inequalities:** The current extreme coordinate would then incorrectly serve as its own missing-side witness.
- **One building:** Its row and column extrema equal its coordinates, so it is not covered.
- **Two buildings on a row:** Neither lies strictly between row extremes; at least three row positions are needed for any covered building.
- **Several buildings share x but not y:** They provide horizontal witnesses only; vertical witnesses must come from the same column.
- **Several buildings share y but not x:** They provide vertical witnesses only.
- **Grid boundary coordinate:** A boundary building could still have some directions, but cannot have a building outside the city; the strict extrema test naturally prevents full coverage when a direction is impossible.
- **Sparse large n:** Dictionaries store occupied lines only, so the unused grid size does not affect memory.
- **Unique-coordinate guarantee:** It avoids duplicate copies of the same building in grouped lists.
- **Coordinate interpretation:** In the source, `g1[x]` varies `y` horizontally and `g2[y]` varies `x` vertically; swapping these meanings would test the wrong directions.
- **Manifest claim:** The source is correct but not linear due to sorting. Min/max aggregation is the relevant alternative when complexity fidelity matters.
