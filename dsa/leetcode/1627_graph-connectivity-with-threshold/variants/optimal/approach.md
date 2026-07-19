## General
**Generate roads by divisor, not by city pair.** A divisor $d>\texttt{threshold}$ directly connects every pair of its multiples. It is unnecessary to materialize that clique: union `d` with `2d`, `3d`, and every later multiple through $n$. After this star of unions, all multiples of $d$ share one disjoint-set representative and therefore have exactly the connectivity contributed by divisor $d$.

**Accumulate transitive connectivity.** Repeat the multiple sweep for every usable divisor. Union-find naturally merges overlapping divisor groups. For example, with threshold 1, cities 2 and 3 do not directly share a usable divisor, but unions through city 6 place both in one component. Path compression and union by size keep representative operations nearly constant amortized time.

**Answer after preprocessing.** Once every divisor group has been merged, query `[a,b]` is true exactly when `find(a) == find(b)`. The construction adds only valid roads, because both endpoints of each union are divisible by its current divisor. Conversely, every direct road has a witnessing divisor above the threshold, and its endpoints are joined through that divisor's union star. Union-find's transitive closure therefore matches path connectivity in the full road graph.

## Complexity detail
The divisor sweep performs at most

$$
\sum_{d=1}^{n}\left\lfloor\frac{n}{d}\right\rfloor=O(n\log n)
$$

union attempts; beginning at `threshold + 1` can only reduce this work. Each disjoint-set operation costs amortized $O(\alpha(n))$, which is conventionally absorbed into the sieve term here. The $q$ queries add $O(q\alpha(n))$ time. Parent and size arrays use $O(n)$ space; answers use output space proportional to $q$.

## Alternatives and edge cases
- **Compare every city pair:** Computing `gcd(x,y)` for all $O(n^2)$ pairs and unioning qualifying pairs is correct but exceeds the required preprocessing bound.
- **Graph traversal per query:** Building explicit roads and searching separately for every query repeats connectivity work and can be prohibitive for $10^5$ queries.
- **Prime-factor grouping:** Factoring labels and merging through factors above the threshold can also derive components, but composite divisors and shared-factor chains make the bookkeeping less direct.
- When `threshold == 0`, divisor 1 connects every city, so every valid query is true.
- When `threshold >= n/2`, no usable divisor has two distinct multiples at most $n$, so every city is isolated.
- City 1 is isolated whenever the threshold is positive.
- Connectivity can be indirect even when the queried endpoints' own greatest common divisor is not above the threshold.
