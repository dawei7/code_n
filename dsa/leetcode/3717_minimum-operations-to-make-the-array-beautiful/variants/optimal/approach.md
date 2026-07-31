## General

The choice made at one position becomes the divisor required at the next position. Consequently, rounding each number to the smallest multiple of its current predecessor is not always optimal: with `[3,7,10]`, changing `7` to `9` forces the last value to `18`, while changing it to `12` allows the last value to become `12` and costs less overall.

Let $M = \max(\texttt{nums})$ and $V = 2M$. No optimal final value needs to exceed $V$. If the previous final value is at most $M$, its smallest multiple not below the current original value is less than $2M$. Once a chosen value exceeds $M$, every remaining original value is smaller, so keeping that chosen value is valid; choosing a still larger multiple would only add operations.

Maintain `dp[value]`, the minimum cost for the processed prefix when its last final value equals `value`. Initially, only the unchanged first value is possible. For each later original value, consider every reachable predecessor and every multiple of that predecessor from the first one not below the original value through $V$. Adding `value - original` accounts exactly for the increments at this position.

Every transition creates a valid adjacent divisible pair. Conversely, every beautiful final array within the proven bound follows one of these transitions at every position, so the dynamic program considers its exact total cost. Taking the smallest final state therefore returns the global minimum.

## Complexity detail

Let $n$ be `nums.length`, $M = \max(\texttt{nums})$, and $V = 2M$. Across all possible predecessor values, enumerating their multiples costs $O(V\log V)$ per position, for $O(nV\log V)$ time. The two one-dimensional dynamic-programming rows use $O(V)$ space. Under the source constraints, $V \leq 100$.

## Alternatives and edge cases

- **Greedy rounding:** Choosing the smallest legal value at every position ignores how that value constrains the suffix and can miss the minimum.
- **Quadratic state transitions:** Testing every predecessor against every possible next value is correct but costs $O(nV^2)$ rather than enumerating multiples directly.
- **First element:** Index `0` cannot be incremented, so the initial dynamic-programming state contains only `nums[0]`.
- **Single element:** No divisibility relation exists, and the initialized cost is `0`.
- **Already beautiful:** Keeping each original value is represented by zero-cost transitions and yields `0`.
- **Values above the original maximum:** Such values may be necessary, as when a fixed predecessor of `40` must precede an original value of `50`; the $2M$ bound retains them.
