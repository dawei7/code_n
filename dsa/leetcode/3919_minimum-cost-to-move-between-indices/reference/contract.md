## Function Contract

**Inputs**

- `nums`: A strictly increasing list of integers. Its indices are the positions between which moves are made.
- `queries`: A list of pairs `[l, r]`, each asking for the minimum cost to travel from index `l` to index `r`.

Let $n=\lvert\texttt{nums}\rvert$ and $q=\lvert\texttt{queries}\rvert$. For an interior index, equal gaps select its smaller, left-hand neighbor as `closest(x)`; either endpoint has only one possible adjacent index.

**Return value**

Return a list of $q$ integers in the same order as `queries`. Entry `i` is the minimum total cost of moving from `queries[i][0]` to `queries[i][1]`. A query whose endpoints are equal has cost `0`.
