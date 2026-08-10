## General

**Treat the inputs as remaining sums**

The source constructs an $M\times N$ zero matrix `ans`. During filling, `rowSum[i]` and `colSum[j]` no longer represent untouched original requirements; they represent how much total still needs to be placed in that row and column.

At cell `(i,j)`, the largest non-negative value that does not exceed either remaining requirement is:

`x = min(rowSum[i], colSum[j])`.

The code stores `x` in the cell, then subtracts it from both remaining sums.

This is the northwest-corner greedy rule for a transportation table. The source visits every matrix coordinate in row-major order.

**Why taking the minimum is always safe**

Any cell value must be no larger than the row’s remaining sum and no larger than the column’s remaining sum. Choosing their minimum satisfies both constraints and makes at least one of them zero:

- if the row remainder is smaller, the current row is completed;
- if the column remainder is smaller, the current column is completed;
- if they are equal, both are completed.

All input sums and all remainders are non-negative, so every assigned `x` is non-negative.

The algorithm does not need to reserve capacity through lookahead. Total row demand equals total column demand. If a row consumes the available amount in one column, that amount had to be assigned somewhere in that column; if a column is exhausted, later rows simply place zero there and use remaining columns.

**How the nested loops behave**

The outer loop fixes a row `i`, and the inner loop visits every column `j`.

If a prior cell exhausts the current row, `rowSum[i]` becomes zero. Every later cell in that row receives `min(0, colSum[j]) = 0`.

If earlier rows exhaust a column, `colSum[j]` is zero. Later rows place zero in that column.

The source does not skip these completed rows or columns, so it performs all $MN$ cell iterations. A pointer-optimized variant could jump after one side reaches zero, but the returned matrix initialization itself is already $O(MN)$.

**Why every row becomes complete**

Consider row `i` when its processing begins. Its remaining demand must be no greater than the total remaining column capacity. This is because the total remaining row demand over row `i` and all later rows equals that same total column capacity.

As the inner loop moves across columns, it repeatedly takes as much as possible. If the row demand were still positive after the final column, then every column must have been exhausted while the row remained positive. That would mean total available column capacity was smaller than the row’s demand, contradicting the equal-total invariant. Thus `rowSum[i]` reaches zero.

**Why every column becomes complete**

Every assignment subtracts the same `x` from one row total and one column total, so the sum of all remaining row demands always equals the sum of all remaining column demands.

After the final row, the previous argument shows every row remainder is zero. Their total is zero, so the equal column remainder total is also zero. Since column remainders never become negative, every individual `colSum[j]` must be zero.

Therefore, the values placed in each row sum to its original requirement, and values in each column sum to its original requirement.

**A sample construction**

For `rowSum = [3,8]` and `colSum = [4,7]`:

- At `(0,0)`, choose three. Row zero becomes zero and column zero retains one.
- At `(0,1)`, choose zero.
- At `(1,0)`, choose one. Column zero becomes zero and row one retains seven.
- At `(1,1)`, choose seven, completing both.

The matrix is `[[3,0],[1,7]]`.

**Input mutation**

The method subtracts directly from the caller-provided `rowSum` and `colSum` lists. On successful completion, both lists contain zeros. This mutation is part of the exact source behavior. A caller that needs the original requirements afterward must pass copies.

**Why any valid matrix is enough**

The problem does not ask to recover an original hidden matrix or optimize cell values. Many matrices can share the same margins. The greedy construction needs only to satisfy non-negativity and all sums, which the invariant proves.

## Complexity detail

Let $M$ be the number of rows and $N$ the number of columns.

Allocating the output matrix takes $O(MN)$ time, and the nested loops visit all $MN$ cells with constant work, so total time is $O(MN)$.

The returned matrix itself contains $MN$ integers, so including output storage the source uses $O(MN)$ space, matching the package manifest. Excluding the required output, it uses only scalar loop variables and mutates the two input arrays, so auxiliary working space is $O(1)$.

## Alternatives and edge cases

- **Pointer-optimized northwest-corner traversal:** Advance the row when its remainder reaches zero, otherwise advance the column. It fills only $O(M+N)$ potentially nonzero positions, though allocating the dense output still costs $O(MN)$.
- **Separate current row and column totals:** This avoids mutating inputs but adds $O(M+N)$ auxiliary arrays.
- **Network flow:** The problem can be modeled as transportation flow, but equal totals and unrestricted non-negative cells make the greedy construction sufficient.
- **Try to reconstruct a unique original matrix:** No unique original is promised or required; any valid margins are accepted.
- **Zero-sum row:** Every cell in it becomes zero.
- **Zero-sum column:** Every row places zero in that column.
- **One row:** Each cell receives the remaining column sum, and the equal-total guarantee completes the row.
- **One column:** Each row’s required sum is placed in its only cell.
- **Equal row and column remainder:** The chosen value exhausts both simultaneously.
- **Large sums:** Python integers handle values through $10^8$ and their totals without overflow.
- **Non-negativity:** Taking the minimum of non-negative remainders and never overspending keeps every cell and remainder non-negative.
- **Input mutation:** Both requirement lists are consumed to zeros; pass copies when preservation matters.
- **Guaranteed equal totals:** The proof relies on `sum(rowSum) == sum(colSum)`. Without it, no valid completion may exist.
