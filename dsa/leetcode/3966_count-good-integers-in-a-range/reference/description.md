## Description

You receive two integers `l` and `r` that define an inclusive range, together with a nonnegative limit `k`. An integer is **good** when the absolute difference between each pair of adjacent decimal digits is at most `k`.

For example, checking a number examines consecutive positions in its ordinary decimal representation. The difference between digits `x` and `y` is `abs(x - y)`; every such difference must satisfy the same upper bound.

Return how many integers from `l` through `r`, including both endpoints, are good.
