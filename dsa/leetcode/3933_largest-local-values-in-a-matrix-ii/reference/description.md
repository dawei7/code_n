## Description

An `n` by `m` matrix contains nonnegative integers. Consider a cell at `(row, column)` whose value is a nonzero integer `x`. Its neighborhood contains every in-bounds cell `(other_row, other_column)` satisfying both

$$
\lvert\texttt{other\_row}-\texttt{row}\rvert\le x
\quad\text{and}\quad
\lvert\texttt{other\_column}-\texttt{column}\rvert\le x.
$$

There is one exception: ignore a position when both distances are exactly `x`. These are the four possible corners `(row ± x, column ± x)` of the square neighborhood; any corner outside the matrix is ignored as well.

The nonzero cell is a local maximum when none of the cells that remain in its neighborhood has a value strictly greater than `x`. Equal values are allowed, so several tied cells can all qualify. Cells whose own value is zero are never local-maximum candidates.

Return the number of cells that satisfy this definition.
