## General
**Replace hours with a signed balance.** Treat each tiring day as $+1$ and each non-tiring day as $-1$. A contiguous interval is well-performing exactly when the sum of its transformed values is positive. Let the running prefix score after index `i` be `score`; the problem becomes finding the longest pair of prefix positions whose later score is strictly greater than the earlier score.

**Take the whole prefix whenever possible.** If `score > 0` at index `i`, then the interval from index `0` through `i` is positive, so its length `i + 1` is automatically the longest interval ending there.

**Remember only the earliest occurrence of each score.** When `score <= 0`, a positive interval ending at `i` needs an earlier prefix with score below the current one. Because every update changes the score by exactly one, if any lower score has occurred, `score - 1` must also have occurred on the path to it. Using the earliest index stored for `score - 1` maximizes the interval length `i - first_seen[score - 1]`. Store a score only on its first occurrence, since a later copy can never form a longer interval with any future endpoint. These two cases examine every endpoint and therefore find the global maximum.

## Complexity detail
The algorithm scans all $n$ days once, and each hash-table lookup or insertion takes expected $O(1)$ time, for $O(n)$ total time. The running score lies in $[-n,n]$, so the earliest-index map contains at most $O(n)$ entries and uses $O(n)$ space.

## Alternatives and edge cases
- **Enumerate every interval:** Prefix sums make each interval test constant time, but there are $O(n^2)$ intervals, so this approach is too slow at the maximum input size.
- **Monotonic prefix stack:** A decreasing stack of prefix indices followed by a reverse scan also finds the widest positive-score gap in $O(n)$ time and $O(n)$ space, but is less direct here.
- **Exactly eight hours:** The strict threshold classifies `8` as non-tiring, so it contributes $-1$, not $+1$.
- **No tiring days:** No positive transformed sum exists, and the result remains `0`.
- **Positive total score:** The entire array is well-performing and must be returned with length $n$.
