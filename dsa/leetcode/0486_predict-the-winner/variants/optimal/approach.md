## General

Trying to track both players' absolute totals makes the game state look larger than it is. The only fact needed at the end is whether Player 1's score is at least Player 2's. The solution therefore measures a score difference from the perspective of whoever is about to move.

Define `dfs(i, j)` as:

> the greatest value of “current player's eventual score minus the other player's eventual score” that the current player can force while the remaining numbers are `nums[i]` through `nums[j]`.

This definition deliberately says “current player,” not specifically Player 1. When the recursive call changes turns, the same function meaning still applies from the new player's perspective. That symmetry eliminates a separate turn flag.

**Choosing the left endpoint.** Suppose the current player takes `nums[i]`. That value immediately contributes positively to the current player's side of the difference. The opponent then becomes the current player on interval `[i + 1, j]` and can force a lead of `dfs(i + 1, j)` from the opponent's own perspective. A gain for the opponent is a loss from the original player's perspective, so it must be subtracted. The resulting difference is

`nums[i] - dfs(i + 1, j)`.

The right choice is symmetric and gives

`nums[j] - dfs(i, j - 1)`.

Both players act optimally, so the current player selects the choice producing the larger guaranteed difference. That gives the recurrence

$$
\operatorname{dfs}(i,j)
=
\max\left(
\texttt{nums}[i]-\operatorname{dfs}(i+1,j),
\texttt{nums}[j]-\operatorname{dfs}(i,j-1)
\right).
$$

The subtraction is the most important step. Adding the recursive result would incorrectly treat the opponent's optimal score advantage as if it also belonged to the current player.

**The empty interval is the base case.** When `i > j`, there are no numbers left for either player, so the future score difference is zero. Returning zero also handles a one-element interval naturally. For `i == j`, each candidate in the recurrence becomes `nums[i] - 0`, so the function returns the only remaining number without needing a separate one-element branch.

For example, on `[1, 5, 2]`, the initial player compares two outcomes. Taking `1` leaves `[5, 2]` to the opponent; taking `2` leaves `[1, 5]`. In either branch the opponent can secure `5`, and the first player eventually receives the other small endpoint. The initial score difference is negative, so the function returns `False`. On `[1, 5, 233, 7]`, the recurrence sees that taking `1` can force the opponent to expose `233` later, producing a nonnegative—and in fact strongly positive—difference.

**Why local maximum choices represent optimal play.** The recurrence does not greedily choose the larger visible endpoint. It compares complete optimal outcomes of both choices. Each recursive value already incorporates every response available to the opponent and every later counter-response. Taking the maximum means the current player selects the better worst-case result after the opponent also acts optimally.

Correctness follows by induction on interval length. The empty interval returns the correct difference zero. Assume `dfs` is correct for all intervals shorter than `[i, j]`. The rules permit exactly two moves: take the left endpoint or take the right endpoint. By the induction assumption, each recursive call gives the exact advantage the opponent can force afterward. Negating that advantage and adding the chosen endpoint therefore gives the exact result of each legal first move. The maximum is the best result the current player can force, so `dfs(i, j)` satisfies its definition.

**Memoization removes repeated game states.** Different move sequences can reach the same remaining interval. Without caching, that interval would be solved repeatedly in an exponential recursion tree. Python's `@cache` stores the result associated with each pair `(i, j)`. Once an interval is solved, every later request for it returns immediately. The state needs only the two boundaries because earlier scores have already been compressed into the score-difference recurrence.

The original call `dfs(0, len(nums) - 1)` is from Player 1's perspective, because Player 1 moves first. A positive value means Player 1 can finish ahead; zero means the players can tie; a negative value means Player 2 can force a lead. Since the statement awards a tie to Player 1, the final comparison is `>= 0` rather than `> 0`.

The nonnegative input constraint is not required for the recurrence itself; the score-difference logic would also work with negative values. It does, however, match the game described by the Reference. The maximum length of twenty makes even several approaches feasible, but memoization gives a clean polynomial guarantee.

## Complexity detail

Let $n$ be the number of values. A cached state is an interval `(i, j)` with `0 <= i <= j < n`, plus a linear number of empty-boundary states. There are $n(n+1)/2 = O(n^2)$ nonempty intervals. Each one performs constant work after its two dependencies are available, so the exact implementation runs in $O(n^2)$ time.

The recursion depth is $O(n)$ because each call removes one endpoint. More importantly, `@cache` retains up to $O(n^2)$ interval results. Therefore the exact source uses $O(n^2)$ total auxiliary space, not merely $O(n)$. The optimal manifest lists $O(n)$ space, which corresponds to the space-compressed bottom-up dynamic-programming variant, but that is not the implementation in this file. An accurate analysis of this cached recursive source must include its quadratic cache.

## Alternatives and edge cases

- **Uncached minimax recursion:** It uses the same recurrence but recomputes overlapping intervals, leading to $O(2^n)$ time and $O(n)$ stack space.
- **Two-dimensional bottom-up DP:** Fill interval answers from length one upward. It avoids recursion and has the same $O(n^2)$ time and $O(n^2)$ storage.
- **One-dimensional bottom-up DP:** Only the previous interval diagonal is needed, so in-place updates achieve $O(n^2)$ time and $O(n)$ space. This is the method matching the manifest's linear-space bound.
- **Track both absolute scores:** A state containing both accumulated totals is unnecessary and makes memoization harder. Their difference contains exactly the information used by the win condition.
- **One value:** The player takes it, the opponent gets zero, and the recurrence returns a nonnegative difference, so Player 1 wins.
- **Tie:** A final difference of zero returns `True` because ties count as wins for Player 1.
- **Zeros:** Choosing a zero may still be strategically correct because it changes which endpoint becomes available. The recurrence evaluates future play rather than treating zero as irrelevant.
- **Do not choose the larger endpoint greedily:** A smaller endpoint can force access to a much larger later value. Only the minimax recurrence accounts for the opponent's response.
