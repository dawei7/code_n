# Design Underground System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1396 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/design-underground-system/) |

## Problem Description

### Goal

Design a system that tracks passengers traveling through an underground network. `checkIn(id, stationName, t)` records that passenger `id` entered at a station and time. `checkOut(id, stationName, t)` completes that passenger's current trip at another station and later time.

`getAverageTime(startStation, endStation)` must return the average duration of every completed trip whose start and end stations match that ordered route. Calls are valid: a passenger cannot check in twice without checking out, a checkout corresponds to an active check-in, and an average is requested only after that route has at least one completed trip. A passenger may make another trip after checking out.

### Function Contract

**Inputs**

- `operations`: $q$ valid calls to `checkIn`, `checkOut`, and `getAverageTime`, with at most $2 \times 10^4$ calls in total.
- Passenger identifiers are positive integers; station names are nonempty strings; times are positive and increase across calls.

Let $A$ be the maximum number of simultaneously active passengers and $R$ the number of distinct completed ordered routes.

**Return value**

- One output per operation: no value for check-ins and checkouts, and the current route average for each `getAverageTime` call.

### Examples

**Example 1**

- Input: check in passenger `1` at `"A"` at time `3`, check out at `"B"` at time `13`, then query `("A", "B")`.
- Output: `[null,null,10.0]`

**Example 2**

- Input: complete route `"A"` to `"B"` in `10` and then in `20` time units, querying afterward.
- Output: average `15.0`.

**Example 3**

- Input: complete trips on routes `"A"` to `"B"` and `"B"` to `"A"`.
- Output: each ordered route has its own average.

### Required Complexity

- **Time:** $O(q)$
- **Space:** $O(A + R)$

<details>
<summary>Approach</summary>

#### General

Maintain one hash table from active passenger ID to `(start_station, start_time)`. A check-in inserts or replaces that passenger's active record. A checkout removes the record, subtracts its start time from the checkout time, and identifies the ordered route `(start_station, end_station)`.

Maintain a second hash table from each completed route to two sufficient statistics: total duration and trip count. Add the new duration and increment the count at checkout. An average query divides those two stored values.

Each completed trip enters exactly one ordered route accumulator with its true elapsed time. The accumulator's total is therefore the sum of all and only the route's durations, and its count is the corresponding number of trips. Their quotient is the requested average. Removing an active check-in on checkout also allows the same passenger ID to begin a later independent trip.

#### Complexity detail

With expected constant-time hash operations, all $q$ calls take $O(q)$ total time. The active table holds at most $A$ passengers and the aggregate table holds $R$ routes, using $O(A + R)$ space.

#### Alternatives and edge cases

- **Store every trip duration:** Keeping a list per route is correct, but re-summing that list for every query can make repeated averages quadratic in the trip count.
- **Store a precomputed average:** Updating only an average risks accumulated floating-point error; integer total and count preserve exact source data until division.
- **Ordered routes:** `("A", "B")` and `("B", "A")` are distinct keys.
- **Repeated passenger:** An ID may travel again after checkout, so its previous active record must be removed.
- **Interleaved passengers:** Active trips may overlap and must remain associated with their own IDs.
- **Changing average:** Every later checkout on a route must affect subsequent queries immediately.

</details>
