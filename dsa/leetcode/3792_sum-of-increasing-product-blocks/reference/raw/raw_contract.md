## Function Contract

**Inputs**

- `n`: The number of consecutive product blocks to include.

Block $i$ contains exactly $i$ values. Across the first `n` blocks, the integers from $1$ through $n(n+1)/2$ are therefore each used exactly once and in increasing order.

**Return value**

Return the sum of the first `n` block products, reduced modulo $1{,}000{,}000{,}007$.
