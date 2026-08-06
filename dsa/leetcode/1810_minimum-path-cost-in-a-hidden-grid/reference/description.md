## Description

A robot starts on one open cell of a hidden $m \times n$ grid and must reach a distinct open target cell. Other cells are either blocked or open with a positive entry cost. Moving orthogonally into an open cell pays that destination cell's cost each time; the starting cell's own cost is not charged before the first move. The grid dimensions, layout, coordinates, target, and costs are unavailable to the submitted algorithm.

The native `GridMaster` interface reveals the grid through interaction. `canMove(direction)` reports whether `"U"`, `"R"`, `"D"`, or `"L"` is currently legal. `move(direction)` performs a legal move and returns the cost of the entered cell; an illegal move leaves the robot in place and returns `-1`. `isTarget()` reports whether the robot currently occupies the target. Return the minimum possible total entry cost from the initial cell to the target, or `-1` when no valid path connects them.
