## Examples

**Example 1**

- **Input:** Sample `Drivers`, `Rides`, and `AcceptedRides` tables for 2020.
- **Output:**
  | month | average_ride_distance | average_ride_duration |
  | --- | --- | --- |
  | 1 | 10.00 | 20.00 |
  | 2 | 0.00 | 0.00 |
  | 3 | 0.00 | 0.00 |
  | 4 | 0.00 | 0.00 |
  | 5 | 0.00 | 0.00 |
  | 6 | 0.00 | 0.00 |
  | 7 | 0.00 | 0.00 |
  | 8 | 0.00 | 0.00 |
  | 9 | 0.00 | 0.00 |
  | 10 | 0.00 | 0.00 |
- **Explanation:** January has distance 30 and duration 60. The 3-month window for month 1 (Jan-Mar) totals 30/3 = 10.00 distance and 60/3 = 20.00 duration.

**Example 2**

- **Input:** January distance 3, February distance 6, March distance 9.
- **Output:**
  | month | average_ride_distance | average_ride_duration |
  | --- | --- | --- |
  | 1 | 6.00 | 0.00 |
- **Explanation:** Window 1 total distance is (3 + 6 + 9) / 3 = 6.00.

**Example 3**

- **Input:** December accepted ride distance 12, duration 24.
- **Output:**
  | month | average_ride_distance | average_ride_duration |
  | --- | --- | --- |
  | 10 | 4.00 | 8.00 |
- **Explanation:** December distance 12 and duration 24 fall in window 10 (Oct-Dec), giving 12/3 = 4.00 distance and 24/3 = 8.00 duration.
