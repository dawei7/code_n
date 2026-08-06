## Description

You are given the positive dimensions `m` and `n` of a 0-indexed rectangular board, together with the knight's starting cell `(r, c)`. Construct a sequence of legal chess-knight moves that visits every board cell exactly once. The starting cell counts as the first visit and must not be visited again.

A move from `(r1, c1)` to `(r2, c2)` is legal when the destination remains inside the board and the absolute row and column differences are $1$ and $2$ in either order. Equivalently,

$$
\min(\lvert r_1-r_2 \rvert,\lvert c_1-c_2 \rvert)=1
\quad\text{and}\quad
\max(\lvert r_1-r_2 \rvert,\lvert c_1-c_2 \rvert)=2.
$$

Return an `m` by `n` matrix whose value at each cell is its visit index, beginning with `0` at `(r, c)` and ending with `m * n - 1`. The input guarantee ensures that at least one complete tour exists. More than one output can therefore be valid.
