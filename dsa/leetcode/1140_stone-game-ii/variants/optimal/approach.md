## General
**Describe a state from the current player's perspective.** Let $F(i,m)$ be the maximum stones the player whose turn it is can collect from the suffix beginning at index $i$ when the current shared value is $m$. This definition removes the need to include the player's identity: Alice and Bob face the same optimization problem whenever the remaining suffix and `M` agree.

**Turn the opponent's optimum into the current score.** Precompute `suffix[i]`, the total stones in `piles[i:]`. If the current player chooses `X`, the opponent can optimally obtain $F(i+X,\max(m,X))$ from everything left. Because all remaining stones eventually belong to one of the two players, the current player's final amount for that move is `suffix[i] - F(i + X, max(m, X))`. Take the maximum over every legal `X`.

**Stop when all remaining piles are available.** When `i + 2 * m >= n`, the current player may take the entire suffix immediately, so $F(i,m)=\texttt{suffix[i]}$. Otherwise memoize the recurrence by `(i, m)`. The base case is plainly optimal. For every other state, the recurrence examines every legal first move and subtracts the opponent's optimal response, so induction on the number of remaining piles proves that it returns the current player's optimum. The requested answer is $F(0,1)$.

## Complexity detail
There are $O(n^2)$ reachable `(i, m)` states. A state considers at most $O(n)$ legal values of `X`, while suffix totals make each transition $O(1)$, giving $O(n^3)$ time. The memoization table and suffix array use $O(n^2)$ space; recursion depth is $O(n)$ and does not change that bound.

## Alternatives and edge cases
- **Bottom-up game DP:** Fill the same `(i, m)` state space from right to left; it has equivalent asymptotic bounds but requires more careful iteration ordering.
- **Score-difference recurrence:** Store the best difference between current and opposing scores instead of the current player's stones; this is valid but needs an additional conversion back to Alice's total.
- **Unmemoized minimax:** The game tree repeats identical suffix-and-`M` states exponentially, making direct recursion impractical.
- **Recomputed suffix totals:** Summing `piles[i:]` inside every transition adds an avoidable factor and degrades the worst-case runtime.
- **Entire suffix available:** If at most `2 * M` piles remain, taking all of them is optimal because every pile size is positive.
- **One or two piles:** Alice can take every pile on the opening turn because `M` starts at `1`.
