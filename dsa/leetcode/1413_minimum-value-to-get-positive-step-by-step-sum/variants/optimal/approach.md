## General
**Measure the array's deepest deficit.** Scan the numbers while maintaining the prefix sum produced by the array alone, as if the starting value were zero. Record the minimum prefix sum seen, also considering the empty prefix value zero.

For any prefix sum $p$, the actual running total is `startValue + p`. The condition `startValue + p >= 1` is strongest at the minimum prefix. Therefore the starting value must be at least one minus that minimum. Choosing exactly `1 - minimum_prefix` makes the deepest total equal to $1$ and every other total no smaller, proving both feasibility and minimality.

Because the empty prefix keeps the recorded minimum at most zero, the formula always returns at least one without a separate special case.

## Complexity detail
The scan visits each of the $n$ values once and performs constant work per value, for $O(n)$ time. Only the current and minimum prefix sums are retained, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Try successive starting values:** Simulate the array for `1`, then `2`, and so on until one works. This repeats work and can be much slower than deriving the exact offset.
- **Recompute every prefix independently:** Summing `nums[:i]` for each endpoint is correct but takes $O(n^2)$ time.
- **All positive values:** The minimum prefix remains zero, so the answer is `1`.
- **Zero values:** A zero does not change the prefix minimum or require a larger start.
- **Lowest prefix at the end:** The full array sum must be included among the checked prefixes.
- **Recovery before a deeper drop:** Tracking only the current sum is insufficient; retain the minimum over the entire scan.
