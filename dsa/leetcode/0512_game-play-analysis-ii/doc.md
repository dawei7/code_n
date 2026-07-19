# Game Play Analysis II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 512 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/game-play-analysis-ii/) |

## Problem Description
### Goal
The `Activity` table records `player_id`, `device_id`, `event_date`, and `games_played`, with at most one activity row for a player on a given date. A player may use different devices on different login dates.

Return one row per player containing `player_id` and the `device_id` from that player's earliest `event_date`. Do not return the device from a later session or aggregate device identifiers. Because the player-date pair is unique, the first login determines one device; return the result rows in any order.

### Function Contract
**Inputs**

- `Activity(player_id, device_id, event_date, games_played)`: one activity record per player and date

**Return value**

- A result grid with columns `player_id` and `device_id`, containing the device from each player's earliest activity row

### Examples
**Example 1**

- Input rows: player `1` uses device `2` on `2016-03-01` and device `3` on `2016-05-02`
- Output row: `[1, 2]`

**Example 2**

- Input rows: player `7` has one activity using device `9`
- Output row: `[7, 9]`

**Example 3**

- Input rows: a later activity is listed before the first chronological activity
- Output: the device attached to the earlier date, not the first inserted row
