## General

Two values have GCD greater than one exactly when they share at least one prime factor. Instead of testing every pair of indices, connect indices through their factors. For each prime, remember the first index containing it; every later index with that prime needs only one union with the remembered owner to place all such indices in the same component.

**Factor values efficiently**

Build a smallest-prime-factor table through $M$ with a sieve. Repeatedly reading the table entry for a remaining value reveals one factor; divide out every copy before continuing so each distinct prime causes at most one union for that index.

Use disjoint-set union with path compression and union by size. After all factors are processed, compare every index's representative with index zero's representative. The graph is connected exactly when all representatives match.

Each union corresponds to a shared prime and therefore to a valid traversal edge. Conversely, every valid GCD edge arises from at least one shared prime, whose owner unions place both endpoints in the same component, possibly through other indices. Thus the DSU components equal the connected components of the traversal graph. A lone index returns `true`; when $n>1$, any value `1` has no prime factor and is necessarily isolated.

## Complexity detail

The smallest-prime-factor sieve takes $O(M\log\log M)$ time and $O(M)$ space. Factoring all values takes $O(n\log M)$ divisions in the worst case, with near-constant amortized DSU operations, so total time is $O(M\log\log M+n\log M)$. DSU arrays, factor owners, and the sieve use $O(M+n)$ space. The benchmark holds $M$ fixed while scaling $n$ and compares factor unions with all-pairs GCD graph construction.

## Alternatives and edge cases

- **Test every index pair:** Computing all pairwise GCDs and building explicit edges is correct but takes $O(n^2\log M)$ time.
- **Use values as DSU nodes:** This can also work by unioning each number with its prime factors, but allocates a component domain through $M$ and still needs careful index handling for duplicates.
- **Trial-divide every value:** Factoring through $\sqrt M$ avoids a sieve but may perform many repeated divisor tests across $10^5$ values.
- A one-element array returns `true`, including `[1]`.
- For more than one index, any occurrence of `1` makes full connectivity impossible.
- Equal composite values share all their prime factors and connect immediately.
- Values need not share one common factor globally; chains through different factors are sufficient.
