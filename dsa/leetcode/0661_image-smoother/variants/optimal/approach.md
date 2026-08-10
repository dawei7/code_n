## General

**Compute each output pixel from the original neighborhood**

For every cell `(i, j)`, the smoother considers the rectangle covering row indices `i - 1` through `i + 1` and column indices `j - 1` through `j + 1`. That rectangle has at most nine positions:

- the cell itself;
- up to eight horizontally, vertically, or diagonally adjacent cells.

Positions outside the image do not exist and must not contribute either to the sum or to the divisor.

The exact solution creates a separate output matrix `ans`. This is important because every result must be based on the original `img` values. Writing smoothed values back into `img` immediately would let later neighborhoods read a mixture of original and already modified pixels.

**Visit every target position**

The outer loops enumerate all `m * n` coordinates:

- `i` selects an output row;
- `j` selects an output column.

For each target, `s` starts as the neighborhood sum zero and `cnt` starts as the number of included cells zero.

Two small loops then try every candidate coordinate `(x, y)` in the surrounding three-by-three region. The condition:

`0 <= x < m and 0 <= y < n`

accepts exactly the coordinates inside the matrix. For each accepted coordinate, increment `cnt` and add `img[x][y]` to `s`.

**Why the divisor must be counted rather than assumed**

An interior pixel of a sufficiently large image has nine valid cells in its neighborhood. A corner normally has four and a non-corner boundary pixel normally has six. However, those familiar counts change for one-row or one-column images. Explicitly counting valid cells handles every shape uniformly.

The current cell `(i, j)` is always inside the image, so `cnt` is never zero. Division is therefore safe without a special fallback.

**Round down with integer division**

After gathering the neighborhood, the required value is the floor of its average:

`ans[i][j] = s // cnt`.

Every grayscale value is nonnegative, so Python's floor-division behavior exactly matches truncating the fractional part. For example, a sum of 550 across four cells becomes `550 // 4 = 137`.

If negative pixel values were allowed, Python `//` would round toward negative infinity rather than toward zero. The source constraints exclude that distinction.

**A corner example**

For the top-left cell `(0, 0)` of a normal matrix, the candidate loops try rows negative one, zero, and one and columns negative one, zero, and one. Bound checks reject every coordinate containing negative one. The accepted cells are:

- `(0, 0)`;
- `(0, 1)` when a second column exists;
- `(1, 0)` when a second row exists;
- `(1, 1)` when both exist.

The algorithm divides by the number that actually exists, not by nine. This is exactly the boundary rule.

**Why a separate answer matrix preserves simultaneity**

Image filters conceptually transform all pixels at once. Consider two neighboring target cells. Their neighborhoods overlap and both must use the same original value from the overlap.

Because `ans` receives writes while `img` remains unchanged, every read during every neighborhood scan observes the original image. The order of the outer loops cannot affect results.

**Why the method is correct**

For a fixed target `(i, j)`, the nested candidate loops enumerate the Cartesian product of the three permitted row offsets and three permitted column offsets. That covers every possible cell at row and column distance at most one exactly once.

The boundary condition includes precisely those candidates belonging to the matrix. Therefore, `s` equals the sum of all and only valid smoother cells, while `cnt` equals their count. Integer floor division produces the specified rounded-down average.

The outer loops apply this correct calculation to every output coordinate, and the independent output matrix prevents cross-cell interference. Thus the returned matrix is exactly the smoothed image.

**No special cases are necessary**

Corners, edges, one-dimensional images, and one-cell images all use the same candidate generation and bounds check. This uniformity reduces the risk of having separate formulas with inconsistent counts.

## Complexity detail

Let `R` be the number of rows and `C` the number of columns.

There are `R * C` target pixels. Each target checks exactly nine candidate coordinate pairs, a fixed constant independent of image size. Total running time is therefore `O(R * C)`.

The output matrix contains `R * C` integers, so it occupies `O(R * C)` space. Apart from this required result, the algorithm uses only loop indices, a sum, and a count, giving `O(1)` auxiliary working space.

The constant nine matters in practical runtime but is omitted from asymptotic notation. Matrix allocation itself also takes `O(R * C)` time because every output cell is initialized.

## Alternatives and edge cases

- **Two-dimensional prefix sums:** Precompute rectangular sums so each clipped neighborhood sum can be queried with four prefix references. This remains `O(RC)` overall but introduces another `O(RC)` table and more indexing complexity for a fixed three-by-three window.

- **In-place bit encoding:** Since original and smoothed values fit within known ranges, store both in different bit regions of each cell, then extract results in a second pass. This can reduce auxiliary space but is less readable and depends on value bounds.

- **Rolling row buffers:** Retain only enough original rows to compute the next output row. This reduces extra working memory when output can be written progressively, but careful ordering is required.

- **Update `img` directly with plain averages:** This is incorrect because later cells would read already smoothed values rather than the original image.

- **Always divide by nine:** This underestimates boundary pixels by counting nonexistent neighbors as zeros. The divisor must be the number of valid cells.

- **Single-cell image:** The only valid neighborhood cell is the pixel itself, so the output equals the input value.

- **Single row:** A middle cell averages itself and at most its left and right neighbors. The row bound check rejects all other candidate rows.

- **Single column:** The analogous vertical behavior is handled automatically.

- **Corner and edge cells:** Their smaller neighborhoods are counted dynamically, avoiding separate case formulas.

- **All zero pixels:** Every sum is zero and the output remains all zeros.

- **Maximum grayscale values:** A neighborhood sum is at most nine times 255, easily within ordinary integer ranges.

- **Fractional average:** `//` discards the fractional part exactly as required; ordinary floating-point division followed by conversion is unnecessary.

- **Rectangular rather than square image:** Row and column bounds use independent `m` and `n` values, so any legal rectangle is supported.

- **Aliased output rows:** The comprehension creates separate rows. Using `[[0] * n] * m` would alias rows and corrupt multiple output positions during assignment.
