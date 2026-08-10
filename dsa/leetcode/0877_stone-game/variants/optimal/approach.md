## General

The exact solution models the game as a two-player interval game with memoized recursion. At any moment, the remaining piles form one contiguous interval `piles[i:j+1]` because each move removes only the leftmost or rightmost pile.

Instead of tracking Alice's and Bob's totals separately, the helper returns a score difference:

$$
\text{dfs}(i,j)=\text{maximum stones the player to move can gain over the other player from piles }i\ldots j.
$$

A positive value means the current player can finish that subgame ahead. A negative value means the opponent can force a lead. This definition automatically handles both players playing optimally because the same question applies after every turn, with the roles exchanged.

**Base case.** If `i > j`, no piles remain. Neither player can collect more stones, so the score difference is zero.

**Take the left pile.** If the current player takes `piles[i]`, the opponent becomes the player to move on interval $(i+1,j)$. The value `dfs(i + 1, j)` measures how much that opponent can lead in the remainder. From the original current player's viewpoint, that future advantage must be subtracted:

$$
\text{left choice}=\text{piles}[i]-\text{dfs}(i+1,j).
$$

**Take the right pile.** By the same reasoning,

$$
\text{right choice}=\text{piles}[j]-\text{dfs}(i,j-1).
$$

The current player chooses optimally, so `dfs(i,j)` is the maximum of those two results.

The subtraction is the key idea. After taking a pile, perspective flips. The recursive value is favorable to the next player, so it is unfavorable by the same amount to the current player. This compact zero-sum representation avoids writing separate “Alice maximizes” and “Bob minimizes” branches.

**Why the recurrence is correct.** For an empty interval, zero is plainly correct. Assume the helper gives the correct best score difference for all shorter intervals. From $(i,j)$, the rules allow exactly two first moves: take the left endpoint or the right endpoint. The induction assumption gives the opponent's optimal advantage after either move. Subtracting it from the stones taken now gives the current player's final advantage for that choice. Taking the larger of the only two legal choices therefore gives the current player's optimal advantage for the interval. By induction, `dfs(0, n - 1)` is Alice's optimal final score minus Bob's optimal final score.

The total number of stones is odd, so a tie is impossible. The solution returns whether the full-game score difference is greater than zero. A positive difference means Alice wins; a negative difference means Bob wins.

**Memoization prevents repeated subgames.** Different move sequences can reach the same remaining interval. Without caching, the recursion would recompute those intervals and form an exponential tree. The `@cache` decorator stores the result for every pair $(i,j)$ and returns it immediately on later calls.

For `piles = [5,3,4,5]`, the first call compares taking the left 5 with taking the right 5. Each branch recursively assumes the next player also chooses the better endpoint for themselves. The returned positive difference proves that Alice has a winning strategy; the method need not explicitly reconstruct which moves produce it.

**Relationship to the special theorem.** This problem has extra guarantees: the number of piles is even, every pile is positive, and the total is odd. Those guarantees imply Alice can always win by committing to either the original even-indexed piles or the original odd-indexed piles, whichever group has the larger sum. Because removing endpoints alternates parity availability in a controlled way, Alice can force ownership of her chosen parity group.

The local manifest's $O(1)$ claim corresponds to the mathematical shortcut of returning true from those guarantees. However, the exact `solution.py` does not use that shortcut; it runs the general memoized interval recurrence described above. An accurate explanation of the shipped code must use its actual quadratic bounds.

## Complexity detail

Let $n$ be the number of piles. A state is determined by an interval $(i,j)$. There are $O(n^2)$ such intervals. Each cached state performs constant work beyond two cached recursive calls.

- **Time complexity of the exact solution:** $O(n^2)$.
- **Space complexity of the exact solution:** $O(n^2)$ for cached interval results, plus $O(n)$ maximum recursion depth.

The $O(n^2)$ cache dominates the stack. The branch manifest states $O(1)$ because the problem-specific parity theorem permits a constant-time implementation, but that is not the implementation stored in the optimal solution file.

## Alternatives and edge cases

- **Parity strategy:** With an even number of positive piles and an odd total, Alice can force the higher-sum original parity group and therefore always wins. Returning `True` takes $O(1)$ time and space and matches the manifest, but the exact solution instead uses general interval DP.
- **Bottom-up interval DP:** Fill score differences for increasing interval lengths. It has the same $O(n^2)$ time and space and avoids recursion.
- **One-dimensional DP:** Reusing shorter-interval values can reduce interval-DP storage to $O(n)$ while retaining $O(n^2)$ time.
- **Greedily take the larger endpoint:** The largest immediate pile may expose an even better response to the opponent. It is not a generally valid strategy for endpoint games.
- **Track absolute scores for both players:** This can work, but score difference produces a smaller and clearer state.
- **Two piles:** Alice takes the larger endpoint and wins because the odd total makes their values unequal. The recurrence evaluates exactly those choices.
- **Tie handling:** The total is odd, so `dfs(...) == 0` cannot describe the full valid game. The strict `> 0` comparison is correct.
- **Positive piles:** The recurrence would still function with other values, but the constant-time parity-winning theorem relies on the stated game guarantees.
- **Repeated values:** Cache keys are indices, not values, so equal pile sizes at different positions remain distinct choices.
- **Maximum length:** Up to 500 piles yields $O(n^2)$ states. The recursion depth is at most $n$, within the intended environment.
- **No strategy reconstruction:** The task asks only whether Alice wins. The cached differences are enough; recording chosen endpoints is unnecessary.
- **Manifest-versus-code distinction:** Quoting $O(1)$ for the exact memoized implementation would be incorrect. Complexity must describe executed operations, not merely a theorem that another implementation could exploit.
