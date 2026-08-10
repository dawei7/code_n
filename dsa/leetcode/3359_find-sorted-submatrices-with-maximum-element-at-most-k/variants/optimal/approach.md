## General

**Reduce each row to valid suffix widths.** Fix a cell `(row, column)` as the right edge of a possible submatrix row. `widths[row][column]` stores the maximum number of consecutive cells ending there that both:

- contain only values at most `k`; and
- are non-increasing from left to right.

The first pass computes this value with a running `run` for each row. If the current value exceeds `k`, no valid segment can end there and `run` becomes zero. Otherwise, the previous valid run can be extended only when the previous value is also at most `k` and `row[column - 1] >= value`. If extension is impossible, the current cell alone starts a new width-one segment.

The explicit previous-value threshold is consistent with the stored run. It ensures a cell larger than `k` cannot be crossed, even if the local ordering comparison would otherwise pass.

**Turn a vertical row interval into a submatrix count.** Now fix a right column $c$ and a top/bottom row interval $[a,b]$. Every row in a width-$w$ submatrix ending at $c$ must support at least $w$ valid cells. Therefore the greatest allowed width is

$$
M=\min_{r=a}^{b}\texttt{widths}[r][c].
$$

For every integer width from 1 through $M$, choosing columns $c-w+1$ through $c$ produces one distinct valid submatrix. Hence this row interval contributes exactly $M$, not merely one.

The complete answer is therefore the sum of minimum widths over every contiguous row interval, computed separately for each right column.

**Maintain sums of row-interval minima with a monotonic stack.** For one column, process bottom rows from top to bottom. `ending_sum` is the sum of minimum widths for all row intervals ending at the current bottom row. Adding it to `answer` counts all valid submatrices whose bottom and right boundaries are the current cell.

The stack contains pairs `(minimum_width, count)`. Each pair groups a number of possible top rows whose interval ending at the previous row had that same minimum width. Stack widths increase strictly from bottom to top after the update.

**Add the current row as a new interval.** Variable `count` starts at one for the height-one interval containing only the current row. If no earlier stack width is at least the new `width`, this new interval keeps its own minimum and contributes `width`.

**Merge groups whose minimum falls.** While the top stack width is greater than or equal to the current width, appending the current row makes the new width the minimum for every interval in that group. The source removes their old contribution

`previous_width * previous_count`

from `ending_sum` and adds their number of top choices into `count`. After all such groups are popped, it pushes `(width,count)` and adds `width * count`, the replacement contribution for all merged intervals plus the one-row interval.

Using `>=` merges equal widths too. This is not required for correctness but keeps one consolidated group per width and preserves a strictly increasing stack.

**Trace one column of widths.** Suppose the widths down a column are `[3,1,2]`.

- At the first row, interval minima sum to 3.
- At the second, width one replaces the previous minimum for the height-two interval and also forms its own interval, so the sum is $1+1=2$.
- At the third, the three ending intervals have minima 2, 1, and 1, summing to 4.

The column contributes $3+2+4=9$ submatrices across all bottom rows and left widths. The stack performs these updates without enumerating the three row intervals separately at every step.

**Why width zero naturally contributes nothing.** A value above `k` creates width zero. It pops all positive groups, consolidates all intervals ending at that row under minimum zero, and makes `ending_sum` zero. Any vertical interval containing that row has no positive feasible width, exactly as required.

**Every valid submatrix is counted exactly once.** A submatrix has one bottom row, one right column, one top row, and one width. At that bottom/right step, the chosen top defines one row interval and the width is among 1 through its minimum stored width, so it is counted. No other step shares the same bottom and right boundaries, preventing duplication.

Conversely, every unit counted by a row-interval minimum chooses a width supported by every row. Each row segment is non-increasing and contains only values at most `k`, so the constructed submatrix meets both conditions. No vertical ordering condition exists in the statement, so rows need not compare with one another.

## Complexity detail

Let the matrix have $m$ rows and $n$ columns. Building `widths` visits every cell once, costing $O(mn)$ time.

For each column, a row's pair is pushed once and popped at most once. The amortized stack work is $O(m)$ per column, or $O(mn)$ total. Overall time is $O(mn)$.

The `widths` table uses $O(mn)$ space. A column stack uses $O(m)$ additional space, which is dominated by the table. The manifest's $O(mn)$ space bound matches the exact source. A more memory-optimized implementation could process widths row-wise with per-column structures, but this source materializes the table.

## Alternatives and edge cases

- **Enumerate all submatrices:** Four boundaries already create $O(m^2n^2)$ candidates, and checking rows would add more work.
- **Histogram expansion from every top row:** It can recompute the same minima repeatedly and degrade to $O(m^2n)$.
- **Segment tree for minima:** It answers interval minima but still leaves too many row intervals; the monotonic stack aggregates them in linear time.
- **Single cell above `k`:** Its width is zero and it contributes no submatrix.
- **Single valid cell:** Its width is one and it contributes exactly one.
- **Equal adjacent row values:** Non-increasing order permits equality, so the run extends.
- **Increasing step left to right:** When the previous value is smaller, the run restarts at one.
- **Barrier above `k`:** Valid suffixes cannot cross it even if later values are small.
- **All cells equal and at most `k`:** Every submatrix is valid; stack minima reproduce the full combinatorial count.
- **Vertical values:** They may rise or fall freely because sorting is required separately within each row only.
- **Width zero in the stack:** It resets `ending_sum` for all intervals containing the invalid row.
- **Equal stack widths:** The `>=` pop condition merges them into one count group.
- **Large answer:** The number of submatrices can be large, but Python integers do not overflow.
- **Input preservation:** The separate `widths` table is built without altering `grid`.
- **Generated source status:** With no local editorial, the explanation follows the exact width recurrence and stack arithmetic in the Optimal file.
