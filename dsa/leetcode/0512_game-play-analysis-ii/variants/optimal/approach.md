## General

The first-login device cannot be obtained by applying `MIN` directly to `device_id`. The smallest device number is unrelated to chronological order. The query therefore solves the problem in two logical stages:

1. compute each player's earliest `event_date`;
2. use the pair `(player_id, earliest_date)` to retrieve the original activity row containing the associated `device_id`.

**Build one identifying tuple per player.** The subquery

`SELECT player_id, MIN(event_date) AS event_date FROM Activity GROUP BY 1`

groups rows by the first selected expression, `player_id`. For every player, it returns a two-column row consisting of that player ID and the minimum login date.

For the example, the subquery result is conceptually:

- `(1, 2016-03-01)`;
- `(2, 2017-06-25)`;
- `(3, 2016-03-02)`.

The alias on the aggregate is not essential to row-value `IN` comparison, which compares by column position, but it clearly describes the second returned field.

**Match both columns together.** The outer predicate is

`(player_id, event_date) IN (subquery)`.

This is a MySQL row-constructor comparison. An outer activity row passes when its two-column tuple exactly equals one of the two-column tuples returned by the subquery.

Matching only `event_date` would be wrong. Two different players can have the same calendar date, and a player's activity could accidentally match another player's first date. Including `player_id` ties each minimum date to the correct player.

Matching only `player_id` would also be insufficient because it would retain every activity row for that player rather than only the first.

**Why exactly one source row survives per player.** `(player_id, event_date)` is the table's primary key. The subquery returns one minimum date per player, and the primary key guarantees that at most one original row has that player-date pair. Because the minimum came from an actual row in that player's group, at least one matching row exists. Thus exactly one row survives for each player.

The outer `SELECT` projects only `player_id` and `device_id` from that unique first-login activity row. `event_date` was necessary to identify the correct row but is not part of the requested output. `games_played` is neither an identification field nor an output field.

For player three, the minimum tuple is `(3, 2016-03-02)`. The outer table row with that tuple has device one, so the query returns `(3, 1)` rather than device four from the later 2018 activity.

**Logical join interpretation.** Although written with `IN`, the operation behaves like a semijoin between `Activity` and the per-player minimum table on both `player_id` and `event_date`. The manifest describes it as aggregating and joining back, which is exactly the relational logic. MySQL's optimizer may physically implement the subquery through a materialized set, semijoin, index lookups, or another equivalent plan.

The query omits `ORDER BY` because result order is unrestricted. It also needs no `DISTINCT`: primary-key uniqueness already proves one selected row per player.

Correctness follows from the two stages. Grouped `MIN` identifies the earliest date for each player. Tuple membership retains precisely the original row with that player and date. The primary key makes the associated device unique. Projecting the player and device therefore returns exactly the first-login device for every player.

## Complexity detail

Let $A$ be the number of activity rows and $P$ the number of distinct players. A hash aggregation can compute the $P$ minimum-date tuples in $O(A)$ expected time and $O(P)$ state. With an efficient semijoin or the composite primary-key index, matching source rows can be linear in the scan or near $O(P\log A)$ through lookups. The manifest summarizes the intended optimized execution as $O(A)$ time and $O(P)$ auxiliary state.

Physical SQL cost is optimizer-dependent. A sort-based group can require $O(A\log A)$ comparison work, and a poorly optimized correlated execution would differ. The composite key is particularly helpful because it matches the exact tuple used to retrieve rows.

## Alternatives and edge cases

- **CTE plus inner join:** Materialize `player_id, MIN(event_date)` and join on both columns. It expresses the same relational plan and is more portable than row-value `IN` in some systems.
- **`ROW_NUMBER` window function:** Partition by player, order by date, and select row one. This directly keeps the associated device but requires window support.
- **`FIRST_VALUE(device_id)`:** Compute the first device in each ordered player partition and apply `DISTINCT`. It works but can be less transparent about row reduction.
- **Aggregate `MIN(device_id)`:** This is incorrect because numeric device order is unrelated to login time.
- **Same date across different players:** Composite tuple matching keeps identities separate.
- **Multiple dates for one player:** Only the minimum-date tuple matches.
- **Primary-key guarantee:** It ensures one device row for a player's earliest date, so no tie-breaking is needed.
- **Any output order:** No final sort is required.
- **MySQL row constructors:** The exact syntax is supported by MySQL; a join is the portability fallback.
- **Keep the device attached to its row:** Aggregating `MIN(device_id)` beside `MIN(event_date)` could combine values from different activity rows. Matching the composite tuple retrieves the device recorded on the actual first-login row.
