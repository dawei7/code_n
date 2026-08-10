## General

The result needs one output row for every activity date, together with the player's cumulative number of games through that date. This is a running-sum problem, which SQL window functions express directly.

The query keeps `player_id` and `event_date` from each source row and computes:

`SUM(games_played) OVER (...)`.

Unlike ordinary aggregation with `GROUP BY`, a window aggregate does not collapse many input rows into one row. It calculates a value over a related set of rows while preserving the current activity row. That is essential because the output needs every player-date combination, not one total per player.

**Separate each player's history.** The window clause begins:

`PARTITION BY player_id`.

Partitioning divides the activity rows into independent logical groups. A row for player one can contribute only to running totals for player one; it can never affect player three.

Each partition starts its own cumulative sum. No explicit reset variable is required because the database window engine applies the aggregate separately to each partition.

**Put a player's events in chronological order.** Inside each partition:

`ORDER BY event_date`

orders rows from earlier dates to later dates. A running total depends on this order: at one event date, the answer must include that date and all prior dates, but not later activity.

The table's composite primary key `(player_id, event_date)` guarantees at most one source row for a player on a particular date. Therefore the chronological position is unambiguous, and default peer-group behavior for equal ordering values cannot combine multiple same-day rows for one player.

**Apply the cumulative sum.** At a player's first date, the window contains that first row and returns its `games_played` value. At the next date, it includes the first and second values. This continues until the final date, whose running total equals that player's complete games sum.

For player one with daily values five, six, and one, chronological window results are five, eleven, and twelve. Player three begins an independent partition with zero and later reaches five.

The alias:

`AS games_played_so_far`

gives the computed column the exact required name. The other two selected expressions already have the required names.

**Why the current date is included.** The running total is “until that date,” which includes games played on that date. A standard ordered cumulative `SUM` includes the current row. No one-row offset or `LAG` is needed.

**Why future dates are excluded.** In an ordered window, the cumulative frame extends from the partition start through the current ordering position. Later rows fall after the current row and do not contribute yet.

MySQL's default frame for an aggregate window with `ORDER BY` is based on the partition start through the current ordering value. Because `event_date` is unique within each player partition, it has the same result here as an explicit:

`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.

Stating the frame explicitly could make intent clearer, but the exact source query is correct under the schema guarantee.

**Why one scan-shaped expression is enough.** A correlated subquery could sum earlier rows separately for every activity row, repeating historical work. A self-join could materialize every earlier/current pair and then group it. The window operation lets the query engine order each player's rows once and carry the sum forward.

Correctness can be viewed row by row. Fix an output row for player `p` at date `d`. Partitioning excludes all other players. Chronological ordering and the cumulative frame include exactly rows for `p` whose dates are no later than `d`. `SUM` adds their `games_played` values, which is precisely the requested total. Since the window preserves every source activity row, this reasoning holds for all required player-date outputs.

The query has no final `ORDER BY` outside the window. The window's internal ordering defines calculation order, not guaranteed presentation order. The contract permits result rows in any order, so no final sort is necessary.

The source comment is inert SQL commentary. The executable statement begins with `SELECT` and reads only the `Activity` table.

## Complexity detail

Let $A$ be the number of activity rows. A typical execution partitions and orders rows by player and date. Without a supporting order, sorting can take $O(A\log A)$ time and the window/result processing adds $O(A)$, giving the manifest's $O(A\log A)$ bound.

The engine may use $O(A)$ memory or temporary storage for sorting and window execution, matching the manifest's $O(A)$ space description. A suitable index beginning with `player_id, event_date` may allow an ordered scan and reduce sorting work, but physical cost depends on the optimizer and storage engine.

The result itself has $A$ rows because the primary key provides one activity row per player-date and the window does not collapse rows.

## Alternatives and edge cases

- **Correlated cumulative subquery:** It is logically direct but may rescan one player's history for every date and become quadratic.
- **Non-equi self-join:** Join earlier rows to each current row and aggregate them. It works but can create a much larger intermediate relation.
- **Ordinary `GROUP BY player_id`:** It returns only one total per player and loses the required per-date history.
- **Window without partitioning:** It would mix games from different players.
- **Window without date ordering:** It would compute a partition total or an undefined running sequence rather than chronological progress.
- **Player with one event:** The running total is simply that row's `games_played`.
- **Zero games on a date:** The row remains in the output and carries forward the prior total.
- **Different players with interleaved calendar dates:** Partitioning keeps their totals independent even if physical rows are interleaved.
- **Unique player-date key:** It removes ambiguity among equal-date peers within one partition.
- **Output order:** The problem accepts any order; internal window ordering does not promise final row presentation.
- **Current-row inclusion:** The default cumulative frame includes the event's own games, matching “through that date.”
