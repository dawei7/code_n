# Trips and Users

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 262 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/trips-and-users/) |

## Problem Description
### Goal
The `Trips` table records trip dates, clients, drivers, and whether each request completed or was cancelled. The `Users` table identifies each user's role and banned status. Consider only trips requested from `2013-10-01` through `2013-10-03` whose client and driver are both unbanned.

For each date having at least one eligible trip, return `Day` and `Cancellation Rate`. The rate is the number of eligible trips cancelled by either client or driver divided by all eligible trips that day, rounded to two decimal places. Exclude any trip involving a banned participant from both numerator and denominator, and return the result table in any order.

### Function Contract
**Inputs**

- `Trips(id, client_id, driver_id, city_id, status, request_at)`: trip requests and outcomes
- `Users(users_id, banned, role)`: user eligibility and role data

**Return value**

Columns `Day` and `Cancellation Rate`, rounded to two decimals, for each qualifying date with at least one eligible trip.

### Examples
**Example 1**

- Eligible daily outcomes: one cancellation among four trips
- Output rate: `0.25`

**Example 2**

- A cancelled trip has a banned client
- Output rate: `0.00` because that trip is excluded

**Example 3**

- Every eligible trip on a date is cancelled
- Output rate: `1.00`
