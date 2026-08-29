# Guided Example: Monotonic Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 2, 3]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An array is **monotonic** if it is either monotone increasing or monotone decreasing.

The objective is to compute `true` from `{"nums": [1, 2, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

An array is monotonic when it satisfies at least one of two complete possibilities:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- every adjacent step is nondecreasing;
- every adjacent step is nonincreasing.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Checking adjacent pairs is sufficient even though the definition quantifies over every $i\le j$. If each neighboring relation is nondecreasing, transitivity gives

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One pass with two flags:** Maintain “still nondecreasing” and “still nonincreasing” while scanning once. This avoids the second pass but has the same asymptotic bounds.
- **Infer direction from the first pair:** Equal leading values make direction undecided, so the method needs to skip ties or maintain both possibilities carefully.
- **Sort and compare:** Comparing with sorted and reverse-sorted copies works but costs $O(n\log n)$ time and $O(n)$ extra space.
- **Compare every pair $i<j$:** This follows the definition literally but costs $O(n^2)$; adjacent transitivity makes it unnecessary.
- **One element:** Both `all` checks are vacuously true.
- **All equal:** Every adjacent pair satisfies both inequalities.
- **Strictly increasing:** Ascending succeeds and descending fails at the first increase.
- **Strictly decreasing:** Descending succeeds and ascending fails at the first decrease.
- **Plateaus:** Equal runs are legal in either monotonic direction.
- **One increase and one decrease:** Each direction has a violating adjacent pair, so the result is false.
- **Negative values:** Only ordering matters; sign does not change the logic.
- **Fresh iterators:** Calling `pairwise(nums)` twice is necessary because one generator cannot be replayed after consumption.
- **No input mutation:** The original element order remains unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. Each `all` call examines at most $n-1$ adjacent pairs. Two passes are still linear.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
