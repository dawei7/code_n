# Cheapest Flights Within K Stops

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 787 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/) |

## Problem Description

### Goal

There are `n` cities numbered from `0` through $n - 1$, with directed flights `[from, to, price]`. Given source city `src`, destination `dst`, and integer `k`, consider routes having at most `k` intermediate stops, equivalently at most $k + 1$ flights.

Return the cheapest total price among all routes satisfying that stop limit. If no permitted route reaches `dst`, return `-1`. Flight direction must be respected, and a cheaper path using too many intermediate cities is not a valid answer.

### Function Contract

**Inputs**

- `n`: the number of cities, numbered from `0` through $n - 1$.
- `flights`: triples `[origin, destination, price]` describing directed flights.
- `src`: the departure city.
- `dst`: the destination city.
- `k`: the maximum number of intermediate cities, so at most $k + 1$ flights may be used.

**Return value**

- The minimum valid route price, or `-1` if the destination cannot be reached within the stop limit.

### Examples

**Example 1**

- Input: `n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1`
- Output: `200`
- Explanation: The route through city `1` uses one stop and is cheaper than the direct flight.

**Example 2**

- Input: `n = 3, flights = [[0,1,2],[1,2,2],[0,2,5]], src = 0, dst = 2, k = 0`
- Output: `5`
- Explanation: With no stops allowed, only the direct flight qualifies.

**Example 3**

- Input: `n = 3, flights = [[0,1,2]], src = 0, dst = 2, k = 1`
- Output: `-1`
- Explanation: No route reaches city `2`.
