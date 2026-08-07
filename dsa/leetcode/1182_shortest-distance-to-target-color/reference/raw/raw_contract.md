## Function Contract

**Inputs**

- `colors`: A list of color values from the set `{1, 2, 3}`.
- `queries`: A list of pairs `[i, c]`, where `i` is a valid zero-based position in `colors` and `c` is one of the three color values.

Let $n = \lvert\texttt{colors}\rvert$ and $q = \lvert\texttt{queries}\rvert$. For a query `[i, c]`, the distance to a matching position $j$ is $\lvert i-j\rvert$.

**Return value**

- Return a list of $q$ integers in query order. For each `[i, c]`, return the minimum distance to a position `j` satisfying `colors[j] == c`, or `-1` when no such position exists.
