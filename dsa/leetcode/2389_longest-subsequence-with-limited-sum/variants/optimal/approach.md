## General

For any fixed length $\ell$, the smallest possible sum of an $\ell$-element subsequence is obtained by choosing the $\ell$ smallest values. If even that sum exceeds a query, no other subsequence of length $\ell$ can fit; if it fits, those selected indices can always be listed in original order to form a valid subsequence.

Sort `nums` and build prefix sums, where prefix position `i` is the minimum sum needed to select `i + 1` elements. Positivity makes this prefix array strictly increasing.

For each query, find the insertion position to the right of all prefix sums less than or equal to the budget. That position is both the number of feasible prefix lengths and the greatest feasible subsequence size. A query below the first prefix produces position zero, while a query at least the full sum produces `n`.

The greedy prefix proves feasibility, and the minimal-sum property proves optimality: any purported longer subsequence has sum at least the corresponding sorted prefix and therefore cannot fit when that prefix exceeds the query.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$ and $m = \lvert\texttt{queries}\rvert$. Sorting costs $O(n\log n)$ and prefix construction costs $O(n)$. The $m$ binary searches cost $O(m\log n)$, for $O(n\log n+m\log n)$ total time. Prefix sums use $O(n)$ space.

## Alternatives and edge cases

- **Scan for every query:** Walking the sorted values until each budget is exceeded is correct but takes $O(nm)$ time when many queries admit most elements.
- **Sort queries offline:** Processing budgets in increasing order with one moving prefix pointer also achieves $O(n\log n+m\log m)$ time, but must restore query order.
- **Budget below the minimum:** No nonempty subsequence fits, so the answer is zero.
- **Exact prefix sum:** Equality is allowed; use a right-bound binary search.
- **Budget above the total:** Every element can be selected.
- **Repeated values or queries:** Prefix positions and answers remain multiplicity-aware without special handling.
