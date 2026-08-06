## Description

The `ParkingTransactions` table records each time a car enters and leaves a parking lot together with the fee paid for that stay. A car may have transactions in several lots, although the data guarantees that one car is never parked in multiple lots at the same time.

Produce one row per car containing its total fee across every parking lot and its average hourly fee, rounded to two decimal places. The average hourly fee is the total fee divided by the car's total parked duration in hours. Also report the parking lot in which that car accumulated the greatest total parked duration across all of its visits.

Return the columns `car_id`, `total_fee_paid`, `avg_hourly_fee`, and `most_time_lot`, with result rows ordered by `car_id` in ascending order.
