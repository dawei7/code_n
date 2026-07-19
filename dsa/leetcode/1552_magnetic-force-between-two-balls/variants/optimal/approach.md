## General
**Convert a candidate distance into a feasibility question**

Sort the basket coordinates. For a proposed minimum distance `distance`, place the first ball at the leftmost basket, then scan from left to right and place each next ball at the earliest coordinate at least `distance` beyond the previous placement.

This greedy placement leaves every subsequent ball as much remaining space as possible. If any placement with the candidate distance can fit $m$ balls, replacing its first position by the leftmost basket and each later position by the greedy earliest feasible basket never moves a ball rightward. The greedy scan therefore also fits $m$ balls. Conversely, every greedy placement directly satisfies the distance requirement.

**Exploit monotonic feasibility**

If a distance is feasible, every smaller nonnegative distance is feasible. If it is infeasible, every larger distance is infeasible. Binary-search this monotone boundary between one and the span divided by $m-1$, which is an upper bound because $m-1$ gaps must fit inside the full span.

When the midpoint is feasible, search above it; otherwise search below it. At termination, the last feasible value is the largest achievable minimum force.

## Complexity detail
Sorting a copied list of $n$ coordinates costs $O(n \log n)$ time and $O(n)$ space for the copy. Each feasibility scan costs $O(n)$ and binary search performs $O(\log R)$ scans, giving $O(n \log n+n \log R)$ total time. Beyond the sorted copy, the scan and search use $O(1)$ state.

## Alternatives and edge cases
- **Try every integer distance:** reuse the greedy feasibility test but check distances one by one, which can take $O(nR)$ time.
- **Enumerate basket subsets:** examining all choices of $m$ baskets is combinatorial.
- **Dynamic programming over coordinates:** possible state formulations are much heavier than the monotone feasibility search.
- With $m=2$, the answer is the distance between the extreme baskets.
- With $m=n$, every basket is used and the answer is the smallest adjacent sorted gap.
- Input order has no effect after sorting.
- Large unused gaps can dominate the answer even when many baskets are clustered elsewhere.
- The upper-bound division by $m-1$ is safe because the selected positions create exactly $m-1$ adjacent gaps.
