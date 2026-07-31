## General

Process `nums` from left to right so that every stored subsequence already respects index order. For each possible final value, keep both the number of consecutive subsequences ending there and the sum of all their element sums. Maintain separate tables for increasing and decreasing directions.

When the current value is $x$, a new increasing subsequence is either the singleton `[x]` or an earlier increasing subsequence ending at $x-1$ extended by $x$. If there are $c$ such earlier subsequences whose values sum to $s$, the extensions contribute $s+xc$: every old element sum remains and $x$ is appended to each of the $c$ choices. Including the singleton gives a new contribution of $x+s+xc$. The decreasing transition is identical using states ending at $x+1$.

Add both directional contributions to the answer, then subtract $x$ once because the singleton is present in both. Longer sequences cannot be counted in both directions. Finally merge the new counts and sums into the states ending at $x$; accumulating rather than replacing preserves subsequences ending at different occurrences. These transitions create every valid subsequence at its last index and no invalid one, so every required index choice contributes exactly once.

## Complexity detail

Let $n=\lvert nums\rvert$ and $V=\max(nums)$. Allocating the four value-indexed tables takes $O(V)$ time and space. Each array element performs constant work, taking $O(n)$ more time. The total is $O(n+V)$ time and $O(V)$ auxiliary space. All counts, state sums, and the answer are reduced modulo $10^9+7$ after each transition.

## Alternatives and edge cases

- **Enumerating subsequences:** There are $2^n-1$ non-empty index choices, so direct generation is infeasible.
- **Hash-map states:** Sparse maps give expected $O(n)$ time and $O(k)$ space for $k$ observed values, but arrays are deterministic and $V\le10^5$ makes their bound practical.
- **Duplicate values:** Equal adjacent subsequence values differ by zero and cannot extend one another; their states still accumulate for later neighboring values.
- **Singleton overlap:** Each element is both increasing and decreasing by itself, so subtracting it once is necessary; no longer subsequence has both constant directions.
- **Modulo arithmetic:** The number and total value of valid subsequences can grow exponentially, so every stored aggregate must be reduced modulo $10^9+7$.
