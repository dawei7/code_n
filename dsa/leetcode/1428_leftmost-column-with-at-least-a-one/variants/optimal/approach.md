## General

**Start at the top-right corner.** At `(row, col)`, a `0` proves that every cell to its left in the same row is also `0`, because that row is non-decreasing. No cell in that row can improve the answer, so move down. A `1` proves that `col` is feasible, but an earlier feasible column may still exist, so record `col` and move left.

**Discard one boundary on every query.** After moving down, the completed row contains no `1` at or left of the current search boundary. After moving left, the recorded column contains a witnessed `1`, while every column to its right is irrelevant to finding a smaller index. The only cells that can still improve the answer lie in the remaining lower-left rectangle. Repeating the same decision therefore never discards a possible smaller answer.

The walk stops after passing the final row or moving left of column zero. `answer` is updated on every observed `1`, and columns are visited from right to left, so its final value is the smallest witnessed feasible column. If no `1` was observed, it remains `-1`. Because each query is followed by one left or downward move, at most $m+n-1$ calls to `get` are made; with $m,n \le 100$, this is at most $199$, safely below the source limit of 1,000.

## Complexity detail

Let $m$ and $n$ be the row and column counts. The row index increases at most $m$ times and the column index decreases at most $n$ times, so the staircase walk takes $O(m+n)$ time and `get` calls. It stores only indices and the best column, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Binary search each row:** Finding every row's first `1` independently takes $O(m\log n)$ calls. It fits the source limit at the stated bounds but is asymptotically slower than the staircase walk.
- **Inspect every cell:** A full $O(mn)$ scan can make 10,000 `get` calls and violate the 1,000-call contract.
- **Direct matrix access:** Reading fixture storage instead of using `get` and `dimensions` violates the hidden-interface contract.
- **All zeroes:** Every query causes a downward move, no feasible column is recorded, and the result is `-1`.
- **All ones:** The first row drives the pointer all the way left and records column `0`.
- **Single row:** The walk moves left across its trailing ones or ends after discovering that the rightmost value is zero.
- **Single column:** Each zero advances downward until a `1` is found or all rows are exhausted.
- **Non-square matrix:** The proof and call bound depend independently on $m$ downward moves and $n$ leftward moves, not on equal dimensions.
