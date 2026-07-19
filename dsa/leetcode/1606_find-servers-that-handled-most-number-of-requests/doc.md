# Find Servers That Handled Most Number of Requests

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1606 |
| Difficulty | Hard |
| Topics | Array, Heap (Priority Queue), Simulation, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/) |

## Problem Description
### Goal
There are `k` servers numbered from 0 through `k - 1`. A server can process at most one request at a time, although different servers operate concurrently. Request $i$ arrives at the strictly increasing time `arrival[i]` and occupies its assigned server for `load[i]` time units.

Assignment starts at server $i \bmod k$. If that server is busy, inspect later server IDs in circular order, wrapping from `k - 1` to 0, and use the first available server. Drop the request when every server is busy. A server finishing exactly at the new request's arrival time is already available for that request.

Return the IDs of all servers that successfully handled the maximum number of requests. The result may list tied IDs in any order.

### Function Contract
**Inputs**

- `k`: the number of servers, with $1 \le k \le 10^5$.
- `arrival`: a strictly increasing array of $n$ positive arrival times, where $1 \le n \le 10^5$.
- `load`: an array of $n$ positive processing durations. Every time and duration is at most $10^9$.

**Return value**

Return every server ID whose handled-request count equals the maximum count, in any order.

### Examples
**Example 1**

- Input: `k = 3`, `arrival = [1, 2, 3, 4, 5]`, `load = [5, 2, 3, 3, 3]`
- Output: `[1]`
- Explanation: Servers 0, 1, and 2 take the first three requests. At time 4, server 1 has become free and takes request 3; every server is busy when request 4 arrives.

**Example 2**

- Input: `k = 3`, `arrival = [1, 2, 3, 4]`, `load = [1, 2, 1, 2]`
- Output: `[0]`

**Example 3**

- Input: `k = 3`, `arrival = [1, 2, 3]`, `load = [10, 12, 11]`
- Output: `[0, 1, 2]`
