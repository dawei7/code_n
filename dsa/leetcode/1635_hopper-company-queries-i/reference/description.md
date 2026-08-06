## Description

Table: `Drivers`

| Column Name | Type |
| --- | --- |
| `driver_id` | `int` |
| `join_date` | `date` |

`driver_id` is the primary key (column with unique values) for this table.
Each row of this table contains the driver's ID and the date they joined the Hopper company.

Table: `Rides`

| Column Name | Type |
| --- | --- |
| `ride_id` | `int` |
| `user_id` | `int` |
| `requested_at` | `date` |

`ride_id` is the primary key (column with unique values) for this table.
Each row of this table contains the ID of a ride, the user's ID that requested it, and the day they requested it.
There may be some ride requests in this table that were not accepted.

Table: `AcceptedRides`

| Column Name | Type |
| --- | --- |
| `ride_id` | `int` |
| `driver_id` | `int` |
| `ride_distance` | `int` |
| `ride_duration` | `int` |

`ride_id` is the primary key (column with unique values) for this table.
Each row of this table contains some information about an accepted ride.
It is guaranteed that each accepted ride exists in the `Rides` table.

Write a solution to report the following statistics for each month of **2020**:

- The number of drivers currently with the Hopper company by the end of the month (`active_drivers`).
- The number of accepted rides in that month (`accepted_rides`).

Return the result table ordered by `month` in ascending order, where `month` is the month's number (January is `1`, February is `2`, etc.).
