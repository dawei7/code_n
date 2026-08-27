# Guided Example: Maximum Distance in Arrays

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arrays": [[1, 2, 3], [4, 5], [1, 2, 3]]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given `m` `arrays`, where each array is sorted in **ascending order**.

The objective is to compute `4` from `{"arrays": [[1, 2, 3], [4, 5], [1, 2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Use the sorted property to discard interior values.** For one sorted array, its first element is its minimum and its last element is its maximum. When pairing that array with another array, no interior value can create a wider distance than one of those endpoints. The global answer must therefore combine a minimum endpoint from one array with a maximum endpoint from a different array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arrays": [[1, 2, 3], [4, 5], [1, 2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

A tempting shortcut is to find the absolute global minimum and maximum across all arrays. That fails when both belong to the same array because the two chosen integers must come from different arrays. The exact solution avoids this by processing arrays in order and comparing the current array only with extrema collected from earlier arrays.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A tempting shortcut is to find the absolute global minimum a... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Define the running state.** Before the loop:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arrays": [[1, 2, 3], [4, 5], [1, 2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Index-based single scan:** Iterate indices 1 t:** - **Index-based single scan:** Iterate indices 1 through $M-1$ to preserve the exact logic while avoiding the Python slice allocation.
- **Compare every array pair:** Endpoints reduce each pair to constant work, but considering all pairs still costs $O(M^2)$ and is unnecessary.
- **Compare every element:** This ignores the sorted structure and can be dramatically slower while producing no better candidate.
- **Global minimum and maximum only:** It is unsafe unless their array identities are tracked, because both extrema may come from one array.
- **Exactly two arrays:** The one loop iteration compares their opposite endpoints and returns the correct maximum.
- **Single-element arrays:** Their first and last endpoints are the same; the formulas still work.
- **All values equal:** Both candidates remain zero, so the answer is zero.
- **Negative values:** Absolute difference handles signs naturally; a negative minimum and positive maximum often create the largest result.
- **Extrema in the current array:** Candidate calculation must occur before state update so they are never illegally paired with each other.
- **Long inner arrays:** Their length does not affect scan time beyond constant endpoint access, provided indexing is constant time.
- **Nonempty-array guarantee:** It makes `arr[0]` and `arr[-1]` safe for every array.
- **At least two arrays:** It guarantees that a legal cross-array pair exists; otherwise initial `ans = 0` would not represent a chosen pair.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M)$. Let $M$ be the number of arrays. Initialization is constant time, and each remaining array contributes a constant number of endpoint reads, subtractions, comparisons, and assignments. The algorithm never scans interior elements because sorted order makes endpoints sufficient. Time complexity is therefore $O(M)$, matching the manifest.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
