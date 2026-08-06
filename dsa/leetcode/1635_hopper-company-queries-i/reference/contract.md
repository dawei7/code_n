## Function Contract

**Inputs**

- `Drivers`: Table containing `driver_id` and `join_date`.
- `Rides`: Table containing `ride_id`, `user_id`, and `requested_at`.
- `AcceptedRides`: Table containing `ride_id`, `driver_id`, `ride_distance`, and `ride_duration`.

**Return value**

Return a table with columns `month`, `active_drivers`, and `accepted_rides` for each month of 2020 (1 through 12) ordered by `month` ascending.
