## General
**Map each type to cumulative candy positions**

Number all candies from one in mandatory eating order. A prefix sum gives the position immediately before each type and the last position belonging to it. If `before` candies have earlier types and `through` candies have types up to the favorite, then the favorite occupies positions `before + 1` through `through`.

**Bound consumption through the favorite day**

By the end of zero-indexed day `d`, at least `d + 1` candies have been eaten because every active day consumes at least one. Under cap `c`, at most `(d + 1) * c` candies can have been eaten. These bounds describe all relevant schedule flexibility.

**Test whether the two intervals overlap**

The favorite type can be eaten on day `d` precisely when the maximum possible cumulative consumption reaches beyond `before`, while the minimum mandatory consumption has not already passed `through`:

$$
\texttt{before} < (d+1)c
\quad\text{and}\quad
d+1 \le \texttt{through}.
$$

The first strict inequality ensures at least one favorite candy can be reached by that day. The second inclusive inequality allows the last favorite candy to be eaten exactly on that day. Together they are sufficient because daily amounts can be adjusted between one and the cap to hit any cumulative total between those bounds.

## Complexity detail
Building all type prefix sums takes $O(n)$ time. Each of the $q$ queries uses two prefix values and constant arithmetic, so total time is $O(n+q)$. The prefix array stores $n+1$ cumulative counts and uses $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Sum earlier types per query:** Recomputing `before` from the raw counts takes $O(nq)$ time in the worst case.
- **Simulate days:** Favorite days and caps can reach $10^9$, so day-by-day simulation is neither necessary nor feasible.
- **Day zero:** The minimum cumulative amount is one, not zero.
- **Same-day type transition:** A day may finish one type and immediately begin the next, so reaching `before + 1` within the cap is enough.
- **Exact last candy:** `d + 1 == through` remains feasible because the favorite's last candy may be the mandatory candy for that day.
- **Too early:** If `(d + 1) * dailyCap <= before`, even the fastest schedule cannot reach the favorite type.
- **Too late:** If `d + 1 > through`, eating at least one per day forces the schedule past the favorite type.
- **Large products:** Use integer arithmetic wide enough for `(favoriteDay + 1) * dailyCap`.
