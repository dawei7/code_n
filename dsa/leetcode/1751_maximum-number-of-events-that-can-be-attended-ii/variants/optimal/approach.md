## General
**Sort and precompute every legal jump**

Sort events by start day and collect the sorted starts. For each event ending on day $e$, binary-search for the first start strictly greater than $e$. Using an upper-bound search is essential because an event starting exactly on day $e$ still overlaps the inclusive end day.

**Choose between skipping and attending**

For a fixed attendance allowance, process event indices from right to left. At index $i$, skipping gives the best value at $i+1$ with the same allowance. Attending earns the current value and adds the best result from its precomputed next compatible index using one fewer event. The larger choice is optimal because every valid selection either contains event $i$ or does not.

**Roll the attendance dimension**

Build one DP row for each allowed count from one through `k`. The previous row represents one fewer selectable event, while the current row is filled from right to left. Once a row is complete, the older row is no longer needed. The final value at index zero is the best selection using at most `k` events.

## Complexity detail
Sorting and the $n$ binary searches take $O(n\log n)$ time. The dynamic program evaluates $n$ states for each of the $k$ attendance limits, adding $O(nk)$ time. The start array, compatible-index array, and two rolled DP rows each contain $O(n)$ entries, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Memoized recursion:** The same skip-or-attend recurrence is direct, but an $O(nk)$ recursion can exceed language stack limits and an unprecomputed linear next-event scan raises the time to $O(kn^2)$.
- **Full DP table:** Storing every count and index state is correct but uses $O(nk)$ space instead of rolling two rows.
- **Sweep-line formulations:** They can solve unrestricted weighted interval scheduling, but enforcing an attendance count still requires a count-indexed state.
- **Inclusive end day:** `next_start == current_end` is a conflict; compatibility requires a strict inequality.
- **At most `k`:** The optimum may select fewer events when a single valuable event overlaps all others.
- **Identical intervals:** At most one may be selected, so keep whichever value benefits the optimum.
- **Unsorted input:** Sorting is part of the algorithm and must not be assumed by callers.
- **Large day values:** Only comparisons are needed; no day-sized array should be allocated.
