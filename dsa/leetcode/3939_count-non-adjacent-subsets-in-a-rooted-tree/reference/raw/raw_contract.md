## Function Contract

**Inputs**

- `parent`: The rooted-tree encoding. `parent[0]` is `-1`; for every later node `i`, `parent[i]` is its unique direct parent and has a smaller index.
- `nums`: The node values, where `nums[i]` belongs to node `i`.
- `k`: The positive divisor used to test a selected subset's value sum.

Let $N=\lvert\texttt{parent}\rvert=\lvert\texttt{nums}\rvert$ and $K=k$. Two nodes are adjacent exactly when one is the direct parent of the other. A counted subset must be nonempty, contain no adjacent pair, and have total value congruent to zero modulo $K$.

**Return value**

Return the number of valid node subsets modulo $1{,}000{,}000{,}007$.
