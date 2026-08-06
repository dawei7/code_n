## Description

Consider an $n$-by-$m$ grid whose rows and columns are numbered from one. The
arrays `source` and `dest` each identify one cell as `[row, column]`. During one
move, you may choose any different cell in the current cell's row or any
different cell in its column. Remaining at the current cell is not a move.

Count the distinct sequences of cells that start at `source`, finish at `dest`,
and contain exactly $k$ moves. A route that reaches the destination early is
counted only if its later moves return to the destination at step $k$. Return
the count modulo $10^9+7$.
