## Activity Table

| Column Name | Type |
|---|---|
| `player_id` | int |
| `device_id` | int |
| `event_date` | date |
| `games_played` | int |

The pair (`player_id`, `event_date`) is the primary key, so a player has at most one activity row on any date. Each row records that a player logged in on `event_date`, used `device_id`, played `games_played` games, and then logged out. A login with zero games played is still an activity row.
