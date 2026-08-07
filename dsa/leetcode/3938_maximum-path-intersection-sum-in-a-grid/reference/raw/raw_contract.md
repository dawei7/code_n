## Function Contract

**Inputs**

- `grid`: A rectangular integer matrix with at least two rows and at least two columns.

Let $M=\lvert\texttt{grid}\rvert$ and $N=\lvert\texttt{grid[0]}\rvert$. Path one connects $(0,0)$ to $(M-1,N-1)$ using only right and down moves. Path two connects $(M-1,0)$ to $(0,N-1)$ using only right and up moves.

For a chosen pair of paths, each matrix coordinate visited by both paths contributes its value exactly once to the intersection score.

**Return value**

Return the greatest intersection score attainable by any valid pair of paths.
