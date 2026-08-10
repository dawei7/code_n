## General

**This is weighted interval scheduling with a limit of four choices.** The usual weighted interval scheduling problem sorts intervals by finishing time and decides for each interval whether to skip it or combine it with the best compatible earlier solution. Here the state also records how many intervals are selected, because at most four are allowed, and it carries the original indices to resolve score ties lexicographically.

The source transforms each input interval into

`(right, left, weight, original_index)`

and sorts those tuples. Sorting primarily by `right` means the first $i$ entries are the $i$ earliest-finishing intervals, with deterministic secondary ordering from the remaining tuple fields. The array `ends` stores the sorted right endpoints.

**Find the compatible prefix with binary search.** Suppose the current sorted interval has left endpoint $l$. Earlier interval endpoints that are strictly less than $l$ are compatible. Equality is not allowed because intervals sharing a boundary point overlap.

`bisect_left(ends, left, 0, i - 1)`

returns the first earlier position whose end is at least `left`. Consequently, `previous` is also the number of earlier intervals with end strictly less than `left`. The prefix of length `previous` contains exactly the intervals that may precede the current one.

Using `bisect_right` here would include an interval ending exactly at the current left boundary and would violate the statement's closed-interval overlap rule.

**Define the dynamic-programming state.** `dp[chosen][i]` is a pair:

`(maximum_score, lexicographically_smallest_sorted_index_tuple)`

for selecting exactly `chosen` non-overlapping intervals from the first `i` sorted intervals. The zero-choice row contains `(0, ())` for every prefix. Positive-choice rows begin with `(-1, ())`, called `impossible`. All real weights are positive, so score $-1$ safely means the state cannot be formed.

The table has only five rows: zero through four selected intervals. For each `chosen` from one to four and each prefix length `i`, there are two possibilities.

**Skip the current interval.** The best solution remains `dp[chosen][i - 1]`. The source initializes `best` to that state.

**Take the current interval.** The remaining `chosen - 1` intervals must come from the compatible prefix. The source reads

`score, indices = dp[chosen - 1][previous]`.

If `score >= 0`, the predecessor exists. Adding the current weight forms the new score. The source adds `original_index` to the predecessor tuple and sorts the at-most-four indices:

`tuple(sorted((*indices, original_index)))`.

The output is defined as an array of original input indices in lexicographic order, so retaining the sorted tuple makes every state immediately comparable in exactly that output order.

The candidate replaces `best` if its score is larger. If scores tie, it replaces `best` only when its index tuple is lexicographically smaller. This local tie-breaking is safe: future transitions add the same future interval index to either tied predecessor, and choosing the lexicographically smaller available index set preserves the best final tie result.

After all intervals are processed, `dp[chosen][n]` gives the best solution using exactly that many choices. The problem permits any count from one through four, so a final loop compares those four states by the same score-then-lexicographic rule. The returned tuple is converted to a list.

**Why the recurrence finds every feasible selection.** Consider an optimal exact-`chosen` selection from the first $i$ intervals. If it omits interval $i-1$, it belongs to the skip state. If it includes that interval, every other selected interval must end before its left endpoint and therefore lies in the compatible prefix found by binary search; removing the current interval leaves a valid `dp[chosen - 1][previous]` candidate. The recurrence considers both exhaustive cases and keeps the better one.

Induction over $i$ and `chosen` proves every table score is optimal. Because every comparison applies the required lexicographic tie rule to sorted original indices, each state also stores the smallest index array among solutions attaining that score. The final comparison across selection counts therefore returns exactly the requested answer.

For intervals ending at the same coordinate, tuple sorting still gives a deterministic order, but correctness does not rely on that secondary ordering. They overlap at their common end region or are independently handled by skip/take transitions, and compatibility is decided strictly by end versus left.

## Complexity detail

Let $n=\lvert\texttt{intervals}\rvert$. Constructing and sorting `ordered` costs $O(n\log n)$. There are $4n$ dynamic-programming states. Each performs one binary search in `ends`, costing $O(\log n)$. Sorting a tuple of at most four indices is $O(1)$ because four is a fixed limit. Total time is therefore $O(n\log n)$.

The table has $5(n+1)$ pairs, and each stored tuple has at most four integers, so it uses $O(n)$ space. `ordered` and `ends` also use $O(n)$. Total auxiliary space is $O(n)$. A rolling DP could reduce some table storage, but future compatibility queries refer to arbitrary earlier prefixes, so the full previous-count row is useful.

## Alternatives and edge cases

- **Brute-force combinations:** Trying every subset of up to four intervals takes $O(n^4)$ candidates before overlap checks, which is too large for $n=5\cdot10^4$.
- **Greedy by weight:** Choosing the heaviest available interval first can block several compatible intervals whose combined weight is greater. Weighted scheduling requires dynamic programming.
- **Weighted scheduling without a count dimension:** A one-row DP may choose more than four intervals. The explicit `chosen` dimension enforces the limit.
- **Boundary equality:** Intervals `[1,3]` and `[3,5]` overlap at point $3$. `bisect_left` correctly excludes the first from the second's compatible prefix.
- **Original versus sorted indices:** Scheduling uses right-end order, but output uses original input indices. Both must be retained separately.
- **Lexicographic tie-breaking:** Comparing only scores can return an arbitrary maximum. Every state stores and compares its sorted original-index tuple.
- **Fewer than four intervals:** The final loop compares exact counts one through four instead of forcing four. Positive weights encourage choices when compatible, but overlap may limit how many can be selected.
- **Single interval:** Its one-choice state is formed from the zero-choice compatible prefix and its original index is returned.
- **Impossible exact counts:** The score-$-1$ sentinel prevents transitions from inventing selections containing more mutually compatible intervals than exist.
- **Positive weights:** The sentinel and the omission of the zero-choice result rely on all weights being at least one, as guaranteed. At least one real interval always beats the empty score.
