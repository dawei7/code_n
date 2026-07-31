## Function Contract

**Inputs**

- `grid`: A nonempty rectangular matrix of integers.
- `k`: The common height and width of every submatrix that one operation increments.

Let $m=\lvert\texttt{grid}\rvert$ and $n=\lvert\texttt{grid[0]}\rvert$. Operations may overlap, and a submatrix may be selected repeatedly. Values can only increase.

**Return value**

Return the minimum number of $k \times k$ increments needed to make all $mn$ entries equal, or `-1` if equality is impossible.
