# Power Grid Maintenance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3607 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Depth-First Search, Breadth-First Search, Union-Find, Graph Theory, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/power-grid-maintenance/) |

## Problem Description

### Goal

There are `c` power stations numbered from $1$ through $c$. Each pair in `connections` is a bidirectional cable, and stations joined directly or indirectly belong to the same power grid. Every station begins online.

Process two kinds of query in order. A query `[2, x]` takes station `x` offline. A query `[1, x]` requests a maintenance check: if `x` is online, it handles the request itself; otherwise, the online station with the smallest identifier in `x`'s grid handles it. If that grid has no online station, the result is `-1`.

An offline station remains part of its original grid. Outages change operational state only; they never remove vertices or cables and therefore never split a connected component. Return the result of every type-1 query in its original order.

### Function Contract

**Inputs**

- `c`: The number of stations, identified from $1$ through $c$.
- `connections`: The bidirectional cables, each represented as `[u, v]`.
- `queries`: The ordered maintenance checks `[1, x]` and outage operations `[2, x]`.

The constraints are $1 \le c \le 10^5$, at most $10^5$ connections, and between $1$ and $2 \cdot 10^5$ queries. Every referenced station identifier is valid.

**Return value**

Return one integer for each type-1 query: either the station that resolves the check or `-1` when no station in the relevant grid is online.

### Examples

#### Example 1

- **Input:** `c = 5, connections = [[1, 2], [2, 3], [3, 4], [4, 5]], queries = [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]`
- **Output:** `[3, 2, 3]`
- **Explanation:** Station 3 initially answers for itself. After stations 1 and then 2 go offline, their checks are handled by the smallest remaining online identifiers 2 and 3.

#### Example 2

- **Input:** `c = 3, connections = [], queries = [[1, 1], [2, 1], [1, 1]]`
- **Output:** `[1, -1]`
- **Explanation:** Each station is an isolated grid, so station 1 has no substitute after its outage.
