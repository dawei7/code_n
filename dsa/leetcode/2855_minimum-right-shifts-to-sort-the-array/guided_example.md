# Guided Example: Minimum Right Shifts to Sort the Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 4, 5, 1, 2]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` of length `n` containing **distinct** positive integers. Return *the **minimum** number of **right shifts** required to sort *`nums`* and *`-1`* if this is not possible.*

The objective is to compute `2` from `{"nums": [3, 4, 5, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

**A sortable rotation has at most one descent.** Right shifts only rotate the circular order of distinct values. If a rotation can become strictly increasing, the original array must consist of an increasing suffix followed circularly by an increasing prefix, with one drop at their boundary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 4, 5, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The intended solution is therefore to find the first descent, verify that everything after it forms the smaller increasing block, and move that block to the front.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The intended solution is therefore to find the first descent... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Find the end of the initial increasing prefix.** The source starts `i = 1` and advances while `nums[i - 1] < nums[i]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 4, 5, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Corrected boundary scan:** Find the first desc:** - **Corrected boundary scan:** Find the first descent, reject a second descent, require `nums[-1] < nums[0]` when a descent exists, and return the suffix length. This retains $O(n)$ time and $O(1)$ space.
- **Count circular descents:** A rotation of a distinct sorted array has exactly one circular descent unless already sorted. Care is needed because the wrap pair in an already sorted array is itself a circular descent.
- **Try every right shift:** Construct or compare all rotations in $O(n^2)$ time. It is simple at $n=100$ but unnecessary.
- **Already sorted:** `i == n` and zero shifts are returned.
- **Valid one-element suffix:** An array such as `[2,3,1]` correctly returns one because the final value is below the first.
- **Invalid one-element suffix:** `[1,3,2]` exposes the exact source defect; it returns one instead of negative one.
- **Suffix length at least two:** The chained first comparison indirectly checks the suffix's first value against `nums[0]`.
- **Second descent:** Suffix monotonicity fails and the source returns negative one.
- **Two-element descending array:** The one-element suffix is necessarily smaller than the first, so one shift is valid.
- **Distinctness:** It turns nondecreasing checks into strict comparisons and guarantees a unique sorted rotation.
- **Input preservation:** The method calculates a shift count without performing rotations.
- **Manifest claim:** The intended boundary validation is sound, but the exact implementation omits one required edge check.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The first pointer moves from one to at most $n$. The second pointer also moves only forward through the remaining suffix. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
