# Number of Times a Driver Was a Passenger

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2238 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/) |

## Problem Description

### Goal

The `Rides` table records rides by unique `ride_id`. Each row names the
`driver_id` of the person who drove that ride and the `passenger_id` of the
person who rode as its passenger. Within one row, the driver and passenger are
different people.

Report every distinct person who appears as a driver in at least one row. For
each such driver, count how many rows list that same person as the passenger.
A driver who never appears in the passenger column must still be included with
a count of zero. The result rows may be returned in any order.

### Function Contract

**Inputs**

- `Rides`: A table with integer columns `ride_id`, `driver_id`, and `passenger_id`.

`ride_id` is unique, and every row satisfies `driver_id != passenger_id`.

**Return value**

Return one row per distinct driver with columns `driver_id` and `cnt`, where
`cnt` is the number of `Rides` rows whose `passenger_id` equals that driver.
Result order is unrestricted.

### Examples

**Example 1**

- Input: `Rides = [[1, 7, 1], [2, 7, 2], [3, 11, 1], [4, 11, 7], [5, 11, 7], [6, 11, 3]]`
- Output: `[[7, 2], [11, 0]]`

**Example 2**

- Input: `Rides = [[1, 4, 9]]`
- Output: `[[4, 0]]`

**Example 3**

- Input: `Rides = [[1, 1, 2], [2, 2, 1]]`
- Output: `[[1, 1], [2, 1]]`
