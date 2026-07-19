# Minimum Cost to Reach Destination in Time

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) |
| Frontend ID | 1928 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A connected country has cities numbered from `0` through `n - 1` and undirected roads. Each road record `[x, y, time]` gives its travel time; multiple roads with different times may connect the same pair. Every time a route passes through a city, its positive passing fee is paid.

Begin in city `0` and reach city `n - 1` in at most `maxTime` minutes. The total cost includes the fees of both the source and destination and every intermediate visit. Return the minimum cost among time-feasible routes, or `-1` if none reaches the destination within the budget.

### Function Contract

**Inputs**

- `maxTime`: the inclusive time budget, with $1 \le \texttt{maxTime} \le 1000$.
- `edges`: undirected roads `[x, y, travel_time]`; parallel roads are allowed.
- `passingFees`: positive fees for $V$ cities, with $2 \le V \le 1000$.
- The number of roads $E$ is between $V-1$ and $1000$.

**Return value**

- Return the minimum sum of paid city fees for a route from `0` to `V - 1` taking at most `maxTime`.
- Return `-1` if no such route exists.

### Examples

**Example 1**

- Input: `maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]`
- Output: `11`

The route `0 -> 1 -> 2 -> 5` uses exactly 30 minutes.

**Example 2**

- Input: the same graph with `maxTime = 29`
- Output: `48`

The cheap route is too slow, so `0 -> 3 -> 4 -> 5` is optimal.

**Example 3**

- Input: the same graph with `maxTime = 25`
- Output: `-1`

### Required Complexity

- **Time:** $O(\texttt{maxTime}\,E)$
- **Space:** $O(\texttt{maxTime}\,V)$

<details>
<summary>Approach</summary>

#### General

**Keep time as part of the state**

A cheapest arrival at one city may have used too much time to finish, while a more expensive but faster arrival can remain useful. A single best cost per city therefore loses necessary information.

Define `cost[t][v]` as the minimum fee of a route that reaches city `v` in exactly `t` minutes. Initialize `cost[0][0]` with the source fee and every other state to infinity.

**Relax from earlier time layers**

Process elapsed times from one through `maxTime`. For every undirected road `(u, v, d)` with `d <= t`, a finite state at `cost[t - d][u]` can reach `v` by paying `passingFees[v]`; the reverse direction is symmetric.

All road times are positive, so every transition comes from a strictly earlier layer that is already final. Induction on `t` shows that each table entry is the cheapest exact-time route: the final edge of any such route supplies one considered predecessor, and every relaxation constructs a legal route with the recorded time and fee.

Take the minimum destination cost over every layer from zero through `maxTime`. If all are infinite, no route meets the budget.

#### Complexity detail

There are `maxTime` layers and each scans all $E$ roads with constant work per direction, giving $O(\texttt{maxTime}\,E)$ time. The table stores $V$ costs for each layer, using $O(\texttt{maxTime}\,V)$ space.

#### Alternatives and edge cases

- **Dijkstra by fee per city only:** Discarding a faster, costlier arrival can make the destination appear unreachable.
- **Dijkstra over `(city, time)`:** This is also correct, using a heap over the expanded state graph.
- **Enumerate all routes:** Cycles and branching make the number of walks exponential.
- **Exact budget:** Arrival at exactly `maxTime` is allowed.
- **Source and destination fees:** Both must be included once when visited.
- **Parallel roads:** Different travel times create distinct transitions and may change feasibility.
- **No feasible route:** Connectedness alone does not guarantee arrival within the time limit.

</details>
