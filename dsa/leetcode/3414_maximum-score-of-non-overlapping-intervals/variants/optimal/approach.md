## General

Sort the intervals by their inclusive right endpoint while retaining every original index. For each sorted prefix and each exact selection count from one through four, store a pair consisting of the greatest obtainable score and the lexicographically smallest sorted index tuple attaining that score. The zero-selection layer has score zero for every prefix; all other states begin as impossible.

Consider the $i$th interval in right-end order. One choice skips it and inherits the best state for the preceding prefix. The other choice selects it. Because touching endpoints overlap, a compatible predecessor must end strictly before the current left endpoint. `bisect_left(ends, left, 0, i - 1)` gives the number of earlier intervals whose right endpoint is smaller than `left`, so the appropriate state comes from the preceding selection-count layer at exactly that prefix boundary.

Add the current weight to that predecessor score and insert the original index into its tuple. Between the skip and take candidates, prefer the larger score and then the lexicographically smaller tuple. The state therefore represents the optimum for its exact count: every valid choice either omits the current interval or includes it after a compatible choice of one fewer interval, and those are precisely the two transitions compared.

After all prefixes have been processed, compare the terminal states for one, two, three, and four selected intervals. Positive weights guarantee that an optimal answer is nonempty, while this final comparison implements the contract's *up to four* rule and its lexicographic tie-break across different selection counts.

## Complexity detail

Let $n=\lvert\texttt{intervals}\rvert$. Sorting costs $O(n\log n)$. There are four dynamic-programming layers with $n$ states each; every state performs one binary search and handles an index tuple of length at most four, so the dynamic program also costs $O(n\log n)$. The total time is $O(n\log n)$.

The sorted interval list, endpoint list, and five dynamic-programming rows use $O(n)$ space. Each stored index tuple has length at most four, which is constant.

The benchmark defines `size` as the number of intervals $n$ and uses 40, 160, and 320 mutually disjoint singleton intervals, spanning 8x. The accepted sort-and-binary-search method is $O(n\log n)$. A correct slower dynamic program that scans every earlier interval to find compatible predecessors takes $O(n^2)$ time and must fail only the scaling verdict.

## Alternatives and edge cases

- **Scan all earlier intervals per state:** This preserves the weighted-interval recurrence but takes $O(n^2)$ time instead of using binary search.
- **Greedily choose the heaviest remaining interval:** A locally heavy interval can block several compatible intervals with a greater combined score.
- **Treat endpoint equality as compatible:** This violates the inclusive-interval rule; the predecessor must satisfy $r_j<l_i$, not $r_j\le l_i$.
- **Always select four intervals:** The contract allows fewer, and a single heavy interval may beat every larger compatible choice.
- **Unsorted input:** Sorting by right endpoint is part of the algorithm, while returned indices always refer to the original order.
- **Equal scores:** Carry the lexicographically smallest sorted original-index tuple in every state and apply the same comparison across final counts.
- **Fewer than four compatible intervals:** Impossible exact-count states remain excluded, and the best feasible terminal layer supplies the answer.
