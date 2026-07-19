# Game Play Analysis I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 511 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/game-play-analysis-i/) |

## Problem Description
### Goal
The `Activity` table records a player's identifier, device, login date, and games played. A player may have activity on several dates, while the `(player_id, event_date)` pair is unique, so at most one row represents that player on a particular date.

For every player appearing in the table, return columns `player_id` and `first_login`, where `first_login` is that player's earliest recorded `event_date`. Include one row per player and return the result table in any order. Later logins and game counts do not affect the selected date.

### Function Contract
**Inputs**

- `Activity(player_id, device_id, event_date, games_played)`: one activity record per player and date

**Return value**

- A result grid with columns `player_id` and `first_login`, containing one row per player

### Examples
**Example 1**

- Input rows: player `1` appears on `2016-03-01` and `2016-05-02`; player `2` appears on `2017-06-25`
- Output rows: `[1, 2016-03-01]`, `[2, 2017-06-25]`

**Example 2**

- Input rows: player `7` has only one activity on `2024-01-09`
- Output rows: `[7, 2024-01-09]`

**Example 3**

- Input rows: player `3` appears on dates supplied out of chronological order
- Output: the earliest date, independent of input order
