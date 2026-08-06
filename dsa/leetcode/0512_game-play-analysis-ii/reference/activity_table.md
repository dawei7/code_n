## Activity Table

| Column | Type |
|---|---|
| `player_id` | integer |
| `device_id` | integer |
| `event_date` | date |
| `games_played` | integer |

The composite primary key is `(player_id, event_date)`, so a player has at most one activity record on a given date.
Each row records a login made from one device and the number of games played before logout; that count may be zero.
