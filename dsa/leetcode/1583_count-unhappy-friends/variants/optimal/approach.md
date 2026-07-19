## General
**Make preference comparisons constant-time**

Build `rank[x][u]`, the position of friend `u` in `x`'s preference list. A smaller position means a stronger preference. Also expand `pairs` into `partner[x]` so every assigned partner is available in constant time.

**Inspect only alternatives preferred over the current partner**

For each friend `x`, scan `preferences[x]` from the beginning and stop upon reaching `partner[x]`. Every earlier friend `u` satisfies the first unhappiness condition automatically.

For each such `u`, compare `rank[u][x]` with `rank[u][partner[u]]`. If the first is smaller, `u` reciprocally prefers `x`, so mark `x` unhappy and stop scanning alternatives for `x`.

Every possible witness for `x` occurs before its assigned partner and is examined. Friends after the partner cannot satisfy the first condition. The rank comparison is exactly the second condition, so the method finds a witness if and only if `x` is unhappy, while the early break counts `x` at most once.

## Complexity detail
Building the rank table processes $N(N-1)$ preference entries. Across all friends, witness scans examine at most another $N(N-1)$ entries, giving $O(N^2)$ time.

The rank table uses $O(N^2)$ space, and the partner array uses $O(N)$.

## Alternatives and edge cases
- **Use inverse-rank dictionaries:** store one mapping per friend instead of a dense table. This has the same asymptotic bounds.
- **Repeated linear rank searches:** search each preference list linearly for every candidate comparison. It is correct but can take $O(N^3)$ time.
- **Check every pair of friends:** test all $x,u$ combinations with precomputed ranks. This remains $O(N^2)$ but ignores the useful partner cutoff.
- **Two friends:** each is paired with the only possible partner, so neither can be unhappy.
- **Partner ranked first:** that friend has no preferred alternative and cannot be unhappy.
- **No reciprocal preference:** preferring another person is insufficient unless that person also prefers the friend over their own partner.
- **Several witnesses:** the friend still contributes only one to the answer.
- **Asymmetric outcome:** one friend may be unhappy without their assigned partner being unhappy.
- **All friends unhappy:** every friend is counted independently.
