# Guided Example: Car Pooling

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"trips": [[2, 1, 5], [3, 3, 7]], "capacity": 4}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

The objective is to compute `false` from `{"trips": [[2, 1, 5], [3, 3, 7]], "capacity": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Record changes at locations instead of simulating every trip

Passengers from trip `[x, f, t]` occupy seats beginning at pickup location `f` and stop occupying them at drop-off location `t`. The occupied interval is therefore half-open: it includes `f` and excludes `t`.

The solution represents this interval with two events. It adds `x` to `d[f]` and subtracts `x` from `d[t]`. No entry is needed at every intermediate kilometer. When these changes are accumulated from west to east, the added passengers remain in the running total until the subtraction at their destination removes them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"trips": [[2, 1, 5], [3, 3, 7]], "capacity": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Size the location timeline

`mx = max(e[2] for e in trips)` finds the farthest drop-off location. The input is guaranteed nonempty, so the maximum exists. The difference array has indices zero through `mx`, giving every pickup and drop-off a valid bucket.

Locations farther east than `mx` do not matter because all trips have ended. Locations with no event remain zero, meaning the occupancy continues unchanged across them.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Combine simultaneous pickups and drop-offs

Several trips can start or end at the same location. Their changes add in one bucket. A drop-off contributes a negative value and a pickup contributes a positive value; the net bucket applies both before the car continues east.

This matches the half-open trip semantics. Passengers whose destination is location five no longer consume seats after reaching five, so those seats can be used by passengers picked up there. The net difference correctly allows that transfer without depending on an arbitrary ordering of separate events.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"trips": [[2, 1, 5], [3, 3, 7]], "capacity": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sorted event list:** Create pickup and drop-off events, sort by location, and scan the running occupancy. This supports large coordinates in $O(n\log n)$ time; drop-offs must be ordered before pickups at the same point or combined by location.
- **Ordered difference map:** Store only nonzero changes in a dictionary, sort its keys, and accumulate. It uses $O(n)$ space and avoids a dense coordinate range.
- **Min-heap of active trips:** Sort trips by pickup, remove all destinations reached before each pickup, and track occupied seats. This costs $O(n\log n)$ and is more complex than the bounded-coordinate difference array.
- **Simulate each passenger or kilometer per trip:** Updating every point inside every interval can cost $O(nL)$. Endpoint differences encode the same coverage much more efficiently.
- **Pickup and drop-off at the same location across trips:** Negative and positive changes share one bucket, so freed seats are immediately available.
- **Capacity exactly reached:** The check uses `<=`, so occupancy equal to capacity is valid.
- **Capacity exceeded briefly:** Even one prefix sum above capacity makes `all` return false, as required.
- **Overlapping trips:** Their interval contributions add automatically in the prefix total.
- **Nonoverlapping trips:** Earlier passengers are subtracted before later pickups, so only each trip’s own load remains on its segment.
- **Trip ending at `mx`:** Its subtraction fits at the final array index. The value after that location is irrelevant because no trip continues.
- **Pickup at zero:** The addition at `d[0]` appears in the first prefix sum, representing passengers entering at the initial location.
- **Input order:** Trips may be arbitrary because event additions are commutative and the prefix scan supplies geographic order.
- **Nonempty trips:** The maximum drop-off call relies on the guaranteed minimum of one trip.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+L)$. Let $n$ be the number of trips and $L$ the farthest drop-off coordinate. Finding `mx` costs $O(n)$, recording events costs another $O(n)$, and scanning the difference array costs $O(L)$. The precise generalized time is $O(n+L)$.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
