## Examples

**Example 1**

- **Input:**

`Drivers` table:

| driver_id | join_date |
| --- | --- |
| 10 | 2019-12-10 |
| 8 | 2020-01-13 |
| 5 | 2020-02-16 |
| 7 | 2020-02-20 |
| 4 | 2020-03-04 |
| 1 | 2020-10-24 |
| 6 | 2020-01-05 |

`Rides` table:

| ride_id | user_id | requested_at |
| --- | --- | --- |
| 6 | 75 | 2019-12-09 |
| 1 | 54 | 2020-02-09 |
| 10 | 63 | 2020-03-04 |
| 19 | 39 | 2020-04-06 |
| 3 | 41 | 2020-06-03 |
| 13 | 52 | 2020-06-22 |
| 7 | 69 | 2020-07-16 |
| 17 | 70 | 2020-08-25 |
| 20 | 81 | 2020-09-25 |
| 5 | 57 | 2020-11-09 |
| 2 | 42 | 2020-12-09 |
| 11 | 68 | 2020-12-26 |
| 15 | 76 | 2020-12-28 |

`AcceptedRides` table:

| ride_id | driver_id | ride_distance | ride_duration |
| --- | --- | --- | --- |
| 10 | 10 | 82 | 53 |
| 13 | 10 | 96 | 56 |
| 7 | 8 | 114 | 16 |
| 17 | 8 | 143 | 43 |
| 2 | 10 | 131 | 60 |
| 11 | 8 | 37 | 43 |
| 15 | 8 | 108 | 82 |

- **Output:**

| month | active_drivers | accepted_rides |
| --- | --- | --- |
| 1 | 2 | 0 |
| 2 | 3 | 0 |
| 3 | 4 | 1 |
| 4 | 4 | 0 |
| 5 | 5 | 0 |
| 6 | 5 | 1 |
| 7 | 5 | 1 |
| 8 | 5 | 1 |
| 9 | 5 | 0 |
| 10 | 6 | 0 |
| 11 | 6 | 2 |
| 12 | 6 | 1 |

- **Explanation:**
  - By end of January 2020, drivers 10 and 6 joined (2 active drivers). Accepted rides in January: 0.
  - By end of February 2020, drivers 10, 6, 8, 5, 7 joined (3 active drivers by Feb end: 10, 6, 8... 5 and 7 joined in Feb). Accepted rides: 0.
  - By end of March 2020, driver 4 joined (4 active drivers). Accepted ride 10 requested in March (1 accepted ride).
