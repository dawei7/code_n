## General

**A previous maximum, not merely the previous row.** Partition events by `hall_id` and order each partition by `start_day`, then `end_day`. Before each row, compute the maximum `end_day` among all earlier rows. The current event starts a new merged interval exactly when its `start_day` is later than that previous maximum. Comparing only with `LAG(end_day)` is insufficient: a short interval nested inside a longer one could hide the longer reach from the next row.

Because event endpoints are inclusive, equality means overlap. Therefore `start_day > previous_max_end` creates a gap, whereas `start_day = previous_max_end` remains in the current merged interval. The first row has no previous maximum and receives the initial group marker.

**Turn gap markers into stable island identifiers.** Cumulatively sum the new-group markers within each hall, using the same deterministic ordering. Every row connected by direct or transitive overlap receives the same `group_id`; the identifier increases exactly at a genuine uncovered gap.

Finally group by `hall_id` and `group_id`. The minimum start and maximum end in each group are the required merged endpoints. Duplicate rows neither create a gap nor change either aggregate, so they naturally collapse into the same result.

## Complexity detail

Let $r$ be the number of rows in `HallEvents`. The database must order rows within halls for the window calculations, which takes $O(r\log r)$ time in the general comparison model; the window scans and final aggregation are linear after that ordering. The ordered intermediate relations and window state use $O(r)$ auxiliary space. A suitable physical index or execution plan can reduce the actual sorting work.

## Alternatives and edge cases

- **Recursive interval sweep:** A recursive CTE can consume one ordered event at a time and carry the active range, but it is more verbose and often less friendly to database optimizers.
- **Pairwise overlap joins:** Joining every event to all earlier events can recover the running maximum, but it may create $O(r^2)$ intermediate pairs instead of using an ordered window.
- **Previous row only:** `LAG(end_day)` is incorrect when a nested short event follows a long event; use the maximum end over all preceding rows.
- **Touching endpoints:** Ranges sharing one endpoint overlap because both dates are inclusive; split only when the next start is strictly later than the running end.
- **Transitive bridges:** An event may connect multiple ranges even when the outer ranges do not overlap directly; the running maximum preserves that connection.
- **Duplicate rows:** Duplicates remain in one island and do not change its minimum start or maximum end.
- **Different halls:** Partition both window calculations by `hall_id` so dates in one hall cannot join an interval in another.
