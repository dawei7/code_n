# Guided Example: Reshape the Matrix

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mat": [[1, 2], [3, 4]], "r": 1, "c": 4}`
- **Required output:** `[[1, 2, 3, 4]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In MATLAB, there is a handy function called `reshape` which can reshape an `m x n` matrix into a new one with a different size `r x c` keeping its original data.

The objective is to compute `[[1, 2, 3, 4]]` from `{"mat": [[1, 2], [3, 4]], "r": 1, "c": 4}` while avoiding redundant calculations and unnecessary overhead.

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

Reshaping changes row and column boundaries but must preserve the single row-major sequence of elements. The solution assigns every element a flat position and converts that same position into coordinates in both shapes.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mat": [[1, 2], [3, 4]], "r": 1, "c": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Let the original dimensions be `m` rows and `n` columns. The original element count is `m * n`, while the requested count is `r * c`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Reject an impossible shape immediately.** If these products differ, some elements would need to be lost or invented. The method returns the original `mat` object unchanged.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 2, 3, 4]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mat": [[1, 2], [3, 4]], "r": 1, "c": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 2, 3, 4]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Flatten then regroup:** Building a separate one-dimensional list is clear but adds another $O(mn)$ temporary buffer.
- **Nested source loops with destination pointers:** It is equivalent but requires manually updating row and column counters.
- **Different element counts:** Return the original matrix without partial allocation.
- **Same shape:** The code creates an equivalent new matrix because the reshape is legal.
- **One-row target:** Flat positions become consecutive columns.
- **One-column target:** Every flat position becomes a separate row.
- **Single element:** Any legal one-cell shape is one by one.
- **Negative or zero values:** Values are copied without interpretation.
- **Independent destination rows:** The list comprehension avoids shared-row aliasing.
- **Input immutability:** Legal reshaping copies references/values into a new outer structure.
- **Row-major guarantee:** One flat index is the invariant connecting both coordinate systems.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn)$. For a legal reshape, let $N=mn=rc$. Allocation and the flat loop each take $O(N)$ time, so time is $O(mn)$.
- **Auxiliary Space Complexity:** $O(rc)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
