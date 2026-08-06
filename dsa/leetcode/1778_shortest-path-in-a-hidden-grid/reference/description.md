## Description

A robot occupies the starting cell of a hidden $m \times n$ grid. Every cell is either open or blocked, and a distinct open cell is the target. The grid dimensions, coordinates, obstacles, and target location are not directly available.

The native interface supplies a `GridMaster`. `canMove(direction)` reports whether the robot can move one cell in `"U"`, `"R"`, `"D"`, or `"L"`; `move(direction)` performs a legal move and otherwise leaves the robot in place; and `isTarget()` reports whether its current cell is the target. Discover enough of the hidden grid to return the minimum number of moves from the starting cell to the target, or `-1` if no path exists.

For deterministic app-local execution, cOde(n) reconstructs that same stateful interface from a `master` fixture. Its matrix uses `-1` for the unique start, `2` for the unique target, `1` for an open cell, and `0` for a blocked cell. The solution still receives only a `GridMaster`, never the matrix.
