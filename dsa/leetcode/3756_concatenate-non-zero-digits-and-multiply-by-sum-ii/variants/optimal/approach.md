## General

Zeros never contribute to either the concatenated value or its digit sum. Compress `s` into the sequence of only its nonzero digits, and store at every original string boundary how many compressed digits have appeared. A query `[l,r]` then maps in constant time to the half-open compressed range `[a,b)`, where `a` is the number of nonzero digits before `l` and `b` is the number through `r`.

Build three prefixes over the compressed digits: their concatenated values modulo $M=10^9+7$, their ordinary digit sums, and powers of ten modulo $M$. If `P[k]` is the value of the first $k$ compressed digits, the value belonging only to `[a,b)` is

$$
x = \bigl(P[b] - P[a]10^{b-a}\bigr) \bmod M.
$$

Multiplying by `digit_sum[b] - digit_sum[a]` produces the required result. When `a = b`, both differences are zero, so an all-zero substring is handled without a separate query case. The prefix subtraction is correct because `P[b]` consists of `P[a]` shifted left by exactly $b-a$ decimal places followed by the digits selected for the query.

## Complexity detail

Let $m$ be the string length and $q$ the number of queries. Constructing the boundary mapping and compressed prefixes takes $O(m)$ time. Each query performs a constant number of array accesses and arithmetic operations, so all answers take $O(q)$ time. The total time is $O(m+q)$, and the prefix arrays use $O(m)$ auxiliary space.

## Alternatives and edge cases

- **Scan every queried substring:** Filtering and rebuilding `x` independently is correct, but a query may span $m$ digits, producing $O(mq)$ time in the worst case.
- **Prefix digit sums alone:** They recover `sum` but cannot reconstruct the ordered decimal concatenation `x`.
- **Keep zeros in decimal positions:** A removed zero occupies no place in `x`; powers of ten must use the count of retained digits rather than the original substring length.
- **All-zero range:** Its compressed boundaries are equal, which yields both `x = 0` and digit sum zero.
- **Large concatenations:** Store concatenation prefixes and powers modulo $10^9+7`; constructing the unbounded integer is unnecessary.
- **Inclusive source indices:** Map `l` at boundary `l` and `r` at boundary `r + 1` so both endpoints are included.
