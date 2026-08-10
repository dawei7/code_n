## General

After choosing one integer from each interval, sort the chosen values. The minimum absolute difference among all pairs is then attained by two adjacent chosen values. Therefore asking whether score `g` is possible is equivalent to asking whether values can be placed in interval order with every consecutive gap at least `g`.

The source sorts `start`. Because every interval has equal length `d`, sorting left endpoints also sorts right endpoints. A feasible selection can be considered in this order.

For a candidate gap `mi`, helper `check` greedily chooses the earliest possible value in each interval. If `last` was previously chosen and the current interval begins at `st`, the new value must be at least both `st` and `last + mi`:

`last = max(st, last + mi)`.

Before assigning it, the helper checks whether `last + mi > st + d`. If so, even the earliest value respecting the gap lies beyond the interval's right endpoint and feasibility fails.

`last` starts at negative infinity, so the first chosen value becomes exactly the first interval's left endpoint.

**Why earliest placement is optimal for feasibility.** Any feasible current choice cannot be smaller than the greedy maximum of interval start and previous choice plus gap. Choosing anything larger only makes every later lower bound larger and cannot help. By induction, greedy's `last` is no greater than the corresponding choice in any feasible construction. If greedy exceeds a right endpoint, no construction can succeed; if it finishes, its choices witness feasibility.

Feasibility is monotone. If gap `g` works, every smaller nonnegative gap works using the same choices. If `g` fails, every larger gap also fails. This makes binary search appropriate.

The search begins with `l=0`, always feasible. A safe upper bound is the entire possible span from the first interval's left endpoint to the last interval's right endpoint: `start[-1] + d - start[0]`. No pairwise minimum can exceed that overall span.

The upward-biased midpoint `(l + r + 1) >> 1` prevents an infinite loop when two candidates remain. A feasible midpoint moves `l` up; an infeasible one moves `r` to `mid - 1`. On termination they equal the largest feasible score.

For `start=[6,0,3],d=2`, sorting gives intervals `[0,2],[3,5],[6,8]`. Gap four greedily chooses zero, four, and eight, so it is feasible. Gap five would require zero, five, then ten beyond the final endpoint, so four is maximal.

The method sorts `start` in place, so caller-visible order changes. Interval identity does not matter to the score, but this mutation is part of the exact behavior.

## Complexity detail

Let $n$ be the interval count and $R=start[-1]+d-start[0]$ after sorting. Sorting costs $O(n\log n)$. Each feasibility check scans $n$ intervals, and binary search performs $O(\log(R+1))$ checks. Total time is $O(n\log n+n\log R)$.

The check uses $O(1)$ extra state. Python's in-place sort can use $O(n)$ temporary references, so the practical auxiliary-space bound is $O(n)$ as declared.

## Alternatives and edge cases

- **Try every possible score:** Coordinate values reach $10^9$, so linear search over gaps is too slow.
- **Choose interval midpoints:** Fixed local choices do not maximize the global minimum gap.
- **Dynamic programming over coordinates:** The coordinate range is enormous; monotone feasibility avoids coordinate-sized state.
- **Different interval lengths:** Sorting starts would not necessarily sort ends, and this exact greedy proof would need reconsideration. Equal `d` is essential.
- **`d = 0`:** Every choice is fixed at its start; binary search finds the minimum adjacent difference among sorted starts.
- **Duplicate starts:** Intervals may overlap completely. Positive separation may still be possible using different values within their shared width.
- **Score zero:** Always feasible because equal chosen integers are allowed unless a larger score is sought.
- **Two intervals:** The result is simply their greatest achievable separation, and the general search handles it.
- **Greedy equality at right endpoint:** `last + mi == st + d` is feasible; the failure comparison is strict greater-than.
- **Negative infinity sentinel:** It ensures the first interval is unconstrained by a fictional predecessor.
- **All starts sorted already:** Sorting preserves their order while retaining the same asymptotic guarantee.
- **Input mutation:** Use `sorted(start)` instead if caller order must be preserved, at explicit $O(n)$ copy space.
- **Why only adjacent chosen values matter:** In sorted order, any nonadjacent difference is the sum of one or more nonnegative adjacent gaps and therefore cannot be smaller than every intervening adjacent gap.
- **Interval association after sorting:** Reordering intervals is safe because the output asks only for a set of one choice per interval and a symmetric pairwise score; original indices have no separate meaning.
- **Upper bound looseness:** The total span may be much larger than the true score, especially for many intervals. Binary search needs only a safe bound, not a tight one.
- **No explicit chosen array:** `check` stores only the latest greedy choice because the next constraint depends on no earlier value once consecutive spacing is enforced.
