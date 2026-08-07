## Function Contract

**Inputs**

- `grid`: A non-empty rectangular matrix of nonnegative integers.

Let $m=\lvert\texttt{grid}\rvert$, let $n=\lvert\texttt{grid[0]}\rvert$, and let $b=10$. Every legal cell value and every XOR formed from them belongs to $[0,2^b)$.

Every path contains exactly $m+n-1$ cells and may use only right and down moves. The start and destination values both participate in its XOR.

**Return value**

Return the minimum integer among the XOR costs of all valid paths from `(0, 0)` to `(m - 1, n - 1)`.
