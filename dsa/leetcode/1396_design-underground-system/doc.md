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
