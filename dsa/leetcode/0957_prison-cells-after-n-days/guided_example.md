# Guided Example: Prison Cells After N Days

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"cells": [0, 1, 0, 1, 1, 0, 0, 1], "n": 7}`
- **Required output:** `[0, 0, 1, 1, 0, 0, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `8` prison cells in a row and each cell is either occupied or vacant.

The objective is to compute `[0, 0, 1, 1, 0, 0, 0, 0]` from `{"cells": [0, 1, 0, 1, 1, 0, 0, 1], "n": 7}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A huge day count hides a tiny state space

There are eight binary cells, so only `2^8 = 256` complete states exist. After one day, both endpoints are always zero because they lack two neighbors. From then on, only six interior bits vary, giving at most `2^6 = 64` reachable states.

The transition is deterministic: the same state always produces the same next state. A sufficiently long simulation must repeat a state and enter a cycle. Once its length is known, billions of days can be skipped with a remainder.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"cells": [0, 1, 0, 1, 1, 0, 0, 1], "n": 7}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use immutable state keys

The input list becomes `state = tuple(cells)`. Tuples are hashable dictionary keys, unlike mutable lists.

Dictionary `seen` maps each state to the remaining `n` when it was encountered. The code counts days downward rather than storing elapsed days.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The input list becomes `state = tuple(cells)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Detect and measure a cycle

At each loop start, if `state` exists in `seen`, cycle length is:

`seen[state] - n`.

For example, if the same state was seen with twenty days remaining and returns with six remaining, fourteen transitions separate equal states. Evolution will now repeat every fourteen days.

The assignment `n %= cycle_length` discards all complete cycles. Each full cycle begins and ends at the same state, so removing it cannot change the final result.

The current state is then recorded with its possibly reduced remaining-day count.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 0, 1, 1, 0, 0, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"cells": [0, 1, 0, 1, 1, 0, 0, 1], "n": 7}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 0, 1, 1, 0, 0, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Simulate every day:** Correct for small `n` bu:** - **Simulate every day:** Correct for small `n` but infeasible near one billion.
- **Hard-code a fourteen-day cycle:** This problem has a familiar short cycle, but general detection is clearer and self-verifying.
- **Bitmask state:** Eight bits can encode the cells compactly while preserving the same cycle logic.
- **In-place left-to-right update:** Incorrect because new values would influence other cells during the same day.
- **Endpoint cells:** They become zero on every transition.
- **Equal occupied neighbors:** The new interior value is one.
- **Equal vacant neighbors:** It is also one.
- **Different neighbors:** The new value is zero.
- **Cycle remainder zero:** Break without applying an extra day.
- **Input preservation:** Tuple conversion leaves the caller's list unchanged and the function returns a new list.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. With exactly eight cells, at most 256 states can appear, and after the first transition at most 64 endpoint-zero states are possible. Every transition examines six interior positions.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
