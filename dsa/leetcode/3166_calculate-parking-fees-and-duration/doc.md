# Calculate Parking Fees and Duration

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3166 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-parking-fees-and-duration/) |

## Problem Description

### Goal

The `ParkingTransactions` table records each time a car enters and leaves a parking lot together with the fee paid for that stay. A car may have transactions in several lots, although the data guarantees that one car is never parked in multiple lots at the same time.

Produce one row per car containing its total fee across every parking lot and its average hourly fee, rounded to two decimal places. The average hourly fee is the total fee divided by the car's total parked duration in hours. Also report the parking lot in which that car accumulated the greatest total parked duration across all of its visits.

Return the columns `car_id`, `total_fee_paid`, `avg_hourly_fee`, and `most_time_lot`, with result rows ordered by `car_id` in ascending order.

### Function Contract

**Input table**

- `ParkingTransactions(lot_id, car_id, entry_time, exit_time, fee_paid)`: Each row identifies a lot and car, gives the entry and exit datetimes, and records the decimal fee paid. The composite primary key is `(lot_id, car_id, entry_time)`.

**Return value**

- An ordered table with columns `car_id`, `total_fee_paid`, `avg_hourly_fee`, and `most_time_lot`.

Let $r$ be the number of transaction rows and $c$ the number of distinct cars.

### Examples

**Example 1**

Input `ParkingTransactions`:

| lot_id | car_id | entry_time | exit_time | fee_paid |
|---:|---:|---|---|---:|
| 1 | 1001 | `2023-06-01 08:00:00` | `2023-06-01 10:30:00` | 5.00 |
| 1 | 1001 | `2023-06-02 11:00:00` | `2023-06-02 12:45:00` | 3.00 |
| 2 | 1001 | `2023-06-01 10:45:00` | `2023-06-01 12:00:00` | 6.00 |
| 2 | 1002 | `2023-06-01 09:00:00` | `2023-06-01 11:30:00` | 4.00 |
| 3 | 1001 | `2023-06-03 07:00:00` | `2023-06-03 09:00:00` | 4.00 |
| 3 | 1002 | `2023-06-02 12:00:00` | `2023-06-02 14:00:00` | 2.00 |

Output:

| car_id | total_fee_paid | avg_hourly_fee | most_time_lot |
|---:|---:|---:|---:|
| 1001 | 18.00 | 2.40 | 1 |
| 1002 | 6.00 | 1.33 | 2 |

Car `1001` paid 18.00 over 7.5 hours and spent 4.25 of those hours in lot `1`. Car `1002` paid 6.00 over 4.5 hours and spent more time in lot `2` than in lot `3`.
