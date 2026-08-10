## General

**Fix two row boundaries to reduce the matrix to one dimension**

A submatrix is determined by top, bottom, left, and right boundaries. The solution enumerates every top and bottom row pair. Once those two boundaries are fixed, it compresses all included rows into one array of column sums.

If `col[k]` is the sum of matrix cells in column `k` between the fixed top and bottom rows, then the sum of a submatrix spanning columns `left` through `right` equals the sum of the one-dimensional subarray `col[left:right + 1]`.

The two-dimensional counting problem for one row band therefore becomes the familiar problem of counting one-dimensional subarrays with sum `target`.

**Count target-sum subarrays with prefix frequencies**

The helper `f(nums)` begins:

```python
d = defaultdict(int)
d[0] = 1
cnt = s = 0
```

`s` is the running prefix sum through the current position. `d[value]` records how many earlier prefixes had that value. `cnt` accumulates matching subarrays.

The artificial empty prefix has sum zero and occurs once. Initializing `d[0] = 1` allows a subarray starting at index zero to be counted. If the current prefix sum itself equals `target`, then `s - target` is zero and that empty prefix supplies one match.

For each value:

```python
s += x
cnt += d[s - target]
d[s] += 1
```

Suppose an earlier prefix sum was `p`. The sum after that prefix through the current index is `s - p`. This subarray equals `target` exactly when:

```text
p = s - target
```

Every previous occurrence of `s - target` gives a different starting boundary, so the helper adds its frequency.

Only after counting does it record the current prefix. This order ensures a nonempty subarray: the current prefix cannot pair with itself.

Negative numbers cause no difficulty. Prefix sums need not be monotonic because the hash map finds exact differences rather than relying on a sliding window.

**Build each compressed row band incrementally**

The outer loops are:

```python
for i in range(m):
    col = [0] * n
    for j in range(i, m):
```

`i` is the top row. `j` advances from that top through every possible bottom row.

For a new top row, `col` starts at zeros. When bottom `j` is included:

```python
for k in range(n):
    col[k] += matrix[j][k]
```

adds that entire row to the compressed column sums.

After the update, `col[k]` equals:

```text
matrix[i][k] + matrix[i + 1][k] + ... + matrix[j][k]
```

The code reuses the previous band rather than recomputing all rows from `i` through `j`. Extending the bottom boundary costs only one pass over columns.

**Count every horizontal interval in the band**

After updating `col`:

```python
ans += f(col)
```

counts every contiguous column interval whose compressed sum equals `target`. Each such interval corresponds to one submatrix with top row `i`, bottom row `j`, and those left and right columns.

The helper returns a count, not the actual boundaries, because only the total number is requested.

**Why every submatrix is counted exactly once**

Take any target-sum submatrix. It has one unique top row `i` and bottom row `j`. The outer loops reach exactly that pair. At that moment, `col` contains precisely the vertical sums across its rows.

The submatrix's unique left and right columns form a contiguous subarray in `col` with the same total. The prefix-frequency helper counts that subarray once.

Conversely, every subarray counted by `f(col)` selects contiguous columns for the current fixed row band. Combining those boundaries produces a real nonempty submatrix, and the compressed sum proves it equals `target`.

Different boundary quadruples are processed through different row pairs or different subarray boundaries, so no submatrix is double-counted.

**A small conceptual trace**

For a fixed band of two rows, suppose compression produces `col = [2, -1, 1]` and the target is two.

The helper counts the first element `[2]` and the full range `[2, -1, 1]`. These correspond to two different submatrices sharing top and bottom rows but using different column boundaries.

When the bottom row expands, `col` changes and the helper counts submatrices for that new row band independently.

## Complexity detail

Let `R` be the number of rows and `C` the number of columns.

There are `R(R + 1) / 2` top-bottom row pairs. For each pair, updating `col` across the newly added row costs `O(C)`, and `f(col)` also costs `O(C)` expected time using hash-map operations. Total exact time is `O(R^2C)`.

`col` uses `O(C)` space. The prefix-frequency map inside `f` can hold `O(C)` distinct sums. It is recreated per row band, so peak auxiliary space is `O(C)`.

The manifest uses `S` for the shorter matrix dimension and `L` for the longer dimension, recording `O(S^2L)` time and `O(L)` space. The exact source reaches that bound when rows are the shorter dimension.

If `R > C`, the exact row-pair orientation takes `O(R^2C)`, which is `O(L^2S)` rather than the stronger manifest target. To guarantee `O(S^2L)`, pair boundaries along the smaller dimension: use row pairs when `R <= C` and column pairs otherwise, or transpose the matrix first. The one-dimensional helper remains unchanged.

## Alternatives and edge cases

- **Choose the smaller paired dimension:** Transpose or branch so the squared dimension is `min(R, C)`. This guarantees the manifest's `O(S^2L)` time and `O(L)` space.
- **Two-dimensional prefix sums plus four boundaries:** Constant-time rectangle queries still leave `O(R^2C^2)` boundary combinations, much slower than the reduction.
- **Column-pair compression:** Fix left and right columns, compress row sums, and run the same prefix-map helper. It is symmetric and preferable when columns are fewer.
- **Target zero:** The initial zero-prefix frequency correctly counts zero-sum intervals, including those created by cancellations.
- **Negative cells:** A two-pointer window would fail because sums can decrease. Prefix differences remain correct.
- **One cell:** The single row band and single column interval contribute one exactly when the cell equals target.
- **One row:** The algorithm reduces directly to one call of the one-dimensional subarray-sum method.
- **One column:** Every row band produces one compressed value, counting all vertical submatrices with the target sum.
- **Repeated prefix sums:** Frequencies, not just set membership, are necessary because each occurrence creates a different starting boundary.
- **Empty prefix:** `d[0] = 1` counts intervals beginning at column zero; it does not represent an empty returned submatrix.
- **Nonempty submatrices:** Recording the current prefix after the lookup prevents pairing a prefix with itself.
- **Large count:** Python integers avoid overflow when many boundary combinations match.
- **Input preservation:** Compression accumulates into `col` and never modifies `matrix`.
