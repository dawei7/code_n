## General
**Handle the one-passenger base case.** When `n` is `1`, the first passenger is also the last and seat `1` is the only choice, so the probability is `1.0`.

**Condition on the first random seat.** For $n>1$, choosing seat `1` immediately guarantees that every later passenger finds their own seat, while choosing seat `n` immediately prevents the last passenger from doing so. If the first passenger chooses an intermediate seat $k$, passengers before $k$ sit normally and passenger $k$ becomes the next displaced passenger. The remaining uncertain process has the same structure on a smaller set containing the original first and last seats.

**Derive the invariant probability.** Assume every smaller nontrivial instance succeeds with probability $1/2$. Among the first passenger's $n$ equally likely choices, seat `1` contributes probability $1$, seat `n` contributes $0$, and each of the $n-2$ intermediate choices contributes $1/2$. Therefore

$$
P_n=\frac{1+(n-2)/2}{n}=\frac12.
$$

The base $P_2=1/2$ starts the induction, proving that every `n > 1` has the same answer.

## Complexity detail
The result requires one comparison and returns one of two constants, so time and auxiliary space are both $O(1)$.

## Alternatives and edge cases
- **Linear probability recurrence:** Computing all values from $P_1$ through $P_n$ reproduces the result but takes $O(n)$ time.
- **Monte Carlo simulation:** Random trials approximate the probability and introduce sampling error, while the exact value is available directly.
- **Explicit state distribution:** Tracking which passenger is displaced is correct but retains states whose aggregate probability collapses to the same symmetry.
- **One passenger:** This is the only case with probability `1.0`.
- **Every larger input:** The answer is exactly `0.5`, not merely an asymptotic limit.
- **Floating-point return:** Both representable outputs, `1.0` and `0.5`, are exact in binary floating point.
