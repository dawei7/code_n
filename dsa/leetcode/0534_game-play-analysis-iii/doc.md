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
