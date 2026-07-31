## General

Begin by reducing the raw table to eligible user-days. Group by (`user_id`, `action_date`) and retain only groups whose row count is one. `MIN(action)` then extracts that day's sole action. This filtering is essential because the composite primary key permits two different actions for the same user and date; retaining either one would incorrectly treat that date as stable.

Next, number the eligible dates separately for each (`user_id`, `action`) pair. For a truly consecutive run, subtracting this row number from the calendar date produces the same value on every row: both the date and the number advance by one. A missing date, an excluded multi-action date, or an intervening different action changes that value and therefore starts another island.

Aggregate each island to obtain its length and endpoint dates, then discard islands shorter than five. Rank the remaining islands inside each user by decreasing length and retain rank one. The additional start-date and action keys make the query deterministic if two maximum runs have equal lengths, a situation for which the source does not prescribe a tie rule. Finally, apply the required result ordering.

The construction is exact in both directions. Every grouped island contains one identical action on adjacent calendar dates, because an ineligible date was removed and a date gap changes the island key. Thus every retained island satisfies the definition. Conversely, every qualifying source run survives the single-action filter, receives consecutive row numbers within its user and action, and shares one island key, so its aggregate cannot be lost before maximum-length ranking.

## Complexity detail

Let $R$ be the number of rows in `activity`. Grouping the raw rows and ordering the window partitions take $O(R\log R)$ time under a general sort-based database plan. The final ranking and output sort do not exceed that bound. Materialized grouped rows, window state, and sort storage can use $O(R)$ space. A database may exploit indexes or hash aggregation, but the query does not depend on those optimizations.

The benchmark defines size as $R$. Each tier contains many independent users with same-action runs, so the windowed query performs a bounded number of grouped and ordered passes while the slower control repeatedly rescans dates for individual candidate starts.

## Alternatives and edge cases

- **`LAG` plus a cumulative break count:** Comparing each eligible date and action with the preceding row can mark island starts, followed by a running sum. It is equally valid but needs an additional window stage.
- **Correlated streak expansion:** Testing every date as a possible start and repeatedly counting later dates is correct, but repeated table scans can approach $O(R^2)$ work.
- **Recursive calendar walk:** A recursive CTE can extend one date at a time, but it is more elaborate and can materialize many overlapping partial runs.
- **Multiple actions on one date:** The entire user-date is ineligible. Choosing an arbitrary action from that date would violate the exactly-one rule.
- **Exactly five days:** Five is inclusive, so a length-five island qualifies.
- **Calendar gaps:** Consecutive table rows are insufficient; dates themselves must differ by one day.
- **Action changes and returns:** A different action ends the island. Returning later to the earlier action starts a new island rather than joining the two portions.
- **Several qualifying runs:** Only a maximum-length run is returned for each user. The source does not specify which equal-length maximum to choose; the query uses the earliest start as a deterministic fallback.
- **Output order:** Longer selected runs come first, and only equal lengths use increasing `user_id`.
