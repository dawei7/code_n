## General

**Turn Chebyshev distance into an axis-aligned square**

A sensor at `(r, c)` covers a cell `(i, j)` when

`max(|r - i|, |c - j|) <= k`.

For a maximum of two non-negative quantities to be at most `k`, both quantities must be at most `k`. Therefore the condition is equivalent to

`|r - i| <= k` and `|c - j| <= k`.

Along the row axis, one sensor reaches from `r - k` through `r + k`. Along the column axis, it reaches from `c - k` through `c + k`. Ignoring clipping at the grid boundary, its coverage is an axis-aligned square containing

`2k + 1` rows and `2k + 1` columns.

The source names this one-dimensional reach

`span = 2 * k + 1`.

The formula includes the sensor’s own row or column. For example, with `k = 1`, a sensor can cover one position before itself, its own position, and one position after itself, for a span of three rather than two.

**First solve one dimension**

Consider only a line of `n` row positions. One radius-`k` sensor can cover at most `span` consecutive rows. Covering all `n` rows therefore needs at least

`ceil(n / span)`

row bands. The standard integer expression for this ceiling is

`(n + span - 1) // span`.

To see why it works, write `n = q * span + r` with `0 <= r < span`. If `r = 0`, the expression returns `q` exact full bands. If `r > 0`, adding `span - 1` makes integer division return `q + 1`, accounting for the final partial band.

The same reasoning applies independently to the `m` columns, giving

`column_bands = ceil(m / span)`.

Because a sensor covers a row interval and a column interval simultaneously, pairing one row band with one column band produces a rectangular block that one sensor may cover.

**Construct a placement using one sensor per band pair**

Partition the rows into consecutive bands of at most `span` rows, and partition the columns into consecutive bands of at most `span` columns. Their Cartesian products form

`row_bands * column_bands`

rectangular blocks. Every block has height and width at most `2k + 1`.

For one block, choose a grid cell near the midpoint of its row interval and near the midpoint of its column interval. A discrete interval of length at most `2k + 1` has a midpoint whose distance from either endpoint is at most `k`. Consequently, every block row is within `k` of the chosen row, and every block column is within `k` of the chosen column.

Every cell in that block then has both row difference and column difference at most `k`, so its Chebyshev distance from the sensor is at most `k`. Placing one sensor in each block covers the whole grid. This gives an upper bound of

`ceil(n / span) * ceil(m / span)`.

The final row or column band may be shorter than `span`, but that only makes it easier to cover. Its sensor can be shifted toward the grid boundary while remaining a valid grid cell.

**Prove that fewer sensors cannot work**

The construction shows that the formula is sufficient. To prove it is minimal, choose specially spaced witness cells.

Choose row witnesses at positions

`0, span, 2 * span, ...`

while they remain below `n`. There are exactly `ceil(n / span)` such rows. Choose columns in the same way, producing `ceil(m / span)` witness columns. Take every Cartesian pair of a witness row and witness column. The number of witness cells is exactly the product returned by the source.

Any two distinct witness cells differ by at least `span = 2k + 1` in their row coordinate or their column coordinate. Their Chebyshev distance is therefore at least `2k + 1`, which is strictly greater than `2k`.

If one sensor covered two witness cells, each would be within distance `k` of the sensor. By the triangle inequality, those two cells would then be within distance at most `2k` of each other. That contradicts their spacing. Hence one sensor can cover at most one witness cell.

Since every witness cell must be covered, at least as many sensors as witnesses are necessary. The lower bound equals the constructive upper bound, proving that the product of the two ceiling divisions is the exact minimum.

**Trace the examples**

For `n = 5`, `m = 5`, and `k = 1`, the span is three. Five rows require `ceil(5 / 3) = 2` row bands, and the columns likewise require two bands. Their four combinations require and suffice with four sensors, matching the example. The exact four coordinates can differ from the sample placement; only the minimum count is returned.

For a `2 x 2` grid with `k = 2`, the span is five. Both dimensions fit inside one band, so `row_bands = column_bands = 1` and the answer is one. A sensor at any grid cell is within Chebyshev distance at most one of every other cell, which is already no greater than `k`.

**Why multiplication is necessary**

Adding the row-band and column-band counts would be incorrect. A row band does not cover all columns by itself, and a column band does not cover all rows. Each sensor corresponds to one pairing of a row interval with a column interval. Covering every pair requires the Cartesian-product count.

The formula works specifically because Chebyshev balls are axis-aligned products of independent row and column intervals. A different distance metric, such as Manhattan distance, would produce diamond-shaped coverage and would not justify the same simple product.

## Complexity detail

The method performs a fixed number of integer additions, multiplications, and divisions, regardless of the grid area. It never iterates through rows, columns, cells, or possible sensor locations. Its time complexity is `O(1)`.

It stores only `span`, `row_bands`, and `column_bands`, so its auxiliary-space complexity is `O(1)`.

The arithmetic values are small under the constraints: `span <= 2001`, each band count is at most 1000, and their product is at most one million when `k = 0`. Python integers also expand automatically, so overflow is not a concern.

The proof discusses partitions and witness sets, but the implementation does not materialize either structure. They establish why the closed-form answer is exact; constructing them would add unnecessary work.

## Alternatives and edge cases

- **Greedy placement by explicit bands:** Iterate through uncovered rows and columns and place one sensor near the center of each next block. This constructs valid coordinates but costs time proportional to the number of sensors when only the count is requested.
- **Mark every covered cell:** Trying candidate sensor positions and maintaining a covered matrix can require work proportional to the grid area or worse. The geometric formula avoids simulation entirely.
- **Use floor division:** `n // span` misses a final partial band whenever `n` is not divisible by `span`. Ceiling division is required.
- **Add instead of multiply:** Row and column partitions combine as Cartesian products, so the minimum count is their product, not their sum.
- **Use `2k` as the span:** A radius includes the center position, making the correct number of discrete coordinates `2k + 1`.
- **`k = 0`:** Each sensor covers only its own cell. Then `span = 1` and the formula returns `n * m`.
- **Coverage larger than both dimensions:** When `2k + 1 >= n` and `2k + 1 >= m`, both ceiling counts are one and a single sensor suffices.
- **Coverage larger than only one dimension:** If all rows fit but columns need several bands, the answer is exactly the column-band count, and symmetrically for the other orientation.
- **One-row or one-column grid:** One band count is one, reducing the formula to the ordinary one-dimensional interval-cover result.
- **Partial final bands:** They still need one sensor each, but their midpoint can be shifted inside the grid so that every contained coordinate remains within distance `k`.
- **Alternative sensor coordinates:** The problem asks only for the minimum count. Many placements may attain it, so the method need not reproduce the sample’s coordinates.
- **Manhattan-distance confusion:** Chebyshev coverage is a square because both coordinate differences are bounded separately. A diamond-covering argument would solve a different problem.
- **Input preservation:** The method receives only integers and does not mutate any external data.
