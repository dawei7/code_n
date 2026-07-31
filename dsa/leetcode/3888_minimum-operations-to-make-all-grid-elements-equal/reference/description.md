## Description

An integer matrix `grid` has $m$ rows and $n$ columns. One operation selects any consecutive $k \times k$ submatrix and increases every cell inside that square by exactly $1$.

The selected submatrix may begin at any row and column for which all $k^2$ cells remain inside the grid. Equivalently, an inclusive rectangle `(x1, y1, x2, y2)` contains every `grid[x][y]` satisfying $x_1 \le x \le x_2$ and $y_1 \le y \le y_2$; an allowed operation uses $x_2-x_1+1=y_2-y_1+1=k$.

Find the smallest number of operations that makes every grid element equal. Return `-1` when no sequence of allowed increments can do so.
