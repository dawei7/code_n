## General

**Attach each player’s install date to every activity row**

The install date is the minimum `event_date` for one `player_id`. The common table expression `T` computes it with `MIN(event_date) OVER (PARTITION BY player_id)`. Unlike a grouped minimum, this window function preserves every activity row while adding the player-level minimum beside it.

This preserved detail is important because the query must later see whether an activity occurred exactly one day after installation. Every row for a player now carries the same `install_dt`, making the difference between that row’s date and the first date directly testable.

**Create one cohort per install date**

The outer query groups `T` by `install_dt` through `GROUP BY 1`, where one refers to the first selected expression. All players whose first login occurred on the same date enter the same cohort.

Because `T` contains one row per activity rather than one row per player, a player with many logins appears several times in the cohort. `COUNT(DISTINCT player_id)` is therefore necessary for `installs`. It counts each player once regardless of later activity frequency.

**Count exact next-day returns**

`DATEDIFF(event_date, install_dt)` gives the number of calendar-day boundaries between an activity row and installation. Comparing it with one yields true only for a login on the immediately following date. In MySQL numeric aggregation, true contributes one and false contributes zero, so:

`SUM(DATEDIFF(event_date, install_dt) = 1)`

counts next-day activity rows.

The composite primary key `(player_id, event_date)` guarantees that one player has at most one activity row on a given date. Therefore, a retained player can contribute at most one true row. The sum is not merely a count of events; under this key it is exactly the number of distinct retained players.

The installation row itself has difference zero and contributes nothing. A return two days later has difference two and also contributes nothing. Device changes and games played never enter the calculation, correctly reflecting the contract.

**Divide by cohort membership and round**

The numerator counts retained players, and `COUNT(DISTINCT player_id)` counts all installed players in the cohort. Their quotient is day-one retention. MySQL’s division operator produces a non-integer result, so a cohort with one retained player out of two yields `0.5` rather than zero.

`ROUND(..., 2)` reports the ratio to two decimal places. Every produced cohort has at least one player because it exists only from activity rows, so the denominator cannot be zero.

The result order is unrestricted, so no `ORDER BY` is required. If `Activity` is empty, the CTE and grouping produce no rows, which is the correct empty result.

**Why the complete query is correct**

The window minimum assigns the true first login to each player. Grouping that value places the player in exactly one install-date cohort. Distinct counting prevents repeated activities from inflating installations, while the exact one-day predicate and primary key make the Boolean sum equal the number of retained cohort members. Dividing those two verified quantities gives the required retention for every cohort.

## Complexity detail

Let $A$ be the number of Activity rows. A typical execution sorts or otherwise partitions rows by `player_id` to compute the window minimum, then groups them by install date. Sort-based implementations take $O(A\log A)$ time, matching the package manifest.

The window stage may retain or materialize $O(A)$ rows, and sorting or grouping can require $O(A)$ working space. The output contains at most $A$ cohorts, so the conservative space bound is $O(A)$.

Database indexes and the optimizer can improve constants or choose different physical operators. The logical result does not depend on whether partitioning and grouping use sorting, hashing, or indexed access.

## Alternatives and edge cases

- **Grouped installs plus self join:** First compute one row per player with `MIN(event_date)`, then left join Activity on the same player and date plus one day. This makes the player-level numerator explicit and avoids relying on the primary key when summing events.
- **Conditional distinct count:** Use `COUNT(DISTINCT CASE WHEN DATEDIFF(...) = 1 THEN player_id END)`. It remains correct even if the source allowed multiple same-day rows per player.
- **Correlated existence check:** For each player’s install row, test whether a next-day row exists. This expresses retention directly but may require careful indexing for performance.
- **Multiple logins after installation:** Only the row exactly one day later contributes; all later rows are false in the Boolean sum.
- **No next-day return:** The numerator is zero, so the rounded ratio is `0.00` numerically.
- **Single-player cohort:** Retention is either zero or one depending on that player’s next-day row.
- **Several players with many activities:** `COUNT(DISTINCT player_id)` ensures each player contributes once to installs.
- **Same-day installation activity:** Its date difference is zero and is not mistaken for retention.
- **Calendar boundaries:** `DATEDIFF` handles month and year changes, so December 31 to January 1 is exactly one day.
- **Composite primary key:** It is what makes the plain Boolean sum safe as a player count. Without date uniqueness, repeated next-day rows could inflate the numerator.
- **Empty table:** No window rows means no grouped cohorts and therefore an empty result.
- **Result casing:** The alias is written `day1_retention` while the displayed contract uses different capitalization. SQL identifiers are normally case-insensitive here, and the semantic column is the same.
