## General
**View every match from both sides.** Emit one point event for `host_team` and one for `guest_team`. A host event awards 3, 1, or 0 according to whether `host_goals` is greater than, equal to, or less than `guest_goals`. The guest event applies the symmetric comparison.

**Aggregate events by team ID.** Combining these two projections with `UNION ALL` preserves both teams' contributions from every match. Grouping by the emitted team ID and summing points produces exactly each participating team's total.

**Restore the complete team catalog.** Left join `Teams` to the point events before grouping, or to their totals afterward. A team with no event then has a null sum, which `COALESCE` converts to zero. Grouping with the catalog also supplies the team name.

**Apply the standings order.** Sort the final rows by total points descending. For equal totals, sort `team_id` ascending. This explicitly implements both levels of the required order rather than relying on group output order.

## Complexity detail
The event stream contains exactly $2m$ rows. Building it, aggregating it, and joining the $t$ team rows take $O(t+m)$ logical time with hash aggregation and indexed or hash joins. The event and grouping state can occupy $O(t+m)$ space. Physical engines may choose different join or sort plans.

## Alternatives and edge cases
- **Join with `team_id = host_team OR team_id = guest_team`:** This is concise and correct, but an optimizer may use a nested comparison of teams and matches, taking $O(tm)$ time.
- **Two separate aggregates joined to Teams:** Host and guest totals can be computed independently and added, but null handling becomes more verbose.
- **Idle team:** The left join and `COALESCE` are necessary to return zero points.
- **Draw:** Both perspective events must award one point.
- **Away win:** The guest event, not the host event, receives three points.
- **No negative scores:** A loss contributes zero rather than subtracting points.
- **Tied standings:** Smaller `team_id` comes first regardless of team name.
