## General

For the larger input limit, transitions cannot inspect every earlier index. Compress all partial subsequences that share two properties: their final value and the maximum number of adjacent changes they may use. For each encountered value $x$ and budget $c$, store the longest processed-prefix subsequence ending at $x$ with at most $c$ changes. A second array stores the best length over every ending value for each budget.

Appending the current value $x$ has two complete possibilities. Extending a state already ending at $x$ adds no unequal adjacency, so it increases the same $(x,c)$ state by one. For $c>0$, appending $x$ to the globally best state with budget $c-1$ also gives a legal candidate. If that state ends at another value, the new adjacency spends one change; if it already ends at $x$, the append spends none and is still valid because the state permits at most $c$ changes.

Process budgets from $k$ down to $0$. This direction ensures that the global state for $c-1$ and the ending-at-$x$ state for $c$ still refer only to earlier positions when the current transition reads them. Ascending updates could insert the current position into a smaller-budget state and immediately append the same position again.

The states are complete by induction over the processed prefix. Any legal subsequence ending at the current position either follows an earlier selected $x$ without adding a change or follows some other ending value while consuming one allowed change; the two transitions cover those cases. Conversely, each transition appends the current position once to a previously legal subsequence. The global value at budget $k$ is therefore the required maximum length.

## Complexity detail

Let $n$ be the length of `nums`, let $k$ be the maximum allowed changes, and let $U$ be the number of distinct values. The algorithm performs $k+1$ constant-time updates per input element, so it takes $O(nk)$ time. The value-indexed states require $O(Uk)$ space and the global array requires $O(k)$; since $U \le n$, the overall auxiliary-space bound is $O(nk)$.

## Alternatives and edge cases

- **Index-pair dynamic programming:** Trying every earlier position as a predecessor is correct but costs $O(n^2k)$ time, which is too slow for $n=5000$.
- **Top-two ending values:** Tracking the best and second-best distinct ending value for every exact change count can also achieve $O(nk)$, but it requires more tie and replacement bookkeeping than at-most-budget global states.
- **Ascending in-place updates:** Reading a budget state already changed for the current value can reuse one array position more than once; descending iteration prevents that.
- **Zero budget:** Only equal selected values may be adjacent, so the answer is the maximum frequency of one value.
- **Maximum budget:** Even when $k=50$, a subsequence may use fewer changes; the contract is at most, not exactly.
- **Skipped positions:** A change is counted between consecutive chosen values, regardless of how many original array positions lie between them.
