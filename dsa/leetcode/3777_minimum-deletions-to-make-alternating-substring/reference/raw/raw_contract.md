## Function Contract

**Inputs**

- `s`: A nonempty binary-alphabet string containing only `'A'` and `'B'`.
- `queries`: A nonempty sequence of flip queries `[1, j]` and range queries `[2, l, r]`.

Let $N=\lvert s\rvert$ and $Q=\lvert\texttt{queries}\rvert$. All indices are zero-based, and both endpoints of `s[l..r]` are included. Queries are stateful: each flip affects all queries that follow it.

**Return value**

Return one integer for each type-2 query, in the same relative order as those queries. Each integer is the fewest deletions needed to leave an alternating subsequence of the requested current substring.
