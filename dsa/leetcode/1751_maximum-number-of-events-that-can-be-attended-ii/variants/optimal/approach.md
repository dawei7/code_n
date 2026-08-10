## General

**Sort events so every decision has a forward remainder**

Each event is `[startDay, endDay, value]`. If an event is attended, a later chosen event must start strictly after its inclusive end day. Sorting `events` lexicographically places them in nondecreasing start-day order, with end day and value only breaking ties.

After sorting, a subproblem can be described by two numbers:

- `i`, the first event index still available for consideration.
- `k`, the maximum number of events that may still be attended.

The cached helper `dfs(i, k)` returns the greatest total value obtainable from sorted indices `i` onward while choosing at most `k` events. Reusing the name `k` inside the helper shadows the outer parameter but does not change the meaning; each recursive call carries its own remaining capacity.

**The base case for an exhausted suffix**

If `i >= len(events)`, no event remains, so the best additional value is zero. The code checks this before indexing the list.

There is no separate early base case for `k == 0`. Instead, such a state can only skip events because the attending branch is guarded by `if k`. It recursively advances `i` until reaching the end. Caching ensures each zero-capacity suffix state is computed once. This is correct, though returning zero immediately when `k == 0` would save those recursive steps.

**Consider skipping the current event**

For current event `i`, one valid choice is not to attend it. The remaining problem then starts at `i + 1` with the same capacity:

`ans = dfs(i + 1, k)`.

This option is essential even though all event values are positive. A low-value current event may overlap a later, more valuable event or may consume one of the limited selections needed for a better combination.

**Find the first compatible event after attending**

The assignment `_, ed, val = events[i]` extracts the current inclusive end day and value. If capacity remains, the code uses:

`bisect_right(events, ed, lo=i + 1, key=lambda x: x[0])`.

Because events are sorted by start day and the key extracts `x[0]`, this binary search returns the first index `j` whose start day is strictly greater than `ed`. `bisect_right` is crucial: an event starting exactly on `ed` is not compatible because end days are inclusive.

The lower bound `lo=i + 1` restricts the search to later list positions. Every index before `j` either is the current event or starts no later than its end and therefore cannot follow it. Every index from `j` onward has a start day greater than `ed` and belongs to the valid future suffix.

**Consider attending the current event**

Attending gains `val`, consumes one selection, and jumps over all overlapping events. Its total is:

`dfs(j, k - 1) + val`.

The helper takes the maximum between this total and the skip total. These are exhaustive choices: every optimal plan either includes event `i` or it does not. If it includes the event, no index before `j` can be selected afterward, and all potential later choices are represented by `dfs(j, k - 1)`.

The problem allows attending fewer than the original maximum. The skip branch and zero-valued base cases naturally model that; the recurrence never forces exactly `k` selections.

**Why caching is necessary**

Different decision paths can reach the same pair `(i, k)`. Without memoization, the include-or-skip recursion would recompute suffixes exponentially many times.

The `@cache` decorator stores the integer returned for each argument pair. Once a state is solved, later calls with the same starting index and remaining capacity return immediately. Sorting occurs before the first call to `dfs`, so the cached function sees one stable event order throughout execution.

Although `dfs` is defined before `events.sort()` in source order, Python does not execute its body at definition time. The body first runs only after sorting, when `return dfs(0, k)` is evaluated.

**Trace the main recurrence**

For events `[[1,2,4],[2,3,1],[3,4,3]]` after sorting and capacity two, consider index zero. Skipping leads to the best plan from index one.

Attending the first event ends on day two. `bisect_right` finds the event starting on day three, not the event starting on day two. The attend total is four plus the best one-event plan from that compatible index, yielding seven. This beats alternatives in the first example.

If a single overlapping event has value ten, the skip branch can select it, and the remaining capacity need not be filled. That explains why “at most `k`” rather than “exactly `k`” is embedded in the state.

**Why the returned value is correct**

Use induction on the number of events remaining. With no event, zero is optimal. For state `(i, k)`, any feasible plan either excludes event `i` and is bounded by `dfs(i + 1, k)`, or includes it. In the second case, inclusivity of `ed` forces the next selected start to be greater than `ed`, so all later choices lie in the suffix beginning at binary-search index `j` and are bounded by `dfs(j, k - 1)`.

The recurrence evaluates both categories and takes their maximum. By the induction hypothesis, each recursive suffix value is optimal for its state. Thus `dfs(i, k)` is optimal, and `dfs(0, original k)` is the maximum total for the complete event set.

## Complexity detail

Let $n$ be the number of events and let $K$ be the original attendance limit. Sorting costs $O(n\log n)$ time. The cache can contain up to $O(nK)$ distinct states `(i, remaining capacity)`. In the exact source, every state with positive capacity performs its own `bisect_right`, which costs $O(\log n)$. Therefore the implementation's conservative worst-case time is:

$$
O(n\log n+nK\log n)=O(nK\log n).
$$

This is looser than the manifest's $O(n\log n+nK)$ claim. Achieving that tighter time would require computing the next compatible index once per event and reusing it across all capacity states. The exact `solution.py` does not precompute those indices.

The memoization cache can store $O(nK)$ results, not $O(n)$. The recursion stack can also reach $O(n)$ depth through repeated skip calls, and sorting uses implementation-dependent temporary space. Thus the exact auxiliary-space bound is $O(nK)$ in the worst case, rather than the manifest's stated $O(n)$. This document preserves the exact source behavior instead of attributing an unimplemented rolling-space optimization to it.

The constraint $nK \le 10^6$ bounds the theoretical cache count, but Python recursion depth may still be a practical concern for long skip chains.

## Alternatives and edge cases

- **Precompute next indices:** Run one binary search per event, then every cached transition is $O(1)$, yielding $O(n\log n+nK)$ time while retaining $O(nK)$ memo space.
- **Bottom-up two-dimensional DP:** It avoids recursion and uses the same skip/attend recurrence, but stores $O(nK)$ values.
- **Rolling DP by event count:** With carefully ordered transitions and precomputed compatibility, memory can be reduced toward $O(n)$, matching the manifest's target space rather than the exact source.
- **Weighted interval scheduling without k:** Ordinary one-dimensional DP is insufficient because the attendance limit adds a second state dimension.
- **Linear search for the next event:** It would make transitions slower; binary search uses the sorted start days.
- **Inclusive end day:** `bisect_right` rejects events whose start equals the current end.
- **Same start day:** Sorting keeps them adjacent, and the skip/attend choices compare their downstream value effects.
- **Single event:** Attending its positive value beats skipping when capacity is at least one.
- **Capacity one:** The recursion chooses the greatest individual value, regardless of overlaps.
- **Capacity at least number of mutually compatible events:** It may attend all useful compatible events but is never forced to fill unused capacity.
- **All events overlap:** At most one is selected, and skip decisions allow the maximum-value one to win.
- **No events overlap:** The DP selects up to `K` values while preserving chronological order.
- **Large day values:** Binary search compares integers and does not allocate a calendar-sized structure.
- **Zero-capacity cached states:** They walk to the end through skip calls because the exact source lacks an immediate `k == 0` return.
- **Input mutation:** `events.sort()` changes the caller-provided list order in place; the algorithm relies on that sorted order.
- **Recursion limit:** A long chain of `dfs(i + 1, k)` calls can be deeper than Python's default recursion limit even though the asymptotic recurrence is valid.
- **Positive values:** Skipping remains necessary because overlap and the event-count cap can make a later combination more valuable.
