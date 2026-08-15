# The Number of Passengers in Each Bus I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2142 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [the-number-of-passengers-in-each-bus-i](https://leetcode.com/problems/the-number-of-passengers-in-each-bus-i/) |

## Problem Description

### Goal

The `Buses` table records each bus's unique `bus_id` and `arrival_time` at a
station. Bus arrival times are also unique. The `Passengers` table records each
passenger's unique `passenger_id` and arrival time.

When a bus arrives at time $t_b$, every passenger who arrived at time $t_p$
with $t_p \leq t_b$ and has not already taken an earlier bus boards this bus.
Thus each passenger uses the first bus whose arrival is not earlier than the
passenger's arrival; passengers arriving after the final bus use none.

Report every bus together with the number of passengers who use it. Order the
result by `bus_id` in ascending order.

### Function Contract

**Inputs**

- `Buses(bus_id, arrival_time)`: One row per bus. `bus_id` is unique, and no
  two buses share an arrival time.
- `Passengers(passenger_id, arrival_time)`: One row per passenger, with a
  unique `passenger_id`.

**Return value**

Return a table with columns `bus_id` and `passengers_cnt`, containing one row
for every bus, including buses boarded by zero passengers. Sort rows by
`bus_id` in ascending order.

### Examples

#### Example 1

- **Input:** 
  - `Buses = [(1,2),(2,4),(3,7)]`
  - `Passengers = [(11,1),(12,5),(13,6),(14,7)]`
- **Output:** `[(1,1),(2,0),(3,3)]`
- **Explanation:** Passenger `11` takes the bus at time `2`. No waiting passenger
  exists at time `4`. The remaining three passengers, including the one
  arriving exactly at time `7`, take the final bus.
