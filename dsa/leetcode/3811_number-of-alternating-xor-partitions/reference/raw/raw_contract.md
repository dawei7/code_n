## Function Contract

**Inputs**

- `nums`: A non-empty integer array to be partitioned.
- `target1`: The required XOR of the first block and every subsequent odd-numbered block.
- `target2`: The distinct required XOR of every even-numbered block.

Let $N=\lvert\texttt{nums}\rvert$. Every chosen block must contain at least one array element, and the ordered blocks must cover indices $0$ through $N-1$ exactly once.

**Return value**

Return the number of complete partitions whose block XOR values follow `target1`, `target2`, `target1`, and so on. Reduce the count modulo $1{,}000{,}000{,}007$.
