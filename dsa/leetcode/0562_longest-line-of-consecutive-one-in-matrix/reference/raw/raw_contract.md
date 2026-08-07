## Function Contract

**Inputs**

- `mat`: a nonempty rectangular matrix whose entries are `0` or `1`.

Let $r = \lvert\texttt{mat}\rvert$ be the number of rows and $c = \lvert\texttt{mat[0]}\rvert$ be the number of
columns. A line's length is its number of cells, and every consecutive step must remain inside the matrix while using
one unchanged direction.

**Return value**

Return the maximum length among all horizontal, vertical, diagonal, and anti-diagonal runs of ones. Return `0` when
the matrix contains no `1`.
