## General

The relevant history of a partial subsequence is its final value and how many adjacent unequal pairs it has used. For every encountered value $x$ and every budget $c$ from $0$ through $k$, maintain the longest processed-prefix subsequence that ends at $x$ and uses at most $c$ changes. Also maintain the best length over all ending values for each budget.

When the next array value is $x$, one option extends a subsequence already ending at $x$; the new equal adjacency consumes no change, so its length is the previous state for $(x,c)$ plus one. If $c>0$, another option appends $x$ to the globally best subsequence using at most $c-1$ changes. When that subsequence ends at a different value, the append consumes one change. If it already ends at $x$, no change is consumed, but the result still remains legal under the larger at-most budget $c$. Taking the better option therefore covers every possible predecessor.

Budgets must be updated from $k$ down to $0$. At the moment budget $c$ is computed, both the old state ending at $x$ and the global state for $c-1$ still describe only earlier array positions. An ascending update would let the current element enter the $c-1$ state and then be appended to itself at budget $c$, violating the subsequence model.

After processing each value, the maintained states contain exactly the best legal subsequences of the processed prefix by ending value and budget: every transition appends the current position to an earlier legal state, and every legal subsequence either omits the current position, extends the same ending value, or changes from some previous ending value. The answer is consequently the global best length for budget $k$ after the scan.

## Complexity detail

Let $n$ be the length of `nums`, let $k$ be the allowed change count, and let $U$ be the number of distinct values. Each input element updates $k+1$ states, giving $O(nk)$ time. The per-value tables use $O(Uk)$ space and the global table uses $O(k)$; because $U \le n$, the overall auxiliary-space bound is $O(nk)$.

## Alternatives and edge cases

- **Index-pair dynamic programming:** Comparing every earlier index as a possible predecessor gives a straightforward $O(n^2k)$ solution, but it repeats work shared by subsequences with the same ending value.
- **Ascending in-place budget updates:** This can reuse the current element more than once during one iteration and produce impossible lengths; descending budgets preserve the processed-prefix invariant.
- **Zero change budget:** The answer is the highest frequency of any value because every selected adjacent pair must be equal.
- **At most, not exactly:** A longest answer may leave some of the $k$ changes unused, so states and transitions must remain valid for any smaller consumption.
- **Non-contiguous equal values:** Skipped array elements do not become adjacent in the chosen subsequence; only consecutive selected values determine whether a change is counted.
