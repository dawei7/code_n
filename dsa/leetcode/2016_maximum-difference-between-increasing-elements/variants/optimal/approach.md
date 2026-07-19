## General
**Keep the best earlier endpoint.** Scan from left to right while maintaining
`minimum`, the smallest value strictly before the current position. If the
current `value` is larger, `value - minimum` is the greatest valid difference
ending at this position, because no other earlier value can yield a larger
subtraction result.

**Update only after evaluating the current position.** Compare the candidate
against the best answer, then incorporate `value` into `minimum` for future
positions. Initializing the answer to `-1` preserves the required result when
every current value is less than or equal to its prefix minimum.

For any valid optimal pair $(i,j)$, the stored minimum when the scan reaches
$j$ is no larger than `nums[i]`. The candidate considered at $j$ is therefore
at least the optimal pair's difference and is itself valid. Conversely, every
recorded candidate uses an earlier minimum and a strictly larger current
value. The maximum recorded candidate is consequently exactly the optimum.

## Complexity detail
Here $N$ is the length of `nums`. Each value is processed once, giving $O(N)$
time. The prefix minimum and best difference use $O(1)$ space.

## Alternatives and edge cases
- **Check every index pair:** Direct enumeration is correct but takes
  $O(N^2)$ time.
- **Prefix-minimum array:** Precomputing the smallest earlier value for every
  index also yields $O(N)$ time but consumes unnecessary $O(N)$ space.
- Equal values do not form an increasing pair because the inequality is
  strict.
- A decreasing or constant array returns `-1`, not zero.
- Values near $10^9$ require ordinary integer subtraction but do not change
  the algorithm.
