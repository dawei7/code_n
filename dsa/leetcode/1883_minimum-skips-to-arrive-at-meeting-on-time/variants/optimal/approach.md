## General
**Measure time in distance units**

Multiplying time by `speed` turns every road duration into its integer distance. In these units, an integer-hour boundary is a multiple of `speed`, and the deadline is `hoursBefore * speed`. This avoids floating-point comparisons entirely.

**Keep the best elapsed distance for each skip count**

After processing some non-final roads, let `best[j]` be the smallest elapsed distance-unit total achievable with exactly $j$ skipped rests. Only that smallest total matters: every future addition and rounding operation is monotone, so a larger total with the same state can never lead to a better arrival.

For the next non-final road of length $d$, first form `elapsed = best[j] + d`. Taking its rest rounds upward with `((elapsed + speed - 1) // speed) * speed` and keeps $j$ skips. Skipping the rest keeps `elapsed` unchanged and moves to $j+1$. A fresh array prevents one road from being used twice.

**Treat the final road separately**

There is no rest after the last road. Add its distance to every reachable state without rounding, then scan skip counts from zero upward. The first total no greater than the scaled deadline is minimal. If the sum of all road distances already exceeds the deadline, no pattern of skipped rests can help.

These transitions examine both legal choices after every non-final road. By induction, `best[j]` is the minimum elapsed total among all ways to make exactly $j$ skips. The final scan therefore returns precisely the least feasible number.

## Complexity detail
There are $O(N)$ skip counts after each of $N-1$ possible rests, and each transition takes constant time, for $O(N^2)$ total time. Two length-$N$ arrays are sufficient, so auxiliary space is $O(N)$.

## Alternatives and edge cases
- **Floating-point dynamic programming:** It follows the same states but needs an epsilon around ceiling operations; scaled integer arithmetic is exact.
- **Enumerate skipped-rest subsets:** Trying every subset is correct but requires $O(2^N N)$ time in the worst case.
- **Repeat a bounded-skip feasibility DP:** Testing each candidate skip limit with a fresh $O(NK)$ dynamic program is correct but can take $O(N^3)$ time; one pass computes all exact skip counts together.
- **Two-dimensional table:** Storing every road/skip state is simpler to reconstruct but consumes $O(N^2)$ space without changing the answer.
- **One road:** There is no rest to skip; return `0` if its travel time meets the deadline.
- **Exact hour boundary:** A road ending on a multiple of `speed` adds no waiting time.
- **Final road:** Never round after it, because arrival itself creates no rest.
- **Impossible raw travel:** If $\sum_i \texttt{dist[i]} > \texttt{hoursBefore}\cdot\texttt{speed}$, return `-1` immediately.
