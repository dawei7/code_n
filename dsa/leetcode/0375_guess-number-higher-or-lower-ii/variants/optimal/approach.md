## General
**Define the cost of guaranteeing an interval**

Let `dp[left][right]` be the minimum money needed to guarantee the answer when the target is known to lie in the inclusive interval `[left,right]`. An empty or one-value interval costs zero because no wrong paid guess is necessary.

**Price each possible first guess by its worse branch**

If the first guess is `guess`, a wrong answer costs `guess`. The response then leaves either `[left, guess - 1]` or `[guess + 1, right]`. A guaranteed strategy must afford the more expensive of those two possibilities, so this first choice costs

`guess + max(dp[left][guess - 1], dp[guess + 1][right])`.

Take the minimum of this value over every possible first guess.

**Fill shorter intervals before longer ones**

Process interval lengths from two through `n`. Every transition reads only strictly shorter intervals, so their optimal costs are already known. The final answer is `dp[1][n]`.

**Why minimax matches the guarantee**

For any selected first guess, an adversarial hidden value can force the more expensive remaining side, making the transition's maximum a necessary cost. Conversely, after either response, following the stored optimal strategy for that subinterval succeeds within that same maximum. Minimizing over first guesses therefore gives both a lower bound no strategy can beat and a strategy that achieves it.

**Trace two possible values**

For interval `[1,2]`, guessing one costs one only if it is wrong; that wrong response identifies two immediately. Guessing two could cost two. The minimum guaranteed cost is therefore one.

## Complexity detail
There are $O(n^2)$ intervals. Each tries up to $O(n)$ first guesses, for $O(n^3)$ time. The two-dimensional interval table stores $O(n^2)$ scalar costs.

## Alternatives and edge cases
- **Recursive minimax without memoization:** repeats the same intervals exponentially many times.
- **Top-down memoization:** evaluates the same $O(n^2)$ states and $O(n)$ choices per state with recursion overhead.
- **Enumerate every hidden target for each pivot:** computes the same worst branch directly but adds another factor of `n`, reaching $O(n^4)$ time.
- Guessing the mathematical midpoint is not always cost-optimal because larger wrong guesses cost more.
- A single possible target requires zero guaranteed payment.
- The objective minimizes worst-case cost, not the expected cost for a probability distribution.
- The paid amount includes only wrong guesses; the final correct guess costs nothing.
