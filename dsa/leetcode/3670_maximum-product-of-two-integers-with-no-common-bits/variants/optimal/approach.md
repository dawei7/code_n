## General

A partner $y$ is valid for a value $x$ exactly when $x\mathbin{\&}y=0$. Within the lowest $B$ relevant bits, this means every set bit of $y$ belongs to the complement mask

$$
C=((1\ll B)-1)\mathbin{\mathsf{xor}}x.
$$

Thus $y$ must be a submask of $C$. The problem becomes: for every possible mask, know the largest input value that is one of its submasks.

**Initialize exact masks.** Create an array `best_submask` of length $2^B$. For every input value $v$, store $v$ at index $v$. Values are themselves masks and positive; duplicates do not change the maximum exact value.

**Propagate maxima with SOS DP.** For each bit, compare every mask containing that bit with the same mask after removing it. If the smaller mask has a larger recorded value, copy that value upward. After all bits are processed, `best_submask[m]` equals the largest present array value $v$ satisfying $v\subseteq m$.

This invariant follows by induction over processed bits. Initially only exact masks are known. Processing one bit adds all candidates obtained by omitting that bit, while retaining candidates that keep it. After all $B$ bits, every submask choice has been incorporated.

For each input $x$, query `best_submask[full_mask ^ x]`. Every returned value uses only bits absent from $x$, so it is a valid partner; the propagated maximum makes it the largest such partner and therefore gives the largest product for that fixed $x$. Taking the maximum over all $x$ yields the global optimum. If no complement contains a present positive submask, the query returns zero and contributes no product.

Because every input is positive, a value cannot be a submask of its own complement. Therefore a query never pairs one occurrence with itself, and the distinct-index condition needs no separate correction.

## Complexity detail

Let $n$ be the array length and $B$ the bit length of its maximum value. Initialization and final queries take $O(n)$. The SOS transform processes $B$ bit layers and $2^{B-1}$ mask pairs per layer, taking $O(B2^B)$ time. Total time is $O(n+B2^B)$.

The table has $2^B$ entries, so auxiliary space is $O(2^B)$. The contract limits $B$ to $20$.

The benchmark defines its size as $n$ while keeping $B=6$ fixed. The accepted transform has fixed mask preprocessing plus one pass over the array. A calibrated correct alternative checks all index pairs explicitly, producing quadratic growth while returning the same maximum.

## Alternatives and edge cases

- **Check every pair:** Testing all $\binom n2$ pairs is straightforward but takes $O(n^2)$ time.
- **Iterate unique value pairs:** Removing duplicate masks can help some inputs, but up to $n$ distinct values remain.
- **Duplicate positive values:** Two equal values share every set bit they contain and cannot pair with each other.
- **No valid pair:** The untouched zero table value naturally yields answer `0`.
- **Single-bit powers:** Distinct powers of two are pairwise compatible.
- **Multi-bit values:** Compatibility depends on bitwise intersection, not numerical closeness.
- **Maximum bit width:** Allocate from the actual maximum's bit length, never a smaller mask that would discard a high bit.
- **Distinct indices:** Positivity guarantees a queried disjoint partner differs in mask from the current value.
