## Function Contract

**Inputs**

- `m`: The number of grid rows.
- `n`: The number of grid columns.
- `penalty`: An $m \times n$ matrix where `penalty[i][j]` is the extra cost of waiting in zero-based cell `(i, j)` or leaving it in a direction not permitted at the current second.

Let $N=mn$ denote the number of cells in the grid. The initial state is cell `(0, 0)` at odd second $1$, and its entrance cost is already included. A move must remain inside the grid. Both moving and waiting advance time by exactly one second.

**Return value**

Return the minimum total cost of reaching cell `(m - 1, n - 1)`. Arrival ends the journey immediately; no action or penalty is required at the destination.
