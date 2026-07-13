# Game Play Analysis IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 550 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/game-play-analysis-iv/) |

## Problem Description
### Goal
The `Activity` table records unique `(player_id, event_date)` rows for game logins. For each player, identify their earliest login date and determine whether that same player also has an activity row on the immediately following calendar day.

Return one column named `fraction`: the number of players who logged in on that next day divided by the total number of distinct players, rounded to two decimal places. Count each player at most once, ignore activity on later nonconsecutive dates, and use all players in the denominator even when they never return.

### Function Contract
**Inputs**

- `Activity(player_id, device_id, event_date, games_played)`: one row per player and activity date

**Return value**

- A one-row result grid with column `fraction`

### Examples
**Example 1**

- Input: three players, only player `1` returns one day after their first login
- Output: `0.33`

**Example 2**

- Input: every player has activity on the day after their first login
- Output: `1.00`

**Example 3**

- Input: no player returns on the day after their first login
- Output: `0.00`

### Required Complexity

- **Time:** $O(A \log A)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Find one first date per player**

Group `Activity` by `player_id` and compute `MIN(event_date)`. The resulting common table expression has exactly one row for each of the `P` players.

**Join only the required return date**

Left-join each first-login row back to `Activity` for the same player and the date exactly one calendar day later. A successful join means that player satisfies the retention condition; later returns do not count.

**Aggregate matched players into a fraction**

Count joined activity rows for the numerator and all first-login rows for the denominator. Multiplying by a floating-point value before division preserves the fractional result, and `ROUND(..., 2)` produces the requested precision.

**Why every player is counted correctly**

The grouped date is the unique earliest activity date for its player. Because the join requires both the same player and exactly the next calendar date, it matches if and only if that player returned on the required day. The table key permits at most one activity per player and date, so each player contributes either zero or one to the numerator and exactly one to the denominator.

#### Complexity detail

For `A` activity rows, grouping typically sorts or hashes the rows in $O(A \log A)$ time, and the join can use the player-date key to probe once per player. The first-login relation stores $O(P)$ rows for `P` players. An appropriate index may allow near-linear execution.

#### Alternatives and edge cases

- **Correlated first-date subqueries:** can express the same condition but may rescan `Activity` for every player and degrade toward $O(A^2)$.
- **Window functions:** `MIN(event_date) OVER (PARTITION BY player_id)` can label first dates, but it retains duplicate player rows and needs another distinct aggregation step.
- **Self-join every activity pair:** can find next-day pairs but must still ensure the earlier row is the player's first and may materialize many irrelevant pairs.
- **Return after a gap:** activity two or more days later does not qualify.
- **Several later sessions:** still contribute only one player to the denominator and at most one to the numerator.
- **Month or year boundary:** calendar-date arithmetic, not integer manipulation of the date text, identifies the next day.
- **Insertion order:** does not affect `MIN(event_date)`.
- **Rounding:** the final ratio, rather than the individual counts, is rounded to two decimal places.

</details>
