## General
**Allocate each row with its boundary coefficients already fixed**

For zero-based `row_index`, allocate `row_index + 1` entries initialized to `1`. Pascal's boundary identity $\binom{i}{0} = \binom{i}{i} = 1$ means the first and last entries need no recurrence calculation.

**Every interior coefficient has exactly two parents**

For each `column` from `1` through `row_index - 1`, assign `triangle[-1][column - 1] + triangle[-1][column]`. These are the two diagonally adjacent entries above the new position. Only the immediately preceding row is needed for computation, while older rows remain because the output contract requires the full triangle.

**Completed rows are immutable inputs to the next row**

Before constructing `row_index`, every earlier row is complete and satisfies Pascal's recurrence. After filling the interior, that row has correct boundaries and every interior sum, extending the invariant.

**Trace the fifth row from its two-parent sums**

From `[1, 3, 3, 1]`, the interior values become $1+3=4$, $3+3=6$, and $3+1=4$. With boundary ones, the new row is `[1, 4, 6, 4, 1]`.

**Boundary ones and adjacent sums are Pascal's definition**

The first row contains the single boundary value one. For every later row, the two boundaries are again one, while each interior entry is the sum of the two entries above it in the preceding row.

Those assignments are exactly Pascal's recurrence. Starting from the correct base row and applying it to every position constructs each requested row without omission or alteration.

## Complexity detail
The triangle contains $1 + 2 + \dots + numRows = O(numRows^2)$ values, each written once. Time and returned storage are therefore both $O(numRows^2)$; auxiliary working storage beyond the output is $O(numRows)$ for the current row.

## Alternatives and edge cases
- **Compute binomial coefficients independently:** can avoid previous-row access but performs more arithmetic or requires careful multiplicative formulas.
- **Recursive definition:** repeats the same coefficient subproblems without memoization.
- **Return only the final row:** solves Problem 119, not this full-triangle contract.
- `numRows = 1` returns only `[1]`; no previous-row access occurs.
- Each returned row must be a distinct list. Reusing one mutable row object would make earlier output rows change during later updates.
