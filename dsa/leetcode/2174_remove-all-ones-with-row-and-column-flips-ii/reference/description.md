## Description

You are given a 0-indexed $m \times n$ binary matrix `grid`. An operation must
select a cell `(i, j)` whose current value is `1`. That operation changes every
cell in row `i` and every cell in column `j` to `0`; cells already equal to
zero remain zero.

Because an operation can only remove ones, each choice changes which later
intersections are still legal to select. Return the minimum number of
operations required to make every cell zero.
