# Game Play Analysis III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 534 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/game-play-analysis-iii/) |

## Problem Description
### Goal
The `Activity` table stores one row per unique `(player_id, event_date)` pair, including that day's `games_played`. A player's activity may span several dates, and cumulative totals must be computed independently for each player.

Return `player_id`, `event_date`, and `games_played_so_far` for every activity row, where the cumulative value sums that player's games from their first recorded date through the current date inclusively. Do not mix players or omit zero-game dates. Return the result table in any order while preserving the correct date-bounded total for each row.

### Function Contract
**Inputs**

- `Activity(player_id, device_id, event_date, games_played)`: one row per player and activity date

**Return value**

- A result grid with `player_id`, `event_date`, and `games_played_so_far`, containing one row per activity record

### Examples
**Example 1**

- Input rows: player `1` plays `5` games on `2016-03-01` and `6` on `2016-05-02`
- Output rows: `[1, 2016-03-01, 5]`, `[1, 2016-05-02, 11]`

**Example 2**

- Input row: player `2` plays `1` game on `2017-06-25`
- Output row: `[2, 2017-06-25, 1]`

**Example 3**

- Input rows: player `3` has activities supplied out of date order
- Output: chronological rows whose running totals follow event-date order, not insertion order

### Required Complexity

- **Time:** $O(A \log A)$
- **Space:** $O(A)$

<details>
<summary>Approach</summary>

#### General

**Create an independent timeline for each player**

Partition the rows by `player_id` so activity belonging to one player never contributes to another player's total.

**Order each timeline chronologically**

Within each partition, order by `event_date`. The table contract has at most one activity per player and date, so this order identifies an unambiguous prefix ending at every row.

**Sum the prefix with a window aggregate**

Apply `SUM(games_played)` over the player partition from its first row through the current row and alias it `games_played_so_far`. A window aggregate preserves every input activity row, unlike `GROUP BY`, while adding the cumulative value derived from earlier rows.

**Why every running total is exact**

For an activity row on date `d`, the window frame contains exactly the same player's records whose dates are no later than `d`. Summing their `games_played` values is therefore precisely the requested total through that date. Partitioning prevents cross-player contributions, and chronological ordering prevents later activity from entering the prefix.

#### Complexity detail

For `A` activity rows, a typical window plan sorts rows by player and date in $O(A \log A)$ time and stores ordered partitions in $O(A)$ space. An index or already ordered input may let the database stream the window with less sorting work. The final `ORDER BY` makes local result serialization deterministic.

#### Alternatives and edge cases

- **Correlated prefix subquery:** returns the same totals but may rescan `Activity` for every output row and take $O(A^2)$ work.
- **Self-join on earlier dates plus grouping:** is compatible with older SQL versions but materializes many row pairs and can also become quadratic.
- **Recursive CTE:** can advance through a player's dates, but it is more complex and unnecessary when window functions are available.
- **First activity:** its running total equals its own `games_played` value.
- **Zero games:** preserves the previous cumulative total while still producing an output row.
- **Interleaved players:** remain independent because the window is partitioned.
- **Insertion order:** does not affect the result; `event_date` defines accumulation order.
- **Empty table:** yields an empty result grid.

</details>
