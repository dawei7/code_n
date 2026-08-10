## General

**Store the current player’s future score advantage**

The two players have opposite goals, but a single zero-sum state handles both. `dfs(i, j)` is the maximum score difference that the player whose turn it is can secure over the opponent when stones `i` through `j` remain.

After the current player makes a move, roles swap. If the opponent can obtain advantage `D` from the remaining interval, that same quantity counts as `-D` from the current player’s perspective. This is why every transition subtracts the recursive result.

The state does not need a Boolean telling whether Alice or Bob moves. Both use exactly the same optimal rule: maximize their own score minus the other player’s score from the current interval.

**Use prefix sums for move scores**

`s` is a prefix-sum array with initial zero. The sum of stones from index `l` through `r` is `s[r + 1] - s[l]`.

If the current player removes the left stone at `i`, the remaining stones are `i + 1` through `j`, and those remaining values are the points earned:

`s[j + 1] - s[i + 1]`.

If the player removes the right stone at `j`, the remaining values are `i` through `j - 1`, whose sum is:

`s[j] - s[i]`.

These constant-time formulas avoid resumming an interval in every recursive state.

**Evaluate the two legal moves**

For left removal, the current player’s final advantage is

$$
a
=
\left(\text{sum of }i+1\ldots j\right)
-\texttt{dfs}(i+1,j).
$$

The source computes:

`a = s[j + 1] - s[i + 1] - dfs(i + 1, j)`.

For right removal:

`b = s[j] - s[i] - dfs(i, j - 1)`.

The player acts optimally, so `max(a, b)` is the state value.

**Base cases, including one remaining stone**

The explicit base case is `i > j`, representing an empty row and returning zero.

When exactly one stone remains, `i == j`. Either removal earns the sum of the remaining empty row, which is zero, and recurses to an empty interval. Both `a` and `b` therefore evaluate to zero without a separate single-stone branch.

This matches the game rule: removing the final stone gives no points.

**Memoization avoids exponential game-tree repetition**

Different move sequences often leave the same interval. For example, removing left then right and right then left can reach the same middle subarray. `@cache` stores each `(i, j)` result and reuses it.

After computing the initial state, `dfs.cache_clear()` releases stored entries. That cleanup happens after the peak computation and does not change asymptotic peak space.

**Trace the decision meaning**

Suppose two stones `[x, y]` remain. Removing `x` earns `y`; the opponent then removes the last stone for zero. Removing `y` earns `x`. Thus the state returns `max(x, y)`, exactly as the recurrence computes.

For larger intervals, a move with the larger immediate remaining sum is not automatically best. It may give the opponent a much stronger future interval. Subtracting the opponent’s optimal advantage is what accounts for strategic consequences and prevents an incorrect greedy choice.

**Why the recurrence is correct**

At any nonempty interval, the rules permit exactly two choices: remove the left endpoint or remove the right endpoint. Each transition adds the current move’s exact points and subtracts the best advantage the opponent can force afterward. Therefore `a` and `b` are the exact final differences for the two choices under optimal continuation.

Taking their maximum gives the current player’s optimal advantage. Induction on interval length proves every cached state, starting from empty and single-stone intervals. In the initial state Alice is the current player, so `dfs(0, n-1)` is precisely Alice’s final score minus Bob’s under optimal play.

## Complexity detail

There are $O(n^2)$ distinct intervals `(i, j)`. Each cached state performs constant-time prefix arithmetic and two cached calls, so total time is $O(n^2)$.

The prefix array uses $O(n)$ space, while the cache can hold $O(n^2)$ results. The recursion stack can reach $O(n)$ depth. Peak auxiliary space of this exact source is therefore $O(n^2)$.

This contradicts the manifest’s $O(n)$ space claim, which would require a space-optimized bottom-up recurrence. Clearing the cache after computing `ans` does not reduce its peak usage.

## Alternatives and edge cases

- **Two-dimensional bottom-up DP:** Fill intervals from short to long with the same recurrence. It avoids recursion but uses $O(n^2)$ space.
- **One-dimensional rolling DP:** Reuse interval values in a carefully chosen loop order to retain $O(n^2)$ time and reduce auxiliary storage to $O(n)$, matching the manifest.
- **Greedy largest immediate score:** It can fail because the chosen remaining interval determines the opponent’s future advantage.
- **Two stones:** The first player removes the smaller endpoint to leave the larger value as their score, producing difference `max(stones)`.
- **Final stone:** Removing it scores zero; the recurrence derives this naturally.
- **Positive values:** Prefix sums increase monotonically, though correctness of the zero-sum recurrence does not depend on monotonicity.
- **Equal endpoint choices:** `max` may choose either when their optimal differences tie; only the difference is requested.
- **Repeated interval states:** Caching is essential; without it the binary recursion is exponential.
- **Cache clearing:** It releases memory before returning but cannot justify an $O(n)$ peak-space label.
- **Recursion depth near 1000:** A long skip path can approach Python’s default recursion limit; an iterative formulation is safer operationally.
- **No absolute value needed:** The optimized state is always the current player’s maximum advantage. The initial result is already Alice-minus-Bob as requested.
