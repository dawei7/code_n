## General

**Keep comparison groups exact.** Partition sessions by both `user_id` and
`session_type`, then order each partition by `session_start` and `session_id`.
The ID tie-breaker makes equal start times deterministic, while the partition
prevents a `Viewer` session from being paired with a `Streamer` session.

**Remember the best prior endpoint.** For each current row, compute the maximum
`session_end` over all earlier rows in its partition, excluding the current
row. This is stronger than using only `LAG`: the immediately preceding start
is not necessarily the prior session with the latest end. If the current start
is at most twelve hours after that maximum prior end, at least one distinct
same-type prior session forms a qualifying pair. Overlapping sessions also
have no positive gap and satisfy the maximum-gap condition.

Filter rows that satisfy the bound, deduplicate their users, and sort the IDs.
The running maximum represents the closest possible prior end, so failing its
twelve-hour test means every earlier same-type session is too far away; passing
it supplies a valid pair.

## Complexity detail

Let $n$ be the number of sessions and $u$ the number of qualifying users.
Partition ordering for the window function takes $O(n\log n)$ time, and sorting
the distinct output costs at most $O(u\log u)$, which is contained in the same
bound. Window and sorting state use $O(n)$ space.

## Alternatives and edge cases

- **Quadratic self-join:** Comparing every pair directly is correct but repeats work and can take $O(n^2)$ time for one large user/type group.
- **Partition only by user:** This can incorrectly combine a `Viewer` session with a `Streamer` session.
- **Use only `LAG(session_end)`:** The previous start-time row need not have the latest prior end when sessions overlap or have different durations.
- The two sessions must be distinct; excluding the current row from the window frame enforces this automatically.
- A gap of exactly twelve hours qualifies, while any positive amount beyond it does not.
- One session alone cannot qualify its user because no prior endpoint exists.
- Input row order is irrelevant; chronological order comes from the window definition.
