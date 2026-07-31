## General

Every entry of `big_nums` is a power of two. If an interval contains exponents $e_1,e_2,\ldots,e_k$, its product is therefore

$$
2^{e_1+e_2+\cdots+e_k}.
$$

The task reduces to finding the sum of the bit positions represented by any prefix of the implicit sequence.

**Count complete integers by periodic bits**

For a non-negative integer $N$, consider all integers from $0$ through $N$. At bit position $b$, zeroes and ones occur in blocks of length $2^b$. With $T=N+1$, the number of set occurrences is

$$
\left\lfloor\frac{T}{2^{b+1}}\right\rfloor 2^b
+ \max\bigl(0,\ T \bmod 2^{b+1}-2^b\bigr).
$$

Summing these occurrences over $b$ gives $C(N)$, the number of elements contributed to `big_nums` by integers through $N$. Weighting each occurrence by $b$ gives $S(N)$, the sum of their exponents. Both statistics take $O(\log N)$ time.

**Locate an arbitrary sequence prefix**

For a prefix containing $L$ elements, binary-search the smallest integer $N$ with $C(N) \ge L$. All powerful arrays through $N-1$ are complete, contributing $S(N-1)$. The remaining elements come from the powerful array of $N$; inspect its set bits from least significant to most significant, matching the required sorted order, and add the first remaining bit positions.

Call this prefix exponent sum $P(L)$ for the first $L$ elements. An inclusive query `[from, to, mod]` has exponent

$$
P(\texttt{to}+1)-P(\texttt{from}).
$$

Modular exponentiation then returns `pow(2, exponent, mod)` without ever materializing the enormous sequence.

## Complexity detail

Let $q$ be the number of queries and $U$ one plus the largest queried index. A prefix lookup performs $O(\log U)$ binary-search iterations, and each iteration evaluates bit statistics in $O(\log U)$ time. Two prefix lookups per query therefore take $O(q \log^2 U)$ time.

Only scalar counters and binary-search bounds are retained. The fixed machine-scale bit loop does not grow with the materialized sequence, so auxiliary space is $O(1)$ excluding the returned list.

## Alternatives and edge cases

- **Generate `big_nums` explicitly:** Enumerating integers and their set bits works for small indices but requires linear work and storage in the queried position, which is impossible near $10^{15}$; it is the principal slower benchmark comparison.
- **Store counts for every bit position:** A per-bit array can also recover the exponent sum, but only the aggregate count and weighted sum are needed, so scalar accumulation is simpler.
- **Multiply powers individually:** Repeated modular multiplication is correct but scales with the interval length; summing exponents reduces the entire range to one modular power.
- A prefix of length zero contributes exponent zero and is needed when a query starts at index zero.
- The powerful array of an integer lists its set-bit powers in ascending order, so a partial final integer must consume set bits from low to high.
- When `mod` is one, modular exponentiation correctly returns zero without a special product path.
- Single-position queries and endpoints that split one integer's powerful array are handled by the same prefix difference.
