## General
**A rolling row stores optimal costs from above and left**

Let `cost[column]` hold the minimum sum to reach the relevant cell in that column. While scanning a new row, its old value is the best cost from above, and the already updated `cost[column - 1]` is the best cost from the left. This mixed old/new meaning is why columns must be processed left to right.

**Initialize the only-path boundaries before using the recurrence**

The first cell starts with its own value. Along the first row, only movement from the left is possible; along the first column of later rows, only movement from above is possible. These boundaries must accumulate directly rather than taking a minimum against a nonexistent predecessor.

For every interior cell, add its unavoidable value to `min(cost_from_above, cost_from_left)`.

**Local optimal substructure is sufficient because moves never go backward**

After updating `(row, column)`, `cost[column]` is the minimum sum of any valid path ending there. Entries left of it describe the current row; entries right of it still describe the preceding row, supplying exactly the predecessor values needed next.

**Trace the rolling costs row by row**

For `[[1,3,1],[1,5,1],[4,2,1]]`, the first row produces `[1,4,5]`. The next becomes `[2,7,6]`, and the last becomes `[6,8,7]`; the destination minimum is 7.

**The final predecessor exposes the optimal substructure**

Every path to a non-start cell makes its final move from above or from the left. Once the best cost to each predecessor is known, no path through a more expensive predecessor route can improve the destination cell; choose the smaller predecessor cost and add the current cell's unavoidable value.

Row-major processing computes those predecessor optima before they are used. Repeating the final-move argument across the grid makes every stored state minimal, including the bottom-right answer.

## Complexity detail
Every cell is processed once, so time is $O(mn)$. The rolling array stores one value per column, using $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Full matrix DP:** is equally direct but consumes $O(mn)$ additional space.
- **Unmemoized recursive path search:** evaluates every movement sequence and grows exponentially.
- **Overwrite the input grid:** achieves $O(1)$ auxiliary space but violates a nonmutating adapter expectation.
- A one-cell grid returns that cell's value. One-row and one-column grids have exactly one path, so their answer is the sum of all cells.
- Nonnegative values are part of the contract, but the acyclic right/down recurrence would still compute a minimum correctly for arbitrary finite weights because no cycle can be exploited.
