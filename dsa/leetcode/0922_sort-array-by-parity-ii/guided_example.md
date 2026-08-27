# Guided Example: Sort Array By Parity II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 2, 5, 7]}`
- **Required output:** `[4, 5, 2, 7]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `nums`, half of the integers in `nums` are **odd**, and the other half are **even**.

The objective is to compute `[4, 5, 2, 7]` from `{"nums": [4, 2, 5, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

Even indices must contain even values, and odd indices must contain odd values. Because the input contains equal numbers of even and odd values, every misplaced odd value at an even index can be paired with a misplaced even value at an odd index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 2, 5, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 4

Pointer `j` scans odd indices and begins at 1.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Pointer `j` scans odd indices and begins at 1.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[4, 5, 2, 7]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 2, 5, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[4, 5, 2, 7]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two output arrays or one new result:** Place e:** - **Two output arrays or one new result:** Place evens at even result indices and odds at odd indices. This is linear but uses $O(n)$ space.
- **Two mismatch pointers:** Advance one pointer over even indices looking for odd values and one over odd indices looking for even values, then swap. This is an equivalent in-place method.
- **Sort numerically:** Numerical order does not directly enforce index parity and costs extra time.
- **Scan every odd index from the beginning:** Correct but can repeat work and become quadratic.
- **Already valid array:** No swaps occur.
- **Minimum length two:** Either it is already valid or one swap fixes both positions.
- **Zero:** Zero is even and belongs at an even index.
- **Duplicate values:** Only parity matters, so duplicates require no special handling.
- **Equal parity counts:** This contract guarantee is what prevents `j` from running out during a needed search.
- **Odd value at even index:** It always pairs with some even value at an odd index.
- **Any answer order:** Values within parity classes may be rearranged freely.
- **Input mutation:** Pass a copy if original order must be preserved.
- **Follow-up:** The exact solution meets the in-place requirement with constant auxiliary storage.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. The even-index loop processes $n/2$ positions. Pointer `j` moves only forward through odd indices, at most $n/2$ steps total.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
