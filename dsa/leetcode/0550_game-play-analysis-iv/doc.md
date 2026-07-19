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
