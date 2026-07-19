## General
**Find each player's first date**

Group `Activity` by `player_id` and compute `MIN(event_date)` as `first_login`. This derived relation has one row per player and identifies the exact date whose device is required.

**Join the date back to its source row**

Join the derived relation to `Activity` on both `player_id` and `event_date = first_login`. Matching on the player prevents equal dates from different players from mixing, and matching on the date selects the earliest row rather than an arbitrary activity.

**Why the returned device is associated correctly**

The table key permits only one activity row for a given player and date. The grouped minimum identifies one earliest date per player, and the two-column join therefore matches exactly that player's unique earliest row. Selecting `device_id` from the matched source row preserves the required association.

## Complexity detail
An expected hash aggregate followed by a hash join scans `A` activity rows a constant number of times and stores one first-date entry per `P` players, for $O(A)$ time and $O(P)$ auxiliary space. Actual SQL costs depend on indexes and the optimizer; sort aggregation can require $O(A \log A)$ work.

## Alternatives and edge cases
- **Correlated minimum subquery:** is concise but may rescan `Activity` for every outer row and take $O(A^2)$ work.
- **Tuple membership against grouped minima:** `(player_id, event_date) IN (...)` expresses the same selection where row-value syntax is supported.
- **Window `ROW_NUMBER`:** correctly retains the complete earliest row but generally sorts each player's partition.
- **Aggregate `MIN(device_id)`:** is incorrect because the numerically smallest device need not belong to the first date.
- **One activity:** that row's device is returned directly.
- **Input order:** does not determine which activity is first.
- **Same date across players:** is safe because the join also matches `player_id`.
