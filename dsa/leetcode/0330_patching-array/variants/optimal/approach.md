## General
**Track the first sum that coverage cannot reach**

Maintain `missing` so every sum in `[1, missing - 1]` is representable. Initially `missing = 1`, describing an empty covered interval. If the next array value $x$ is at most `missing`, combining $x$ with every already representable sum extends coverage continuously through `missing + x - 1`; update `missing += x` and consume the value.

Because `nums` is sorted, when the next value exceeds `missing`, no unused input value can form the gap at `missing`. A patch is unavoidable.

**Patch with the missing value itself**

When a gap exists, add exactly `missing`. This new value alone covers the gap, and adding it to every old sum from zero through `missing - 1` extends coverage through `2 * missing - 1`. Set `missing *= 2` and count one patch.

No other single patch can extend coverage farther without leaving the current gap: a value larger than `missing` cannot form `missing`, while a smaller value was already within the covered interval and extends the upper endpoint by less. Thus choosing `missing` is both necessary for immediate feasibility and maximal for future coverage.

For `[1,5,10]`, consuming one covers through one, so `missing = 2`. The next input is too large, so patch two and then four, expanding coverage to seven. Five and ten can then be consumed, covering beyond twenty with two patches.

At every iteration the invariant interval is exact and gap-free. Consuming a usable input value needs no patch; when it is unusable, every valid solution must patch the current gap, and the greedy patch dominates every feasible alternative. Repeating this exchange argument proves the final patch count is minimal.

## Complexity detail
Each of the `m` input values is consumed at most once. Every patch at least doubles `missing`, so at most $O(\log n)$ patches occur. Total time is $O(m + \log n)$, and the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Maintain every reachable subset sum explicitly:** can require $O(n)$ space and much more work than tracking one continuous boundary.
- **Patch with the next input value or with one:** may cover the immediate gap poorly or fail to cover it at all, producing extra patches.
- **Use total input sum alone:** does not prove there are no holes in the representable interval.
- An empty array is handled by repeatedly doubling coverage. Inputs already spanning `[1,n]` need no patches, and values beyond `n` never need to be consumed.
