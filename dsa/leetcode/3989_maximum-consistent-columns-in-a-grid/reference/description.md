## Description

You are given an integer matrix `grid` with `m` rows and `n` columns, together with a nonnegative integer `limit`. You may remove any number of columns, including none, but at least one column must remain. The relative order of every retained column is unchanged.

The retained grid is consistent when each adjacent retained pair meets the same condition in every row. If retained column `a` is immediately followed by retained column `b`, where $a<b$, then

$$
\lvert \texttt{grid[i][b]}-\texttt{grid[i][a]} \rvert \le \texttt{limit}
$$

must hold for every row `i`. Only neighboring columns in the retained order are compared; columns separated by another retained column do not need to satisfy the condition directly.

Return the maximum possible number of columns in a consistent grid after the removals.
