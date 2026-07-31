## General

**Turn maximization into a monotone decision**

First compute every city's existing power with prefix sums. If it is possible to give every city power at least $T$, then every smaller target is also possible. Conversely, failure at $T$ implies failure for every larger target. The answer can therefore be found by binary search. The initial minimum power is achievable without additions, and that same weakest city can gain at most all `k` new stations, so the search interval ends at `min(power) + k`.

**Check one target from left to right**

Sweep cities in increasing order while a difference array tracks how much power previously added stations currently contribute. When city $i$ is below $T$, its exact deficit must be supplied; no later decision can avoid filling it. Place all required stations as far right as possible, at `min(n - 1, i + r)`. This placement still covers $i$ but reaches at least as far into the unprocessed suffix as any other placement that could repair $i$, so it cannot make future cities harder to satisfy.

If the placement is not clipped by the array boundary, its contribution lasts through city $i+2r$ and expires at $i+2r+1$. A difference-array subtraction at `min(n, i + 2 * r + 1)` records that expiration. Thus every feasibility check visits each city once, and it fails immediately if the accumulated deficit exceeds `k`.

The greedy sweep uses the fewest additions needed for each prefix: at city $i$, any feasible construction must provide at least the observed deficit, and moving those mandatory stations rightward only maximizes help to the remaining suffix. Therefore the check accepts exactly the achievable targets, making the binary search return the optimal minimum.

## Complexity detail

Let $n = \lvert\texttt{stations}\rvert$. Prefix sums and initial powers take $O(n)$ time. The binary search examines $O(\log(k+1))$ targets, and each feasibility sweep costs $O(n)$ time, giving $O(n\log(k+1))$ overall. The power and difference arrays use $O(n)$ space.

## Alternatives and edge cases

- **Recompute every coverage window:** Summing the active added stations across a radius-sized slice at every city preserves the greedy decision but costs $O(nr)$ per feasibility check.
- **Simulate stations individually:** Trying one placement for each of up to $10^9$ additions is far too slow and does not directly optimize the global minimum.
- **Range zero:** Each addition affects only its own city, so the method reduces to balancing independent counts.
- **Range covers all cities:** Every new station raises every city, regardless of its placement.
- **No additions:** When `k = 0`, the search interval contains only the existing minimum power.
- **Right boundary clipping:** Placing at `n - 1` still covers the deficient city near the end, and its contribution remains active through the end of the sweep.
- **Large totals:** Power and station budgets can exceed 32-bit signed range, so fixed-width implementations need 64-bit arithmetic.
