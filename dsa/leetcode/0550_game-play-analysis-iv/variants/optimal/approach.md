## General
**Find one first date per player**

Group `Activity` by `player_id` and compute `MIN(event_date)`. The resulting common table expression has exactly one row for each of the `P` players.

**Join only the required return date**

Left-join each first-login row back to `Activity` for the same player and the date exactly one calendar day later. A successful join means that player satisfies the retention condition; later returns do not count.

**Aggregate matched players into a fraction**

Count joined activity rows for the numerator and all first-login rows for the denominator. Multiplying by a floating-point value before division preserves the fractional result, and `ROUND(..., 2)` produces the requested precision.

**Why every player is counted correctly**

The grouped date is the unique earliest activity date for its player. Because the join requires both the same player and exactly the next calendar date, it matches if and only if that player returned on the required day. The table key permits at most one activity per player and date, so each player contributes either zero or one to the numerator and exactly one to the denominator.

## Complexity detail
For `A` activity rows, grouping typically sorts or hashes the rows in $O(A \log A)$ time, and the join can use the player-date key to probe once per player. The first-login relation stores $O(P)$ rows for `P` players. An appropriate index may allow near-linear execution.

## Alternatives and edge cases
- **Correlated first-date subqueries:** can express the same condition but may rescan `Activity` for every player and degrade toward $O(A^2)$.
- **Window functions:** `MIN(event_date) OVER (PARTITION BY player_id)` can label first dates, but it retains duplicate player rows and needs another distinct aggregation step.
- **Self-join every activity pair:** can find next-day pairs but must still ensure the earlier row is the player's first and may materialize many irrelevant pairs.
- **Return after a gap:** activity two or more days later does not qualify.
- **Several later sessions:** still contribute only one player to the denominator and at most one to the numerator.
- **Month or year boundary:** calendar-date arithmetic, not integer manipulation of the date text, identifies the next day.
- **Insertion order:** does not affect `MIN(event_date)`.
- **Rounding:** the final ratio, rather than the individual counts, is rounded to two decimal places.
