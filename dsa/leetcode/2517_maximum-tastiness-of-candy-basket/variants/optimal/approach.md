## General

Sort the candy prices. For any chosen candies in this order, the smallest pairwise price difference must occur between two consecutive chosen prices: every nonconsecutive pair spans one or more consecutive gaps and cannot have a smaller difference. The task is therefore to place `k` selections along the sorted prices while maximizing their smallest consecutive gap.

For a proposed minimum gap `d`, choose the cheapest candy first and then scan left to right, taking the earliest price that is at least `d` above the most recently chosen price. This greedy choice leaves every later candidate at least as much remaining space as any alternative first choice. Repeating the exchange argument at each selection shows that if any basket can achieve gap `d`, the greedy scan will choose at least `k` candies.

Feasibility is monotone: if a gap `d` is possible, every smaller non-negative gap is also possible. Binary-search this predicate. Zero is always feasible because there are at least `k` candies. An upper bound is $\lfloor R/(k-1) \rfloor$, because `k` sorted selections create `k - 1` consecutive gaps whose sum cannot exceed the total range $R$. When the search finishes, `high` is the greatest feasible gap.

## Complexity detail

Let $n$ be the number of candies and let $R = \max(\texttt{price}) - \min(\texttt{price})$. Sorting takes $O(n \log n)$ time. Each feasibility check scans at most $n$ prices, and binary search performs $O(\log R)$ checks, for total time $O(n \log n + n \log R)$. Python's in-place sort may use $O(n)$ auxiliary memory; the greedy check itself uses $O(1)$ space.

## Alternatives and edge cases

- **Enumerate every candidate gap:** Testing `0, 1, 2, ...` with the same greedy scan is correct but takes $O(nR)$ time and is impractical when prices approach $10^9$.
- **Enumerate baskets:** Trying all choices of `k` candies is combinatorial and cannot handle $n$ up to $10^5$.
- Equal prices belong to distinct candies but contribute a zero difference when both are selected.
- When `k = 2`, choosing a minimum-priced and maximum-priced candy achieves the full range $R$.
- When `k = n`, every candy must be selected, so the answer is the smallest adjacent difference after sorting.
