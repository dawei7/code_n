## General
**Materialize one install row per player.** Group `Activity` by `player_id` and take `MIN(event_date)` as `install_dt`. This prevents later activity from being counted as another install and gives exactly one row for every cohort member.

**Join only the exact next date.** Left join each install row back to `Activity` for the same player where the activity date equals `date(install_dt, '+1 day')`. Because `(player_id, event_date)` is unique, each install row matches at most one retained activity row and therefore remains one cohort member after the join.

**Aggregate the retention indicator.** Group the joined rows by `install_dt`. `COUNT(*)` is the number of installs. Convert a successful next-day match to `1.0` and a missing match to `0.0`; their average is retained players divided by installs. Rounding that average to two decimal places gives `Day1_retention`.

The initial grouping assigns every player to the unique date of their first activity. The left join marks that player precisely when an activity exists one calendar day later, while preserving non-returning players. Consequently, the final count and average use exactly the numerator and denominator in the retention definition.

## Complexity detail
Grouping $A$ activity rows and joining the resulting install rows back to `Activity` takes $O(A \log A)$ time under standard sort-based plans; indexed or hash-based plans may be linear on average. The grouped relation, join state, and result aggregation require at most $O(A)$ working space. Actual constants and plan choices depend on the database engine and indexes.

## Alternatives and edge cases
- **Window minimum:** `MIN(event_date) OVER (PARTITION BY player_id)` can annotate every activity row, but the query must then avoid counting a player more than once per cohort.
- **Correlated next-day subquery:** Testing `Activity` separately for every installed player is concise, but without an index it may repeatedly scan the table and approach $O(A^2)$ time.
- **Later return:** Activity two or more days after installation does not count toward day-one retention.
- **No return:** The left join must preserve the player and contribute zero rather than remove that player from the denominator.
- **Multiple install dates:** Cohort counts and retention rates are computed independently for each first-login date.
- **Zero games played:** Such a row is still a login and participates in both install and retention calculations.
