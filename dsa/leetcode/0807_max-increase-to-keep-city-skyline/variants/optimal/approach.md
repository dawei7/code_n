## General

**Reduce each skyline to row and column maxima**

Looking from east or west, only the tallest building in each row determines that row's visible outer height. Looking from north or south, only the tallest building in each column matters.

Therefore the four directional skylines are preserved exactly when:

- every row keeps its original maximum;
- every column keeps its original maximum.

The method records those limits before changing anything:

`row_max[i] = max(grid[i])`

and:

`col_max[j] = max(grid[r][j] for every row r)`.

`zip(*grid)` transposes rows into column tuples, so the column comprehension can apply `max` directly.

**Derive one building's highest allowed height**

Building `grid[i][j]` belongs to row `i` and column `j`.

To preserve the row skyline, its new height cannot exceed `row_max[i]`. To preserve the column skyline, it cannot exceed `col_max[j]`.

Both restrictions must hold, so the largest feasible height is:

$$
\min(row\_max[i],col\_max[j]).
$$

Any higher value would exceed at least one original maximum and visibly raise that direction's skyline.

**Why raising to the minimum does not lower or change a maximum**

The algorithm only increases heights; it never lowers the building that originally realized a row or column maximum.

Setting one cell no higher than both original limits cannot create a new larger row or column maximum. The original maximum-height cells remain, so neither maximum can decrease.

Thus the computed ceiling is feasible for that cell.

**Why every cell can be raised independently**

A concern might be that raising many cells to their individual ceilings could interact and change a skyline collectively.

It cannot. Every raised value in row `i` remains at most the fixed `row_max[i]`, so their collective row maximum remains at most that value. An original cell still equals the value, so the maximum remains exactly equal.

The same argument holds for every column. Therefore all individual maximum increases can be applied simultaneously.

There is no budget or coupling constraint requiring tradeoffs between cells.

**Compute the contribution of one cell**

For original height `x = grid[i][j]`, its maximum increase is:

`min(row_max[i], col_max[j]) - x`.

This value is never negative. Since `x` belongs to its row and column, it is no greater than either corresponding maximum.

Summing these independent contributions yields the greatest possible total increase.

**Trace a representative cell**

In the first example, cell `(0,1)` has height zero. Row zero's maximum is eight, and column one's maximum is four.

Its ceiling is `min(8,4)=4`, so it can gain four units. Raising it to five would change the column-one skyline, even though the row could allow more.

Cell `(1,0)` has height two. Its row maximum is seven and its column maximum is nine, so its ceiling is seven and its increase is five.

**Why a current skyline maximum may have zero increase**

If a cell equals the smaller of its row and column maxima, its computed contribution is zero.

For example, a row's unique tallest building cannot rise above the row maximum without changing the east/west skyline. It may also already be limited by its column.

The goal permits increasing any number of buildings, including leaving some unchanged.

**All-zero grid**

Every row and column maximum is zero. Each cell's ceiling is zero, so every contribution is zero.

Raising even one building would create a positive maximum in its row and column, visibly changing skylines. The total answer zero is therefore necessary.

**The fixed-limit invariant**

`row_max` and `col_max` are computed from the original grid and never updated.

This is intentional. Updating them while imagining increases would allow later buildings to use already raised maxima, progressively changing the skyline. The constraints are the original visible contours, so all cells must be compared with fixed original limits.

**Why the total is globally maximal**

For any feasible modified grid, cell `(i,j)` is bounded above by the minimum of its original row and column maxima. Hence its increase cannot exceed the term summed by the algorithm.

The algorithm's proposed height reaches that bound for every cell simultaneously while preserving all maxima. It achieves the sum of per-cell upper bounds, so no other feasible modification can have a larger total.

This proves both feasibility and optimality.

## Complexity detail

Let $n$ be the square grid dimension. Computing all row maxima examines $n^2$ values. Transposing and computing column maxima also processes $n^2$ values. The final sum visits every cell once. Total time is $O(n^2)$.

The two maximum arrays contain $n$ values each, using $O(n)$ auxiliary space. In Python, `zip(*grid)` yields column tuples lazily one at a time; the active tuple has length $n$, which remains within the same $O(n)$ peak bound.

## Alternatives and edge cases

- **Scan columns by index:** Avoid `zip` and compute each column maximum with nested indexing. It has the same $O(n^2)$ time and $O(n)$ stored maxima.

- **Try incremental increases:** Repeatedly raising buildings obscures the direct upper bound and may take time proportional to height differences.

- **Use only row maxima:** It can violate north/south skylines.

- **Use only column maxima:** It can violate east/west skylines.

- **Update maxima after raises:** Incorrect because the allowed skyline is fixed by the original grid.

- **All-zero grid:** No positive increase is possible.

- **Cell already at its ceiling:** Its contribution is zero.

- **Several row maxima:** Raising other cells up to the same maximum does not change the outer contour.

- **Zero-height building:** It may be raised whenever both its row and column limits are positive.

- **Input preservation:** The exact solution calculates the total without modifying `grid`.
