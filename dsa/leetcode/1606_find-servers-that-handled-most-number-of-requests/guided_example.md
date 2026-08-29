# Guided Example: Find Servers That Handled Most Number of Requests

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"k": 3, "arrival": [1, 2, 3, 4, 5], "load": [5, 2, 3, 3, 3]}`
- **Required output:** `[1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have `k` servers numbered from `0` to `k-1` that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but **cannot handle more than one request at a time**. The requests are assigned to servers according to a specific algorithm:

The objective is to compute `[1]` from `{"k": 3, "arrival": [1, 2, 3, 4, 5], "load": [5, 2, 3, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Maintain free servers and busy completion times separately

At each arrival, the assignment rule needs two operations:

- release every server whose current request has finished;
- among free servers, find the first identifier at or after `i % k`, wrapping to zero if necessary.

The source uses two ordered structures suited to those tasks:

- `busy` is a min-heap of `(finish_time, server_id)`;
- `free` is a `SortedList` of currently available server identifiers.

`cnt[server]` records how many requests each server successfully handles.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"k": 3, "arrival": [1, 2, 3, 4, 5], "load": [5, 2, 3, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initial state

`free = SortedList(range(k))` contains every server ID from zero through `k - 1` in sorted order. `busy` is empty because no request has started, and every count is zero.

The request loop uses `enumerate(zip(arrival, load))`. Index `i` identifies the request and determines its preferred starting server, while `start` and `t` are its arrival time and duration.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Release completed servers before assignment

Before assigning request `i`, the source repeatedly checks the smallest finish time in `busy`:

`while busy and busy[0][0] <= start`.

A server finishing exactly at the new request’s arrival time is available, so the comparison is inclusive.

For each completed entry, its server ID is added back to `free` and the heap entry is removed. The code reads `busy[0][1]` before `heappop(busy)`; both refer to the same root tuple.

Because `busy` is ordered by finish time, once the root finishes after `start`, every other busy server also finishes later and the release loop can stop.

Each server handles at most one request at a time, so it has at most one heap entry.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"k": 3, "arrival": [1, 2, 3, 4, 5], "load": [5, 2, 3, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

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
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((R+K)$. Let $R$ be the number of requests and $K$ the number of servers.
- **Auxiliary Space Complexity:** $O(K)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
