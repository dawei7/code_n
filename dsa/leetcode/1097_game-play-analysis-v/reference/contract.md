## Function Contract

**Input table**

- `Activity(player_id, device_id, event_date, games_played)`: one row for a player's login on a particular date, with (`player_id`, `event_date`) as the composite primary key.

For each player, let `install_dt` be the minimum `event_date` in that player's activity. The player contributes once to the cohort for that date. A cohort member is retained only if another row for the same `player_id` has an `event_date` exactly one calendar day after `install_dt`; a return two or more days later does not count. The device and the number of games played do not affect either membership or retention.

**Return value**

- `install_dt`: the cohort's common first-login date.
- `installs`: the number of players in that cohort.
- `Day1_retention`: the number of those players with an exact next-day login divided by `installs`, rounded to two decimal places.

Produce one result row per install date. Result order is unrestricted. If `Activity` is empty, the result is empty.
