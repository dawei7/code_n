## General

**Turn a maximum-length bound into forbidden windows.** Suppose the proposed final stability factor is at most $k$. A stable subarray longer than $k$ exists if and only if some window of exactly $k+1$ consecutive elements has GCD greater than $1$: every longer stable subarray contains such a window, while that window itself already violates the bound. Therefore, a modification plan is feasible precisely when it can touch every offending length-$(k+1)$ window.

Set every chosen position to `1`. Any window containing that position then has GCD $1$, so selecting indices that intersect all offending windows is sufficient; there is no need to model replacement values separately.

**Greedily hit equal-length intervals.** Scan the windows by increasing left endpoint. When an offending window is not already covered by the most recent modification, change its rightmost position. Every later window that could have been covered by any position in the current window ends no earlier than this right endpoint, so choosing the right endpoint preserves at least as much future coverage as any other valid choice. Exchanging an optimal plan's first point for this right endpoint cannot increase its number of changes. Repeating this argument proves that the scan uses the minimum possible number of modifications for the chosen $k$.

**Answer each GCD query in constant time.** GCD is idempotent: overlapping blocks may be combined without changing the result. A sparse table stores the GCD of every power-of-two block. A range is answered from two possibly overlapping blocks of its largest fitting power-of-two length. The greedy feasibility scan is therefore linear after preprocessing.

If a bound $k$ is feasible, every larger bound is also feasible because it forbids fewer subarrays. Binary search this monotone predicate over $0$ through $n$. The endpoint $n$ is always feasible, while $k=0$ correctly asks whether all stable singletons can be hit within the change budget.

## Complexity detail

Let $n$ be the length of `nums`. Building the sparse table takes $O(n \log n)$ time and space. Each feasibility test scans at most $n$ windows with $O(1)$ GCD queries, and binary search performs $O(\log n)$ tests, for another $O(n \log n)$ time. The total time is $O(n \log n)$ and the total auxiliary space is $O(n \log n)$.

## Alternatives and edge cases

- **Segment tree:** Range GCD queries use $O(\log n)$ time and $O(n)$ space, producing an $O(n \log^2 n)$ solution after the outer binary search.
- **Recomputing every window GCD:** This remains correct but can spend linear time per window, degrading toward quadratic work for a single feasibility check.
- **No modifications:** With `maxC = 0`, feasibility reduces to whether the original array already has no stable window longer than the candidate bound.
- **Eliminating every stable singleton:** A bound of zero requires changing every element at least $2$; values equal to `1` need no change.
- **Overlapping offending windows:** One change can cover many windows, which is why counting bad windows directly overestimates the required changes.
- **GCD equal to one:** Such a window is already non-stable and never needs to be hit.
