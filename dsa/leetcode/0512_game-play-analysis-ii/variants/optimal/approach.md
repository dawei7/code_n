## General

**Derive one earliest date per player**

Group `Activity` by `player_id` and compute `MIN(event_date)` as `first_login`. This derived relation contains one row
per player and identifies the date whose device must be returned.

**Join each date back to its complete activity row**

Join the derived relation to `Activity` on both `player_id` and `event_date = first_login`. Matching the player keeps
equal dates belonging to different players separate. Matching the date selects the source row associated with the
minimum rather than aggregating an unrelated device value.

The composite primary key guarantees at most one activity row for each `(player_id, event_date)` pair. Consequently,
each grouped minimum joins to exactly one earliest row for that player, and projecting that row's `device_id` returns
the required device.

## Complexity detail

Let $A$ be the number of `Activity` rows and $P$ the number of distinct players. With hash aggregation followed by a
hash join, the query performs expected $O(A)$ work and stores $O(P)$ grouped entries. Actual execution depends on the
database engine, indexes, and optimizer; a sort-based aggregate can require $O(A \log A)$ work.

## Alternatives and edge cases

- **Correlated minimum subquery:** is concise and correct but may rescan `Activity` for each outer row, causing
  quadratic work without a supporting access path.
- **Tuple membership against grouped minima:** expresses the same selection where row-value syntax is supported.
- **Window `ROW_NUMBER`:** correctly retains the complete earliest row but normally sorts each player's partition.
- **Aggregate `MIN(device_id)`:** is incorrect because the numerically smallest device need not occur on the earliest
  date.
- **Single activity:** that row is necessarily the player's first login.
- **Input order:** has no bearing on chronological order.
- **Same date for different players:** remains unambiguous because the join also matches `player_id`.
