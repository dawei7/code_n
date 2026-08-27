# Guided Example: Split Array with Equal Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 1, 2, 1, 2, 1]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` of length `n`, return `true` if there is a triplet `(i, j, k)` which satisfies the following conditions:

The objective is to compute `true` from `{"nums": [1, 2, 1, 2, 1, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

Three separator indices `i < j < k` are excluded from the four subarrays. The goal is to make these four sums equal:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 1, 2, 1, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

1. indices zero through `i - 1`;
2. `i + 1` through `j - 1`;
3. `j + 1` through `k - 1`;
4. `k + 1` through `n - 1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | 1.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Trying every triplet would take cubic time. The solution fixes the middle separator `j`, summarizes every valid left split by its shared sum, and then tests right splits against that set.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 1, 2, 1, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all triplets:** Prefix sums make eac:** - **Enumerate all triplets:** Prefix sums make each check constant time, but $O(n^3)$ triplets are still too many.
- **Two sets split around `j`:** The implemented one-set method builds left possibilities and streams right checks, avoiding extra storage.
- **Assume positive values:** Values may be negative, so sliding-window monotonicity does not apply.
- **Fewer than seven elements:** Three separators plus four nonempty sections cannot fit; loop ranges naturally return false.
- **Separator values:** They must be omitted, and the prefix formulas explicitly skip them.
- **Zero shared sum:** Zero is a normal set value and can validate a split.
- **Negative shared sum:** Hash membership works without ordering assumptions.
- **Several left indices with one sum:** The set intentionally stores the sum once because only existence matters.
- **Valid split at extreme legal indices:** Loop endpoints include `i = 1` and `k = n - 2` while preserving one-element outer sections.
- **No valid middle separator:** Completing all loops returns false.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the array length. Prefix construction takes $O(n)$. There are $O(n)$ middle indices, and each performs $O(n)$ total left/right separator checks. Time is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
