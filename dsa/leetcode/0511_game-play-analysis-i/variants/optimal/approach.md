## General
**Form one group per player**

Use `GROUP BY player_id` so every distinct player contributes exactly one output row. All activity rows belonging to that player are then available to one aggregate computation.

**Select the chronologically earliest date**

Apply `MIN(event_date)` within each group and alias the expression as `first_login`. SQL date values use chronological ordering, so the minimum is the first recorded login regardless of insertion order or device.

**Why the aggregation produces the contract**

Each input row belongs to exactly one `player_id` group, and every player present in `Activity` creates one such group. `MIN` returns a member date no later than every other date in that group. Consequently each output row contains precisely one player and that player's earliest recorded event date.

## Complexity detail
An expected hash-aggregation plan scans `A` activity rows once and keeps one aggregate state for each of `P` players, giving $O(A)$ time and $O(P)$ auxiliary space. A database may instead choose sort aggregation with $O(A \log A)$ work depending on indexes, statistics, and its physical plan.

## Alternatives and edge cases
- **Correlated minimum subquery:** can produce the same result but may rescan `Activity` for every outer row and take quadratic work.
- **Window function with `ROW_NUMBER`:** can select the first row per player, but sorting full partitions is unnecessary when only the minimum date is needed.
- **Join against a grouped subquery:** is useful when other columns from the first activity are required, but adds a join that this output does not need.
- **One activity:** its date is automatically that player's minimum.
- **Input order:** has no effect on `MIN`.
- **Shared dates across players:** remain in separate groups.
- **Empty table:** yields an empty result because there are no player groups.
