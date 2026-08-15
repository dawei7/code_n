# Status of Flight Tickets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2793 |
| Difficulty | Hard |
| Category | Database |
| Topics | Uncategorized |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/status-of-flight-tickets/) |

## Problem Description

### Goal

The `Flights` table records each flight's seat capacity. The `Passengers` table records which flight each passenger requested and the distinct time at which that passenger booked.

For a particular flight, bookings are handled from earliest to latest. A passenger is `Confirmed` when their position in that flight's booking order does not exceed its capacity; every later booking is placed on the `Waitlist`. Determine the current status of every passenger and return the rows ordered by `passenger_id` in ascending order.

### Function Contract

**Tables**

- `Flights(flight_id, capacity)`: `flight_id` is unique; each row gives one flight and its number of available seats.
- `Passengers(passenger_id, flight_id, booking_time)`: `passenger_id` and `booking_time` are unique; each row associates a passenger with a requested flight and booking timestamp.

**Return value**

Return two columns:

- `passenger_id`: The passenger's identifier.
- `Status`: `Confirmed` if the passenger is among the first `capacity` bookings for their flight, otherwise `Waitlist`.

Sort the result by `passenger_id` ascending.

### Examples

#### Example 1

Given flights with capacities `(1, 2)`, `(2, 2)`, and `(3, 1)`, rank each passenger only against bookings for the same flight. Passenger 103 booked flight 1 before passengers 101 and 102, so 103 and 101 are confirmed while 102 is waitlisted. Flight 2 confirms both requests, and flight 3 confirms only its earlier request from passenger 107.

The ordered result is:

| passenger_id | Status |
|---:|---|
| 101 | Confirmed |
| 102 | Waitlist |
| 103 | Confirmed |
| 104 | Confirmed |
| 105 | Confirmed |
| 106 | Waitlist |
| 107 | Confirmed |

#### Example 2

For one flight of capacity $1$ with passengers 20, 30, and 10 booking in that chronological order, only passenger 20 is confirmed. The output is still ordered by identifier: passenger 10 is waitlisted, passenger 20 is confirmed, and passenger 30 is waitlisted.
