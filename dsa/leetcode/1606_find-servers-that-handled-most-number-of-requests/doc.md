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

### Required Complexity
- **Time:** $O((n+k)\log k)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Separate completion order from server-ID order.** Maintain a min-heap of busy servers keyed by `(finish_time, server_id)`. Before assigning a request at time `t`, repeatedly release every heap entry whose finish time is at most `t`. This makes the availability structure describe exactly the servers eligible for the new request.

**Represent availability with a Fenwick tree.** Store 1 at an available server index and 0 at a busy one. Prefix sums count available servers in any ID range. For preferred index `i % k`, compare the total availability with the prefix count before that index. If an available server exists at or after the preferred index, select the next 1 there; otherwise select the first available server from the beginning, which implements circular wraparound. Fenwick binary lifting finds the index of a selected availability rank in $O(\log k)$ time.

After selection, change that server's tree value from 1 to 0, increment its handled count, and push its finish event. If the tree's total is zero, drop the request without changing any server count. Because releases happen before selection and rank selection returns the first available index in the required circular order, every request is assigned exactly as specified. The final scan returns all indices tied at the maximum count.

#### Complexity detail

Building the initial Fenwick representation takes $O(k)$ time. Each request performs a constant number of Fenwick prefix, selection, and update operations, while every accepted request enters and leaves the busy heap at most once. These operations cost $O(\log k)$ each, giving $O((n+k)\log k)$ total time. The availability tree, busy heap, and count array each use $O(k)$ space.

#### Alternatives and edge cases

- **Circularly scan server IDs:** This is correct but can inspect all $k$ servers for each request, taking $O(nk)$ time when requests repeatedly arrive while every server is busy.
- **Sorted available list with ordinary array deletion:** Binary search finds the next ID quickly, but removing an interior Python list element costs $O(k)$; an ordered tree or Fenwick tree avoids that shift.
- **Track only finish times:** A completion heap identifies which servers become free, but it cannot by itself find the first available ID at or after the preferred server.
- A server whose finish time equals `arrival[i]` must be released before request $i$ is assigned.
- If no server is available, the request is dropped and its duration is irrelevant.
- Circular search wraps to server 0 only after exhausting available IDs at or above `i % k`.
- With `k = 1`, every non-overlapping request goes to server 0 and overlapping requests are dropped.
- Multiple servers can tie for busiest, and any output order is valid.

</details>
