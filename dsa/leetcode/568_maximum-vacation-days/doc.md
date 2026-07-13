# Maximum Vacation Days

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 568 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-vacation-days/) |

## Problem Description
### Goal
You begin in city `0` on Monday of week `0` and have a fixed number of weeks available for travel. At the start of each week, you may remain in your current city or take one directed flight that exists in `flights`; taking that flight consumes no vacation days. You then receive the vacation allowance recorded for the city where you spend that week.

Choose the weekly sequence of stays and flights that maximizes the total vacation days collected from `days`. A city that cannot be reached from your current location at that week's start is not a valid choice, and future connectivity may make a smaller immediate allowance part of the optimal schedule.

### Function Contract
**Inputs**

- `flights`: a square matrix where `flights[i][j] = 1` permits travel from city `i` to city `j`
- `days`: a matrix where `days[i][w]` is the vacation allowance in city `i` during week `w`

**Return value**

- The maximum total vacation days achievable

### Examples
**Example 1**

- Input: `flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]`
- Output: `12`

**Example 2**

- Input: no flights and weekly allowances `[[1,1,1],[7,7,7],[7,7,7]]`
- Output: `3`

**Example 3**

- Input: all intercity flights and allowances `[[7,0,0],[0,7,0],[0,0,7]]`
- Output: `21`

### Required Complexity

- **Time:** $O(kn^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Record the best total for each current city**

Let `dp[city]` be the maximum vacation days after all weeks processed so far when the traveler is in that city. Initially only city `0` is reachable, with total zero.

**Choose travel before collecting each week**

For every reachable origin, try every destination. The transition is legal when origin equals destination, because staying never requires a flight, or when the directed flight matrix contains an edge. Add `days[destination][week]` to the origin total.

**Keep only the best route to each destination**

Several origins may reach the same destination for the week. Store their maximum in a fresh array; future choices depend only on the city and accumulated total, not the earlier route.

**Why discarding smaller totals is safe**

Two schedules that finish the same week in the same city have identical travel options and future allowances. The one with fewer accumulated days can never overtake the larger one under identical future decisions, so only the maximum is needed. Inductively, every DP entry is the best feasible schedule ending in that city, and the maximum after the final week is globally optimal.

#### Complexity detail

For each of `k` weeks, the algorithm checks all $n^{2}$ origin-destination pairs, giving $O(kn^2)$ time. The current and next city totals use $O(n)$ space.

#### Alternatives and edge cases

- **Top-down memoization:** uses states `(week, city)` with the same $O(kn^2)$ time and $O(kn)$ cache space.
- **Enumerate every itinerary:** is correct but branches by possible destinations each week and is exponential in `k`.
- **No outgoing flight:** the traveler can always remain in the current city.
- **Directed flights:** `flights[i][j]` does not imply `flights[j][i]`.
- **Unreachable city:** must retain negative-infinity state rather than an artificial zero total.
- **Travel timing:** a flight is chosen before that week's vacation allowance is collected.
- **Single city:** the answer is the sum of its weekly allowances.

</details>
