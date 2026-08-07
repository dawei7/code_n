## Function Contract

**Input**

- `Activity(player_id, device_id, event_date, games_played)`: login activity uniquely keyed by player and date

**Return value**

- Return one row per player with columns `player_id` and `device_id`, where `device_id` comes from that player's
  minimum `event_date` row. Result order is unrestricted.
