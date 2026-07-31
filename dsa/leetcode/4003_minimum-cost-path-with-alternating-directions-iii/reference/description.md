## Description

An $m \times n$ grid is indexed from the upper-left corner. You begin in cell $(1,1)$ at the first second and pay that cell's entrance cost. Entering cell $(i,j)$ costs $i \cdot j$, using one-based row and column indices.

At each second, choose one of two kinds of action:

- move to an orthogonally adjacent cell; or
- remain in the current cell for one second.

Direction and time parity determine whether a move incurs an extra charge. During an odd-numbered second, moving right or down is permitted without a penalty. During an even-numbered second, moving left or up is permitted without a penalty. A valid move in one of the other two directions is still possible, but it additionally costs the value of `penalty` at the cell being left. Waiting also costs the current cell's penalty. Every move or wait consumes one second, so the next action uses the opposite parity.

Find the minimum total cost needed to reach cell $(m,n)$. The total includes the initial cost of cell $(1,1)$, every later cell entrance cost, and every direction or waiting penalty paid along the chosen timed walk.
