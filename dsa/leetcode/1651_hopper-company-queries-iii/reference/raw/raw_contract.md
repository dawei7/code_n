## Function Contract

**Inputs**

- `Drivers`: Table with columns `driver_id` (int), `join_date` (date).
- `Rides`: Table with columns `ride_id` (int), `user_id` (int), `requested_at` (date).
- `AcceptedRides`: Table with columns `ride_id` (int), `driver_id` (int), `ride_distance` (int), `ride_duration` (int).

**Return value**

Return a table with columns `month` (int from 1 to 10), `average_ride_distance` (decimal rounded to 2 decimal places), and `average_ride_duration` (decimal rounded to 2 decimal places) for each 3-month rolling window in 2020.
