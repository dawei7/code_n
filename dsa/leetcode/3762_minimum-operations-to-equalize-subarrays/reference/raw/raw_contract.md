## Function Contract

**Inputs**

- `nums`: The source integer array whose inclusive subarrays are queried.
- `k`: The exact positive amount added or subtracted in one operation.
- `queries`: An array of inclusive index pairs `[l_i, r_i]`.

Let $n=\lvert\texttt{nums}\rvert$ and $q=\lvert\texttt{queries}\rvert$. Each query is hypothetical and independent: its operations do not mutate `nums` for later queries.

**Return value**

Return an array of $q$ integers containing the minimum operation count for each query, or `-1` wherever equalization is impossible.
