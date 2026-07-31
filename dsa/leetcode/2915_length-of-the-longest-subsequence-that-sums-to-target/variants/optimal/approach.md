## General

**Keep the best length for each reachable sum.** Let `best_length[sum]` be the
largest number of processed positions that can produce `sum`, using `-1` for
an unreachable positive sum and zero for sum zero. When the next value is
considered, any already reachable `sum - value` can extend by this one
position, producing a candidate length one larger for `sum`.

**Update sums downward to enforce subsequences.** Visit totals from `target`
down to `value`. A descending scan reads every predecessor state before the
current value can modify it, so the same array position cannot be taken more
than once. For each processed prefix, induction shows that the table stores
the greatest length for every reachable sum: an optimal choice either omits
the newest position and keeps the old entry, or includes it and extends an
optimal predecessor for `sum - value`. These are exactly the two possibilities
used by the update. The final target entry is consequently the longest valid
subsequence, and remains `-1` precisely when no such subsequence exists.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $T=\texttt{target}$. Each value scans
at most $T$ table entries, giving $O(nT)$ time. The one-dimensional table has
$T+1$ entries, so the auxiliary space is $O(T)$.

## Alternatives and edge cases

- **Enumerate every subsequence:** Checking all $2^n$ selections is correct but exponential; the sum-indexed table merges selections that have the same sum while retaining only their greatest length.
- **Two-dimensional prefix table:** A table indexed by both position and sum also takes $O(nT)$ time but uses $O(nT)$ space; descending updates compress the position dimension.
- **Ascending sum updates:** Scanning upward can reuse the current position repeatedly and solves an unbounded-knapsack problem instead of the required subsequence problem.
- **Fewest-elements knapsack:** Minimizing the number of selected values answers a different question; each state must retain the maximum length.
- **Duplicate values:** Equal values at different positions are independent 0/1 choices and may all appear in the subsequence.
- **Value above target:** Because all numbers are positive, such a value cannot participate and naturally performs no table update.
- **Unreachable target:** If the target state is still `-1` after every position, no valid subsequence exists.
