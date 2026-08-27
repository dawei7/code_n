# Guided Example: Seat Reservation Manager

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"], "arguments": [[5], [], [], [2], [], [], [], [], [5]]}`
- **Required output:** `[null, 1, 2, null, 2, 3, 4, 5, null]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a system that manages the reservation state of `n` seats that are numbered from `1` to `n`.

The objective is to compute `[null, 1, 2, null, 2, 3, 4, 5, null]` from `{"operations": ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"], "arguments": [[5], [], [], [2], [], [], [], [], [5]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Maintain all currently available seats in a min-heap.** The required reservation is always the smallest-numbered unreserved seat. A min-heap is designed to expose the smallest stored value while supporting removals and later insertions efficiently.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"], "arguments": [[5], [], [], [2], [], [], [], [], [5]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The single field `q` represents exactly the set of available seat numbers. Reserved seats are absent. Because the operation guarantees prevent unreserving an already available seat, no seat number appears twice.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The single field `q` represents exactly the set of available... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Initialization is already a valid heap.** The constructor assigns

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, 1, 2, null, 2, 3, 4, 5, null]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"], "arguments": [[5], [], [], [2], [], [], [], [], [5]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, 1, 2, null, 2, 3, 4, 5, null]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Counter plus returned-seat heap:** Track the s:** - **Counter plus returned-seat heap:** Track the smallest never-reserved number and heap only unreserved seats. This avoids storing all seats initially and often uses less memory.
- **Balanced ordered set:** It also supports minimum removal and reinsertion in logarithmic time, but Python’s standard library has no built-in tree set.
- **Boolean array plus linear scan:** Availability flags are simple, but finding the next smallest seat can degrade to `O(n)` after arbitrary unreservations.
- **Simple increasing counter alone:** It fails when a previously reserved smaller seat is unreserved and must be chosen before new larger seats.
- **One seat:** The heap alternates between one entry and empty under the guaranteed valid reserve and unreserve sequence.
- **Unreserve the smallest number:** Heap push moves it toward the root, making it the next reservation.
- **Unreserve a large number:** It remains in the appropriate heap position until all smaller available seats are used.
- **Reserve when none available:** The source does not guard this because the contract guarantees it never occurs.
- **Duplicate unreserve:** The source does not prevent duplicate heap entries because the contract guarantees only reserved seats are unreserved.
- **Seat bounds:** The constructor and valid calls ensure every stored number remains from one through `n`.
- **Already-heapified initialization:** The increasing list needs no `heapify` call; adding one would be correct but redundant.
- **No stored `n`:** The heap fully captures runtime availability, so the constructor parameter need not remain as a field.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Constructing `range` and its list takes `O(n)` time and `O(n)` space. No separate heap-building pass is required because the increasing list already satisfies heap order.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
