## General
**Separate completion order from server-ID order.** Maintain a min-heap of busy servers keyed by `(finish_time, server_id)`. Before assigning a request at time `t`, repeatedly release every heap entry whose finish time is at most `t`. This makes the availability structure describe exactly the servers eligible for the new request.

**Represent availability with a Fenwick tree.** Store 1 at an available server index and 0 at a busy one. Prefix sums count available servers in any ID range. For preferred index `i % k`, compare the total availability with the prefix count before that index. If an available server exists at or after the preferred index, select the next 1 there; otherwise select the first available server from the beginning, which implements circular wraparound. Fenwick binary lifting finds the index of a selected availability rank in $O(\log k)$ time.

After selection, change that server's tree value from 1 to 0, increment its handled count, and push its finish event. If the tree's total is zero, drop the request without changing any server count. Because releases happen before selection and rank selection returns the first available index in the required circular order, every request is assigned exactly as specified. The final scan returns all indices tied at the maximum count.

## Complexity detail
Building the initial Fenwick representation takes $O(k)$ time. Each request performs a constant number of Fenwick prefix, selection, and update operations, while every accepted request enters and leaves the busy heap at most once. These operations cost $O(\log k)$ each, giving $O((n+k)\log k)$ total time. The availability tree, busy heap, and count array each use $O(k)$ space.

## Alternatives and edge cases
- **Circularly scan server IDs:** This is correct but can inspect all $k$ servers for each request, taking $O(nk)$ time when requests repeatedly arrive while every server is busy.
- **Sorted available list with ordinary array deletion:** Binary search finds the next ID quickly, but removing an interior Python list element costs $O(k)$; an ordered tree or Fenwick tree avoids that shift.
- **Track only finish times:** A completion heap identifies which servers become free, but it cannot by itself find the first available ID at or after the preferred server.
- A server whose finish time equals `arrival[i]` must be released before request $i$ is assigned.
- If no server is available, the request is dropped and its duration is irrelevant.
- Circular search wraps to server 0 only after exhausting available IDs at or above `i % k`.
- With `k = 1`, every non-overlapping request goes to server 0 and overlapping requests are dropped.
- Multiple servers can tie for busiest, and any output order is valid.
