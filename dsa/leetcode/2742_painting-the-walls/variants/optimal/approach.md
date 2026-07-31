## General

Paying for wall $i$ completes that wall and keeps the paid painter busy long enough for the free painter to complete up to `time[i]` additional walls. Treat this choice as buying `time[i] + 1` units of effective wall coverage for `cost[i]`. The task becomes a 0/1 minimum-cost knapsack: select paid walls whose total effective coverage reaches at least $n$.

**Cap coverage at the target.** Let `dp[covered]` be the minimum price of a subset whose effective coverage is exactly the capped value `covered`, where all totals at or above $n$ map to $n$. Start with `dp[0] = 0` and every other state infinite.

For each `(price, duration)`, scan coverage states downward. Choosing that wall moves `covered` to `min(n, covered + duration + 1)` and adds `price`; not choosing it leaves the old state unchanged. Descending order prevents the same wall from being used again during its own iteration.

Every subset of paid walls corresponds to a sequence of these choose-or-skip transitions, with the same cost and capped effective coverage. Conversely, each finite DP state arises from such a subset. Therefore `dp[n]` is precisely the minimum cost among subsets whose paid walls plus available free-painter time cover all walls.

## Complexity detail

There are $n$ items and $n+1$ capped coverage states. Updating all states for every item takes $O(n^2)$ time. The one-dimensional DP array uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate paid-wall subsets:** Testing all $2^n$ subsets is correct but exponential.
- **Two-dimensional knapsack:** Storing a row for every processed wall and coverage value also takes $O(n^2)$ time but $O(n^2)$ space.
- **Top-down memoization:** Recursing on the wall index and remaining coverage has the same $O(n^2)$ state bound, with recursion and cache overhead.
- A single paid wall may cover the entire workload when `time[i] + 1 >= n`.
- The cheapest individual wall need not belong to the optimum if a more expensive wall supplies much more free-painter time.
- Effective coverage beyond $n$ has no additional value and must be capped to keep the state space bounded.
- All costs and times are positive, so paying for no wall can never complete a non-empty input.
- Total cost may reach $5\cdot10^8$, which fits ordinary 32-bit signed integers but should still be handled deliberately.
