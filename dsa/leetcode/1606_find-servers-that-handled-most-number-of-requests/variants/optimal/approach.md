## General

**Maintain free servers and busy completion times separately**

At each arrival, the assignment rule needs two operations:

- release every server whose current request has finished;
- among free servers, find the first identifier at or after `i % k`, wrapping to zero if necessary.

The source uses two ordered structures suited to those tasks:

- `busy` is a min-heap of `(finish_time, server_id)`;
- `free` is a `SortedList` of currently available server identifiers.

`cnt[server]` records how many requests each server successfully handles.

**Initial state**

`free = SortedList(range(k))` contains every server ID from zero through `k - 1` in sorted order. `busy` is empty because no request has started, and every count is zero.

The request loop uses `enumerate(zip(arrival, load))`. Index `i` identifies the request and determines its preferred starting server, while `start` and `t` are its arrival time and duration.

**Release completed servers before assignment**

Before assigning request `i`, the source repeatedly checks the smallest finish time in `busy`:

`while busy and busy[0][0] <= start`.

A server finishing exactly at the new request’s arrival time is available, so the comparison is inclusive.

For each completed entry, its server ID is added back to `free` and the heap entry is removed. The code reads `busy[0][1]` before `heappop(busy)`; both refer to the same root tuple.

Because `busy` is ordered by finish time, once the root finishes after `start`, every other busy server also finishes later and the release loop can stop.

Each server handles at most one request at a time, so it has at most one heap entry.

**Drop a request only when no server is free**

After releases, `not free` means every one of the $k$ servers is busy at `start`. The request must be dropped, and `continue` advances without changing counts or the busy heap.

If at least one server is free, the assignment rule must be followed exactly rather than selecting merely the smallest ID.

**Find the cyclic successor**

The preferred server is `i % k`. The call:

`j = free.bisect_left(i % k)`

finds the first position whose server ID is greater than or equal to the preferred ID.

If `j < len(free)`, `free[j]` is exactly the first available server encountered while scanning upward from `i % k`.

If `j == len(free)`, no free server has an ID at or above the preference. The scan wraps around, so the source sets `j = 0` and selects the smallest free ID.

This lower-bound plus wrap implements the circular assignment rule in $O(\log k)$ search time.

**Mark the server busy**

After selecting `server = free[j]`, the source:

- increments `cnt[server]`;
- pushes `(start + t, server)` into `busy`;
- removes the identifier from `free`.

`start + t` is the first time the server becomes available again. Removing it from `free` prevents another request from being assigned before then.

The order of push and removal does not expose an inconsistent state externally because no other operation interleaves within the sequential method.

**Why the simulation is exact**

Before each request, the release loop makes `free` contain exactly servers whose finish times are at most the arrival, and `busy` contain exactly servers still occupied. If `free` is empty, dropping is required.

Otherwise, sorted lower-bound search returns the first free ID in the prescribed cyclic order. The chosen server’s new finish time and count are then recorded, restoring the state invariant for the next request.

By induction over the strictly increasing arrivals, every request is assigned to the same server as the specification or dropped exactly when required.

**Collect all busiest servers**

After simulation, `mx = max(cnt)` finds the greatest handled-request count. The list comprehension returns every index `i` with `cnt[i] == mx`.

Ties are intentionally preserved, and the comprehension returns IDs in ascending order. The statement allows any order, so ascending output is valid.

## Complexity detail

Let $R$ be the number of requests and $K$ the number of servers.

Initializing the sorted free structure takes at most $O(K\log K)$ under a general insertion-based view, though construction from an already sorted range may be linear in the implementation. Each accepted request performs a sorted-list search, removal, and heap push. Each busy entry is later popped at most once and its server reinserted. These operations cost $O(\log K)$ each.

Total time is $O((R+K)\log K)$ under the manifest’s bound. Counting and final scanning add $O(K)$.

At all times, each server appears in exactly one of `free` or `busy`. Together they store $K$ server records, and `cnt` has length $K$. Auxiliary space is $O(K)$.

## Alternatives and edge cases

- **Two heaps with shifted server priorities:** Released servers can be inserted under a request-relative transformed ID, avoiding a balanced sorted container. It retains $O(R\log K)$ time but is subtler.
- **Linear scan for a free server:** Checking up to $K$ IDs per request costs $O(RK)$ and is too slow at the limits.
- **Only a finish-time heap:** It can release servers but cannot efficiently find the cyclic successor among arbitrary free IDs; a second ordered structure is needed.
- **Finish exactly at arrival:** `<= start` releases the server in time for the new request.
- **All servers busy:** The free collection is empty, so the request is dropped without changing counts.
- **Preferred server free:** `bisect_left` finds its exact ID and assigns it.
- **Wraparound:** If no free ID is high enough, index zero selects the smallest available server.
- **Several servers finish together:** The release loop returns all of them before assignment.
- **Equal finish times:** Heap tuples use server ID as a harmless tie-breaker; every finished server is released.
- **One server:** Every non-overlapping request goes to server zero, and overlapping requests are dropped.
- **More servers than requests:** Some counts remain zero, but at least the initially available servers handle incoming requests according to preference.
- **Tied busiest servers:** The final comprehension includes every server at the maximum count.
- **Sorted arrivals:** Strict increase lets processing occur chronologically without sorting requests.
- **External `SortedList` behavior:** The complexity relies on logarithmic lower-bound, insertion, and removal operations supplied by that ordered container.
