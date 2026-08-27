# Guided Example: Maximum Building Height

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5, "restrictions": [[2, 1], [4, 1]]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You want to build `n` new buildings in a city. The new buildings will be built in a line and are labeled from `1` to `n`.

The objective is to compute `2` from `{"n": 5, "restrictions": [[2, 1], [4, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

**A restriction affects every building, not only its own index.** If building `i` has height at most `h` and adjacent heights may differ by at most one, then building `j` can be at most `h + abs(j - i)`. A low restriction creates a cone-shaped upper bound spreading left and right. The true limit at any position is the minimum of all such propagated bounds.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5, "restrictions": [[2, 1], [4, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The number of buildings can be one billion, so calculating a limit for every index is impossible. The solution works only with explicitly restricted positions plus two boundary anchors. Between consecutive anchors, the maximum possible shape is determined mathematically.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The number of buildings can be one billion, so calculating a... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Add the fixed first building.** The code aliases the input with `r = restrictions` and appends `[1, 0]`, representing the rule that building one must have height zero. It then sorts `r` by building index.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5, "restrictions": [[2, 1], [4, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate every building:** Propagating a full:** - **Enumerate every building:** Propagating a full length-`n` limit array is impossible when `n` reaches one billion.
- **Binary search a global height:** One could test whether some building can reach a candidate height, but interval peak formulas provide the exact answer more directly.
- **No explicit restrictions:** The default anchors yield the increasing sequence with maximum `n - 1`.
- **Restriction already at building `n`:** It serves as the final anchor, so the harmless `[n, n - 1]` row is not added.
- **Very loose restriction:** Propagation lowers it when a neighboring or fixed-boundary constraint is tighter.
- **Zero-height restriction:** Its cone may force nearby buildings low, and both passes carry that effect in each direction.
- **Odd versus even interval balance:** Integer floor handles a peak lying between two building positions.
- **Endpoint peak:** Propagated consistency ensures the formula includes cases where the highest feasible value occurs at an interval boundary.
- **Fixed first building:** Appending `[1, 0]` makes its rule participate in the same propagation logic.
- **Input mutation:** The exact source appends rows, sorts the list, and rewrites height fields. Callers needing preservation must pass a deep enough copy.
- **Large indices and heights:** Python integer arithmetic safely handles sums near billions; fixed-width implementations should use a wide integer type.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(r log r)$. Let `r` be the original number of explicit restrictions. Adding at most two anchors changes the count only by a constant. Sorting takes `O(r log r)` time. The two propagation passes and peak scan are linear, so total time is `O(r log r)`.
- **Auxiliary Space Complexity:** $O(r)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
