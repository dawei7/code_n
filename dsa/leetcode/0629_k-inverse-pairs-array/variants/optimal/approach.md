## General
**Define counts by length and inversions**

Let `dp[j]` be the number of permutations of the previously processed length with exactly `j` inversions. Before adding values, the empty permutation contributes one way at inversion count zero.

**Insert the new largest value**

When extending a permutation from length `length - 1` to `length`, place the new largest value in any position. Moving it left across `added` existing values creates exactly `added` new inversions, where `added` ranges from 0 through `length - 1`. Therefore the new count at `j` is the sum of old counts from `j - (length - 1)` through `j`, clipped at zero.

**Maintain the transition as a sliding window**

Sweep `j` upward while adding `dp[j]` to a running window. Once the window spans more than `length` entries, subtract `dp[j - length]`. The current window is exactly the recurrence range, so one constant-time update replaces an inner summation.

**Why every permutation is counted once**

Removing the largest value from any length-`length` permutation leaves one unique shorter permutation, and its former position uniquely determines how many inversions that value contributed. Conversely, inserting it at that position reconstructs the original permutation. The transition is therefore a bijective partition by `added`, and induction over lengths makes every DP count exact.

## Complexity detail
There are `n` length layers and $k + 1$ tracked inversion counts. Each cell uses one sliding-window addition and at most one subtraction, giving $O(nk)$ time. Reusing the previous and current rows requires $O(k)$ space. Modular reduction keeps values bounded.

## Alternatives and edge cases
- **Direct transition summation:** add up to `length` previous states for every cell; it is correct but costs $O(n^2k)$ time.
- **Two-dimensional DP table:** stores all length layers for easier inspection, but uses $O(nk)$ space without changing the optimized time.
- **Enumerate permutations:** count inversions in every permutation; factorial growth makes it infeasible beyond tiny `n`.
- $k = 0$ has exactly one increasing permutation.
- $k = n(n - 1) / 2$ has exactly one decreasing permutation.
- Larger `k` values are impossible and return zero immediately.
- The distribution is symmetric around half the maximum because reversing value order maps `k` inversions to `maximum - k`.
