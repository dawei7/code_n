## General

Each grid cell $(i,j)$ holds a vertical tower of `grid[i][j]` unit cubes. A projection collapses one spatial axis, so overlapping cubes hide one another. The three viewing directions therefore require three different summaries:

- From above onto the $xy$ plane, only whether a tower exists matters.
- From one side onto the $yz$ plane, only the tallest tower in each row matters.
- From the perpendicular side onto the $zx$ plane, only the tallest tower in each column matters.

The solution calculates these three areas independently and adds them.

**Top projection onto $xy$.** A nonempty tower covers exactly one unit square when viewed from above, regardless of whether its height is 1 or 50. An empty cell covers nothing. Thus

```text
xy = sum(v > 0 for row in grid for v in row)
```

visits every cell and sums booleans. In Python, `True` contributes 1 and `False` contributes 0, so `xy` is exactly the number of positive cells.

**Side projection summarized by rows.** Fix one row. Towers in that row line up behind one another when projected along the corresponding horizontal axis. At height level 1, the shadow is present if any tower reaches height 1; at level 2, it is present if any tower reaches height 2; and so on. The visible vertical extent is therefore the maximum height in that row. Summing row maxima gives

```text
yz = sum(max(row) for row in grid)
```

area for one side projection. Shorter towers in the same row lie within the shadow already created by the tallest tower and do not add separate area.

**Perpendicular side projection summarized by columns.** The other side view applies identical reasoning to each column. The expression `zip(*grid)` groups values at the same column index into tuples. Calling `max(col)` finds the tallest tower in each column, and summing those maxima produces `zx`.

For `grid = [[1,2],[3,4]]`:

- All four cells are positive, so the top area is 4.
- Row maxima are 2 and 4, so one side area is 6.
- Column maxima are 3 and 4, so the other side area is 7.

The total is $4+6+7=17$.

**Why maxima, not sums, describe a side shadow.** Consider heights 2 and 4 aligned along the viewing direction. The height-2 tower covers projected levels 1 and 2, while the height-4 tower covers levels 1 through 4. Their shadows overlap on the first two levels, so their union has area 4, not $2+4=6$. Taking the maximum counts each visible unit square once.

**Why the three values can simply be added.** The problem asks for the total areas of three separate planar projections, not the area of a union in one common plane. An area square seen from above and another seen from the side belong to different projection measurements, so adding them is exactly the requested operation.
In the top view, each grid position contributes one if and only if at least one cube occupies that vertical line, which the positive test captures. In a row side view, the projected unit squares are precisely heights $1$ through the tallest tower, so their count is the row maximum. The same argument applies to each column for the other side. Rows and columns occupy disjoint horizontal positions within their respective projection planes, so summing their maxima introduces no overlap within a view. Therefore `xy + yz + zx` equals the full requested area.

The method never needs to represent individual cubes. A tower height is already the sufficient statistic for all three shadows.

## Complexity detail

Let $n$ be the side length of the square grid. Each of the three calculations examines all $n^2$ values once overall up to a constant factor.

- **Time complexity:** $O(n^2)$.
- **Space complexity:** $O(n)$ under the manifest's implementation-level accounting. `zip(*grid)` maintains one iterator per row and creates one column tuple of length $n$ at a time.

No $n\times n$ auxiliary matrix is created. Excluding temporary iterator and tuple storage, the mathematical aggregation uses only a constant number of totals.

## Alternatives and edge cases

- **One explicit nested loop:** Track positive cells, row maxima, and column maxima manually. This has the same time bound and uses an $O(n)$ column-maximum array.
- **Build a transposed matrix:** Then take row maxima of both orientations. It works but allocates $O(n^2)$ data unnecessarily.
- **Model every unit cube:** Expanding towers takes time proportional to the sum of all heights, even though only occupancy and maxima matter.
- **Sum tower heights for side views:** This double-counts overlapping shadow levels along the viewing direction.
- **All zeros:** Every positive test is false and every row and column maximum is zero, so total projection area is zero.
- **One cell of height `v`:** Top area is 1 when $v>0$, and each side area is $v$, giving $1+2v$. For `v=2`, the result is 5.
- **Sparse diagonal towers:** Each positive cell contributes separately to the top, while row and column maxima capture the separated side positions.
- **Several towers in one row:** Only the tallest affects that row's side projection.
- **Several towers in one column:** Only the tallest affects that column's perpendicular projection.
- **Equal maxima:** Equal-height towers aligned in one viewing line still create one shadow of that height, not multiple copies.
- **Square-grid guarantee:** Every row is nonempty and has equal length, so `max(row)` and `zip(*grid)` are safe.
- **Value magnitude:** Heights affect maxima but not the number of grid positions traversed.
