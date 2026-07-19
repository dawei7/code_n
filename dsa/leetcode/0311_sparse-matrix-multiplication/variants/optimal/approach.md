## General
**A product contribution needs two compatible nonzero entries**

The ordinary formula is
`result[i][j] = sum(mat1[i][t] * mat2[t][j])`.
A term can matter only when both `mat1[i][t]` and `mat2[t][j]` are nonzero.

Precompute, for each row `t` of the second matrix, the pairs `(j, mat2[t][j])` whose values are nonzero. Then scan each first-matrix row. Whenever `mat1[i][t]` is nonzero, multiply it only by the stored nonzero entries from second-matrix row `t` and accumulate those contributions into result row `i`.

**The shared index chooses exactly one propagation list**

For a fixed nonzero `mat1[i][t]`, every possible contribution uses row `t` of `mat2`; no other second-matrix row has the matching inner dimension. The precomputed list therefore supplies all possible destinations `j` for that value and excludes only terms whose product is certainly zero.

In the first sample, the first row's sole nonzero uses second-matrix row zero and contributes seven to column zero. The second result row processes `-1` through row zero and `3` through row two, producing `[-7,0,3]`.

**Sparse propagation is algebraically identical to the dense sum**

Every update performed by the algorithm corresponds to one triple `(i,t,j)` with two nonzero factors and adds exactly the term required by matrix multiplication. No invalid term is introduced.

Conversely, every nonzero term in the dense product has a nonzero first factor, so the outer scan reaches `(i,t)`, and a nonzero second factor, so `(j, mat2[t][j])` appears in that row's list. The algorithm adds every potentially nonzero term once. Omitted terms contain a zero factor and would add nothing, proving the resulting matrix exact.

## Complexity detail
Scanning both inputs to find nonzero entries costs $O(mk + kn)$. Let `z` be the number of compatible nonzero factor pairs actually multiplied; propagation costs $O(z)$, for total $O(mk + kn + z)$. The second-matrix index uses at most $O(kn)$ auxiliary space; the required `m × n` result is output storage.

## Alternatives and edge cases
- **Dense triple loop:** always performs $O(mkn)$ factor checks even when almost all entries are zero.
- **Compress both matrices:** can reduce repeated zero scans further and has the same sparse-product principle, at the cost of more indexing storage.
- All-zero rows produce zero result rows. Negative contributions may cancel, and cancellation must occur through normal accumulation rather than deduplication.
