## General

**Map every output position to one fixed window**

The output has size $(n-2)\times(n-2)$. An output coordinate `(i, j)` corresponds to the contiguous $3\times3$ input window whose top-left corner is `(i, j)`. Equivalently, that window is centered at input coordinate `(i+1, j+1)`.

Its rows are:

```text
i, i + 1, i + 2
```

and its columns are:

```text
j, j + 1, j + 2
```

The largest of those nine cells is exactly `ans[i][j]`. Once this coordinate mapping is clear, the solution is a direct simulation of the definition.

**Why there are exactly `n - 2` starting positions**

A $3\times3$ window starting at row `i` needs index `i + 2` to remain inside the matrix, so `i <= n - 3`. The valid zero-based starts are `0` through `n - 3`, which is `n - 2` choices. The same reasoning applies to columns.

Therefore, both outer loops use `range(n - 2)`, and the result matrix is allocated with `n - 2` rows and columns. No padding or boundary checks are needed inside a valid window.

**Inspect the nine cells with a generator**

For one output coordinate, the exact assignment is:

```python
ans[i][j] = max(
    grid[x][y]
    for x in range(i, i + 3)
    for y in range(j, j + 3)
)
```

The first generator loop chooses each of the three rows. For each selected row, the second chooses each of the three columns. Their Cartesian product yields all nine coordinates in the window exactly once.

`max` consumes these values and returns their greatest value. The generator is lazy: it does not allocate a separate nine-element list. It produces one cell value at a time for `max`.

All input values are positive, but the implementation does not depend on choosing zero as an initial maximum. Python's `max` initializes from actual generated values. This would remain correct even if negative grid values were allowed.

**Overlapping windows are intentionally recomputed**

Adjacent $3\times3$ windows share six cells, but the solution examines all nine cells for each output. Since the window dimensions are fixed constants, nine inspections are still constant work. More advanced sliding-window structures would reduce repeated comparisons but would not improve the asymptotic $O(n^2)$ bound.

For the second example, the central value `2` lies in every possible $3\times3$ window of the $5\times5$ grid. Each independent generator encounters it, so every output position receives `2`.

**Trace one output cell**

For the top-left output coordinate `(0, 0)`, the generator examines input rows `0, 1, 2` and columns `0, 1, 2`. In:

```text
9 9 8
5 6 2
8 2 6
```

the maximum is `9`, so `ans[0][0] = 9`.

For `ans[1][0]`, the window moves down one row and examines input rows `1, 2, 3` while keeping columns `0, 1, 2`. Its maximum is `8`. The output indices therefore track window starts, not input centers directly.

**Why the result is correct**

Fix any valid output coordinate `(i, j)`. By construction, the two nested generator ranges enumerate precisely the row and column indices of the contiguous $3\times3$ input submatrix beginning at `(i, j)`. Every one of its nine cells is supplied to `max`, and no cell outside it is supplied.

The mathematical definition of a maximum guarantees that the returned value is at least every cell in the window and equals one of them. It is thus exactly the largest local value required for this output coordinate.

The outer loops visit every valid top-left coordinate once, and the allocated output contains exactly those coordinates. Hence, every required local maximum is written to its corresponding cell, with no missing or extra output.

**Why no mutation is needed**

The output is allocated separately from `grid`. This matters because neighboring windows overlap. If the method overwrote input cells with local maxima before later windows were evaluated, those later windows could read modified rather than original values. Keeping `grid` read-only avoids that hazard and matches the function's clean data flow.

## Complexity detail

There are $(n-2)^2$ output cells. For each, the generator yields exactly nine input values. The number of cell inspections is:

$$
9(n-2)^2,
$$

which is $O(n^2)$. The fixed factor nine is omitted in asymptotic notation.

The output matrix stores $(n-2)^2$ integers, so including required result storage the space complexity is $O(n^2)$. Beyond the result, loop variables and the small generator state use $O(1)$ auxiliary space. The exact code does not allocate a per-window list.

## Alternatives and edge cases

- **Two-pass sliding maxima:** Compute width-three row maxima and then height-three column maxima with deques. This is useful for variable or very large windows, but fixed $3\times3$ scanning is simpler and already $O(n^2)$.
- **Helper function per window:** Moving the nine-cell scan into a named function may improve readability but performs the same work.
- **Materialize each window:** Building a list of nine values before calling `max` is correct but creates unnecessary temporary objects; the generator avoids them.
- **Minimum size `n = 3`:** There is exactly one valid window, so the result is a $1\times1$ matrix containing the maximum of the entire input.
- **All values equal:** Every local maximum equals that common value.
- **Maximum on a window boundary:** The generator includes all three rows and columns, so corners and edges are treated the same as the center.
- **One large value shared by windows:** Every overlapping window that contains it independently reports it.
- **Input preservation:** A separate `ans` matrix ensures later windows never see altered values.
- **Off-by-one boundary:** `range(n - 2)` ends at `n - 3`, the last start whose `+2` index is `n - 1`.
