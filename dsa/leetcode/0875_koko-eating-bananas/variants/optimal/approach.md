## General
**Turn a candidate speed into a monotone feasibility test**

At speed $k$, a pile containing $p$ bananas requires $\lceil p/k\rceil$ hours because an hour cannot be shared between piles. Thus the total required time is

$$
H(k)=\sum_{p\in\texttt{piles}}\left\lceil\frac{p}{k}\right\rceil.
$$

In code, each term can be evaluated with `(pile + k - 1) // k`. Increasing `k` never increases $H(k)$, so infeasible speeds form a prefix of the positive integers and feasible speeds form the suffix that follows it.

**Binary-search the first feasible speed**

Speed `1` is the smallest possible candidate, while $M$ is always sufficient because it finishes every pile in one hour and `h >= n`. Maintain a closed interval containing the minimum feasible speed. For its midpoint, sum the required hours, stopping early if the sum already exceeds `h`. If the midpoint is feasible, keep it as the upper bound; otherwise, discard it and every smaller speed.

The interval invariant always retains the first feasible speed: monotonicity justifies removing the appropriate half, and both initial bounds contain the transition. When the bounds meet, their common value is feasible and every smaller speed has been excluded as infeasible, so it is the required minimum.

## Complexity detail
Each feasibility test scans at most $n$ piles, and binary search performs $O(\log M)$ tests, giving $O(n\log M)$ time. The search uses only scalar bounds and counters, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Try speeds in increasing order:** This returns the correct minimum but may require $O(nM)$ time when the answer is large.
- **Use the average bananas per hour:** The ceiling cost is paid separately for every pile, so `ceil(sum(piles) / h)` is only a lower bound and can be infeasible.
- **Sort the piles:** Sorting does not make the feasibility sum cheaper and adds unnecessary $O(n\log n)$ work.
- **One hour per pile:** When `h == len(piles)`, the answer is exactly $M$.
- **Enough hours for one banana at a time:** When `h` is at least the total banana count, the minimum speed is `1`.
- **Single pile:** The same ceiling formula applies, and binary search finds `ceil(piles[0] / h)`.
- **Large totals:** Fixed-width implementations should accumulate $H(k)$ in a sufficiently wide integer type or stop once it exceeds `h`.
