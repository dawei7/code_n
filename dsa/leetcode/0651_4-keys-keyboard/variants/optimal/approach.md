## General
**Describe an optimal ending**

Let `best[i]` be the maximum screen length after at most `i` keypresses. One possible final action is pressing `A`, which extends an optimal $i - 1$ result and gives `best[i - 1] + 1`.

Otherwise, the final phase begins with Select All and Copy, then performs one or more pastes. If that phase produces `m` copies of the earlier screen, it uses $m + 1$ keypresses: two for select and copy, followed by $m - 1$ pastes. Its result is therefore `best[i - (m + 1)] * m`.

**Why only a constant number of paste counts matter**

A phase multiplier of at least six never needs to remain intact. Split a multiplier $m \ge 6$ into multipliers `2` and $m - 3$. Their two phases cost $3 + (m - 2) = m + 1$, exactly the original phase cost, while producing multiplier $2(m - 3)$, which is at least `m`. Repeating this replacement leaves only multipliers from two through five without reducing the result.

Thus each state needs only five constant-time choices: append one `A`, or end with a multiplication phase of `2`, `3`, `4`, or `5`.

**Build all budgets from smaller budgets**

Process keypress counts in increasing order. Every transition reads a smaller `best` entry, so its value has already been optimized. Each candidate describes a legal sequence of keypresses. Conversely, the final phase of an optimal sequence is covered by the direct `A` transition or can be reduced to one of the four multiplication transitions above. Taking their maximum therefore computes the optimum for every budget, including `n`.

## Complexity detail
There are `N` dynamic-programming states, and each evaluates one direct-key transition plus four multiplication transitions. The total time is $O(N)$. The `best` array contains $N + 1$ values, using $O(N)$ space.

## Alternatives and edge cases
- **Enumerate every possible final copy point:** gives a straightforward $O(N^2)$ dynamic program, but checks paste batches that the constant-transition proof eliminates.
- **Screen-and-clipboard state search:** explicitly models all four keys, but creates unnecessary state dimensions and duplicate configurations.
- **Fixed-window storage:** only the previous seven states are needed by the optimized recurrence, so auxiliary space can be reduced to $O(1)$ with a circular buffer at the cost of less direct indexing.
- For small budgets, typing `A` repeatedly is optimal because Select All and Copy do not create characters by themselves.
- A copy phase requires at least one paste to improve the screen, so its multiplier is at least two.
- $n = 1$ returns `1`; the single useful action is pressing `A`.
