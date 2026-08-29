# Guided Example: Design Ride Sharing System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["RideSharingSystem", "matchDriverWithRider"], "arguments": [[], []]}`
- **Required output:** `[null, [-1, -1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A ride sharing system manages ride requests from riders and availability from drivers. Riders request rides, and drivers become available over time. The system should match riders and drivers in the order they arrive.

The objective is to compute `[null, [-1, -1]]` from `{"operations": ["RideSharingSystem", "matchDriverWithRider"], "arguments": [[], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent arrival order with a unique timestamp

The system needs FIFO order independently among riders and among drivers. The source maintains one counter `t`. Every addition—rider or driver—receives the current counter value, and the counter then increases.

Since `t` never repeats, timestamps encode global arrival order. Using one global clock is stronger than necessary, but it also preserves arrival order within each category: if rider A was added before rider B, A's timestamp is smaller, regardless of driver additions between them.

The source stores:

- `riders` as a `SortedList` of `(timestamp, riderId)`;
- `drivers` as a `SortedList` of `(timestamp, driverId)`;
- `d[riderId]` as the rider's timestamp, used to locate that exact ordered entry during cancellation.

Tuple ordering compares timestamps first. Because timestamps are unique, the first tuple is always the earliest still-available member of that category.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["RideSharingSystem", "matchDriverWithRider"], "arguments": [[], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Add a rider

`addRider` records the current timestamp in `d`, inserts `(timestamp, riderId)` into the ordered rider collection, and increments the clock.

The rider-ID guarantee says each rider is added at most once, so one ID never has two waiting entries. The timestamp dictionary is authoritative only for locating the rider's original tuple; waiting status is represented by whether that tuple still exists in `riders`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Add a driver

`addDriver` inserts `(timestamp, driverId)` into `drivers` and increments the same clock. Drivers cannot be canceled, so no driver-to-timestamp dictionary is needed.

Rider IDs and driver IDs live in separate namespaces for system behavior. The same numeric value may identify one rider and one driver, as in the second example, without collision because their tuples are stored in different ordered collections.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, [-1, -1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["RideSharingSystem", "matchDriverWithRider"], "arguments": [[], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, [-1, -1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Deque plus active rider set:** Append arrivals to deques, mark active riders in a set, and lazily pop canceled rider IDs from the front before matching. Each entry is removed at most once, giving $O(Q)$ total expected time. This matches the manifest summary.
- **Linked FIFO queue with ID-to-node map:** Directly unlink canceled riders in $O(1)$ while keeping FIFO ends, but implementing a robust linked structure is more complex.
- **Ordinary list queues:** Appending is cheap, but removing index 0 and arbitrary cancellations can be linear, leading to $O(Q^2)$ total time.
- **No rider available:** A waiting driver must remain queued; the early return mutates neither collection.
- **No driver available:** Waiting riders, including their order, remain unchanged.
- **Cancel a matched rider:** Its ordered tuple is already gone, so `discard` safely has no effect.
- **Cancel an unknown rider:** `defaultdict` creates a timestamp entry and discards a nonexistent tuple. Behavior is correct, though it has a small state side effect.
- **Cancellation before a later allowed addition:** The real add overwrites the default timestamp and inserts the correct tuple.
- **Interleaved categories:** A global clock still preserves the independent relative order of riders and of drivers.
- **Equal rider and driver IDs:** They are stored in separate collections and can be matched together without ambiguity.
- **Unique additions:** The contract prevents duplicate waiting tuples for one rider or driver ID.
- **Ordered result pair:** The method returns `[driverId, riderId]`, not the reverse.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Q\log Q)$. Let $Q$ be the total number of method calls. `SortedList.add`, `discard`, and `pop(0)` are treated as $O(\log Q)$ operations. Dictionary access is expected $O(1)$, and emptiness checks are $O(1)$.
- **Auxiliary Space Complexity:** $O(Q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
