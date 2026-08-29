## General

**Process queries offline by increasing size threshold.** A query needs room IDs from rooms whose size is at least `minSize`, then chooses the ID closest to `preferred`. The two dimensions need different orderings: room size decides eligibility, while room ID decides closeness.

The solution sorts `rooms` by size ascending and creates `idx`, the query indices sorted by each query’s minimum size. It also initializes `sl` as a `SortedList` containing every room ID.

As query thresholds increase, rooms that are too small are removed from `sl`. Thus `sl` remains ordered by ID while representing exactly the rooms eligible for the current query.

**Preserve original query order with indices.** `idx = sorted(range(k), key=lambda i: queries[i][1])` does not rearrange `queries` itself. It sorts integer positions by `minSize`. Results are written into `ans[j]`, so processing order can differ from output order without losing the required correspondence.

**Maintain the eligibility invariant.** Pointer `i` identifies the first room in size-sorted `rooms` not yet removed. Before answering a query, the loop removes rooms while `rooms[i][1] < minSize`. The inequality is strict because a room whose size equals the minimum is eligible.

Because queries are processed with nondecreasing thresholds, a removed room can never become eligible for a later query. Each room is removed at most once. After the loop, every ID in `sl` has size at least the current threshold, and every absent processed room has smaller size.

If `i == n`, every room has been removed. Current and later queries cannot have an answer because later thresholds are no smaller, so `break` safely leaves their prefilled answers as minus one.

**Only two IDs can be closest.** `p = sl.bisect_left(prefer)` finds the first eligible room ID not less than `prefer`.

- If `p < len(sl)`, `sl[p]` is the closest possible candidate on the right.
- If `p > 0`, `sl[p - 1]` is the closest possible candidate on the left.

Any farther-right ID is no closer than `sl[p]`, and any farther-left ID is no closer than `sl[p - 1]`. Therefore no other eligible room needs inspection.

The code first assigns the right candidate when one exists. It then chooses the left candidate if there was no right candidate or if

`ans[j] - prefer >= prefer - sl[p - 1]`.

The greater-than-or-equal comparison is deliberate. When distances tie, the left candidate has the smaller ID and must win.

**Trace a tie.** Suppose eligible IDs are one and three and the preferred ID is two. The lower bound points to three, so the provisional answer is three. Both distances are one. The condition uses `>=`, selects the left predecessor one, and implements the tie rule.

If the preferred ID itself is eligible, lower bound returns its position. The right distance is zero, and no left candidate can beat it, so the exact preferred ID remains.

**Why the sweep is correct.** For each processed query, the threshold-removal loop makes `sl` exactly the eligible-ID set. Sorted lower bound identifies the nearest candidate on each side of the preferred value. Comparing those two distances, with equality favoring the smaller left ID, applies exactly the query rule. Writing to the original index places the correct answer in the output position. Induction over increasing thresholds proves removals remain valid for every later query.

**The exact method mutates room order.** `rooms.sort(key=lambda x: x[1])` reorders the caller’s outer room list by size. It does not change individual room pairs or the `queries` collection. This mutation is harmless to the judge but relevant to callers that expect the original room ordering afterward.

## Complexity detail

Let `r` be the number of rooms and `q` the number of queries. Sorting rooms costs `O(r log r)`, and sorting query indices costs `O(q log q)`. Building the sorted ID structure costs up to `O(r log r)` under a general ordered-container construction.

Each room is removed once at `O(log r)` cost, and each query performs a binary search plus constant candidate access at `O(log r)`. Total time is

`O(r log r + q log q + q log r)`.

This is often summarized as `O((r + q) log r)` when the scale assumptions make the query-sort term comparable, but the explicit `q log q` term describes the exact sorting step even when `r` is very small.

`sl` stores up to `r` IDs, `idx` and `ans` store `q` integers, and sorting may use temporary memory. Total space is `O(r + q)`.

## Alternatives and edge cases

- **Process thresholds descending:** Sort rooms and queries by size descending and add newly eligible IDs to an initially empty ordered set. It is the symmetric standard sweep.
- **Scan every room per query:** This costs `O(rq)` and ignores shared threshold work across queries.
- **Binary search only in room IDs:** IDs alone do not encode size eligibility; the offline sweep is what makes the ordered set valid.
- **No eligible room:** The answer remains minus one; if all rooms are removed, the loop safely stops for all later thresholds.
- **Room size equals `minSize`:** It remains because only strictly smaller sizes are removed.
- **Preferred ID exists and is eligible:** Lower bound finds it and distance zero wins.
- **Preferred below every eligible ID:** There is no left candidate, so the smallest eligible ID is chosen.
- **Preferred above every eligible ID:** There is no right candidate, so the greatest eligible ID on the left is chosen.
- **Equal distances:** The `>=` test replaces the right candidate with the smaller left ID.
- **Unique room IDs:** The sorted structure has no ambiguity from duplicate identifiers.
- **Repeated query thresholds:** No extra rooms need removal between them; each query still performs its own closest-ID search.
- **Input mutation:** Rooms are reordered by size, while queries retain their original order and answers use index mapping.
