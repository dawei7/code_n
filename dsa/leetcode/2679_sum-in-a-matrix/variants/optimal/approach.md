## General

**Replace repeated removals with sorted ranks**

Every round removes the largest remaining number from each row, then adds the largest of those removed numbers to the score.

Within one row, the removal order is completely determined by value: largest, second largest, third largest, and so on. Ties do not change the values removed.

Sorting each row once records this order in a stable layout. The exact solution sorts in ascending order, so the rightmost column contains each row's largest value, the column just left of it contains each row's second largest value, and so forth.

**Why ascending order still represents largest-first rounds**

After sorting a row of length $n$:

- column $n-1$ represents round one;
- column $n-2$ represents round two;
- column zero represents the final round.

The implementation later processes columns from left to right, which is the reverse of the chronological removal order.

That reversal is harmless because the final score is a sum. Addition is commutative, so summing round contributions from last round to first produces the same total as summing them from first to last.

**Align equal order statistics across rows**

Once all rows are sorted, a fixed column has the same rank in every row.

For example, the rightmost column holds every row's maximum. Taking the maximum of that column gives exactly the score added in the first removal round.

Similarly, the next column holds every row's second-largest remaining value, and its maximum is the second round's contribution.

This turns a changing-matrix simulation into a static column calculation.

**What `zip(*nums)` does**

The star operator supplies the rows as separate arguments to `zip`. The result iterates over tuples of values at matching column positions.

For sorted rows:

`[[1, 2, 7], [2, 4, 6], [3, 5, 6]]`

`zip(*nums)` conceptually yields:

- `(1, 2, 3)` for column zero;
- `(2, 4, 5)` for column one;
- `(7, 6, 6)` for column two.

Applying `max` to each tuple yields 3, 5, and 7. Their sum is 15.

Chronologically, the game adds 7, then 5, then 3. The same three contributions appear in reverse order.

**Why sorting each row independently is enough**

The rules never compare positions within a row when choosing which element to remove; they compare values and always remove a maximum. Therefore original column positions have no semantic importance.

Sorting one row cannot affect which values another row offers in each rank. After every row is ranked independently, taking a maximum across equal ranks exactly performs the inter-row selection for that round.

There is no need to sort the entire matrix globally, which would lose row membership and fail to enforce one removal per row.

**Trace ties**

Suppose a row contains `[5, 5, 1]`. Either 5 may be removed first, but the row's value sequence is still 5, 5, 1.

Sorting gives `[1, 5, 5]`, so both largest-rank columns contain 5. The algorithm therefore represents either permitted tie choice without needing to track element identity.

**The column maximum is the exact round score**

In a particular round, one equal-rank value is removed from every row. The rule adds only the highest removed value, not their sum.

That is why the expression uses `map(max, zip(*nums))`. Replacing `max` with `sum` would calculate a different game score by charging every removed element.

The outer `sum` then combines one maximum per round.

**Input mutation**

`row.sort()` changes each inner row in place. After the method returns, `nums` contains sorted rows rather than the original ordering.

This is safe for the challenge because the answer depends only on row values and the solution does not need original positions later. If a caller needed to preserve the matrix, it would need to sort copies, which uses more storage.

**Rectangular-matrix assumption**

The transpose operation aligns columns and is intended for a matrix whose rows have the same length. That is also necessary for the original process to remove one value from every row until the matrix becomes empty simultaneously.

Python's `zip` would stop at the shortest row for a ragged input, so the exact code relies on the matrix contract rather than repairing irregular rows.


After sorting, column $j$ contains the $(j+1)$-th smallest value of every row. Equivalently, it contains the values removed in one specific round when rounds are viewed in reverse.

The maximum of that column is exactly the value added for that round. Every removal rank corresponds to one column and every column is used once. Summing all column maxima therefore equals the final game score.

**Why this is efficient**

Repeatedly searching every row for its current maximum would scan or maintain changing structures across many rounds. Sorting performs the ranking once.

Afterward, transpose iteration and maxima examine each matrix element only once.

## Complexity detail

Let $m$ be the number of rows and $n$ their common length. Sorting one row costs $O(n\log n)$, so sorting all rows costs $O(mn\log n)$. Computing all column maxima visits $mn$ values, which does not exceed the sorting term.

The rows are sorted in place. Python's sorting algorithm may use $O(n)$ temporary space for one row, and `zip` produces column tuples lazily. Thus auxiliary space is $O(n)$ at a time, excluding the input. No output collection proportional to the matrix is created.

## Alternatives and edge cases

- **Simulate with repeated row scans:** Correct but can cost $O(mn^2)$ because maxima are rediscovered.
- **Max-heap per row:** Supports repeated removals in $O(mn\log n)$ but uses additional heap storage.
- **Counting frequencies:** Values are bounded, so counts can avoid comparison sorting, though the implementation is more specialized.
- **Sort rows descending:** Then columns correspond to chronological rounds directly; the final sum is unchanged.
- **One cell:** Sorting changes nothing and that value is returned.
- **One row:** Every removed value becomes a round maximum, so the answer is the row sum.
- **Tied maxima:** Element identity is irrelevant; sorted value ranks remain correct.
- **Zero values:** They participate normally and can contribute zero in late rounds.
- **Rectangular input:** Required by the transpose logic and the simultaneous-emptying process.
- **Ragged input:** The exact `zip` behavior would truncate to the shortest row and is not intended for that case.
- **Mutation:** Every inner row is reordered in place.
- **Maximum versus sum:** Each column contributes only its largest value.
