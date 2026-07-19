## General
Each column sum fixes how its two bits can look. A zero forces `[0, 0]`, a two forces `[1, 1]`, and a one must place exactly one bit in either row. This makes the columns with sum two mandatory and leaves only the sum-one columns to distribute.

**Commit the forced columns first**

For every `colsum[i] == 2`, set both output entries to `1` and decrement both remaining row sums. If either remaining requirement becomes negative, the forced ones already exceed that row's target, so no reconstruction exists.

**Distribute flexible columns greedily**

For a column with sum one, assign its single `1` to a row that still needs one. Choosing the row with the larger remaining requirement keeps the demands balanced, although assigning to either positive remainder is sufficient. Decrement the selected remainder after the assignment.

After all columns, both remainders must be zero. If so, every column has its required sum and both row totals match. If either remainder is nonzero, there were not enough sum-one columns to meet the requested totals, so return `[]`.

## Complexity detail
The two passes inspect the $n$ columns a constant number of times, taking $O(n)$ time. The two output rows contain $2n$ bits and therefore require $O(n)$ space; auxiliary counters use $O(1)$ space beyond the returned matrix.

## Alternatives and edge cases
- **Backtracking over sum-one columns:** It explores every distribution and can take exponential time even though only the remaining row totals matter.
- **Count-only feasibility check:** Counting sum-two and sum-one columns can decide existence, but a second step is still needed to construct the requested matrix.
- **Too many forced ones:** If the number of sum-two columns exceeds either row target, return `[]` immediately.
- **Mismatched total:** A necessary condition is $\texttt{upper}+\texttt{lower}=\sum_i \texttt{colsum[i]}$; the final remainder check enforces it.
- **Zero row target:** Every flexible one must go to the other row, while any sum-two column makes a zero target impossible.
- **Multiple answers:** The order in which flexible columns are assigned may change the matrix without affecting validity.
