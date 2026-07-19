## General
**Measure an interval by score advantage**

For an interval `[left, right]`, store the largest score difference the player whose turn it is can force. A one-number interval has that number as its advantage.

**Subtract the opponent's best response**

Taking the left endpoint yields `nums[left] - advantage(left + 1, right)` because the remaining interval belongs to the opponent. Taking the right endpoint yields `nums[right] - advantage(left, right - 1)`. Optimal play keeps the larger value.

**Compress the interval table**

Initialize a one-dimensional array with single-element advantages. Fill longer intervals from left to right: `dp[left + 1]` still represents the interval missing the left endpoint, while the old `dp[left]` represents the interval missing the right endpoint. After the full interval is processed, a nonnegative `dp[0]` means player one can force at least a tie.

**Why the recurrence is correct**

Each legal turn has exactly the two endpoint choices considered by the transition. Subtracting the opponent's optimal advantage accounts for all later play, so induction on interval length proves every stored value is the best enforceable difference.

## Complexity detail
There are $n(n + 1) / 2$ intervals and each transition is constant time, giving $O(n^2)$ time. The compressed table stores `n` integers, so space is $O(n)$.

## Alternatives and edge cases
- **Top-down memoization:** evaluates the same interval recurrence lazily with the same asymptotic bounds, plus recursion stack space.
- **Two-dimensional table:** is easier to visualize but uses $O(n^2)$ space.
- **Recompute each interval sum:** is correct but raises time to $O(n^3)$.
- **Unmemoized minimax:** revisits intervals along exponentially many move sequences.
- **Single number:** the first player takes it and succeeds.
- **Tie:** a zero final difference returns `True`.
- **Zero scores:** do not change the recurrence.
