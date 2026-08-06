## Constraints

- `driver_id` is the primary key for `Drivers`.
- `ride_id` is the primary key for `Rides`.
- `ride_id` is the primary key for `AcceptedRides`.
- Every `ride_id` in `AcceptedRides` exists in `Rides`.
