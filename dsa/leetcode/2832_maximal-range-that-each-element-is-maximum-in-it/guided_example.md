# Guided Example: Maximal Range That Each Element Is Maximum in It

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 5, 4, 3, 6]}`
- **Required output:** `[1, 4, 2, 1, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` of **distinct **integers.

The objective is to compute `[1, 4, 2, 1, 5]` from `{"nums": [1, 5, 4, 3, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

**Expansion stops at the first greater value on each side.** Fix index `i`. Any adjacent smaller value may be included while `nums[i]` remains the subarray maximum. The first greater value to the left cannot be crossed because including it would make `nums[i]` cease to be maximum. The same is true on the right.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 5, 4, 3, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Therefore, if `left[i]` is the nearest greater index to the left, or negative one when absent, and `right[i]` is the nearest greater index to the right, or `n` when absent, the largest valid subarray is

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Therefore, if `left[i]` is the nearest greater index to the ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Optimality Decision

Synthesize the final answer directly from validated sub-states.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 4, 2, 1, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 5, 4, 3, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 4, 2, 1, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Contribution-style single stack:** Pop indices:** - **Contribution-style single stack:** Pop indices when a greater current value arrives and assign one boundary then; a second cleanup or sentinel can finish the other side. It can reduce code duplication but is easier to get wrong.
- **Segment tree with searches:** Range maxima plus boundary binary searches can find blockers in $O(n\log n)$ time and $O(n)$ space, slower than the stack.
- **Brute-force expansion:** Expand left and right independently for every index. It is simple but quadratic in monotone arrays.
- **Global maximum:** Both stacks are empty at its boundary checks, so its answer spans the entire array.
- **Smallest value:** Its nearest neighbors may immediately block it, often giving length one.
- **Strictly increasing array:** Every value's right side is unblocked until a greater immediate successor, while no greater left value exists; answers become one through $n$.
- **Strictly decreasing array:** The symmetric pattern expands each value to the right.
- **Single element:** Sentinels negative one and one yield length one.
- **Distinctness:** It guarantees a unique maximum in every considered subarray. If duplicates were allowed and equality still counted as maximum, equal values should not be blockers; the source's pop condition already treats them as non-blocking.
- **Boundary sentinels:** Negative one and `n` eliminate special formulas at array edges.
- **Indices rather than values:** Distances require exact blocker positions, so storing only values would be insufficient.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each of the $n$ indices is pushed once and popped at most once in the left pass, so that pass is $O(n)$. The same argument applies to the right pass. Building the result is another $O(n)$. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
