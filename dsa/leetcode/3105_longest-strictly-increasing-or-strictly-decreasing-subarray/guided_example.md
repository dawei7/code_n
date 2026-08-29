# Guided Example: Longest Strictly Increasing or Strictly Decreasing Subarray

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 4, 3, 3, 2]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of integers `nums`. Return *the length of the **longest** subarray of *`nums`* which is either **strictly increasing** or **strictly decreasing***.

The objective is to compute `2` from `{"nums": [1, 4, 3, 3, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

**A monotonic subarray is an adjacent run.** Because the answer must be a subarray, its elements are contiguous. A strictly increasing run continues only while each next value is greater than the immediately previous value. A strictly decreasing run continues only while each next value is smaller. One failed adjacent comparison ends every longer run of that direction crossing the boundary.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 4, 3, 3, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact source handles the two directions in two separate passes. This differs from the local manifest's description of tracking both directions together, but it computes the same desired maximum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**First pass: longest strictly increasing run.** The source initializes `ans = t = 1`. Every nonempty array has a one-element subarray, and a singleton is vacuously both strictly increasing and strictly decreasing.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 4, 3, 3, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One combined pass:** Maintain increasing and decreasing run lengths simultaneously, resetting the opposite one after each comparison. This matches the manifest summary and uses half as many comparisons.
- **`pairwise(nums)` in two passes:** It avoids list slices, though a fresh iterator is needed for each traversal.
- **Brute force from every start:** Extend increasing and decreasing candidates until failure, taking $O(n^2)$ time.
- **Single element:** Both loops are empty and initialization correctly returns one.
- **Equal adjacent elements:** They reset both directional runs because the inequalities are strict.
- **Entire array increasing:** The first pass grows `t` to $n$; the second cannot reduce `ans`.
- **Entire array decreasing:** The second pass grows to $n$.
- **Direction change:** The old directional run ends, but a new run may start with the current element as length one and extend on later pairs.
- **Mountain or valley:** The whole shape is not valid; the method returns the longer pure-direction side.
- **Two elements:** One of less, greater, or equal applies, yielding answer two for unequal values and one for equal values.
- **Why `ans` is retained:** It combines the best increasing result with later decreasing candidates.
- **Why `t` is reset between passes:** An increasing run length has no meaning as starting state for the decreasing scan.
- **Slice indexing:** Loop `i` refers to the predecessor in the original list, while `x` is original `nums[i + 1]`.
- **Input mutation:** Slices copy references but the source never changes any element.
- **Manifest space discrepancy:** The abstract run algorithm is constant-state, but the exact list slicing makes auxiliary space linear.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each pass examines $n-1$ adjacent pairs and performs constant work, so total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
