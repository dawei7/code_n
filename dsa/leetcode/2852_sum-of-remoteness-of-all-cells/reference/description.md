## Description

You are given a 0-indexed square matrix `grid` of order $n \times n$. Every cell either contains a positive integer or the value `-1`, which marks that cell as blocked. From a nonblocked cell, movement is allowed to another nonblocked cell only when the two cells share an edge.

For a nonblocked cell `(i, j)`, its remoteness $R[i][j]$ is the sum of the positive values in every nonblocked cell `(x, y)` from which `(i, j)` cannot be reached. Reachability is symmetric under the allowed movements. A blocked cell has remoteness `0`.

Return the sum of $R[i][j]$ over every cell in the matrix.
