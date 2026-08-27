# Guided Example: Design Parking System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"big": 1, "medium": 1, "small": 0, "carTypes": [1, 2, 3, 1]}`
- **Required output:** `[true, true, false, false]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

The objective is to compute `[true, true, false, false]` from `{"big": 1, "medium": 1, "small": 0, "carTypes": [1, 2, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store remaining capacity directly

The system has exactly three independent car types. To decide whether a new car can park, the only needed information is how many spaces of that type remain.

The constructor stores:

`cnt = [0, big, medium, small]`.

Index zero is an unused dummy. Big, medium, and small capacities occupy indices one, two, and three, matching the platform’s `carType` codes exactly.

This one-based layout avoids subtracting one in every operation. The constant extra slot has no asymptotic impact.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"big": 1, "medium": 1, "small": 0, "carTypes": [1, 2, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why remaining slots are sufficient state

An alternative representation could store both the original capacity and the number of cars already admitted, then test whether admitted count is below capacity. Their difference is the remaining capacity.

Keeping that difference directly compresses the state. Every successful admission subtracts one. No method removes cars, changes capacities, or asks how many have parked, so no other information is required.

The three types are independent. A free medium slot cannot accept a big car, and a failed small-car attempt must not affect big or medium counts. Direct indexing isolates each category.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An alternative representation could store both the original ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Processing `addCar`

For a requested `carType`, the method first checks:

`if cnt[carType] == 0`.

Zero means every slot of that exact type is occupied. The method returns `false` immediately and leaves the count unchanged.

If the count is positive, one slot is available. The source decrements it:

`cnt[carType] -= 1`

and returns `true`.

The order is important. A failed request does not decrement capacity below zero. This keeps `cnt` a truthful remaining-slot count after any sequence of calls.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[true, true, false, false]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"big": 1, "medium": 1, "small": 0, "carTypes": [1, 2, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[true, true, false, false]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Zero-based capacity array:** Store `[big, medi:** - **Zero-based capacity array:** Store `[big, medium, small]` and access `carType - 1`. It is equally correct; the checked-in source uses a dummy zero slot for direct indexing.
- **Separate fields per type:** Three named counters work for this fixed problem but repeat branching logic. An indexed array makes the method uniform.
- **Dictionary keyed by type:** It provides constant expected access and could support sparse or dynamic types, but is unnecessary for three dense integer codes.
- **Store occupied and capacity counts:** The availability decision uses only their difference. Remaining capacity is sufficient and simpler.
- **Decrement before checking:** This risks negative counts or requires undoing failure. The source checks zero first and mutates only on success.
- **Initial capacity zero:** Every request of that type returns false, and the counter stays zero.
- **Capacity one:** The first matching request succeeds and every later one fails.
- **Interleaved car types:** Each call changes only its own index, so activity for one type cannot consume another type’s slots.
- **Repeated failed calls:** They return false without pushing the count negative.
- **Maximum initial capacities:** Numeric magnitude does not affect operation count or storage size.
- **Valid car codes:** Direct indexing assumes `carType` is one, two, or three, exactly as guaranteed. An invalid code would need validation but is outside the contract.
- **Dummy index zero:** It is never read by a valid call and costs only one constant list entry.
- **Persistent object state:** Capacities must live on `self` so successive judge calls observe earlier successful admissions.
- **No removal operation:** Because cars never leave through the interface, remaining capacity only decreases and no additional event handling is needed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The constructor creates a list of four integers, a fixed size independent of input capacities, so its time and space are $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
