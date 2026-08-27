# Guided Example: Max Consecutive Ones

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 0, 1, 1, 1]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a binary array `nums`, return *the maximum number of consecutive *`1`*'s in the array*.

The objective is to compute `3` from `{"nums": [1, 1, 0, 1, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

“Consecutive” is the key word. The task does not ask for the total number of ones; it asks for the length of the longest uninterrupted run. A zero separates two runs, so ones on opposite sides of a zero must never be added together. The solution tracks the length of the run ending at the current position and separately remembers the largest run seen anywhere.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 0, 1, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The two variables have distinct meanings:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The two variables have distinct meanings:... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- `cnt` is the number of consecutive ones at the end of the already-processed prefix.
- `ans` is the maximum run length anywhere in that processed prefix.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 0, 1, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Split a converted string on zero:** Converting:** - **Split a converted string on zero:** Converting all values to text, splitting, and taking the longest segment can be concise, but it allocates several linear-size objects and obscures the simple streaming invariant.
- **Store every run length:** Appending completed counts to a list and taking their maximum later works, but retains $O(n)$ unnecessary data. Only the best previous run and current run matter.
- **Two nested loops:** One loop could locate a one and another could consume its entire run. With careful index movement this can still be linear, but the single loop is easier to verify and has fewer boundary conditions.
- **Update only at zeros:** This requires a final `max(ans, cnt)` so that an all-one suffix is not missed. Updating when a one arrives removes that special ending case.
- **All zeros:** The answer is zero because no one-run ever begins; initializing both counters to zero handles it naturally.
- **All ones:** No separator appears, so `cnt` reaches the full array length and `ans` follows it.
- **Alternating values:** Every run has length one, and resets prevent separate ones from being combined.
- **Single element:** The general loop returns `1` for `[1]` and `0` for `[0]` without branching on the array length.
- **Binary-input guarantee:** `if x` is correct only because values are guaranteed to be zero or one. For a more general array, the explicit condition `x == 1` would be required.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of elements in `nums`. The loop reads each element exactly once and performs constant-time comparisons, assignments, addition, and `max` work. The running time is $O(n)$. This matches the lower bound for an arbitrary input array because any skipped element could affect the maximum run.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
