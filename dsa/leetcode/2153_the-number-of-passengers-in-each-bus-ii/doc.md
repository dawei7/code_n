# The Number of Passengers in Each Bus II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2153 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [the-number-of-passengers-in-each-bus-ii](https://leetcode.com/problems/the-number-of-passengers-in-each-bus-ii/) |

## Problem Description

### Goal

The `Buses` table records each bus's unique identifier, distinct arrival time,
and positive passenger capacity. The `Passengers` table records each
passenger's unique identifier and arrival time.

At a bus arrival time $t_b$, passengers who arrived at times $t_p \leq t_b$
and have not boarded an earlier bus are waiting. At most the bus's `capacity`
of those passengers board; any excess remains for later buses. Report how many
passengers use every bus, including buses that take nobody, and order the
result by `bus_id` in ascending order.

### Function Contract

**Inputs**

- `Buses(bus_id, arrival_time, capacity)`: One row per bus. Identifiers and
  arrival times are unique, and every capacity is positive.
- `Passengers(passenger_id, arrival_time)`: One row per passenger, with a
  unique identifier.

**Return value**

Return a table with columns `bus_id` and `passengers_cnt`, one row per bus,
ordered by `bus_id` ascending.

### Examples

#### Example 1

- **Input:** 
  - `Buses = [(1,2,1),(2,4,10),(3,7,2)]`
  - `Passengers = [(11,1),(12,1),(13,5),(14,6),(15,7)]`
- **Output:** `[(1,1),(2,1),(3,2)]`
- **Explanation:** The first bus takes one of the two waiting passengers. The
  second takes the remaining passenger. Three passengers are waiting by time
  `7`, but the final bus can take only two.
