# Minimum Cost to Reach Destination in Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1928 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Graph Theory |
| Official Link | [minimum-cost-to-reach-destination-in-time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) |

## Problem Description & Examples
### Goal
Travel from city `0` to city `n - 1` through weighted edges, paying each visited city's fee, while total travel time stays within `maxTime`. Minimize total fee.

### Function Contract
**Inputs**

- `maxTime`: the time budget.
- `edges`: undirected edges `[u, v, time]`.
- `passingFees`: fee for entering each city.

**Return value**

Return the minimum fee to reach the destination within time, or `-1` if impossible.

### Examples
**Example 1**

- Input: `maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]`
- Output: `11`

**Example 2**

- Input: `maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]`
- Output: `48`

**Example 3**

- Input: `maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
Use Dijkstra-like search over `(cost, time, city)` states or DP over time. Keep the best known cost for each city at each elapsed time, and relax edges only when the new time is at most `maxTime`. A priority queue by cost lets the first destination pop be optimal.

---

## Complexity Analysis
- **Time Complexity**: `O(maxTime * E log(maxTime * V))`
- **Space Complexity**: `O(maxTime * V)`
