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

### Required Complexity

- **Time:** $O(t \log u)$
- **Space:** $O(u)$

<details>
<summary>Approach</summary>

#### General

**Eligibility depends on both participant rows**

Join `Trips` to `Users` once as the client and once as the driver. Filter both joined rows to `banned = 'No'`, and restrict request dates to the required inclusive range.

**A cancellation indicator turns the rate into an average**

Map `completed` to zero and every cancellation status to one. The average indicator within a date is exactly cancellations divided by eligible trips.

After participant and date filtering, every remaining row represents one eligible trip. Grouping by `request_at` therefore contains precisely the denominator for that day, and summing cancellation indicators gives its numerator.

**Filtering before grouping fixes the denominator**

The client and driver joins attach both ban flags to each trip, so the `WHERE` clause retains exactly trips whose two participants are unbanned and whose date is in range. Each surviving row contributes one to its day's denominator and contributes one to the numerator exactly when its status is cancelled. Averaging the indicator and rounding therefore produces the requested rate for each eligible date group.

#### Complexity detail

With indexed user identifiers, two participant lookups per trip cost $O(t \log u)$ and user indexes occupy $O(u)$ space. Database optimizers may implement equivalent hash joins in expected linear time.

#### Alternatives and edge cases

- **Filter only clients:** incorrectly includes trips driven by banned users.
- **Integer division:** can collapse fractional rates; averaging numeric indicators avoids it.
- Dates without eligible trips do not produce a row, and completed trips contribute zero.

</details>
