## Function Contract

**Input**

- `Activity(player_id, device_id, event_date, games_played)`: login activity uniquely keyed by player and date

**Return value**

- Return one row per activity record with columns `player_id`, `event_date`, and `games_played_so_far`.
  `games_played_so_far` is the sum of that player's `games_played` values on dates no later than the row's
  `event_date`. Result order is unrestricted.
